# Agent Expansion Policy — v0

**Status:** Draft. Promote to durable on David's `[APPROVAL: policy-change]`.
**Scope:** Defines what must be specified before a new agent is created in DavidOS / iZZi AI Systems. Implements DAV-17 §5: "Agent expansion is allowed once the role, guardrails, permissions, memory boundaries, runtime validation, approval policy, and success metrics are defined."

## 1. Why this gate

Adding an agent permanently expands the system's autonomy and risk surface. An under-specified agent has unbounded scope, ambiguous authority, no defined permission ceiling, and no way to tell whether it's working. The seven fields below are the minimum specification that lets David approve creation with informed consent and lets the system measure whether the agent is earning its keep.

## 2. The seven required fields

Every new-agent proposal posted as `[APPROVAL-REQUEST] kind: new-agent` MUST include these seven fields, each as a labeled section in the proposal body. Missing any field = the request is rejected with `[REJECT]: incomplete spec` and Atlas posts a revised request.

### 2.1 Role

One paragraph. What does this agent do? What's its primary purpose? What's the one-line job description that distinguishes it from Atlas?

Example: "FamilyAI Lead — owns the FamilyAI project's day-to-day execution: triages FamilyAI-labeled issues, runs deep dives on FamilyAI domains, drafts deliverables, and coordinates with Atlas on architecture decisions. Atlas remains David's primary advisor; FamilyAI Lead is a project-scoped executor."

### 2.2 Guardrails

The hard constraints the agent cannot cross. Written as a bulleted list of "this agent never X" statements.

Required guardrails for every project-lead agent (inherited):
- Never modifies files outside `docs/` and the agent's own project directory.
- Never installs, credentials, paid services, runtime config, or scheduling without an explicit approval gate of the matching kind.
- Never closes or cancels a Paperclip issue (heartbeat-loop mitigation).
- Never escalates its own permissions without an `[APPROVAL: policy-change]`.

Project-specific guardrails go beyond the inherited set.

### 2.3 Permissions

The explicit allow-list. Written as: which Paperclip projects, which folders, which API surfaces, which approval-kinds are pre-approved (if any) for this agent.

Format:
```
projects: [<project-id>, ...]
labels:   [<label>, ...]   # which Paperclip labels does this agent watch
folders:  [<path>, ...]    # which docs/ subfolders may this agent write to
apis:     [<api>, ...]     # Paperclip subset, GitHub, etc.
pre-approved kinds: [<kind>, ...]  # almost always: [safe-doc-edit] only
```

Defaulted-to-empty fields are still listed (e.g. `pre-approved kinds: [safe-doc-edit]` — never `[]` and never silent inheritance).

### 2.4 Memory boundaries

What durable memory does this agent read and write? Specifically:

- Which `docs/` subfolders does it read for context?
- Which `docs/` subfolders does it write to (subject to permissions in §2.3)?
- Does it have its own subfolder under `docs/atlas/<agent-slug>/` for its operating notes? (Default: yes for project-lead agents.)
- How does its memory interact with Atlas's? (Default: read-only access to Atlas's policies; no write to `atlas/` root.)

The goal is to make sure new agents do not pollute Atlas's self-knowledge or each other's working memory.

### 2.5 Runtime validation

How will we know the agent runs cleanly before turning it loose? Required before the first Paperclip issue is assigned to it:

- A dry-run heartbeat invocation that picks up a synthetic test issue, performs a no-op deliverable, and posts a `[STATUS]` comment.
- A confirmation that the agent's identity (agent ID) is correctly resolved by the Paperclip comment route (or, if the comment-route auth bug is still live, a documented mitigation).
- A confirmation that OTel spans (once Langfuse is live) are tagged with the agent's ID and not Atlas's.

The runtime-validation report is attached as a document on the new-agent issue under key `runtime-validation`.

### 2.6 Approval policy (DAV-17 §5 addition)

Which approval-kinds does this agent need that Atlas doesn't, and which inherit unchanged?

The default for a project-lead agent: identical to Atlas's approval policy (per `approval-policy-v0.md`), with all gates inherited at the same strictness. Deviations must be enumerated explicitly:

- Any kind the new agent's actions never touch (e.g., a write-only-prose agent never needs `production`) — list as "n/a, never invoked."
- Any kind the new agent should be MORE strict on than Atlas — list with rationale.
- Any kind the new agent should be LESS strict on than Atlas — list with rationale AND require `[APPROVAL: policy-change]` for the policy diff itself.

### 2.7 Success metrics (DAV-17 §5 addition)

How do we know this agent is earning its keep? Required:

- Three measurable signals, with numeric thresholds, on a 30-day cadence.
- A "kill criterion": a specific signal pattern that, if observed, would trigger Atlas to recommend retirement of the agent.

Example for FamilyAI Lead:
- Signal 1: ≥1 deliverable shipped per FamilyAI-labeled issue assigned, within 7 days of assignment.
- Signal 2: <10% of FamilyAI deliverables require rework after David review.
- Signal 3: Cost per deliverable < $X (set by David at creation time).
- Kill criterion: 0 deliverables in any 14-day window with FamilyAI issues open AND assigned, OR ≥3 deliverables in a row marked rework-needed.

Atlas tracks these signals and includes them in the monthly retrospective memo per project.

## 3. Approval workflow for new-agent creation

1. Atlas (or David) drafts the seven-field spec as a markdown document at `docs/atlas/agents/<agent-slug>-spec-v0.md` (this is a `safe-doc-edit`).
2. Atlas posts `[APPROVAL-REQUEST] kind: new-agent` on a dedicated issue (suggested title: "Commission <agent-name>"), with the spec inline AND attached as the issue's `spec` document.
3. David replies `[APPROVAL: new-agent]` or `[REJECT]` (with reason).
4. On approval, Atlas (a) creates the agent in Paperclip via the agents API, (b) creates `docs/atlas/agents/<agent-slug>/` subfolder, (c) runs the runtime-validation dry-run, (d) attaches the `runtime-validation` document, (e) posts a `[STATUS]` confirming the agent is live and validated.
5. The agent is assigned its first real issue ONLY after step 4(e).

## 4. The first candidate

FamilyAI Lead is the likely first project-lead agent (per DAV-15 §8 and DAV-17 §5). It is NOT auto-created in Stage 1 — it requires its own seven-field spec and its own `[APPROVAL: new-agent]` gate. This file establishes the framework; the FamilyAI Lead spec is a separate Stage 2+ deliverable on a separate Paperclip issue.

## 5. Self-amendment

Edits to this file require `[APPROVAL: policy-change]`.

End of file.
