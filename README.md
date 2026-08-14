# skills

Agent Skills I use with [Claude Code](https://claude.com/claude-code). Each one packages
a workflow I run often enough that re-explaining it every time was the bottleneck.

Built and maintained by [Shiara Arauzo](https://github.com/shiarauzo).

## Skills

| Skill | What it does |
|---|---|
| [`cold-email`](./cold-email) | Writes cold outreach asking a company to sponsor or partner on an event. Researches the prospect's product first, then drafts against a skeleton extracted from emails that actually got replies. Ships with a validator that rejects the draft if it reads like bulk mail. |

## Install

Skills live in `~/.claude/skills/` (available everywhere) or `.claude/skills/` inside a
project (available in that repo only).

```bash
git clone https://github.com/shiarauzo/skills.git
cp -r skills/cold-email ~/.claude/skills/
```

Or symlink, so a `git pull` updates the skill in place:

```bash
ln -s "$(pwd)/skills/cold-email" ~/.claude/skills/cold-email
```

Claude picks the skill up automatically based on its `description` — no configuration.
Invoke it explicitly with `/cold-email`, or just describe the task and let it trigger.

## Structure

Each skill is a directory with a `SKILL.md` at its root:

```
skill-name/
├── SKILL.md          # frontmatter (name, description) + the workflow
├── references/       # loaded only when the workflow needs them
└── scripts/          # executable checks and helpers
```

Two rules that keep them useful:

- **The `description` is the trigger.** It has to say what the skill does *and* when to
  reach for it, because it is the only part always in context.
- **`SKILL.md` stays lean.** Detail moves to `references/`, loaded on demand. Context is
  a shared budget.

## What is public here, and what is not

These skills are written to be used by anyone, so nothing in this repo names a real
person, a real prospect, a live deal, or my own events and links. Examples use
placeholders — `[Company]`, `[Event]`, `/deck/acme` — and the rules are stated so they
transfer to whatever you are pitching.

My working copies are a layer on top: same rules, plus a `references/examples.md` holding
my own emails that got replies, annotated move by move. That file is gitignored, because
it names real recipients.

**If you fork this**, that is the pattern worth copying. The rules are the shareable part;
the examples in your own voice are what make them land, and they belong on your disk, not
in a repo.

## Contributing

Issues and PRs welcome, especially new skills or sharper heuristics in existing ones. If
you adapt `cold-email` for a different kind of outreach, that is worth its own directory
rather than a fork of this one.

## License

MIT — see [LICENSE](./LICENSE). Use them, fork them, ship them.
