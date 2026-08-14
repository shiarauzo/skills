---
name: cold-email
description: Write cold outreach emails asking a company to sponsor or partner on an event (hackathon, summit, conference, community program). Use when the user wants to pitch a sponsor, write a cold email to a company, contact DevRel/partnerships/marketing about an event, ask for credits or prizes, reach out about a Main Partner or Gold/Silver tier, follow up on an unanswered sponsor email, or produce a batch of personalized pitches for a prospect list. Triggers include "cold email", "sponsor", "sponsorship", "patrocinio", "partnership pitch", "reach out to a company about the hackathon", "email para conseguir sponsors".
---

# Sponsor Outreach

Write cold emails that get replies from DevRel, partnerships, and marketing leads.

The core insight: these emails do not sell a sponsorship. They hand the recipient a
ready-made way to hit a goal they already have (developer adoption, employer brand,
LatAm presence) and make the event the vehicle. Generic pitches get ignored; a pitch
that names what their specific users will build gets a reply.

## Workflow

Run these four steps in order. Do not skip step 2 — research is what separates a reply
from a template.

### Step 1 — Intake

Collect the event facts. Never invent a number, date, city, or partner name. If a
required field is missing, ask for it before drafting.

**Never invent the recipient's name.** A plausible-sounding placeholder is the one
fabrication that survives review, because it does not look fabricated. When the address
is a role inbox and no name is known, leave an obvious slot — `[NOMBRE]` — say so when
delivering, and name who can supply it.

**Required:**
- Event name, date, format (e.g. "12-hour in-person", "48-hour global")
- Cities or "global/remote"
- Headcount and how attendees are selected ("300 selected builders")
- Audience composition (product engineers, AI builders, founders, indie hackers, PMs, designers)
- Sender: first name + the organization they represent
- Recipient: first name + company + their role/team

**Required if it exists:**
- Deck URL — always prefer the per-prospect path (`/deck/acme`, `/deck/globex`). Ask for
  the pattern once, then derive it per company.
- Booking link, if the sender uses one
- Tiers available (Main Partner, Gold, Silver, in-kind)

**Ask if unclear:** has the sender genuinely used this company's product? This decides
whether the strongest opener is available. Never fabricate usage.

### Step 2 — Research the prospect

Open the company's site and read it before drafting — never draft from memory of what a
company does. Use `agent-browser` for a single prospect (it renders JS-heavy landing
pages and can screenshot), or `firecrawl-scrape` when working a batch.

Read `references/research.md` for the full path: which pages to walk, the ten things to
harvest, and how to judge fit honestly. The output is three things the draft needs:

1. **The fit thesis** — one specific sentence connecting what builders will ship to what
   this company sells.
2. **Proof of use** — a true, concrete thing the sender built, taught, or shipped with
   the product. Omit entirely if none exists.
3. **Their KPI** — what the recipient's team is measured on, which sets the framing
   (developer adoption vs. employer brand vs. regional expansion).

Two checks that kill drafts before they are written:

- **Footprint.** Which of the event's cities or segments is actually their market? A
  company that operates in one of the event's countries knows it, and pitching them five reads
  as either sloppy or dishonest. Size the ask to the real overlap and name the limit out
  loud in the draft — see "Sizing the ask" below.
- **Slot availability.** Is the activation being offered already promised to another
  partner? Confirm with the organizer before designing a pitch around the prize pool, the
  keynote, or any single-occupancy asset. Rebuilding a pitch after the slot turns out to
  be taken costs more than the one question.

### Step 3 — Draft the email and build the deck

These are one deliverable. See "The deck" below — a cold email without its own
per-prospect deck is not finished.

Follow the skeleton below. Read `references/variants.md` when the pitch is a
talent/employer-brand angle, a warm intro from a teammate, a follow-up, a
non-Main-Partner tier, or a batch.

Optional: add a `references/examples.md` holding two or three of your own emails that
actually got replies, annotated move by move, and point to it here. Real examples in the
sender's own voice beat any amount of instruction. Keep that file out of version control
if the emails name real recipients.

### Step 4 — Self-check

Run the validator on the draft before showing it:

```bash
scripts/check_draft.py path/to/draft.txt
```

It flags banned phrases, bloated paragraphs, missing moves, and length problems. Fix
every ERROR. Judge each WARN on its merits — some are deliberate.

Then read the draft once against this question: **could this exact email be sent to a
different company by swapping the name?** If yes, the fit thesis failed. Rewrite it.

## The skeleton

Ordered moves. Each is one short paragraph unless noted. Total 150–280 words.

1. **Greeting** — `Hi {First},` Optionally one line of warmth (`Hope you're doing great.`).
   Skip the warmth line when move 3 is present; the proof of use is a better opener.

2. **Identity** — one sentence. `I'm {Sender} from {Org}.`

3. **Proof of use** *(optional, highest leverage — use whenever it is true)* — what the
   sender actually built, taught, or shipped with the product, and why it mattered.
   Two or three sentences. This is the single biggest differentiator between the
   examples that landed warm and the ones that landed cold.

4. **The event in hard numbers** — date, duration, cities, headcount, selection.
   Concrete nouns only. `300 selected builders across five cities to ship real products
   in one day.`

5. **The negation** — reposition the ask by naming what it is *not*. Every successful
   example contains one: `not pitch decks` / `not just logo placement` /
   `This would not be CSR-driven.` Pick the negation that kills the recipient's most
   likely objection.

6. **Fit thesis** — why *this* company, specifically. Name the kinds of projects teams
   will build and why they need this product to work. This paragraph must be
   unreusable for any other company.

7. **Activation menu** — 4 to 6 concrete deliverables. Write them as a comma series
   inside one sentence, not as bullets: `credits for teams, starter kits, a pre-event
   workshop, mentorship or judging, and a prize for the best {Company}-powered project.`
   Close with the outcome: `We want builders to leave having shipped real voice agents,
   not just played with the API.`

   **Each item names the payoff, not just the mechanic.** "A mentor room: two people from your team" is a
   logistics note. "A mentor room: two people from your team, the most direct exposure to
   the talent in the room" is an offer. The recipient should never have to
   work out why an item is worth having.

8. **Deck link** — on its own line. Per-prospect URL.

9. **Close** — a low-friction question plus one opening. Choose one:
   - `Would this be interesting to explore?`
   - `Would love to know if this is interesting, and if there's someone else on your side I should include.` *(use when unsure the recipient owns the budget)*
   - Add tier flexibility when Main Partner may be too big an ask: `Main Partner would be the ideal path, but we're also open to Gold, Silver, or in-kind support through credits, prizes, or community activation.`
   - Add the booking link only when the relationship is warm or the ask is large.

10. **Sign-off** — `Best,` or `Thanks,` + first name. Nothing else.

## Always name the price

**Every email states the number.** Never leave the figure for a later call. "Happy to
discuss budget" costs a week and one extra round trip, and the recipient often cannot
start an internal approval without a line item.

Give the number as a **ladder in one paragraph**, so the recipient never has to write
back to negotiate in either direction:

1. **The ask** — the tier that fits, with what it covers.
2. **The adjacent tier** — usually one rung up, since naming only the lower figure caps
   the deal there. Go *down* instead when the footprint check showed partial overlap:
   offering a big-company package to a prospect whose market is a fraction of the event
   contradicts the honesty the rest of the email just bought.
3. **A no-cash path** — mentors, a workshop, credits, amplification. This one needs no
   budget approval, so it converts fastest and creates the history that makes next
   year's cash ask land.

> So you do not have to guess the number: the four items above are USD 2,500, our Gold
> tier. If you want presence across all five cities, Title is USD 5,000. And with no
> budget at all, mentors and a talk still work for us.

**Name the tiers even when the pitch is not about sponsorship.** A large company needs a
line item to raise a purchase order against; without one, someone in finance has to
invent it and the request stalls.

This rule applies to the talent variant too, which historically closed by proposing a
call to define budget range. The number goes in the email.

### When not to name the price

Three situations, and only these. Everywhere else, state the number.

1. **The recipient's budget is an order of magnitude above the tier sheet.** Naming
   USD 2,500 to a company whose employer-brand line runs in the tens of thousands caps
   the deal at 2,500 and signals the sender does not know what they are worth.
2. **What is being sold does not exist yet.** A co-designed program — a talent track, a
   private roundtable, a multi-part activation — cannot be priced before its scope is
   agreed. Pricing it anyway means either guessing high and getting ignored, or guessing
   low and doing the work for free.
3. **The sender genuinely does not know the cost to deliver.** Quote after, not before.

In those cases the close does the work the price would have done. Propose a call with a
**named agenda**, so it reads as a working session and not as a discovery call:

> If this resonates, I suggest a 20–30 min call to define:
>
> - Level of involvement
> - Budget range
> - Talent focus areas (Product, Engineering, Ops)
> - Who from your side would get involved

Naming `budget range` as a line item is what makes this work. It puts money on the agenda
without putting a number on the table, so the recipient arrives to the call expecting to
discuss spend. A close that omits it produces a friendly call and no deal.

The rest of the email still carries hard numbers — headcount, dates, cities. This
exception is about the *price*, never about vagueness.

## Sizing the ask

**Convert the ask into the unit their budget is measured in.** A marketing lead does not
buy "sponsorship", they buy cost per acquisition. A DevRel lead buys developers who ship
something real. A talent lead buys candidate access. Do the division for them and let
them compare it to what they pay today:

> If a third convert, that is 90 accounts at 28 dollars each. Compare it to what you
> pay today for a new account in this market.

Label estimates as estimates. Guarantee only what is inside your control — usually
access, never conversion.

**Name the limit before they do.** When only part of the event is their market, say so
and let the number that is true carry the pitch. Admitting that four of five cities are
brand reach and only one is real users makes the whole email credible; hiding it means the
recipient finds it in ten seconds and stops reading.

**Lower the tier when the overlap is partial.** Asking for the top tier on a fraction of
the audience is how a warm lead goes cold.

## Prefer facts with shelf life

Research surfaces two kinds of fact. Both are true today; only one is still true when the
email is read, forwarded, and read again a week later.

| Short shelf life | Long shelf life |
|---|---|
| "ten open roles in the city" | "an engineering site in the city" |
| a quote from one job posting | the team name that posting belongs to |
| "just launched last week" | what the product does |
| a headcount from a careers page | the market they operate in |

A number that has moved by the time they read it does not read as out of date. It reads as
sloppy, and it discredits the accurate parts of the email with it. When a durable fact
makes the same point, use the durable one — the specificity that earns the reply comes
from naming the right thing, not the freshest thing.

Use a perishable fact only when nothing durable carries the argument, and then attribute
it: `sus vacantes abiertas` rather than `sus diez vacantes abiertas`.

## Every offered item must be operationally possible

Before an activation item goes in the email, answer: **can the sender actually do this?**

Offers fail this check more often than they fail the fit test, and the failure is worse:
it tells the recipient the sender does not understand their product.

- A bank card is issued to a named person after identity verification. It cannot go in
  three hundred swag bags. What goes in the bag is a card *request*.
- Credits usually require the partner to provision them, not the organizer.
- Sharing attendee contact data requires the attendee's consent, and in several countries
  a legal basis. Offer the data of those who opt in, never the list.
- A named track, keynote, or prize slot can only be sold once — see "Slot availability".

When the mechanic is wrong but the intent is good, keep the intent and fix the mechanic.
The card that arrives at someone's home weeks later is a *second* touchpoint, which is a
better story than the one that was impossible.

## Only promise what you can deliver

Separate what the sender controls from what the company measures. The sender controls
placement, audience, and access. The company controls its own signup data.

Never promise a post-event report of accounts, installs, or conversions unless the sender
has a real way to see them. Instead, hand the measurement back:

> Every touchpoint uses a link you provide, so the conversion shows up in your dashboard
> and does not depend on what we tell you.

This is stronger than the promise it replaces. It says the sender has thought about
attribution, and it removes the argument that shows up at invoice time.

## The deck

**Every cold email ships with its own deck.** Not a link to a generic one — a deck built
for that prospect at `/deck/{company-slug}`. Writing the email and building the deck are
one task, not two; if the deck does not exist yet, build it before delivering the email.

The email carries the reasoning. The deck carries the offer. A generic deck behind a
personalized email undoes the personalization the moment they click.

**The one exception: a talent pitch to a large company.** There the numbered email is
already the forwardable artifact, and a thin deck actively subtracts — it repeats the
email with less nuance and gives the recipient a second thing to evaluate. Build the deck
only if it can carry something the email cannot.

**Test the deck the way the email is tested:** swap the company name for a competitor. If
the deck still works, it is a brochure. That usually happens after trimming — the slides
cut first are the ones that named this prospect specifically, because those are the ones
that felt risky to assert. Cut length from those slides instead of cutting the slides.

### Attach the PDF, do not only link it

**Every deck ships as a PDF attached to the email**, with the link alongside it. A link is
a decision the recipient has to make; an attachment is already open by the time they
decide. It also survives being forwarded to someone on a locked-down corporate network, a
phone on a plane, or a procurement folder — all places a link dies.

```bash
scripts/deck_to_pdf.sh https://example.com/deck/acme ~/Desktop/acme-deck.pdf
```

The script screenshots each slide and stitches them, one slide per page at the deck's own
aspect ratio. It hides the deck's navigation UI first, since screenshots do not trigger
print styles and those buttons would otherwise appear in a file sent to a sponsor.

Do not reach for the browser's own print-to-PDF: it ignores the page's `@page { size }`,
so a 16:9 deck lands letterboxed on letter paper.

### Deck copy rules

- **One idea per slide.** If a slide argues two things, it is two slides or one of them is
  filler.
- **No redundancy across slides.** If the event facts appear on slide 3, they do not
  reappear on slide 7. Repetition reads as padding, and a partner who spots padding starts
  skimming.
- **Numbers large and unmissable.** The figures are why the slide exists — headcount,
  price, cities, cost per unit. They should be readable from across a room.
- **No small print.** Footnotes, sources, disclaimers and hedges do not belong on a slide.
  Anything that needs qualifying belongs in the email, where a sentence can carry the
  nuance a caption cannot.

**A deck headline must not promise an outcome the sender does not control.** "You will have the best talent in the city" is the same class of claim as promising a signup report:
the sender cannot deliver it, and a senior reader discounts everything around it. Headline
what is being offered, not what it will produce.

The deck and the email must share **one thesis**. If the email argues account adoption
and the deck argues brand visibility, the recipient trusts neither.

Keep the deck lighter than the email. Reasoning, caveats, and the "why now" belong in the
email, where prose is expected. The deck should be titles, numbers, and short labels — a
partner decides whether to forward it in about thirty seconds.

## Voice

- Short paragraphs, one to three lines. Whitespace does the pacing.
- Plain verbs, concrete nouns: credits, starter kits, judging, demos, office hours.
- Contractions are natural: `We're`, `I've`, `I'd`.
- At most one enthusiasm word in the whole email (`amazing`, `perfect`, `strong fit`).
  Two reads as a pitch deck.
- **Bullets are the house style.** A partnerships or marketing lead scans before they
  read, and a bulleted block survives that first pass where a comma series does not. Use
  them for the event facts and for what the sponsor gets — the two things the recipient
  is actually looking for.
- Keep the argument in prose. Bullets carry facts and deliverables; the fit thesis, the
  negation, and the footprint limit are sentences, because they are reasoning and
  reasoning does not survive being chopped into fragments.
- Bulleted emails may run longer, to about 420 words. They are not read linearly, so the
  length costs less. A prose-only email still stops at 280.
- No emojis. No exclamation marks. One link in the body, at most two total.
- End on a question. Never on a statement.

## Tells that the email was written by a machine

These are what a reader registers as "AI wrote this", even when they could not name why.
All four come from over-applying a rule that is correct in moderation.

**1. A "what you don't get" section.** The footprint rule says to name the limit. It does
not say to give the limit a heading. The limit is a clause inside a sentence about what
they *do* get, never its own block:

- Wrong: `What you do not get: the other four cities are outside your market, and 100
  builders are not 100 recurring customers.`
- Right: `Two of the five cities are your market — those two sell, the other three are
  brand reach.`

One honest sentence reads as confidence. A bulleted list of your own weaknesses reads as
anxiety, and it gives the recipient's objections a headline they did not have to write.
Never more than one limit per email.

**2. Labeled scaffolding.** `Lo que pido:` / `Lo que ganan:` / `El número:` — headings
pretending to be prose. A human writes the sentence; a model labels the box. Lead into a
list with a sentence instead: `For that USD 2,500, you get:`

**3. Announcing your own tone.** `Voy directo.` `Seré breve.` `Sin rodeos.` Being direct
is demonstrated, never declared. The sentence costs a line and proves the opposite.

**4. Manufactured urgency.** `Esto se cierra esta semana.` `Quedan pocos cupos.` Real
deadlines are facts with dates — `las postulaciones cierran el 15 de agosto` — and belong
with the other facts. Invented pressure is the oldest tell there is.

**Never write:** `I hope this email finds you well`, `touch base`, `circle back`,
`synergy`, `leverage` (as a verb), `cutting-edge`, `game-changing`, `revolutionary`,
`unlock`, `seamless`, `delve`, `in today's fast-paced world`, `I wanted to reach out to
see if`, `quick question`, `just wanted to`.

**Never invent:** headcounts, partner logos, past sponsors, testimonials, funding, or
product usage. An unverifiable claim in a cold email to a DevRel lead is a fast no.

## Output

Deliver three things: the email, the per-prospect deck live at its URL, and the deck as
a PDF ready to attach.

Deliver the email as plain text ready to paste — no markdown formatting, no preamble.
Above it, give a one-line subject suggestion and a one-line note on the fit thesis used,
so the sender can sanity-check the angle. When drafting for several prospects, produce
one complete email per prospect; never a template with placeholders.
