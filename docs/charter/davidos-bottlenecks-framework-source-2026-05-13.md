# Highest-Leverage Bottlenecks to Diagnose First — Primary Source

**Captured:** 2026-05-14 (originally authored 2026-05-13 5:47 PM, raw notes by David Izzard)
**Status:** Primary source — do not paraphrase, do not summarize, do not edit
**Audit context:** This is the source material behind what Opus Task 2 consolidated as "P14 — the seven candidate bottlenecks" (folded into Principle 7). The consolidation kept the names but lost the symptom/diagnosis/fix/question framework, which is the more useful artifact for diagnostic work.

---

## Highest-leverage bottlenecks to diagnose first

Wednesday, May 13, 2026 — 5:47 PM

### 1. Context retrieval bottleneck

**Symptom:**
You repeatedly re-explain goals, preferences, project state, or prior decisions.

**Diagnosis:**
- The system does not have durable, queryable memory.
- Context is not assembled before work starts.
- Project state is not explicit.

**Fix:**
- Create project state files.
- Store decisions separately from notes.
- Maintain current operating context per project.
- Build a "context pack" generator for each workflow.

**High-leverage question:**
What information does the system keep asking me for that it should already know?

---

### 2. Decision bottleneck

**Symptom:**
- Work stalls because every next step requires human judgment.
- The system gives options but not recommendations.
- You spend time deciding what to do rather than doing it.

**Diagnosis:**
- No decision policy.
- No risk tolerance model.
- No default operating principles.
- No escalation rules.

**Fix:**
- Define decision rights.
- Use confidence thresholds.
- Create "recommendation format" standards.
- Encode reversible vs irreversible action policies.

**Example policy:**

If action is low-cost, reversible, and confidence > 80%, execute or recommend direct execution.
If action is medium-risk, produce recommendation with rationale.
If action is irreversible, costly, or security-sensitive, pause for approval.

---

### 3. Evaluation bottleneck

**Symptom:**
- Lots of outputs, unclear quality.
- Same mistakes recur.
- You do not know which agents, prompts, or workflows work best.

**Diagnosis:**
- No scoring rubric.
- No regression tests.
- No comparison against prior output.
- No feedback capture.

**Fix:**
- Add output rubrics.
- Track error categories.
- Compare first draft vs final accepted draft.
- Save examples of excellent outputs.
- Run periodic workflow audits.

**High-leverage question:**
How do we know this output was good besides vibes?

---

### 4. Handoff bottleneck

**Symptom:**
- Agents or tools lose context between steps.
- You paste screenshots, logs, or instructions repeatedly.
- Work restarts instead of continues.

**Diagnosis:**
- No standardized handoff packet.
- No shared state.
- No workflow checkpointing.

**Fix:**
Every agent handoff should include:
- objective
- current state
- completed steps
- relevant files
- constraints
- known failures
- next recommended action
- risk notes

This alone dramatically improves AI system reliability.

---

### 5. Human review bottleneck

**Symptom:**
- You are still approving everything.
- The AI produces drafts, but you remain the integration layer.

**Diagnosis:**
- No trust gradient.
- No automation tiers.
- No clear distinction between low-risk and high-risk actions.

**Fix:**
- Identify low-risk reversible actions.
- Let the system execute those.
- Keep high-impact actions gated.
- Track where review changes outcomes.

**Key metric:**
What percentage of human reviews materially change the output?
If review rarely changes the result, automate more.

---

### 6. Tool fragmentation bottleneck

**Symptom:**
- Work is spread across chat, docs, Notion, GitHub, Slack, email, dashboards, and local files.
- No single system knows what is true.

**Diagnosis:**
- No canonical source of state.
- Tools are integrated cosmetically, not operationally.

**Fix:**
- Define source-of-truth hierarchy.
- Separate workspace from system of record.
- Use agents to sync, summarize, and reconcile state.
- Do not let every tool become a memory layer.

---

### 7. Prompt bottleneck

**Symptom:**
- Output quality depends heavily on the exact wording of the user's prompt.
- The operator has to be a prompt engineer every time.

**Diagnosis:**
- No prompt system.
- No workflow-specific templates.
- No automatic prompt improvement.

**Fix:**
- Build a prompt router.
- Convert recurring prompts into reusable workflows.
- Generate "best next prompt" suggestions based on project state.
- Store prompts that produced high-quality outputs.
- The operator should not have to remember the best way to ask.
