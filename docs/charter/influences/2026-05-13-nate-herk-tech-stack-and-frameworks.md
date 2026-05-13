# Influence: Nate Herk — Tech Stack Tier List + Decision Frameworks

**Source:** YouTube — "Overwhelmed By AI? Just Copy My Tech Stack" by Nate Herk | AI Automation, published 2026-05-08 ([video link](https://www.youtube.com/watch?v=35WuZxbAY68))
**Captured:** 2026-05-13 ~4:36 AM CDT
**Status:** Influence under consideration. **Not yet adopted.** The decision framework and "needle moved" framing are the strongest takeaways; the tool tier list is *his* business and is not directly transferable.
**Surfaced by:** David, end of 2026-05-12 evening session

---

## What the video argues (transcript-grounded summary)

**Thesis in one line:** Keep your AI stack lean, anchor on daily drivers that move the needle, evaluate every new tool against a current pain point — and build directories that outlive whatever tool is hot today.

### Three layers of value

1. A specific tier list of tools — useful as a data point, not a recommendation to copy
2. A set of mindset shifts about how to think about tools and switching
3. A formal decision framework for evaluating new tools

The tier list is surface content. The frameworks are the real substance.

### Key direct quotes

- "Coding agents are just harnesses. They're all just AI that work inside some sort of directory."
- "Build directories like they're going to outlive any tool because they will."
- "Productivity is needle moved per hour, not hours worked."
- "Every single time you make a switch in your business, you are going to maybe lose about 20% of your efficiency... is that dip going to ultimately take me higher than where I would have been?"
- "There's a difference between knowing the what and knowing the how. And sometimes you only need to know all the what's. You don't need to know the how's."

### His tier list (his business, not a recommendation for DavidOS)

| Tier | Tools |
|---|---|
| S — Daily Drivers | Claude Code, VS Code, Glydo (speech-to-text) |
| A — Weekly Tools | Codex, Claude chat, Hermes agent, Perplexity, Groq |
| B — Specialists | Hostinger, ClickUp, Fireflies, Apify, GPT image 2, Nano Banana 2, key.ai, Open Router, HeyGen, Eleven Labs, Cloud Design |
| C — Experimenting | Gemini, Anti-Gravity, Ollama, Manifold |
| Graduated | ChatGPT regular chat, Open Claude, Cursor, Notebook LM, Poppy AI, Anytten, WhisperFlow |

He explicitly says graduated tools "doesn't mean they are trash" — it means he extracted the features he liked and worked them into his own ecosystem rather than continuing to pay for them.

### His decision framework for adopting new tools

A clean rule, paraphrased:

> When a new tool/feature/video appears, ask: **does this solve a pain point I have right now?**
> - If no → save the link, do nothing else
> - If yes → test in a real workflow (not mock data, not theoretical), low-risk surface, time-boxed
> - After the test → does this move into daily drivers, or get cut?

### His other named rules

- "AI tools are just harnesses" — the directory is the asset, the tool is the interface
- "Build directories to outlive any tool"
- "20% productivity dip rule" — every switch costs efficiency; require the dip to clear a bar
- "Productivity = needle moved per hour, not hours worked"
- North Star framework — identify yours and evaluate every new shiny against it
- Tool-agnostic mindset — "think about what will never change, not what will change"
- Process decomposition — "for this specific task in this specific context, which tool is best"
- Knowing the what vs the how — "sometimes you only need to know all the what's"

---

## Frameworks ranked by transferability to DavidOS

### Strongly transferable

1. **"AI tools are just harnesses"** — directly maps to ADR-001 reasoning. Hermes-workspace is the daily driver, DavidOS is the asset, the asset survives a runtime change.
2. **"Build directories to outlive any tool"** — exactly what we've been doing all night. Repo is portable. Markdown is durable.
3. **"20% productivity dip rule"** — names the cost of every switch, including the substrate-first foundation phase David is in right now. Naming the dip explicitly defuses some of Frustration 1 ("am I wasting time?"). The answer: yes, productivity is lower this week, that's the cost of durable foundation, it's expected.
4. **"Productivity = needle moved per hour"** — directly serves David's milestone-tracking ask from the charter file. System should surface needle moved, not hours spent.
5. **The decision framework for new tools** — directly addresses Frustration 1 ("question what I'm building every time I see something new on YouTube"). Gives David a defensible "not now" answer to anything novel that doesn't match a current pain.

### Transferable with framing

6. **North Star framework** — David's 11-point outcome list *is* the North Star. Worth making explicit that the charter file functions as the North Star and that every new influence/tool/framework gets evaluated against it.
7. **Tool-agnostic mindset** — already encoded in ADR-001 and ADR-002. Reinforces existing posture.
8. **"Knowing the what vs the how"** — reframes Frustration 1 as permission. David specifies the *what*; Atlas handles the *how*. Worth naming explicitly somewhere in SOUL.md or operating-spec.

### Not directly transferable

- The specific tool tier list (his business is YouTube content + AI community)
- The exact 7 buckets (those are his work, not David's)
- Tool-by-tool API > MCP recommendations (true today, possibly false tomorrow)

---

## Tool observations (data points, not recommendations)

A few items in his stack are worth noticing without adopting:

| Tool | What's relevant |
|---|---|
| **Hermes agent** | A-tier in his stack — validates ADR-001's choice. Also names features ("instant crons," Telegram bridge) DavidOS hasn't explored yet. |
| **Perplexity** | A-tier for research, especially feeding agent workflows. David already has Perplexity as Computer. The pattern ("Perplexity for research → Claude Code/Hermes for synthesis") matches what tonight's session did with the Hermes research subagent. |
| **Glydo / WhisperFlow** | Speech-to-text, his S-tier. Worth saving as a link given David's late-night working schedule. Not a now-pain. |
| **Cloud Design** | Specialist tool for shared design systems. Possibly relevant for LumList UI later. Save the link. |

Tools to actively NOT adopt without reason: GPT image 2, Nano Banana, key.ai, Eleven Labs, HeyGen, Codex, Apify. All possibly useful, all distractions from foundation work right now. Apply his own rule to his own list.

---

## Are we currently applying this mental model?

**Mostly yes on principles. Partially on discipline. Has gaps.**

### Where we're aligned

- Directory-as-asset (DavidOS repo is the asset; tool choices are downstream)
- Hermes as daily driver (ADR-001 picked this with eyes open)
- Lean stack (ADRs, charter, decisions, sessions, reference, influences — minimal)
- Tool-agnostic mindset (repo would survive Hermes shutdown)
- Skills-as-markdown (directionally adopted per Video 1 and Video 2 influence notes)

### Where we have drift or gaps

- **No decision framework for "should I act on this new thing I just saw."** Frustration 1 is exactly this gap. His framework is the answer.
- **Productivity has been measured in hours and decisions, not needle moved.** Tonight's session record uses "zero substrate items shipped" framing (which is needle-moved-shaped), but there's no system-level indicator. Milestone tracking should be needle-moved framed.
- **No "test in real workflow" discipline yet.** When we adopt skill-first framing or Four C's, how do we test? Should be against real prior sessions and pending decisions, not synthetic prompts.
- **The 20% dip isn't named.** David is in it right now. The substrate-first foundation phase *is* the dip. Not naming it generates anxiety; naming it defuses Frustration 1.

---

## How Video 3 composes with Videos 1 and 2

| Layer | Video | What it provides |
|---|---|---|
| **Filter / mindset** | Video 3 (this) | Decision discipline, North Star anchoring, dip-aware switching |
| **Architecture** | Video 2 (Nate Herk AIOS course) | System structure via Four C's, build order |
| **Mechanism** | Video 1 (Anthropic Agent Skills) | Skills as markdown, the core implementation unit |

The three videos compose well as a stack — filter on top, then architecture, then mechanism. Video 3 is the smallest and most operationally protective: it gives David a way to engage with the constant stream of new content without it pulling him off course.

---

## Mapping to the charter outcomes list

From [`outcomes-and-frustrations-2026-05-13.md`](../outcomes-and-frustrations-2026-05-13.md):

| Outcome | Video 3 alignment |
|---|---|
| Aligned with my goals always | **Strong** — North Star framing |
| Applies optimal decision framework | **Strong** — explicit, repeatable decision rule for tool adoption |
| Actively self improves | Partial — graduated-tools concept implies pruning |
| Always stays current on information | Partial — "save the link" addresses currency without forcing adoption |
| Predicts problems and actively avoids them | **Strong** — 20% dip rule forces forward-looking evaluation |
| Easy for me to use | **Strong** — lean stack, daily drivers |
| Is inventive | Neutral |
| Considers monetization | Weak — not addressed |
| Loops me in on decisions that matter | Partial — operator-side discipline, transferable to agent-side |
| Evolves with me | **Strong** — graduated tools, swap when better tool clears the dip bar |
| Doesn't bullshit me | **Strong** — "test in real workflow," "save the link if no current pain," names productivity dip honestly |

**Net read:** 6 strong / 3 partial / 1 neutral / 1 weak. Highest concentration of strong matches across the three influence videos.

---

## Concrete implications

Video 3 doesn't restructure the 5-step path (Video 2 has that question). Video 3 adds **operating discipline** the path needs regardless of how it's sequenced.

**What it adds:**

1. A formal "should-we-adopt-this" rule for handling future tool/framework/video influences. Likely becomes a skill (`skill-evaluate-new-influence.md`) or an ADR.
2. A "20% dip is expected" framing for the current foundation phase. Affects how David experiences and describes the work.
3. A "needle moved per hour" framing for productivity and milestone tracking. Directly serves the milestone-tracking ask.
4. A "what vs how" division of labor — David specifies what, Atlas handles how. Possibly belongs in SOUL.md voice section or operating-spec.

---

## Open questions for next session

1. Adopt the decision framework as a formal DavidOS pattern? Likely becomes ADR-005 or 006 — "Decision rule for adopting new tools, frameworks, or influences."
2. Reframe milestone tracking as "needle moved" rather than "tasks completed" or "hours worked"?
3. Should "the 20% dip is the foundation phase" be added to the charter file or kept as influence-only framing?
4. Should the "what vs how" division belong in SOUL.md voice section explicitly?

---

## Recommendation

Adopt the decision framework and the "needle moved" framing as soon as next-session-Atlas reviews this note. They're the smallest, most defensible additions across all three influences and they directly address David's stated frustrations.

The tool tier list is a useful data point but should not drive any DavidOS tool decision tonight or tomorrow. Apply the decision framework to it: do any of his tools solve a pain David has *right now*? Probably no. Save the links. Move on.
