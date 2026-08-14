#!/usr/bin/env python3
"""Check a cold-email draft against the rules in SKILL.md.

Usage:
    check_draft.py draft.txt
    cat draft.txt | check_draft.py
    check_draft.py draft.txt --talent    # numbered/structured talent variant

Exits 1 if any ERROR is found.
"""

import argparse
import re
import sys

BANNED = [
    "i hope this email finds you well",
    "hope this finds you well",
    "touch base",
    "circle back",
    "reach back out",
    "synergy",
    "synergies",
    "cutting-edge",
    "cutting edge",
    "game-changing",
    "game changing",
    "revolutionary",
    "seamless",
    "delve",
    "in today's fast-paced",
    "quick question",
    "just wanted to",
    "i wanted to reach out to see if",
    "following up on my previous email",
    "just bumping this",
    "per my last email",
    "at your earliest convenience",
    "world-class",
    "best-in-class",
    "unparalleled",
    "we are excited to announce",
]

# "leverage" is only banned as a verb; "unlock" only in the marketing sense.
BANNED_REGEX = [
    (r"\bleverag(e|ing|es)\b", "leverage (use 'use')"),
    (r"\bunlock(s|ing)?\s+(the\s+)?(power|potential|value)", "unlock the power/potential"),
]

NEGATION_CUES = [
    "not just",
    "not pitch decks",
    "would not be",
    "not a ",
    "rather than",
    "instead of",
    "not marketing fluff",
    "no es solo",
    "no son ",
    "no lo son",
    "no te voy a decir",
    "no les voy a decir",
    "sin promesas",
    "más que de",
    "mas que de",
    "en vez de",
    "no es un patrocinio",
]

# Deliverables the sender usually cannot produce: signup data lives with the company.
OVERPROMISE = [
    (r"(les |te )?(mandamos|enviamos|entregamos) el reporte", "promising a signup/metrics report"),
    (r"reporte de (cuentas|registros|conversi)", "promising a signup/metrics report"),
    (r"we('ll| will) (send|share) (you )?(a |the )?report", "promising a metrics report"),
    (r"\bgarantizamos\b(?!.{0,40}acceso)", "guaranteeing an outcome"),
    (r"\bwe guarantee\b(?!.{0,40}access)", "guaranteeing an outcome"),
    (r"(garantiz|guarantee)\w*\s+(\d+|cien|cientos|hundreds)", "guaranteeing a number"),
]

# Over-applied rules that read as machine-written. See "Tells" in SKILL.md.
SLOP = [
    (r"^\s*lo que no (ganan|reciben|incluye|les doy)\b", "a 'what you don't get' section — "
     "the limit is a clause inside a sentence, never its own block", True),
    (r"\bwhat you (don't|do not) get\b", "a 'what you don't get' section", True),
    (r"^\s*(lo que pido|lo que ganan|el n[úu]mero|la propuesta|el pedido)\s*:", 
     "labeled scaffolding — lead into a list with a sentence, not a heading", False),
    (r"\bvoy (a ser |al grano|directo|directa)\b|\bser[ée] (breve|directa?)\b|\bsin rodeos\b",
     "announcing your own tone — being direct is demonstrated, not declared", True),
    (r"\bse cierra esta semana\b|\bquedan pocos (cupos|lugares)\b|\b[úu]ltimos d[íi]as\b",
     "manufactured urgency — real deadlines are dates, and go with the other facts", True),
]

ENTHUSIASM = [
    "amazing", "perfect", "incredible", "awesome", "fantastic",
    "thrilled", "excited", "huge", "massive", "love to",
]

MAX_PARAGRAPH_WORDS = 55
MIN_WORDS = 110
MAX_WORDS = 320
MAX_WORDS_BULLETED = 420  # bullets are scanned, not read linearly
MAX_WORDS_TALENT = 450

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def check(text: str, talent: bool) -> None:
    low = text.lower()
    words = text.split()
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    body = "\n".join(text.strip().splitlines()[:-2]) if len(text.strip().splitlines()) > 2 else text

    # --- banned phrases -------------------------------------------------
    # Quoting the prospect's own words is a recommended move, so their
    # vocabulary inside quotes is not the sender's prose. Strip quoted spans.
    unquoted = re.sub(r'"[^"]{0,400}"|“[^”]{0,400}”|«[^»]{0,400}»', " ", low)
    for phrase in BANNED:
        if phrase in unquoted:
            err(f'banned phrase: "{phrase}"')
    for pattern, label in BANNED_REGEX:
        if re.search(pattern, unquoted):
            err(f'banned phrase: "{label}"')

    # --- length ---------------------------------------------------------
    bulleted = bool(re.search(r"^\s*[-*•]\s", text, re.M))
    cap = MAX_WORDS_TALENT if talent else (MAX_WORDS_BULLETED if bulleted else MAX_WORDS)
    if len(words) > cap:
        err(f"too long: {len(words)} words (max {cap}). Cut the weakest paragraph.")
    elif len(words) < MIN_WORDS:
        warn(f"short: {len(words)} words. Check the fit thesis is actually specific.")

    # --- paragraph density ----------------------------------------------
    if not talent:
        for i, p in enumerate(paragraphs, 1):
            # A bullet block is scanned line by line, so its total is not a wall of text.
            if re.match(r"^\s*[-*•]\s", p):
                longest = max((len(li.split()) for li in p.splitlines() if li.strip()), default=0)
                if longest > 25:
                    warn(f"block {i} has a {longest}-word bullet — bullets should fit one line.")
                continue
            n = len(p.split())
            if n > MAX_PARAGRAPH_WORDS:
                warn(f"paragraph {i} is {n} words — split it. Short paragraphs pace the read.")

    # --- required moves --------------------------------------------------
    greeting = re.match(r"^\s*(Hi|Hey|Hello|Hola)\s+([\w'áéíóúñÁÉÍÓÚÑ-]+)\s*,", text.strip())
    if not greeting:
        err("must open with 'Hi {FirstName},' — no greeting with a first name found.")
    elif greeting.group(2).lower() in {"there", "team", "all", "everyone", "folks"}:
        err(f"generic greeting 'Hi {greeting.group(2)}' — use the recipient's first name.")
    elif not greeting.group(2)[0].isupper():
        err(f"greeting name '{greeting.group(2)}' is not capitalized — check it is a real name.")

    negation_patterns = [
        r"más de .{0,60} que de ",      # "más de marca empleadora que de patrocinio"
        r"mas de .{0,60} que de ",
        r"more .{0,60} than (a )?sponsor",
        r"no es (un |una )?patrocinio",
        r"mejor con .{0,60} que con ",
        r"(más|mas|mejor) .{0,60} que (con |de )?un patrocinio",
        r"\bno es (un|una|solo|solamente)\b",   # "no es un stand ni un logo"
        r"\bno (buscamos|queremos|pedimos) \w+,? sino\b",
        r"\bis not (a|an|just)\b",
    ]
    if not any(cue in low for cue in NEGATION_CUES) and not any(
        re.search(p, low) for p in negation_patterns
    ):
        err("no negation move. Every email that landed named what the ask is NOT "
            "(e.g. 'not just logo placement', 'not pitch decks', 'would not be CSR-driven').")

    if not re.search(r"https?://", text):
        err("no link. Include the per-prospect deck URL (e.g. /deck/company).")

    if not re.search(r"\d", text):
        err("no numbers. Include headcount, duration, date, cities.")

    # --- the price ---------------------------------------------------------
    has_price = re.search(r"(usd|us\$|\$|eur|€)\s?\d|(\d[\d.,]*\s?(usd|dólares|dolares|euros))", low)
    # An explicitly in-kind-only ask is the one case with no figure to state.
    inkind_only = any(
        c in low for c in ["in-kind only", "solo in-kind", "sin aporte económico",
                           "sin aporte economico", "no estamos pidiendo dinero"]
    )
    # Documented exception: a named-agenda close that puts budget on the table.
    budget_agenda = any(
        c in low for c in ["budget range", "rango de presupuesto", "nivel de involucramiento",
                           "level of involvement"]
    )
    inkind_only = inkind_only or budget_agenda
    if not has_price and not inkind_only:
        err("no price. State the number in the email: the ask, one rung up, and a "
            "no-cash path. Leaving budget for the call costs a round trip.")
    elif has_price:
        figures = set(re.findall(r"(?:usd|us\$|\$)\s?([\d.,]+k?)", low))
        if len(figures) < 2 and not inkind_only:
            warn("only one figure given — naming a single number caps the deal there. "
                 "Add one rung up and a no-cash path.")

    # date-ish signal
    if not re.search(
        r"\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|"
        r"ener|febr|marzo|abril|mayo|junio|julio|agost|septiem|octub|noviem|diciem)",
        low,
    ) and not re.search(r"\b\d{1,2}[/-]\d{1,2}\b", low):
        warn("no month named — make the date unmissable.")

    # --- close ------------------------------------------------------------
    # A direct question mark, or an indirect ask ("would love to know if...").
    tail = "\n".join(text.strip().splitlines()[-8:]).lower()
    ask_cues = [
        "would love to know", "let me know", "would this be", "would that be",
        "happy to", "i suggest", "if this resonates", "open to", "me encantaría saber",
        "avísame", "te interesa", "propongo", "si tiene sentido", "si les hace sentido",
        "quedo atenta", "quedo atento", "me dices", "coordinamos",
    ]
    if "?" not in tail and not any(c in tail for c in ask_cues):
        err("close contains no ask. End on a question or an explicit invitation to reply.")

    # --- tone --------------------------------------------------------------
    if "!" in text:
        err("exclamation mark found — remove it.")

    if re.search(r"[\U0001F300-\U0001FAFF☀-➿]", text):
        err("emoji found — remove it.")

    hits = [w for w in ENTHUSIASM if re.search(rf"\b{w}\b", low)]
    if len(hits) > 2:
        warn(f"{len(hits)} enthusiasm words ({', '.join(hits)}) — keep at most one or two.")

    # --- machine-written tells ---------------------------------------------
    for pattern, label, hard in SLOP:
        if re.search(pattern, low, re.M):
            (err if hard else warn)(f"reads as AI-written: {label}.")

    # --- promises the sender probably cannot keep --------------------------
    seen_labels = set()
    for pattern, label in OVERPROMISE:
        if re.search(pattern, low) and label not in seen_labels:
            seen_labels.add(label)
            warn(f"possible overpromise: {label}. Guarantee access, not conversion — "
                 "hand measurement back to the company's own dashboard.")

    links = re.findall(r"https?://\S+", text)
    if len(links) > 2:
        warn(f"{len(links)} links — two is the ceiling (deck + booking).")

    # --- placeholders left behind -------------------------------------------
    # `re.I` here would flag ordinary prose: Spanish "sobre todo" matched TODO.
    if re.search(r"\{\{?\s*\w+\s*\}?\}|\[(company|name|first|city|nombre|empresa)\]", text, re.I) or re.search(
        r"\b(XXX|TODO|FIXME)\b", text
    ):
        err("unfilled placeholder found — every email must be fully written per prospect.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?", help="draft file (default: stdin)")
    ap.add_argument("--talent", action="store_true", help="talent/employer-brand variant")
    args = ap.parse_args()

    if args.file:
        with open(args.file, encoding="utf-8") as fh:
            text = fh.read()
    else:
        text = sys.stdin.read()

    if not text.strip():
        print("empty draft")
        return 1

    check(text, args.talent)

    for e in errors:
        print(f"ERROR  {e}")
    for w in warnings:
        print(f"WARN   {w}")

    words = len(text.split())
    print(f"\n{words} words | {len(errors)} errors | {len(warnings)} warnings")
    if not errors and not warnings:
        print("clean")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
