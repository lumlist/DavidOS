# Influence: Nate Herk — AIOS Course (Three M's + Four C's)

**Source:** YouTube — "Build & Sell Claude Code Operating Systems (2+ Hour Course)" by Nate Herk | AI Automation, published 2026-05-01 ([video link](https://www.youtube.com/watch?v=bCljOfCH8Ms))
**Captured:** 2026-05-13 ~4:00 AM CDT
**Status:** Influence under consideration. **Not yet adopted.** Next session decides whether to fold this into SOUL.md, the Substrate Brief, and the 5-step path — and whether to resequence the path using the Four C's order rule.
**Surfaced by:** David, end of 2026-05-12 evening session

---

## What the video argues (transcript-grounded summary)

**Thesis in one line:** Build a durable, tool-agnostic AI Operating System inside Claude Code (or equivalent runtime) using two layered frameworks — the Three M's for mindset and the Four C's for build order — and structure it as folders of skills, context, connections, and routines that survive vendor changes.

### The Three M's of AI

| M | Meaning | Stated purpose |
|---|---|---|
| **Mindset** | How you think about AI | Default shift ("how could AI do this?"), function breakdown, curiosity rule ("never accept AI output without asking why") |
| **Method** | How you decide what to automate | Ask how much of a task is worth automating and to what extent |
| **Machine** | The technical layer | The AIOS itself, structured per the Four C's |

### The Four C's of an AIOS

| C | Meaning | What it covers |
|---|---|---|
| **Context** | What AI knows about you, your team, your tools, your voice, your business, your money | Operational context — not just system identity |
| **Connections** | What data and systems it can reach | API, CLI, MCP — prefer API/CLI for token efficiency |
| **Capabilities** | What it can produce and do with the data | Skills (markdown SOPs), reference files, scripts |
| **Cadence** | When it acts on its own while you sleep / laptop closed | Routines, scheduled tasks, loops, cron jobs |

**The order rule (single most important claim in the video):**

> "You can't have cadence without connections. You can't have capability without context. You have to go in this order. 1 2 3 4."

### Key direct quotes

- "Treat AI as a mentor, not a vending machine."
- "Skills are reusable instructions."
- "The skill.md is the actual brain itself and the supporting files are the tools that it can use."
- "You're never ever ever going to write a perfect skill the first try." Better skills emerge after 10, 20, 30 uses.
- "The question is never *will* AI do this for me. The question is to what extent can I leverage AI here?"

### The 7 tier-one buckets (his template)

He says to map your work into 7 buckets, captured during onboarding:

1. Revenue (e.g., Stripe, QuickBooks, Skool)
2. Customer
3. Calendar (Google Workspace)
4. Comms (email, Slack, ClickUp)
5. Tasks (ClickUp, Notion)
6. Meetings (Fireflies)
7. Knowledge (transcripts, docs, local files)

These are *his* buckets for a content/community business. They are not universal — adapt them to David's actual work.

### Skill anatomy (consistent with Video 1 but more rigorous)

- YAML frontmatter at the top: `name`, `description`
- Step-by-step workflow (the SOP)
- Reference files (extra context, scripts, brand assets)
- Rules (guardrails and constraints)
- Keep `skill.md` under 500 lines; move detail to separate files
- Progressive context loading: only frontmatter loads initially, full skill loads when matched, reference files load on demand

### Six-step skill-building framework

1. Name and trigger
2. Goal
3. Step-by-step process
4. Reference files
5. Rules
6. Self-improvement loop

### Cadence layer: three primitives

| Primitive | Where it runs | Needs machine on | Needs session open | Local file access | Minimum interval |
|---|---|---|---|---|---|
| Cloud routines (Anthropic) | Anthropic cloud | no | no | no | 1 hour |
| Desktop scheduled tasks | local machine | yes | no | yes | 1 minute |
| Loop | local session | yes | yes | yes | 1 minute |

For us, the relevant equivalents live in Hermes (skills, scheduled tasks via cron, subagents). The principle transfers; the mechanics do not.

### Knowledge system (Karpathy-style markdown wiki)

- Folders only: `raw/` (source clippings), `wiki/` (generated pages), `index`, `log`, optional `hot.md` cache
- No embeddings, no vector DB
- "Literally just a folder with markdown files"
- Examples cited: 23 wiki pages from one article in 10 minutes; 36 YouTube transcripts in 14 minutes; one user reduced 383 scattered files to a compact wiki with 95% token reduction
- Best for small-to-medium knowledge bases, not millions of documents

### What he explicitly recommends *against*

- Overbuilding custom dashboards before proving you'll use them (use Claude artifacts as proof-of-concept first)
- MCP servers when API/CLI would be more token-efficient
- Pasting API keys into chat (use `.env`)
- Browser-automation approaches for routines (cookies / local state not present)
- Large GitHub repos in cloud routines (wastes resources/tokens)

---

## Are we currently applying this mental model?

**Mixed. Stronger alignment than Video 1 on some axes, surprising drift on others.**

### Where we're strongly aligned

- **Skills-as-markdown.** Same underlying pattern as Video 1. Already discussed in [`2026-05-13-anthropic-agent-skills-video.md`](./2026-05-13-anthropic-agent-skills-video.md). Video 2 reinforces with more depth (frontmatter, progressive context loading, the 500-line rule, 6-step build framework).
- **Folder-based knowledge.** `docs/decisions/`, `docs/charter/`, `docs/sessions/`, `docs/reference/`. Not identical to his taxonomy, but the principle matches.
- **Decisions log.** He has a `decisions` folder for "log of important things you decided together." We have [`docs/decisions/approvals-log.md`](../../decisions/approvals-log.md) — same idea, more rigorous schema (intensity field, review-by, references).
- **Reference docs.** He has a `references` folder. We have [`docs/reference/hermes-internals.md`](../../reference/hermes-internals.md) — same pattern.
- **Skill iteration as feedback loop.** Charter Regression Suite (Substrate Brief Item 1) is the same idea — test, find gaps, revise.
- **"Treat AI as mentor, not vending machine"** matches David's charter outcome "Doesn't bullshit me" and the SOUL.md voice section ("ask one sharp question rather than guessing").

### Where we have significant drift

- **No operational/tool/data mapping has happened.** Four C's says start with Context (your work, your tools, your data), then Connections. We have lots of *system* context (ADRs, charter, principles) but **almost no operational context**: no map of revenue sources, no customer system, no comms inventory, no integrations to whatever you use day-to-day. We've been building Atlas in a vacuum — he advises on the *meta-system* but knows nothing about the *operational system* David lives in.
- **No onboarding skill exists.** His onboarding skill creates `about-business.md`, `about-me.md`, `priorities.md`. David's charter file [`outcomes-and-frustrations-2026-05-13.md`](../outcomes-and-frustrations-2026-05-13.md) is *adjacent* to this — it captures outcomes and frustrations — but doesn't capture **what David sells, who he sells it to, what matters this quarter, current 7 buckets, how he sounds**. That's a real gap.
- **No connections layer.** Atlas can't reach ClickUp, can't reach email, can't reach calendar, can't reach any of David's actual work tools. He's an advisor with zero operational reach. The video makes the case (correctly) that capabilities without connections are mostly theoretical.
- **No cadence.** Nothing runs while David sleeps. No "morning coffee" skill that plans the day. No audit that runs weekly. Every interaction is synchronous and David-initiated.
- **The Four C order has been inverted.** We've been working on Capability-shaped substrate (Charter Regression Suite, approval mechanism, decision routing) before either operational Context or Connections are in place. **The Four C's rule says that's wrong sequence.**

### Where the video gets things wrong or is over-fit to its author

- **"Use Claude Code in VS Code" is his runtime.** DavidOS is on Hermes-workspace per [ADR-001](../../decisions/ADR-001-adopt-hermes-workspace.md). Most tactics translate, but not all. Anthropic Cloud Routines don't directly apply; Hermes has equivalents (skills, cron, subagents) but they need to be mapped separately.
- **The 7 buckets are his content business.** Revenue/customer/calendar/comms/tasks/meetings/knowledge maps well to a YouTube + Skool business. David's buckets will differ: enterprise sales pipeline, AI product builds (iZZi, LumList), learning/research, job search prep, family life. Don't copy verbatim.
- **API > MCP for token efficiency** — true today, possibly false tomorrow. Implementation detail.
- **Cadence presupposes autonomy.** Many of his routines run with zero approval prompts. David's charter explicitly requires the opposite — Atlas surfaces decisions for approval per [ADR-004](../../decisions/ADR-004-workspace-native-approval-mechanism.md). Cadence design has to respect that.
- **He sells a community + template.** The video is a funnel. The framework is genuinely useful; the urgency to "buy in now" is marketing pressure. Discount accordingly.

---

## How this interacts with Video 1 (Anthropic Agent Skills)

These two videos largely agree, but Video 2 is the more honest and operational version:

| Topic | Video 1 (Agent Skills) | Video 2 (AIOS Course) |
|---|---|---|
| Core unit | Skill files | Skill files (same) |
| Framing | "Just folders and markdown" | "Folders, markdown, plus Context / Connections / Capabilities / Cadence — in that order" |
| Acknowledges complexity | No — sells simplicity | Yes — explicit 6-step skill build, feedback loop, audit cycle |
| Addresses operational reach | No | Yes — ClickUp / Google Workspace / Fireflies / Stripe / Slack integration patterns |
| Addresses scheduling | No | Yes — routines vs scheduled tasks vs loop distinction |
| Tells you what to skip | No | Yes — "artifacts as proof of concept, only custom dashboards if you actually use them" |
| Caveats acknowledged | No | Yes — 20% productivity dip during change, tools change every 6 months |

**Video 2 is the better mental model for DavidOS.** Video 1 was right about the unit (skills as markdown). Video 2 is right about the *system* (skills + context + connections + cadence, in order).

---

## Mapping to the charter outcomes list

From [`outcomes-and-frustrations-2026-05-13.md`](../outcomes-and-frustrations-2026-05-13.md):

| Outcome | Video 2 alignment |
|---|---|
| Aligned with my goals always | **Strong** — onboarding skill explicitly captures goals and quarterly priorities |
| Applies optimal decision framework | Partial — Four C's is a build framework, not a domain-decision framework |
| Actively self improves | **Strong** — explicit skill feedback loop, audit cycle, level-up skill |
| Always stays current on information | **Strong** — Karpathy wiki for knowledge ingestion |
| Predicts problems and actively avoids them | **Strong** — level-up skill's 5-question framework is exactly forward-looking gap analysis |
| Easy for me to use | **Strong** — slash commands, natural-language triggers, "10-15 min then finished result" goal |
| Is inventive | Partial — depends on skill content |
| Considers monetization | Partial — revenue bucket exists; not a system-level priority |
| Loops me in on decisions that matter | **Weak** — his AIOS is more autonomous than DavidOS's approval-disciplined design |
| Evolves with me | **Strong** — skills get rewritten, audit re-runs |
| Doesn't bullshit me | **Strong** — "treat AI as a mentor, not a vending machine," "never accept AI output without asking why" |

**Net read:** 7 strong / 3 partial / 1 weak. The weak one (loop-in on decisions) is a *deliberate* divergence on his part toward autonomy. DavidOS adopts the opposite posture per ADR-004 — don't adopt that autonomy default.

---

## Concrete implications for the 5-step path

If we adopt Video 2's Four C's framing as our operating mental model, the 5-step path **reorders and gains items**:

| Current step | Reshaped under Four C's order |
|---|---|
| Step 1: Atlas charter-active | **Stays Step 1.** This is partial Context — *system identity*, not operational context. |
| Step 2: Atlas reviews Substrate Brief | **Becomes "Atlas runs onboarding interview against David"** — capture operational context: what David sells, what's selling, what matters this quarter, current 7 buckets for David's work, how he sounds. Outputs: `docs/context/about-david.md`, `docs/context/priorities-2026-Q2.md`, `docs/context/buckets.md`. This is the Context-layer foundation. |
| Step 3: Decisions Register | **Becomes "Connections inventory + first connection"** — map every tool David uses; connect at least one (probably Google Workspace via GWS CLI, since most-leveraged and explicitly recommended). Decisions Register becomes a *skill* (`skill-append-decision.md`) rather than a separate substrate item. |
| Step 4: Roles Register + Session-Start Manifest | **Becomes "First capability skills"** — onboarding (done in new Step 2), audit, level-up, morning coffee. These are Capabilities. Session-Start Manifest collapses into morning coffee skill or its equivalent. |
| Step 5: Project Intake | **Becomes "Cadence — schedule audit + morning coffee + idea-mining on cron."** Includes Project Intake mechanic but reframes it as a skill, not a separate subsystem. |

This is a real restructure. **It's not necessarily right** — it's what adopting Video 2's framing would do to the plan. Worth next-session-Atlas reviewing before committing.

---

## The uncomfortable insight

**The work we've been calling "substrate-first" might actually be Capability-first**, and the real Context (operational) and Connections layers haven't been built yet. The charter file committed tonight is the start of the Context layer at the *system identity* level, but not at the *operational* level — what David actually sells, what his current priorities are, what tools he uses for what.

This is exactly the kind of structural recalibration the Opus-led deep dive would have surfaced. We skipped the deep dive because we trusted the 5-step path. Video 2 is now suggesting the path may have wrong sequencing.

**Don't act on this tonight.** Tomorrow, when next-session-Atlas reviews the charter, the influence notes, and the path, he should consider whether to re-sequence using the Four C's rule.

---

## Open questions for next session

1. Do we adopt the Four C's order rule (Context → Connections → Capabilities → Cadence) as a DavidOS sequencing principle? If yes, becomes ADR-005 or ADR-006.
2. Does Step 2 of the 5-step path get replaced by "Atlas runs onboarding skill against David"? If yes, what does our version of the onboarding interview look like (his 7 questions, adapted to David)?
3. What are *David's* 7 (or N) tier-one buckets? Likely: enterprise sales / iZZi product / LumList / learning & research / family / personal optimization / finance — but David should define them, not us.
4. Which connection do we wire up first? Google Workspace (most-leveraged for David), ClickUp (if used), Linear (since the connector is already in tonight's connector list), Apple HealthKit (already connected per tonight's environment)?
5. How do the Hermes equivalents to his Cloud Routines / Scheduled Tasks / Loop work? Reference: [`docs/reference/hermes-internals.md`](../../reference/hermes-internals.md) Section 5 covers startup; cadence mechanism may need its own research subagent if Hermes docs are thin.
6. Does the "treat AI as mentor, not vending machine" framing belong in Atlas's SOUL.md voice section? Currently the voice section says "ask one sharp question rather than guessing" — adjacent but not identical.
7. How does Video 2's "you should expect a 20% productivity dip during transition" affect David's phase planning? Per the charter, he's prioritizing foundation now then first revenue — the dip is the foundation phase, the rise is supposed to come after. Worth explicitly naming so it isn't experienced as failure.

---

## Recommendation

Do not act on this tonight. The Four C's order rule is the most consequential insight from either video — if it's right, it resequences the 5-step path. The work to fold it in deserves a rested session with charter-active Atlas at the table.

**One rule worth keeping** even before formal adoption: **Context comes before Capabilities.** Before authoring more substrate items (Charter Regression Suite, Roles Register, Session-Start Manifest), capture David's operational context — what he sells, what's selling, what matters this quarter, current tools. Even a single session of operational-context capture would unblock significantly better substrate decisions.
