# DavidOS Design Principles — Primary Source

**Captured:** 2026-05-13, surfaced by David late afternoon CDT
**Source:** OneNote file `DavidOS-Design-Principles-Draft.one` compiled by David on 2026-05-13
**Extraction method:** `strings -n 20` on the binary .one file (OneNote 2010 format)
**Status:** Primary source. **Do not paraphrase. Do not summarize. Do not compress.** This is the second primary-source charter document for DavidOS, alongside `outcomes-and-frustrations-2026-05-13.md`. Derivative documents reference it directly.

---

## Important caveat about extraction order

This text was extracted from a binary OneNote file via `strings`. Section headers and their body content sometimes appear out of sequence. The intended structure must be reconstructed when interpreting this document — do not assume the linear order below reflects David's intended grouping.

When in doubt, consult the original `.one` file (still in David's possession) or ask David directly.

---

## Extracted content (verbatim)

```
Wednesday, May 13, 2026
Wednesday, May 13, 2026
Outputs worth reusing: docs, code, SOPs, templates, datasets
Durable knowledge the system should remember
Rules for routing, automation, risk, cost, security, quality
What information enters the system, how is it classified, where does it live, who or what can act on it, and how does it improve future decisions?
Evidence of whether outputs were good
Most AI-native systems fail because the builder focuses on agents, prompts, automations, or interfaces before defining the information model.
If those primitives are weak, everything becomes chat history soup.
A strong AI-native system has clear primitives:
Explicit choices with rationale and tradeoffs
The system is only as good as its information architecture
Current status of projects, workflows, goals, tasks, constraints
The highest-leverage question is:
Raw messages, documents, data, screenshots, calls, user actions
Human or system-generated corrections
Wednesday, May 13, 2026
Wednesday, May 13, 2026
Standardize Decision Interfaces
What would this look like if it operated 10x larger with 90% less human involvement
Wednesday, May 13, 2026
The Highest Leverage Question
What would this look like if it operated 10x larger with 90% less human involvement
Wednesday, May 13, 2026
The Highest Leverage Questions
Wednesday, May 13, 2026
Separate the system into 4 layers: Input, Reasoning, Execution. Learning
Score quality, risk, completion, confidence
Separate the system into layers: Input, Reasoning, Execution. Learning
Most people build one giant agent that tries to do everything. That creates brittle, opaque systems.
Use tools, APIs, scripts, browsers, email, calendar, code
Execution layer: take action through tools, APIs, workflows
System: Use this architecture:
Learning layer: evaluate outcomes, update rules, improve prompts, improve routing
Diagnose, reason, plan, evaluate tradeoffs
Wednesday, May 13, 2026
Help the operator make decisions quickly
Input layer: capture demand, data, context, intent
Preserve durable knowledge and state
Do not let the execution layer own the strategy. Do not let memory become an unfiltered dump. Do not let the interface become the system.
Reasoning layer: classify, plan, decide, recommend
Wednesday, May 13, 2026
Make Every workflow observable
Log inputs, outputs, model used, cost, latency, confidence, failure reason, human correction, and final business outcome. Without observability, you do not have a system. You have magic that will eventually break.
Wednesday, May 13, 2026
Make Every workflow observable
Wednesday, May 13, 2026
Prefer workflows before autonomy
Wednesday, May 13, 2026
Design for compounding assets
Every run should improve one of these: dataset, prompt, SOP, evaluation rubric, customer profile, knowledge base, automation rule, product insight, or distribution channel. If usage does not make the system smarter or more valuable, it is not compounding.
Wednesday, May 13, 2026
Design for compounding assets
Wednesday, May 13, 2026
Exploit Parallellism
Wednesday, May 13, 2026
Exploit Parallellism
Wednesday, May 13, 2026
Turn tacit expertise into operating code
Capture how an expert thinks: their filters, thresholds, disqualifiers, escalation rules, taste, examples, and anti examples. The moat is not the prompt. The moat is encoded judgment plus proprietary context plus feedback data.
Wednesday, May 13, 2026
Turn tacit expertise into operating code
Wednesday, May 13, 2026
Build a strong router before building more agents
A strong router decides: what type of work is this, what context is required, what tool should handle it, what risk tier applies, what output format is needed, and what approval is required. Routing quality determines system quality.
Wednesday, May 13, 2026
Build a strong router before building more agents
Wednesday, May 13, 2026
Measure leverage with a blunt formula | If a system saves time once, its an automation, if it improves each time it runs, it is infrastructure
Leverage = business value created
  human attention required
Wednesday, May 13, 2026
Measure leverage with a blunt formula
If a system saves time once, it is automation. If it improves every time it runs, it is infrastructure.
A bad system helps you complete more tasks.
Optimize for decision velocity, not task volume
deciding what to do,
A great system makes many decisions unnecessary because the right action is already encoded in the operating model.
Wednesday, May 13, 2026
A good system makes the right tasks obvious.
noticing something,
The most valuable systems compress the time between:
learning from the result.
Every workflow should produce reusable assets
Reusable research protocol
For every workflow, ask:
Persona-specific messaging library
If a workflow only produces the immediate output, it is labor.
Regression test and diagnostic script
What should this create that makes the next similar workflow faster or better?
Compounding byproduct
Customer support reply
Feature evaluation rubric
Wednesday, May 13, 2026
Triage classifier and response template
If it also produces a better prompt, checklist, dataset, routing rule, reusable template, SOP, evaluator, or automation, it is compounding.
Market research memo
reasoning under uncertainty
This is one of the most important operating rules.
Use AI where ambiguity is high and software where repeatability is high
repeatable business logic
Use deterministic software for:
Wednesday, May 13, 2026
Where does throughput, quality, or learning degrade?
no feedback loop after execution
The correct automation target is rarely the most annoying task. It is the constraint that limits the entire system.
inconsistent quality standards
Wednesday, May 13, 2026
Build around bottlenecks, not features
Typical bottlenecks:
too much human review
Execute low-risk reversible actions
The mistake is either giving agents too much autonomy too early or keeping everything in manual review forever.
Wednesday, May 13, 2026
Not all automation should have the same permission level.
Execute within predefined policy limits
Execute and monitor outcomes
Redesign its own workflow with approval
Use graduated autonomy:
Design for trust gradients
Most systems should live between L1 and L3 for a long time.
Memory must be curated, not accumulated
Will this materially improve future decisions or execution?
The worst AI systems remember everything and understand nothing.
If not, it is noise.
Prompts, checklists, templates
Wednesday, May 13, 2026
Memory should be structured into:
Every durable memory should answer:
The architecture pattern I would use for most AI-native systems
Not a chatbot. Not a pile of automations. Not a monolithic agent.
Wednesday, May 13, 2026
I would use a command-center architecture with specialized agents, durable memory, workflow orchestration, evaluation, and human control points.
Reference architecture
Every important output should be evaluated against explicit criteria.
After each meaningful workflow, the system should ask:
It is context compression.
with what evaluation criteria.
durable user preferences
What rule should be updated?
Give the agent the smallest context package that preserves decision quality.
This is where the system compounds.
current constraints
Agents should operate inside workflows. Workflows should improve over time.
audience fit, clarity, persuasion, compliance
What decision was made?
C. Workflow orchestration system
Without evaluation, you do not have compounding. You have production volume.
B. Context assembly system
D. Evaluation system
whether human approval is required
source quality, freshness, contradiction handling
whether web or internal files are needed
E. Memory and learning system
whether this is a new workflow or existing workflow
clear thesis, evidence, tradeoffs, next actions
Before an agent acts, it should assemble the minimum viable context:
applicable policies
reliability, reversibility, observability, cost
passes tests, low complexity, secure, maintainable
What artifact should be saved?
examples of good outputs
Do not let every agent improvise the process.
relevant project state
context use, correctness, actionability, risk handling
with what approval gates,
This prevents the system from treating every request like generic chat.
Wednesday, May 13, 2026
with what retry logic,
by which agent/tool,
What should be easier next time?
The intake layer should classify every request before work begins.
whether memory should be updated
The five essential subsystems
High-leverage question:
This alone dramatically improves AI system reliability.
Compare first draft vs final accepted draft.
Store decisions separately from notes.
1. Context retrieval bottleneck
Add output rubrics.
Keep high-impact actions gated.
The operator has to be a prompt engineer every time.
Define source-of-truth hierarchy.
No automation tiers.
No clear distinction between low-risk and high-risk actions.
You paste screenshots, logs, or instructions repeatedly.
Wednesday, May 13, 2026
If action is irreversible, costly, or security-sensitive, pause for approval.
Use confidence thresholds.
Save examples of excellent outputs.
The system does not have durable, queryable memory.
Tools are integrated cosmetically, not operationally.
Highest-leverage bottlenecks to diagnose first
Work restarts instead of continues.
You are still approving everything.
No automatic prompt improvement.
If action is low-cost, reversible, and confidence > 80%, execute or recommend direct execution.
Maintain current operating context per project.
Track where review changes outcomes.
Identify low-risk reversible actions.
Separate workspace from system of record.
You do not know which agents, prompts, or workflows work best.
Let the system execute those.
No standardized handoff packet.
Use agents to sync, summarize, and reconcile state.
Do not let every tool become a memory layer.
5. Human review bottleneck
Lots of outputs, unclear quality.
If review rarely changes the result, automate more.
How do we know this output was good besides vibes?
What percentage of human reviews materially change the output?
No workflow-specific templates.
You repeatedly re-explain goals, preferences, project state, or prior decisions.
No feedback capture.
Convert recurring prompts into reusable workflows.
3. Evaluation bottleneck
What information does the system keep asking me for that it should already know?
Agents or tools lose context between steps.
Context is not assembled before work starts.
No default operating principles.
The system gives options but not recommendations.
7. Prompt bottleneck
You spend time deciding what to do rather than doing it.
Work is spread across chat, docs, Notion, GitHub, Slack, email, dashboards, and local files.
Same mistakes recur.
4. Handoff bottleneck
Run periodic workflow audits.
Build a prompt router.
Encode reversible vs irreversible action policies.
Track error categories.
Project state is not explicit.
No regression tests.
No comparison against prior output.
Every agent handoff should include:
6. Tool fragmentation bottleneck
No workflow checkpointing.
The AI produces drafts, but you remain the integration layer.
Work stalls because every next step requires human judgment.
Store prompts that produced high-quality outputs.
If action is medium-risk, produce recommendation with rationale.
next recommended action
The operator should not have to remember the best way to ask.
High-leverage question:
Create project state files.
Define decision rights.
No escalation rules.
No decision policy.
No risk tolerance model.
No canonical source of state.
No single system knows what is true.
2. Decision bottleneck
agent workflow modifications
Automate second: judgment-assisted workflows
security-critical approvals
Here the AI should recommend, draft, rank, and explain.
legal/compliance pre-checks
Automate first: context, routing, formatting, and low-risk execution
low-risk notifications
Never fully automate: values, taste, irreversible bets, and accountability
financial transactions
AI can generate options and surface tradeoffs.
access/permission changes
final product taste
The human should approve, refine, or reject.
customer-facing decisions
These are leverage multipliers because they reduce cognitive switching.
The operator owns judgment.
major hiring/firing decisions
lead prioritization
handoff packet generation
financial modeling assumptions
meeting/document summarization
Wednesday, May 13, 2026
changing production code
project state updates
large financial commitments
These require evaluation, not blind execution.
duplicate detection
Automation hierarchy: what to automate first, later, and never
recurring workflow setup
sales messaging personalization
customer support triage
customer segmentation
founder conviction decisions
market research synthesis
Do not fully automate:
Automate with review:
brand-defining creative direction
relationship-sensitive communication
These are the highest ROI because they reduce friction without creating much risk.
Do this only after the system has policies, logs, approval gates, and rollback paths.
outbound sales at scale
A strong system makes judgment easier, not absent.
company positioning
Automate later: actions with external consequences
How much work moved from manual to system-managed?
Are workflows producing reusable leverage?
Human correction rate
Is memory paying off?
Error recurrence rate
Context tax = minutes spent re-explaining known information per workflow
Time to useful first draft
Is scale becoming cheaper?
Most people measure activity. That is a trap.
Decision latency = time from new information arriving to recommended action
If you create 20 outputs and 0 reusable assets, you are using AI as labor.
Wednesday, May 13, 2026
Is the system learning from mistakes?
Decision trace completeness
For mature internal systems, 60 to 80 percent is possible.
If you create 20 outputs and 8 reusable assets, you are building a system.
Is the system reducing ambiguity?
Are low-risk actions trusted?
For external-facing high-risk systems, the safe number may be lower.
Are outputs getting better?
Is throughput increasing?
My favorite operator metric
Metrics that reveal whether the system is compounding
Is context assembly improving?
Operator lift = percentage of workflow completed before human intervention
Can you understand why actions happened?
Core compounding metrics
Compounding ratio = reusable assets created / one-time outputs created
For early systems, 20 to 40 percent is good.
This should trend toward zero.
Are workflows producing durable quality?
Marginal cost per output
This is a brutal but powerful metric.
Approval bypass rate
Cycle time per workflow
You want metrics that show whether future work is becoming easier, faster, better, and less dependent on the operator.
Are one-off tasks becoming systems?
Great operating systems reduce decision latency dramatically.
Another useful metric
opening new revenue capacity
Avoid by creating rubrics for recurring outputs and requiring the system to compare:
A clever agent demo is not a business system.
Avoid by using memory types:
Failure mode 1: Building agents before workflows
The opposite failure is using AI as a smart assistant forever.
AI-native systems should not just feel efficient. They should change the operating economics.
For services and companies, every system should eventually tie to economics.
Each memory should have a purpose.
shrinking cycle time
Start with recommendations and drafts. Move to execution only when the workflow is stable, reversible, and measurable.
improving feedback loops
Failure mode 4: No evaluation loop
failed attempt vs successful attempt
Failure mode 2: Treating memory as storage
Avoid by forcing every tool to justify its role:
The fastest way to destroy trust is to let an immature system take consequential actions.
source of truth for metrics
source of truth for tasks
More tools does not mean more leverage.
Wednesday, May 13, 2026
Avoid by regularly asking:
improving output consistency
If an AI feature does not do one of those, it is probably theater.
You cannot improve what you cannot see.
reducing repeated human effort
Failure mode 5: Over-automation too early
increasing decision quality
Does it improve visibility?
Does this create proprietary data?
Without evaluation, you will not know whether changes improve the system.
Failure mode 9: Confusing novelty with leverage
Does this improve speed to market?
Saving everything is not intelligence.
source of truth for memory
Does this increase revenue capacity?
Failure mode 6: Under-automation forever
creating reusable assets
Does it reduce cost or cycle time?
If not, it is interface clutter.
For serious systems, every important workflow should have traceability.
Does it reduce cognitive load?
source of truth for documents
Does this reduce churn?
Failure mode 3: No source of truth
Does this increase throughput per employee?
Does this reduce cost to serve?
expected output vs actual output
AI can summarize across tools, but it needs canonical state.
source of truth for decisions
Failure mode 7: Too much tool complexity
Failure mode 10: No economic model
Does this create a defensible workflow advantage?
Avoid by using autonomy levels.
old workflow vs new workflow
Failure mode 8: No observability
Leverage comes from:
first draft vs accepted draft
Does it improve quality?
Agents are not the architecture. They are workers inside the architecture.
Does it execute actions?
If the human approves 90 percent of a category unchanged, that category should probably move to higher autonomy.
If project status lives in five places, the system will hallucinate state.
Does this improve gross margin?
Which approvals are ceremonial?
Common failure modes and how to avoid them
What should become faster, cheaper, better, or more scalable?
What metrics matter?
Wednesday, May 13, 2026
I. Define economic value
D. Define the agent/tool design
Use this before building anything.
What should be forgotten?
What should never be automated?
What confidence threshold is required for each action type?
What risk does this reduce?
How will the system learn from failures?
What should be drafted for review?
What cost does this remove?
Which steps are risky?
What are the top failure cases?
Who is the operator or user?
G. Define automation boundaries
How will quality be scored?
What dashboard or review cadence is needed?
H. Define compounding mechanism
What makes a good output?
What revenue does this unlock?
B. Define the information model
What tools does each agent need?
How are handoffs handled?
Can you trace why a decision was made?
What gets added to the prompt library?
What should be logged?
What decisions must it record?
What reusable asset does this workflow create?
What inputs does the system need?
How does the system get better after each run?
Which steps require deterministic software?
What context does each agent receive?
What context does it need?
F. Define observability
What are the steps from intake to output?
What throughput does this increase?
What should each agent not be allowed to do?
Practical checklist before building any new system
How will human edits be captured?
Can you compare workflow performance over time?
C. Define the workflow
What gets added to the workflow library?
E. Define the evaluation model
What outputs should become reusable assets?
Does this need one agent or multiple specialized agents?
What format should each agent return?
What requires approval?
What gets added to the evaluation library?
What is the fallback path when the system is uncertain?
What proprietary advantage could accumulate?
What painful bottleneck exists today?
What should be remembered?
What gets added to memory?
Which steps require human approval?
If you cannot answer these, you are not ready to build. You are ready to prototype.
What state must it maintain?
Which steps are reversible?
What makes a bad output?
Which steps require reasoning?
What can be fully automated now?
What does success look like?
What exact workflow or decision is this system improving?
Build Evaluation Systems Early
```

---

## How to use this file

This is the second primary-source charter document for DavidOS. Future agents and sessions reference it directly when:

- Designing or evaluating the architecture of DavidOS or any iZZi customer system
- Producing derivative documents (SOUL.md, ADRs, Substrate Brief, Charter Regression Suite, Roles Register, Project Intake, audit reports)
- Resolving conflicts between competing system designs

When David revises this material, capture the revision as a new dated file (`davidos-design-principles-source-YYYY-MM-DD.md`) alongside this one rather than overwriting.

**Do not edit this file.** It is a primary source.
