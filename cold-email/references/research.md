# Researching the prospect

Research is not optional. A pitch that could be sent to any company gets deleted; one
that names what *their* users will build gets a reply. Budget 5–10 minutes per prospect.

Contents:
- [How to browse](#how-to-browse)
- [What to harvest](#what-to-harvest)
- [Researching the person](#researching-the-person)
- [Turning findings into the draft](#turning-findings-into-the-draft)
- [Judging fit honestly](#judging-fit-honestly)

## How to browse

**Single prospect — use `agent-browser`.** It renders JS-heavy SPAs (most DevTool
landing pages), follows nav links, and takes screenshots. Load its skill for the full
guide, then:

```bash
agent-browser open <company>.com && agent-browser wait --load networkidle && agent-browser snapshot -i
agent-browser get text @e1                  # pull hero copy, feature sections
agent-browser screenshot --annotate hero.png # when the visual identity matters
```

Walk this path in order, it maps directly onto the email moves:

1. **Landing page** — hero headline, feature sections, the "who it's for" band.
2. **Docs quickstart** — what a team actually does in hour one.
3. **Pricing** — is there a free tier, are credits a real currency for them?
4. **Changelog or blog** — what shipped in the last two months.
5. **Community/Discord/events page** — do they already sponsor hackathons?

**Batch of prospects — use `firecrawl-scrape` or `firecrawl-search` instead.** Driving a
real browser through ten companies is slow; firecrawl returns clean markdown for many
URLs at once. Escalate to `agent-browser` only for the ones firecrawl renders poorly or
where a screenshot is needed.

Never draft from memory of what a company does. Product positioning changes fast, and a
stale claim in the fit thesis is worse than no claim.

## What to harvest

Capture these ten items as notes before writing a single line of email.

| # | Item | Where | Why it matters |
|---|---|---|---|
| 1 | Hero headline, verbatim | Landing | Their own positioning. Echo it, don't restate it in your words. |
| 2 | **The verb list** | Features section | What the product lets you *do*. Vapi's "talk, call, qualify, schedule, teach, support" came straight from here — this is the highest-value harvest. |
| 3 | Product nouns | Docs, nav | `Actor`, `Run`, `Index`, `Assistant`, `Squad`, `Agent`. Using their vocabulary is the cheapest possible proof of research. |
| 4 | Stated audience | Landing, pricing | Do they sell to indie devs or to enterprises? Determines whether 300 builders is an asset or irrelevant. |
| 5 | Free tier / credit model | Pricing | If there is no credit concept, "credits for teams" is a nonsense ask — swap it for licenses or extended trials. |
| 6 | Quickstart shape | Docs | Makes the starter-kit ask concrete: "a starter kit so teams have a working {thing} in 20 minutes." |
| 7 | Recent launch | Changelog, blog, X | A feature shipped in the last two months is the strongest hook: they need adoption for it right now. |
| 8 | DevRel presence | Team page, Discord, events | If they already sponsor hackathons, the ask is routine — pitch scale. If they never have, lower the ask and explain the mechanics. |
| 9 | LatAm / regional presence | Case studies, community | If absent, regional entry becomes its own angle: a bounded, low-cost way to land in five cities at once. |
| 10 | **Legal entity and home market** | Footer, terms, regulator registration | The single most-skipped item. A company whose footer names an Argentine regulator is Argentine, whatever the `.com` implies. Determines which cities of the event are actually their market, and therefore the tier. |

## Researching the person

Two minutes, three questions:

- **Role and team.** DevRel, partnerships, marketing, and founders each buy for
  different reasons. DevRel buys developer adoption. Marketing buys brand and content.
  Founders buy strategic entry into a market.
- **Do they own budget?** If unclear, use the close that asks who else to include. Never
  guess.
- **What do they post about?** A recent post or talk is a legitimate opener when it
  genuinely connects. Skip it if the connection is a stretch — forced personalization
  reads worse than none.

## Turning findings into the draft

Produce these three artifacts before drafting.

**1. The fit thesis.** One sentence, and it must fail this test: *swap the company name
for a competitor — does the sentence still make sense?* If yes, it is too generic.

- Too generic: "Teams will build AI agents, which fits what Exa does."
- Specific: "Many teams will build agents, research products, copilots, content tools,
  automations, and dev workflows that need fresh web context." — names the project types
  *and* the exact dependency.

Build it from item 2 (verb list) plus the project types your audience actually ships.

**2. Proof of use.** Only if the sender genuinely used the product. Rank by strength:

1. Taught it publicly — a workshop, talk, or article. Strongest: it proves the sender can
   make *their* users successful, which is the DevRel lead's actual job.
2. Shipped something real with it.
3. Used it in a project.
4. None — say so plainly (`I've been looking at Apify`) and compensate with a named role
   for them in the event. Never inflate.

**3. Their KPI.** One line naming what the recipient is measured on. It sets the framing
and often belongs verbatim in the close: `whatever makes the most sense for your DevRel
and community goals.`

- DevRel → developers who ship something real and keep using it after
- Marketing → visible brand moments, content, logos in front of the right audience
- Partnerships/BD → pipeline, regional entry, co-marketing
- Talent/HR → candidate access and employer brand (see `variants.md`)

## Judging fit honestly

If the research turns up no real fit, say so to the user instead of forcing a draft. A
weak pitch burns the contact permanently, and DevRel teams talk to each other.

Real signals the fit is weak: the product has no free or credit tier and sells only
annual enterprise contracts; the audience is not developers; the company has visibly cut
community spend. In those cases recommend a smaller ask (in-kind credits, a mentor, a
prize) or a different contact.
