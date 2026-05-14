---
name: davidos-leverage-assessment
description: Score an idea, project, or opportunity on effort/time/return tradeoffs. Produces a defensible recommendation on whether to pursue, defer, or kill. Use after davidos-opportunity-scan surfaces a candidate, or any time David asks "is this worth it?" / "what's the leverage here?" / "should I do this?"
optimization_status: STUB — tag for optimization after first 1-2 invocations
---

# davidos-leverage-assessment

> **Optimization tag:** v0.1 stub. After real use, calibrate: are these the right dimensions? Are the weights right? Is the cost/return frame the right one for David's actual decision pattern? Does the "binding bottleneck" check (P7 from Opus Task 2) belong here?

## When to load

- David asks: "is this worth it?" / "should I pursue X?" / "what's the leverage?" / "do a leverage assessment on Y"
- Output of `davidos-opportunity-scan` includes a candidate worth deeper scoring
- David is deciding between two or more options and needs a stance, not a comparison table

## Inputs Atlas should confirm

1. **The candidate** — one idea, project, or opportunity. Not a list.
2. **The alternative** — what David would do with the same time/money if he didn't pursue this. "Status quo" is acceptable but should be named.
3. **The horizon** — when does this need to pay off? 30 days, 90 days, 6 months, a year+?

## Scoring dimensions

Score each on a 1–5 scale with one-sentence justification.

**Effort dimensions (cost side):**
- **Cash cost** — actual dollars to validate / build to first revenue
- **Time cost** — David's hours, honestly estimated
- **Cognitive cost** — does this require deep context switching or sustained focus David doesn't have right now?
- **Opportunity cost** — what does pursuing this prevent (cite the alternative)

**Return dimensions (value side):**
- **Speed to first signal** — how fast can David know if this is real
- **Speed to revenue** — if it works, how fast does money move
- **Ceiling** — upper bound if everything goes right
- **Defensibility** — does success create a moat or just a transient win
- **Compounding** — does doing this make the next thing easier (system leverage)

**Risk dimensions:**
- **Downside if wrong** — what's the worst case, including reputation/time/cash
- **Reversibility** — can David back out without serious cost
- **Binding bottleneck check** — is this addressing the actual bottleneck in David's system right now (per P7), or is it adjacent work?

## Output

Atlas delivers:
1. **Verdict** — Pursue / Defer / Kill, with confidence (Section 7.2 tag)
2. **Strongest reason for the verdict** — one paragraph
3. **What would change the verdict** — what new information or condition would flip it
4. **If "pursue":** the smallest next step
5. **If "defer":** the trigger that should re-open the question

Atlas takes a stance per §6 "When I am advisory" — recommendation with reasoning, not flattened options. David decides; recommendation is on the record.

## Reference

- `docs/audits/preparation/2026-05-13-task2-consolidated-principles.md` (P7 binding bottleneck)
- `docs/charter/outcomes-and-frustrations-2026-05-13.md` (David's actual outcomes — the ground truth for what "return" means)
