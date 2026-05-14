# Karrigan — Intent Capture (David's verbatim, 2026-05-14 00:25 CDT)

**Status:** Forward-looking roadmap artifact. Karrigan does not exist yet. This document captures David's verbatim intent for the second agent in DavidOS, surfaced during the 2026-05-13 → 2026-05-14 evening session while Atlas activation was in progress.

**Trigger:** David surfaced Karrigan as the next agent to build after Atlas activation completes and the 2026-05-13 structural audit lands.

**Sequencing:** Karrigan is **post-audit work**. Sequence is: complete tonight's Phase 0 (Atlas activation) → run the structural audit in a future session → Karrigan design and build as a substrate item in Phase 1 or Phase 2.

---

## What David said (verbatim)

> Once we have atlas online and the audit is complete, I'd like to build karrigan next. He will be my input coach within the system and the agent i work with to ensure I'm putting the highest leverage prompts into the system and focusing my time in the right places. Him and i will be conversational in nature and he will have reactive and scheduled skills to provide me prompt guidance, help me stay organized/improve UX and conduct research/experiments to always be aware of the best tactics and strategies for operators and the tools/UI I'm engaging with and plan to engage with. I want him to be higher models by default for reasoning tasks.

---

## What this tells us about Karrigan's role

Captured for future design work; not implementation guidance.

### Role
- **Input coach.** David's interface partner. Focused on improving the quality of David's prompts and the focus of David's attention.
- **Highest-leverage filter.** Helps David put the right prompts into the system and focus time on the right things.

### Mode
- **Conversational by default.** Karrigan and David interact in dialogue, not in formal approval rituals.
- **Reactive skills.** Karrigan responds to David's working state in the moment.
- **Scheduled skills.** Karrigan runs cadence-based work (research, experiments, monitoring).

### Functions
- Prompt guidance — surface higher-leverage prompts as David works
- Organization and UX improvement — help David stay organized; surface UX improvements
- Research and experimentation — stay aware of the best tactics and strategies for operators and the tools/UI David is engaging with and plans to engage with

### Model selection
- **Higher models by default for reasoning tasks.** This is a deliberate deviation from SOUL.md's default cost-aware "Sonnet-class only" posture for Atlas. Karrigan's reasoning work warrants higher-model spend.

---

## How this interacts with what exists now

### The autonomy schema was designed for this

The action-map-with-modifiers structure we locked in tonight (P0.1a) is principle-aligned partly because future agents like Karrigan inherit the canonical action map automatically. When Karrigan is built, his actor-specific deviations from the baseline will be expressed as modifiers in `docs/autonomy/modifiers.md`, not as a separate autonomy file. This validates the principle-grounded reasoning behind the structural choice — and Karrigan will be the first real test of whether the multi-agent autonomy structure works in practice.

### Karrigan modifiers will likely include
- **Higher-model defaults** — Karrigan's reasoning tasks use higher models than Atlas's. This is either a modifier on a specific category ("Reasoning tasks: Karrigan uses Opus-class") or a Karrigan-actor-wide profile setting.
- **Conversational vs approval-disciplined posture** — Karrigan operates more conversationally than Atlas. Modifier expression of this is an open design question.
- **Scheduled skill autonomy** — Karrigan's scheduled work runs at L4 (Schedules and Acts), subject to the same schedule-approval mechanism as Atlas's L4 actions.

### Karrigan extends the substrate, doesn't replace it
- Karrigan does not replace Atlas. Atlas remains the Chief Systems Advisor; Karrigan is the input coach.
- Karrigan operates under the same SOUL.md / AGENTS.md framework (with his own identity layer for what makes him Karrigan-specifically).
- Karrigan inherits the consolidated principles, the charter outcomes, and the ADR-004 approval mechanism.

---

## Karrigan-specific outcome alignment (preliminary)

Mapping Karrigan's stated functions to the 11 charter outcomes:

| Charter outcome | Karrigan's contribution |
|---|---|
| O1 Aligned with my goals always | Strong — input coach directly serves goal alignment |
| O2 Optimal decision framework | Indirect — improves David's framing of decisions |
| O3 Actively self improves | Strong — scheduled research keeps Karrigan current |
| O4 Always stays current on information | **Strong — direct match** ("conduct research/experiments to always be aware of the best tactics and strategies") |
| O5 Predicts problems and actively avoids them | Strong — input coach catches low-leverage time spend before it happens |
| O6 Easy for me to use | **Strong — direct match** ("help me stay organized/improve UX") |
| O7 Is inventive to help me achieve my goals | Moderate — research surfaces new tactics |
| O8 Always considers if and how I could make money | Indirect — depends on how Karrigan's research scope is shaped |
| O9 Loops me in on the decisions that matter | Strong — conversational mode is loop-in by design |
| O10 Evolves with me | Strong — scheduled awareness keeps the system current |
| O11 Doesn't bullshit me | Strong — input coach role requires epistemic honesty |

**Notable:** Karrigan addresses O4 and O6 directly in ways Atlas does not. Atlas's role is structural advice; Karrigan's role is operational coaching and organization. The two agents are complementary, not redundant.

---

## What needs to happen before Karrigan can be built

Hard prerequisites:
1. Atlas charter-active (tonight's P0.2)
2. Structural audit complete (future session)
3. Phase 1 substrate landed: AGENTS.md, davidos-router skill, davidos-evaluation skill (per audit verdict)

Soft prerequisites (highly recommended, may be Karrigan-blockers):
1. The autonomy schema-review task completed by Atlas (per `2026-05-13-phase1-schema-review-task.md`) — confirms the multi-agent structure is sound before adding a second agent
2. At least one operational context capture session — Karrigan needs to know what David is actually working on to coach effectively

---

## Open design questions for Karrigan (do not answer tonight)

1. Is Karrigan a separate Hermes profile (his own `~/.hermes/profiles/karrigan/`) or a different identity layer on top of the same profile?
2. How does the conversational-vs-approval-disciplined distinction get expressed? Through SOUL.md voice differences, through modifier rules, or through a different approval intensity scheme?
3. Does Karrigan have his own canary string for charter-active verification, or does he inherit Atlas's verification mechanism with a Karrigan-specific extension?
4. What's the relationship between Atlas and Karrigan when they're both active? Does Atlas spawn Karrigan as a subagent? Are they peers? Does David explicitly switch profiles?
5. Karrigan's "higher models for reasoning tasks" — Opus-class by default, or selectively per task? Cost implications.
6. Karrigan's scheduled research — what's the cadence? What sources? What's the output format that lands in DavidOS state?
7. UX improvement scope — is Karrigan recommending workflow changes to David, or does he have authority to propose Hermes config tweaks, or both?

---

## How to use this document

When Karrigan design work begins (post-audit), this document is the primary-source intent statement. Do not paraphrase. Use it the same way you use `outcomes-and-frustrations-2026-05-13.md` — derivative documents (Karrigan SOUL.md, Karrigan onboarding, Karrigan modifier rules) reference this file directly.

If David revises the Karrigan intent before construction begins, capture the revision as a new dated file (`2026-MM-DD-karrigan-intent-capture.md`) alongside this one rather than overwriting.

**Do not edit this file.** It is a primary-source intent capture.
