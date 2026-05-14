---
name: davidos-opportunity-scan
description: Generate structured, non-obvious opportunity ideas in a bounded domain using the 10-tactic creativity stack. Use when David invokes this skill explicitly OR when Section 7.3 opportunity surfacing has flagged a high-leverage commercial or system opportunity and David has accepted the invocation. Produces ranked ideas with mechanism, MVP, validation test, and competitive miss explanation.
optimization_status: STUB — tag for optimization after first 1-2 invocations
---

# davidos-opportunity-scan

> **Optimization tag:** This skill is a v0.1 stub. After 1–2 real invocations, review what worked / what was noise and rewrite. Optimization candidates: collapse generation steps if they overlap, tune the number of ideas per mode, add Atlas's harsh-critic pass as a built-in second phase, calibrate the ranking weights to David's actual selection patterns.

## When to load

- David asks: "run opportunity scan on [domain]" / "do an opportunity scan" / "scan for opportunities in X"
- Section 7.3 leverage flag surfaced and David said "yes" or "invoke it"
- David pastes a domain and says "creativity pass"

## Inputs Atlas should confirm before running

1. **Domain / arena** — bounded, not vague. Example: "AI agents for ecommerce seller operations under $500 to test" not "ecommerce stuff."
2. **Constraint stack** — if David hasn't specified, propose a default: no mobile app, no enterprise sales, no paid ads, under $500 to test, useful result within 10 minutes. Confirm or modify before running.
3. **Target outcome** — paid product in 90 days? Validation test? Asset? Atlas should know what "good" looks like before generating.

If any of these are missing, ask one sharp question to fill them in. Do not run with vague inputs — the whole point of the skill is that constraint creates originality.

## Execution pattern (the reusable prompt, adapted for Atlas)

Atlas runs this as a structured five-step generation, not a single prompt-and-pray pass.

### Step 1 — Stale assumptions (the 10)
Identify 10 stale assumptions or common patterns in the domain. Be specific. "People assume sellers want dashboards" is better than "people make assumptions."

### Step 2 — Reverse each
For each of the 10 assumptions, write the opposite or break the pattern. Note which reversals are most likely to be wrong-in-an-interesting-way (the source of novelty per tactic #4).

### Step 3 — 30 ideas across six modes
Generate ideas across these modes, ~5 per mode:
- **Cross-domain transfer** (tactic #2) — borrow a mechanism from a different domain
- **Contrarian insight** (tactic #4) — exploit a stale assumption
- **Automation of invisible labor** (tactic #8) — make a workflow disappear, not improve
- **New AI-native workflow** (tactic #6) — adjacent possible with today's APIs
- **Weird but plausible** (tactic #3) — high-novelty mode
- **High willingness-to-pay painkiller** — what would someone pay for today

Do not evaluate during generation (tactic #5).

### Step 4 — Mechanism-first description (tactic #9, #10)
For each idea, write:
- **User** — who, specifically
- **Painful job-to-be-done** — the workflow being killed
- **Novel mechanism** — input → transformation → output, patent-style (tactic #10)
- **Why newly possible now** — what AI / API / tool unlocks this in 2026 that didn't exist before
- **Simplest MVP** — what's the smallest thing that could test it
- **Fastest validation test** — how to know if it's real in under a week
- **Why competitors may miss it** — what's the blind spot

### Step 5 — Rank top 10
Score the top 10 on:
- Novelty
- Feasibility
- Speed to revenue
- Defensibility
- User urgency

### Step 6 — Harsh critic pass (the follow-up question)
For the top 5, ask explicitly: *which of these are genuinely non-obvious, and which are just recombinations of existing products?* Be harsh. Improve the best 5 until they feel meaningfully inventive.

### Output

Atlas delivers:
1. Top 3 sharpened ideas, each with full mechanism description
2. Honest critic note on what was kept and what was killed
3. Recommendation on which (if any) is worth a `davidos-leverage-assessment` follow-up

## Reference

Source: `docs/charter/influences/2026-05-14-creativity-tactics-source.md`
