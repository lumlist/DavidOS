# Highest-Leverage Creativity Tactics — Primary Source

**Captured:** 2026-05-14
**Source:** David Izzard, originally drafted in ChatGPT, pasted into DavidOS session
**Status:** Primary source — do not paraphrase, do not summarize, do not edit
**Used by:** `davidos-opportunity-scan` skill (initial scaffold)

---

## Highest leverage tactics

### 1. Define the "creative arena"
Bad:
Give me creative business ideas.
Better:
Generate novel ideas at the intersection of AI agents, ecommerce seller operations, and low-friction SMB workflows. Optimize for ideas that could become a paid product within 90 days.
Creativity improves when the model has a bounded sandbox.

### 2. Ask for "non-obvious combinations"
Use:
Combine ideas from three unrelated domains: marketplace operations, behavioral psychology, and video game progression systems. Create 20 product concepts that could not come from only one of those domains.
Novelty often comes from cross-domain transfer.

### 3. Force multiple creativity modes
Use:
Generate ideas in five modes: obvious, contrarian, technically ambitious, behaviorally clever, and weird-but-plausible. Give 10 ideas per mode.
This prevents one-note brainstorming.

### 4. Ask what smart people are missing
Use:
What assumptions do most founders/operators make in this space that might be wrong? For each assumption, suggest a startup idea that exploits the opposite view.
This is one of the best novelty triggers.

### 5. Separate generation from judgment
Use:
First generate 50 ideas without evaluating them. Then cluster them. Then identify the 10 most original. Then score only those by feasibility, market pull, defensibility, and speed to test.
Evaluation too early kills originality.

### 6. Request "adjacent possible" ideas
Use:
Suggest ideas that are one step beyond what current tools do, not science fiction. Each idea should be feasible with today's AI APIs, browser automation, no-code tools, and lightweight human review.
This keeps ideas inventive but buildable.

### 7. Use constraint stacking
Use:
Generate ideas that require no mobile app, no enterprise sales, no paid ads, under $500 to test, and can produce a useful result for the user within 10 minutes.
Constraints create originality.

### 8. Ask for anti-pattern reversal
Use:
List the most annoying, manual, repetitive, or emotionally painful workflows in this domain. For each, invent a product that makes the workflow disappear rather than merely improves it.
This pushes toward real leverage.

### 9. Demand mechanism, not vibes
Use:
For each idea, explain the mechanism of value creation: what input becomes what output, why AI makes this newly possible, and why the user would pay.
This filters "cool" ideas from real inventions.

### 10. Ask for "patent-style claims"
Use:
Describe each idea as if drafting a provisional patent claim: system, input, transformation, output, feedback loop, and unique mechanism.
This helps uncover inventive structure.

---

## My best reusable prompt

Act as a founder, invention strategist, and AI systems architect.

I want novel, inventive, non-obvious ideas in this area:
[DOMAIN]

Do not give generic ideas. Use structured creativity.

Step 1: Identify 10 stale assumptions or common patterns in this domain.
Step 2: Reverse or break each assumption.
Step 3: Generate 30 ideas across these modes:
- Cross-domain transfer
- Contrarian insight
- Automation of invisible labor
- New AI-native workflow
- Weird but plausible
- High willingness-to-pay painkiller
Step 4: For each idea, explain:
- The user
- The painful job-to-be-done
- The novel mechanism
- Why this is newly possible now
- The simplest MVP
- The fastest validation test
- Why competitors may miss it
Step 5: Rank the top 10 by:
- Novelty
- Feasibility
- Speed to revenue
- Defensibility
- User urgency

Then pick the top 3 and make them sharper, more original, and more commercially viable.

---

## Highest leverage follow-up question

After the AI gives ideas, ask:

Which of these are actually non-obvious, and which are just recombinations of existing products? Be harsh. Improve the best 5 until they feel meaningfully inventive.
