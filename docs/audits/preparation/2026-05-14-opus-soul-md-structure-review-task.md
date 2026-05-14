# Opus Task: SOUL.md Structure Review

**Date:** 2026-05-14
**Model:** Opus (explicitly approved by David for this task)
**Triggered by:** David's question — "Is our soul file too dense? Are there more optimal and higher-leverage ways to ensure Atlas is operating as intended (such as decoupling certain instructions to system/tasks/skills/processes) that would have a better effect with less contextual overhead?"
**Stakes:** Foundational. SOUL.md shape affects every Atlas session for the foreseeable future. Wrong call = months of context-overhead tax OR invisible behavior drift from over-aggressive compression.

---

## Context Opus must read before answering

1. `/home/user/workspace/davidos-repo/SOUL.md` — the artifact under review (1,823 words, §6 is 935 words / 51% of total)
2. `/home/user/workspace/davidos-repo/docs/autonomy/SCHEMA.md` — autonomy schema (rungs + fields)
3. `/home/user/workspace/davidos-repo/docs/autonomy/action-map.md` — 22 action categories with rungs
4. `/home/user/workspace/davidos-repo/docs/autonomy/modifiers.md` — 3 modifiers
5. `/home/user/workspace/davidos-repo/docs/autonomy/README.md` — orientation for the autonomy files
6. `/home/user/workspace/davidos-repo/docs/decisions/ADR-001-adopt-hermes-workspace.md`
7. `/home/user/workspace/davidos-repo/docs/decisions/ADR-002-anthropic-oauth-over-api-key.md`
8. `/home/user/workspace/davidos-repo/docs/decisions/ADR-003-paperclip-frozen-atlas-memo-library.md`
9. `/home/user/workspace/davidos-repo/docs/decisions/ADR-004-workspace-native-approval-mechanism.md`
10. `/home/user/workspace/davidos-repo/docs/audits/preparation/2026-05-13-task2-consolidated-principles.md` — 7 consolidated principles (P1–P7)
11. `/home/user/workspace/davidos-repo/docs/audits/preparation/2026-05-13-task4-knowledge-pack-integration.md` — knowledge pack integration findings
12. `/home/user/workspace/davidos-repo/docs/audits/preparation/2026-05-13-task5-soul-md-text-integration.md` — the round-trip that produced current SOUL.md text
13. `/home/user/workspace/davidos-repo/docs/reference/hermes-operating-knowledge-pack.md` — confirms Hermes is an actor not recommender; especially §H5 on skills guard
14. `/home/user/workspace/davidos-repo/docs/charter/outcomes-and-frustrations-2026-05-13.md` — David's ground-truth outcomes
15. `/home/user/workspace/davidos-repo/docs/charter/davidos-design-principles-source-2026-05-13.md` — verbatim design principles
16. `/home/user/workspace/davidos-repo/skills/davidos-opportunity-scan/SKILL.md`, `davidos-leverage-assessment/SKILL.md`, `davidos-tactic-research/SKILL.md` — three new skill stubs SOUL.md §7.3 routes to

## Operating constraints Opus must respect

- **Sonnet-class is the default for Atlas runtime.** SOUL.md is loaded into Atlas's context every session. Token weight matters.
- **Customer-zero framing.** David's outcomes come first; generalization is second-pass. Don't optimize for generalizability.
- **Fresh context per session.** Atlas does not persist state. Everything in SOUL.md must earn its place against the cost of re-loading it every time.
- **Canonical-file pointer pattern is already established and working.** The autonomy map split (action-map.md / modifiers.md / SCHEMA.md) is the proof-of-concept for "structured policy in files, thin pointers in identity."
- **No Opus references for runtime Atlas.** Atlas reads SOUL.md as Sonnet. Whatever Opus recommends must work for a Sonnet-class model loading this on every session.

## Sonnet's preliminary analysis (for Opus to validate, refine, or reject)

Sonnet's quick read flagged:

**Density breakdown:**
- §4 Identity context: 131 words (load-bearing — file list)
- §5 Operating principles: 178 words (6 principles)
- §6 Boundaries and Autonomy: **935 words / 51% of document**
- §7 Voice: 367 words (general voice + epistemic tagging + opportunity surfacing)
- §8 Verification: 35 words (canary)
- §9 Status: 65 words

**Sonnet's proposed §6 compression (Opus should validate or reject):**

| §6 content | Sonnet's take | Where it should live |
|---|---|---|
| Four-condition act-without-asking test | Load-bearing | SOUL.md |
| 80%/80% thresholds | Load-bearing | SOUL.md |
| List of "working motions" examples | Redundant | action-map.md (already there) — delete from SOUL.md |
| "Always ask" list | Redundant | ADR-004 + action-map.md L1 rows — delete from SOUL.md |
| Advisory vs. decisive subsection | Load-bearing | SOUL.md (no other home) |
| "Recommending without assuming" | Compressible | 1 sentence in SOUL.md, full version in a process doc |
| SOUL.md autonomy-edit policy paragraph | Wrong home | Move to SCHEMA.md §"Editing this map" |
| "Participating in structural decisions" | Load-bearing | SOUL.md (judgment, not policy) |
| "When I am wrong" 3-step protocol | Load-bearing | SOUL.md (identity behavior) |
| Hermes config snippet | Wrong home | Move to a new `docs/reference/hermes-config.md` (P0.3 anyway) |

Sonnet's projected post-compression: §6 drops from 935 → ~350-400 words. SOUL.md total drops to ~1,250 (~30% reduction).

**§7 take:** Leave as-is for v1.0. Epistemic tagging is load-bearing identity. Opportunity surfacing posture is load-bearing identity. The three skill names in §7.3 could later move to a `docs/atlas/skill-routing.md` but it's not worth it until skill count >~10.

## What Opus must produce

A verdict + structured recommendation, addressing each of these explicitly:

### 1. Is SOUL.md too dense? Verdict.
Answer concretely: yes / no / partially. Cite specific sections. Compare against published agent identity / system prompt design patterns where useful (Anthropic published guidance, OpenAI/Operator, Cognition/Devin, etc.) — but only research if it would materially change the recommendation. Time budget for research: 10–15 minutes max.

### 2. What is the highest-leverage structure for SOUL.md?
Specifically:
- (a) Which content categories belong in identity layer (must be loaded every session)?
- (b) Which belong in canonical pointer files (referenced by path, loaded on demand)?
- (c) Which belong in skills (invoked deliberately)?
- (d) Which belong in tasks / processes (executed in workflows)?
- (e) Which belong in ADRs (decision records)?

Validate or reject Sonnet's table above. If you reject, explain why and propose the alternative.

### 3. Is there content currently MISSING from SOUL.md that should be there?
Audit against:
- The 7 consolidated principles (Task 2)
- The 11 outcomes / 3 frustrations / 3 clarifications (`outcomes-and-frustrations-2026-05-13.md`)
- The Hermes Operating Knowledge Pack findings (especially §H sections David hasn't explicitly addressed in SOUL.md)
- Customer-zero pattern requirements

### 4. What is the right total word count target?
Given Hermes load patterns (SOUL.md loaded fresh every session), Sonnet's context window, and the value of leaving room for the actual conversation — what should SOUL.md aim for? Sonnet's instinct: ~1,250 words. Validate or revise with reasoning.

### 5. Should the canonical-file pointer pattern be extended?
The autonomy map split worked. Should the same pattern be applied to:
- Voice / epistemic tagging policies (§7)?
- Operating principles (§5)?
- Identity load list (§4)?
- Verification mechanics (§8)?

For each, name the tradeoff: load-time cost of file reads vs. context-savings of thinner SOUL.md.

### 6. Self-assessment mechanism (David's flag)
David explicitly flagged this:
> "This is a good example of a configuration that I want our system to have mechanisms in place to assess and improve (a skill that's called by atlas perhaps, or a scheduled agent optimization task, or systemic flag of some kind)."

Propose the highest-leverage mechanism for SOUL.md (and similar foundational configurations) to be assessed and improved over time. Options to evaluate:
- (a) Atlas skill: `davidos-soul-md-audit` or similar
- (b) Scheduled cron task that surfaces drift signals
- (c) Section 7.3 leverage-flag pattern extended to "configuration drift" flags
- (d) ADR-style "structural review" cadence
- (e) Something else entirely

Recommend one. Justify against the alternatives.

### 7. Proposed v1.1 SOUL.md (full text)
Produce the full proposed v1.1 document. David and Computer-Sonnet will review against current v1.0 before approving.

### 8. Risk flags
For any content you propose moving OUT of SOUL.md:
- What's the behavior-drift risk?
- How would we detect drift post-activation?
- What's the rollback path if drift occurs?

### 9. Confidence tagging per §7.2
Apply [verified] / [inferring] / [estimating] / [unknown] tags throughout your recommendation. Where you're inferring something material, name the inference explicitly and propose how confidence could be improved.

## Output

Save to: `/home/user/workspace/davidos-repo/docs/audits/preparation/2026-05-14-opus-soul-md-structure-review-output.md`

Structure:
1. Executive verdict (1 paragraph)
2. Detailed answers to questions 1–8
3. Proposed v1.1 SOUL.md (full text in a fenced code block)
4. Risk register
5. Confidence summary

## Sonnet's biases Opus should watch for

- **Sonnet's compression instinct may be too aggressive.** Sonnet doesn't have first-hand experience of which content quietly load-bears for an agent in production. Opus should be skeptical of any "move this out" recommendation and ask "what's the failure mode if Atlas drifts on this?"
- **Sonnet didn't research.** Opus should check current best-practice patterns from published agent designs before validating Sonnet's structural recommendations.
- **Sonnet may have missed reordering opportunities.** Current section order is 4, 5, 6, 7, 8, 9. Is that the right order for a fresh-context load? (Identity → principles → boundaries → voice → verification → status.) Could reordering improve effective density?

## Non-goals for this task

- Do not rewrite Sections 1–3. They don't exist (intentional — SOUL.md starts at §4 in the substrate-brief inheritance).
- Do not propose changing the canary mechanism (§8). It's solved.
- Do not propose changing the 80%/80% thresholds without strong evidence. David explicitly chose those.
- Do not generalize for "future iZZi customers." This is customer-zero work. Optimize for David's Atlas.
