---
name: davidos-tactic-research
description: When a creativity tactic, prompt pattern, or methodology in DavidOS itself needs sharpening — research how others have refined it, what failure modes are known, and propose a tighter version. Use when David says "this tactic feels weak" / "find a better version of X" / "research how people are using Y in 2026."
optimization_status: STUB — tag for optimization after first 1-2 invocations
---

# davidos-tactic-research

> **Optimization tag:** v0.1 stub. After real use, calibrate: how deep should research go before diminishing returns? Should this skill auto-spawn a research subagent, or always run in-session? Should output format be a draft replacement tactic, or a side-by-side comparison?

## When to load

- David flags that a tactic, prompt pattern, or methodology isn't producing the leverage he expected
- A skill (especially `davidos-opportunity-scan`) has been invoked 2+ times and the output quality is inconsistent — root-cause may be the tactics themselves
- David asks "is there a better version of this prompt / pattern / framework?"
- New research/publication/method has surfaced (e.g., from a YouTube video, paper, post) and David wants a tactic refresh

## Inputs Atlas should confirm

1. **The tactic / pattern under review** — quote it. Source it. (e.g., "tactic #4 from `docs/charter/influences/2026-05-14-creativity-tactics-source.md`")
2. **What's failing** — output is generic? Output is too narrow? Output ignores constraints? Or "I just want to refresh this with current best practice"?
3. **Depth budget** — quick check (15 minutes, web search only) or deep pass (research subagent, multi-source synthesis)?

## Execution pattern

### Quick mode
- 3–5 targeted web searches for current (2025–2026) refinements of the tactic
- Identify 2–3 known failure modes from practitioner sources
- Propose a tightened version with rationale
- Output: side-by-side old vs. proposed

### Deep mode
- Spawn a research subagent with a tight objective (per `<subagent_usage>` patterns)
- Subagent saves findings to a workspace file
- Atlas reads, synthesizes, proposes 1–3 candidate replacement tactics
- Output: ranked candidates with tradeoffs

### Always
- Cite primary sources for any claim about what works / what fails
- Tag confidence per §7.2 (the proposed tactic is `[inferring]` until it's tested)
- Recommend a test plan: how would David know within 1–2 invocations whether the new version is better?

## Output

1. **Diagnosis** — what's wrong with the current tactic, with evidence
2. **Proposed replacement** — the tightened version
3. **Why this is better** — mechanism, not vibes
4. **Test plan** — how to know if it actually is better
5. **Update target** — which file gets edited if approved (usually a skill SKILL.md or a primary source in `docs/charter/influences/`)

If the update target is a primary source file, Atlas does NOT edit it silently — primary sources are do-not-paraphrase. Atlas proposes a new dated influence file instead, and flags the original as superseded.

## Reference

- `docs/charter/influences/` (all primary-source tactics live here)
- `skills/davidos-opportunity-scan/SKILL.md` (most likely consumer of refined tactics)
