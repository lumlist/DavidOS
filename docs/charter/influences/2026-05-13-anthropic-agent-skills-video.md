# Influence: Anthropic Agent Skills mental model

**Source:** YouTube — "the most powerful AI tool." by Jake Van Clief, published 2026-05-06 ([video link](https://www.youtube.com/watch?v=-Uk9gsFWBYw))
**Captured:** 2026-05-13 ~3:55 AM CDT
**Status:** Influence under consideration. **Not yet adopted.** Next session decides whether to fold this into SOUL.md / Substrate Brief / 5-step path.
**Surfaced by:** David, end of 2026-05-12 evening session

---

## What the video argues (transcript-grounded summary)

**Thesis in one line:** Stop building multi-agent infrastructure. Use one capable agent plus a folder of markdown skill files plus scripts. That's it.

**Argument structure:**

1. The hard problem is the **"context wall"** — organizing data, processes, instructions, and tools so an AI doesn't get confused or forget across workflows.
2. The popular answer is agentic frameworks (LangGraph and similar) — complex, expensive.
3. Anthropic's answer is **Agent Skills** — a folder convention where each skill is a markdown file describing actions, paired with scripts (`script.py`) for data/tools access.
4. **The wrong pattern:** one agent per workflow ("an agent here, an agent here, seven agents here").
5. **The right pattern:** one agent (e.g. Claude Code) that can read/write/use tools, plus a folder of skill files it loads on demand per task.
6. Skills create **"agents on the fly"** — the same single agent specializes itself per task by loading the relevant skill, rather than the operator pre-building specialized agents.
7. That single agent can spawn many chat instances and sub-agents, scaling without the operator hand-building infrastructure.

**Specifics named in the video:**

| Item | Value |
|---|---|
| File convention | Actions in `skill.md`; data and tools accessed via `script.py` |
| Example main agent | Claude Code |
| Example open-source model | Gemma |
| Frameworks called out as overkill | LangGraph and similar "agentic frameworks" |
| Final framing of the "secret tool" | "A bunch of folders and markdown files" |

---

## Are we currently applying this mental model?

**Partially.** Honest breakdown:

### Where we're aligned

- **One-agent-with-skills, not many-agents-with-overlap.** Atlas is positioned as the single advisor, not as one of many specialized agents. [`ADR-003`](../../decisions/ADR-003-paperclip-frozen-atlas-memo-library.md) explicitly froze Paperclip's multi-agent direction and recast Atlas as a memo library. That is directly the video's "right way."
- **Markdown-files-as-system-prompt.** SOUL.md, ADRs, the charter file ([`outcomes-and-frustrations-2026-05-13.md`](../outcomes-and-frustrations-2026-05-13.md)), the approvals log — all flat markdown. The system architecture *is* "a bunch of folders and markdown files."
- **Hermes natively uses Agent Skills.** The VPS install has `~/.hermes/skills/` with 26 skill directories (visible in `ls` output captured during 2026-05-12 evening session). The Hermes internals reference (`docs/reference/hermes-internals.md`, Section 6) documents how skills load. The runtime we are already on implements the video's recommended pattern.

### Where we have drifted from it

- **We've been pulled toward multi-agent thinking.** The Hermes research subagent spawned on 2026-05-12 was the right call (a one-off research task). The broader temptation to "have Atlas, then a Builder agent, then a Roles agent…" is exactly the "seven agents here" pattern the video flags as wrong.
- **The Substrate Brief items lean toward complex infrastructure** rather than "more skills + more markdown." The Charter Regression Suite, Decisions Register, Roles Register, and Session-Start Manifest could all be implemented as **skill files** rather than separate subsystems. They have not been framed that way to date.
- **SOUL.md is bloating.** The v0.2 draft has 7 principles, 9 file loads, boundaries, voice, and verification all in one document. The cleaner pattern would be a minimal SOUL.md plus a folder of skill files Atlas loads per task. We are currently carrying complexity in SOUL.md that may belong in skills.

---

## Should we apply this more deliberately?

**Yes, with one caveat.**

### Why yes

1. **It is already the runtime we are on.** Hermes implements Agent Skills natively. Fighting against the runtime is fighting the platform.
2. **It directly addresses Frustration 3** from the charter primary source ("hard to conceptualize what I'm building, stay organized"). Folders + markdown is the simplest possible organization scheme. The system is readable. It is greppable. It is diffable.
3. **It directly addresses Frustration 1** ("don't know modern AI best practices"). Anthropic itself shipped this pattern — it *is* the modern best practice for the runtime tier we are operating at.
4. **It reduces substrate scope.** Several items in the Substrate Brief may collapse into skill files rather than full registers. Cheaper to ship, easier to maintain, easier to revise.
5. **The "agents on the fly" model maps cleanly to David's goal of a system that handles many ideas.** One Atlas + folder of skills per project type = the Project Intake pattern scoped for Step 5 of the 5-step path.

### The caveat — what the video gets wrong or oversimplifies

1. **Skills aren't free of orchestration logic.** When there are 100 skills, knowing which to load when *is* the problem. The video hand-waves this. A routing convention is still required: file naming, frontmatter metadata, skill-discovery patterns. Hermes provides some of this; DavidOS-specific skills would need their own conventions defined.
2. **Single-agent does not scale to truly parallel work.** Research, deep analysis, and long-running tasks still benefit from subagents — tonight's Hermes research subagent is the proof point. The video frames subagents as "spawned by the main agent on demand," which is correct, but doesn't acknowledge that subagent orchestration is still meaningful infrastructure when done well.
3. **Skill files can drift just like agents can.** The failure mode captured tonight ("Atlas was never charter-active") has an equivalent in a skills world: "the skill file said X but the agent loaded Y, or didn't load it at all." Same verification problem, different wrapper. Charter Regression Suite remains necessary.
4. **"Just markdown" is a marketing claim.** The video sells simplicity. Reality is markdown + frontmatter conventions + `script.py` for tools + skill discovery rules + version control + drift detection. Still simpler than LangGraph. Not free.

---

## Implications for the 5-step path (if adopted)

The 5-step path sequence doesn't change. The *implementation* changes:

| Step | Without skill-first framing | With skill-first framing |
|---|---|---|
| 1 — Atlas charter-active | SOUL.md carries 7 principles, 9 file loads, etc. | SOUL.md stays minimal (identity + canary + "load skills from `docs/skills/` as needed"). Most current operating principles become individual skill files. |
| 2 — Substrate Brief review | Atlas loads SOUL.md, reviews brief in one long prompt. | Atlas loads a `skill-substrate-brief-review.md` rather than carrying everything in SOUL.md. |
| 3 — Decisions Register + Approvals polish | Register is a flat file; approvals log is appended manually. | Register stays as data, but appending becomes a skill: `skill-append-approval.md` invoked by any agent action. |
| 4 — Roles Register + Session-Start Manifest | Manifest is a standalone document. | Manifest is almost certainly itself a skill: a markdown file that says "at session start, read these files in this order." Roles Register stays as data. |
| 5 — Project Intake | Intake form + lifecycle definitions. | Intake becomes a folder of skills: `skill-idea-intake.md`, `skill-revenue-fastest-path.md`, `skill-business-component-lifecycle.md`, `skill-personal-system-lifecycle.md`. Lifecycles are skills, not agents. |

---

## Mapping to the charter outcomes list

From [`outcomes-and-frustrations-2026-05-13.md`](../outcomes-and-frustrations-2026-05-13.md):

| Outcome | Video alignment |
|---|---|
| Aligned with my goals always | Neutral — skill files don't inherently increase alignment, but they make alignment auditable in a way agent black-boxes don't. |
| Applies optimal decision framework | Partial — skills can encode frameworks, but the video doesn't address how frameworks compose or conflict. |
| Actively self improves | Strong fit — skills are revisable text files. The system can rewrite its own skills as it learns. |
| Always stays current on information | Neutral — orthogonal to skill model. |
| Predicts problems and actively avoids them | Weak — the video doesn't address forward-looking analysis. |
| Easy for me to use | Strong fit — flat folders and markdown are the easiest possible mental model. |
| Is inventive | Neutral. |
| Considers monetization | Neutral — skills can be designed for revenue-fastest-path; the video doesn't speak to this. |
| Loops me in on decisions that matter | Strong fit — `skill-append-approval.md` style enforces the loop-in pattern. |
| Evolves with me | Strong fit — same reason as self-improvement; markdown is editable. |
| Doesn't bullshit me | Partial — video itself oversimplifies, which is a yellow flag for adopting its claims uncritically. |

**Net read:** The mental model aligns with 5 of 11 outcomes strongly, 4 neutrally, and 2 partially. No outcome is anti-aligned. The strongest fit is on the outcomes that match David's most acute frustrations (ease of use, evolution, loop-in).

---

## Open questions for next session

1. Do we formally adopt "skill-first" as a DavidOS design principle? If yes, it probably becomes ADR-005 ("Adopt Agent Skills as the primary unit of system extension") with an explicit "Only escalate to register, subagent, or subsystem when X conditions met" boundary.
2. Which Substrate Brief items collapse into skill files versus remaining as standalone substrate? Tentative read above suggests Roles Register and Session-Start Manifest may be skill-shaped; Decisions Register stays data; Charter Regression Suite stays a separate test harness; Project Intake becomes a folder of skills.
3. How does the SOUL.md draft v0.2 (paused mid-review) change if we adopt this framing? Operating principles section especially — does each principle become its own skill file?
4. What is the DavidOS skill-discovery convention? File naming, frontmatter metadata, location (`docs/skills/`? `skills/`?), versioning. Needs to be decided before authoring the first DavidOS skill.
5. The video's `skill.md` + `script.py` convention — does that map cleanly to Hermes' existing skill format, or do we need a translation layer? Reference: `docs/reference/hermes-internals.md` Section 6.

---

## Recommendation

Do not act on this tonight. The mental model is worth adopting deliberately. The work to fold it into the substrate plan is meaningful enough that it deserves a rested session — likely the first half of next session after the charter review.

**One rule worth keeping** even before formal adoption: **if a piece of substrate can be a skill file, it should be.** Only when something genuinely needs to be its own register, subagent, or subsystem do we make it more than a markdown file. That single rule, applied as a default during the upcoming substrate work, will pull the implementation toward the video's mental model without requiring a full adoption decision tonight.
