# Substrate Brief v1

**Status:** Draft — Awaiting Opus review pass
**Author:** Atlas (Sonnet 4.6 drafting pass)
**Date:** 2026-05-12
**Approval basis:** Option B approved in approvals-log.md (row 33); Substrate Brief scope approved rows 34–35
**Completion criterion:** All seven items have shipped their first artifact and passed their success criterion. M6b design session begins immediately after.

---

## Dependency graph (read before sequencing)

Item 6 (Opus access) must ship before Items 1 and 7 can be properly built.
Item 6 must ship before Item 1 because behavioral baselines written without Opus access cannot represent high-judgment synthesis behavior — the most important thing to baseline.
Item 7 (model selection discipline) is inert without Item 6.
Items 3, 5 have no upstream dependencies — they can ship in parallel with Item 6.
Item 2 has no hard upstream dependency but is validated more precisely after Item 1 baselines are in place.
Item 4 (Session-Start Manifest) depends on Items 2, 3, and 5 being populated enough to be worth surfacing. It is the integration artifact — it ships last.

Recommended sequencing:
  Phase 1 (parallel): Items 3, 5, 6
  Phase 2 (parallel, after 6): Items 1, 7
  Phase 3 (after 2 is populated): Item 2
  Phase 4 (after 2, 3, 5): Item 4

---

## Item 1 — Charter Regression Suite

**Purpose:**
Atlas currently has no mechanism for detecting behavioral drift. When the charter is updated or a new Hermes version is loaded, there is no way to confirm Atlas still behaves consistently with its prior operating norms. Without this, the charter is aspirational documentation — not a behavioral contract. The regression suite turns the charter into a testable artifact by defining specific input scenarios with expected output shapes, checked after any charter patch, ADR addition, or major Hermes version bump.

**Success criterion:**
A file at `docs/charter/regression-suite.md` exists containing a minimum of 10 test cases. Each test case specifies: scenario description, input prompt (or category of input), expected behavior (what Atlas should do), failure indicators (what would signal a regression), and the charter clause being tested. At least one test case covers each of: cost-control triggers, approval intensity selection, escalation to Opus, self-correction when operating outside role, and transparency obligations. The suite has been run once manually against Atlas with results recorded.

**Dependencies:**
Hard dependency on Item 6 (Opus access). The most important behaviors to baseline are high-judgment synthesis decisions — the exact behaviors that only surface under Opus. Writing regression tests for Opus-class behaviors without access to Opus produces tests that can't be validated against the model they're designed to catch regressions in. Do not ship Item 1 until Item 6 is live.
Soft dependency on Item 2 (Agent Roles Register): role-specific behavioral tests require knowing what roles exist and what each is permitted to do.

**First artifact to ship:**
`docs/charter/regression-suite-v0-skeleton.md` — 10-case skeleton with scenario titles, expected behavior columns, and failure indicator columns filled in, test case bodies left as stubs for Opus review pass to complete. This is enough to validate structure before content.

**Full approval required?**
Yes. The charter regression suite defines what "correct Atlas behavior" means. Getting the baseline wrong has compounding downstream effects — every future regression check is calibrated against a flawed standard. The suite is also a policy artifact: it implicitly encodes which behaviors David considers non-negotiable. This requires David's explicit review and approval of the test cases before the suite is used operationally. Flag this for a Full approval on the populated v1 (not the skeleton).

**Opus dependency flag:**
HIGH. Do not run the first manual regression pass on Sonnet. The value of the suite is catching high-judgment synthesis regressions. Running it only on Sonnet validates the wrong capability tier.

---

## Item 2 — Agent Roles / Capabilities Register

**Purpose:**
Atlas currently has no authoritative list of what roles it occupies, what each role is permitted to do, and what it is explicitly not permitted to do. The research subagent identified this as "the single most visible structural gap." Without a roles register, behavioral guardrails are implicit, M6b's Layer 2 agent model cannot be designed with clear interface contracts, and handoff protocols (a core M6b concern) have no anchor.

**Success criterion:**
A file at `docs/roles/agent-roles-register.md` exists containing a minimum of 3 defined roles (Atlas as strategic advisor, Atlas as implementation executor, and at least one Layer 2 agent template). Each role entry contains: role name, activation context (when this role is in use), permitted actions, explicitly prohibited actions, escalation path (what triggers a handoff or approval request), and the charter clause that governs this role. David has reviewed and approved the role definitions — they represent his intent, not Atlas's inference.

**Dependencies:**
Soft dependency on Item 1: once the regression suite exists, role-specific behavior can be validated. Without that, the register is a written contract with no enforcement mechanism. Ship Item 2 before Item 4 (the session-start manifest surfaces the active role).

**First artifact to ship:**
`docs/roles/agent-roles-register-v0.md` — two roles fully populated (Atlas Strategic Advisor, Atlas Implementation Executor) with all columns filled. Layer 2 agent template left as a stub with column headers only, flagged as "M6b input required."

**Full approval required?**
Light approval sufficient for the initial register. Full approval recommended when the register is used to constrain Atlas behavior in a binding way (i.e., when it is referenced in the Session-Start Manifest as an active constraint). At that point it transitions from a documentation artifact to a policy artifact.

**Opus dependency flag:**
MEDIUM. The strategic advisor role boundaries are high-judgment enough that Opus drafting is preferable. Sonnet can scaffold the structure and populate the implementation executor role; Opus should review the permitted/prohibited boundaries for the advisor role before David signs off.

---

## Item 3 — Decisions / Open Questions Register

**Purpose:**
Open decisions are currently scattered across session notes, pre-session memos, and inline TODO comments. The research subagent identified three separate files where open decisions live with no canonical home. Without a register, decisions don't get resolved — they decay into stale TODOs or get re-litigated in future sessions because neither party knows the question was already raised. The register also serves as the working interface for the approval mechanism: when Atlas surfaces a Full approval request, the open question that prompted it should trace back to a register entry.

**Success criterion:**
A file at `docs/decisions/open-questions-register.md` exists. It has a defined schema (columns: ID, date opened, question, status, owner, resolution date, link to resolution artifact). All open questions surfaced in the pre-session prep memo and the two research reports are entered and triaged. At least one open question has been resolved and its resolution linked. Atlas uses the register as the default destination when surfacing an unresolved question mid-session (rather than inline notation in session docs).

**Dependencies:**
None. This is the most independent item in the brief. Can ship in Phase 1 alongside Item 6.

**First artifact to ship:**
`docs/decisions/open-questions-register.md` — schema defined, pre-populated with open questions from the pre-session prep memo and both research reports (estimated 8–12 questions). Status column filled for each.

**Full approval required?**
No. The register is a tracking artifact, not a policy artifact. Light approval on the initial schema is sufficient.

**Opus dependency flag:**
LOW. Schema and population work is Sonnet-appropriate. The only Opus-level judgment involved is deciding which open questions are consequential enough to warrant their own future Full approval request vs. which are resolvable tactically.

---

## Item 4 — Session-Start Substrate Manifest

**Purpose:**
Each session currently starts with Atlas reconstructing context from memory and whatever documents David surfaces. This is lossy and slow. The Session-Start Manifest is a machine-readable (or at minimum, structured) artifact that Atlas consults at the top of every session to establish: active role, open decisions requiring resolution, pending approvals, current sprint/phase, and any charter patches that took effect since last session. It is the integration artifact for the substrate — the place where Items 2, 3, and 5 surface into operational use.

**Success criterion:**
A file at `docs/substrate/session-start-manifest.md` exists with a defined schema. Atlas is able to read the manifest at session start and produce a session-context summary in under 60 seconds (one read + one synthesis). The manifest has been used for at least one full session with no reported context failures (Atlas mis-stated active role, missed an open decision, etc.).

**Dependencies:**
Hard dependencies: Item 2 (active role must be populated), Item 3 (open decisions must be populated), Item 5 (tool registry must have enough content to be worth surfacing). Item 4 ships last.

**First artifact to ship:**
`docs/substrate/session-start-manifest-schema.md` — schema only, no live data, with field definitions and a worked example showing what a session-start read would produce.

**Full approval required?**
Light approval on schema. Full approval when the manifest becomes the canonical session-start protocol (i.e., when David commits to providing it to Atlas at every session start). That transition makes it a behavioral policy for both parties.

**Opus dependency flag:**
LOW for schema design. MEDIUM for the first live use — the first session that uses the manifest as canonical context should use Opus for the session-start synthesis so the interpretation is high-fidelity.

---

## Item 5 — Tool Registry scaffolding

**Purpose:**
Atlas has no authoritative list of what tools are available, how they are invoked, what their failure modes are, or which require special permissions. Tool knowledge is currently implicit — Atlas infers capability from the toolset exposed at runtime. This produces subtle errors: tools get used in configurations that technically work but violate intended patterns, or Atlas wastes tokens attempting tools that aren't available in a given context. The Tool Registry converts implicit tool knowledge into explicit, queryable state.

**Success criterion:**
A file at `docs/substrate/tool-registry.md` exists containing entries for all Hermes built-in tools currently in use (terminal, search_files, read_file, write_file, patch, browser tools, delegate_task, cronjob, memory, skill tools). Each entry has: tool name, invocation pattern, primary use case, known pitfalls, permission requirements, and a "do not use when" field. Atlas references the registry when recommending tool selection during planning.

**Dependencies:**
None. Ships in Phase 1.

**First artifact to ship:**
`docs/substrate/tool-registry-v0.md` — five highest-use tools fully documented (terminal, read_file, write_file, search_files, patch). Remaining tools stubbed with name and primary use case only.

**Full approval required?**
No. Documentation artifact. Light approval on schema.

**Opus dependency flag:**
LOW. The "known pitfalls" and "do not use when" columns benefit from Opus review for completeness, but Sonnet can produce a useful first draft that Opus refines.

---

## Item 6 — Opus access via Hermes gateway

**Purpose:**
The Hermes gateway currently exposes a single configured model to workspace clients. There is no way for Atlas to escalate to Opus mid-task via the gateway model picker — the capability exists in principle (Anthropic's API supports it, the ADR-002 OAuth path allows it) but the gateway plumbing doesn't expose multi-model selection. This is a substrate gap, not a preference gap: the within-task model selection discipline (Item 7) and the Charter Regression Suite (Item 1) both require Opus to be genuinely accessible, not just theoretically available. Without Item 6, Items 1 and 7 are aspirational.

**Success criterion:**
Atlas can invoke Opus (claude-opus-4 or equivalent) from within the Hermes workspace via the approved gateway path. This is confirmed by a test invocation that returns an Opus-attributed response. The cost-control rule from ADR-002/memory is still in effect: Opus is reserved for high-judgment synthesis, not default. The gateway configuration documents which model IDs are available and what the invocation pattern is.

**Dependencies:**
Dependency on ADR-002 (Anthropic OAuth path) — confirmed active in approvals log. Dependency on Hermes gateway configuration access — this may require David to take a configuration action that Atlas cannot take unilaterally.

**First artifact to ship:**
A configuration change or documented invocation path that enables Opus access. If the change requires David's action (gateway config edit, API key scope change, or Hermes config update), the first artifact is a specific, actionable instruction set for David to execute, not a document Atlas authors alone.

**Full approval required?**
Yes. This is a new model spend commitment with cost implications that cannot be precisely estimated without knowing David's usage patterns under Opus access. It also changes Atlas's capabilities in a non-trivial way — any approval given under "Sonnet-only" context was implicitly bounded by that model tier. Expanding to Opus access changes the risk profile of Atlas recommendations. The cost-control rule (DAV-17 [REVISION]) already exists in memory but it was written under the assumption that Opus access was either unavailable or unreliable. A Full approval on the gateway configuration is the right gate.

**Opus dependency flag:**
N/A (this item IS the Opus access enablement).

**Atlas note:** This is the highest-priority item in the brief. Everything else is scaffolding; this is the enablement gate for the two highest-value items (Charter Regression Suite and model selection discipline). If David can address Item 6 in the first session of Substrate Brief work, Items 1 and 7 can follow immediately. If Item 6 slips, the brief degrades to Items 2, 3, 4, 5 — which are still valuable but are the supporting cast, not the lead.

---

## Item 7 — Within-task model selection discipline

**Purpose:**
Atlas currently operates on whatever model Hermes exposes by default for the session. There is no documented pattern for escalating to Opus within a task and dropping back to Sonnet for routine components. This produces two failure modes: (a) Atlas uses Sonnet for high-judgment synthesis work that genuinely requires Opus-class reasoning, producing subtly wrong outputs that look reasonable; (b) Atlas uses Opus for file reads, search, and format compliance, burning cost for no quality gain. The within-task model selection discipline codifies the escalation/de-escalation pattern as an operational procedure.

**Success criterion:**
A charter patch or ADR patch exists documenting the within-task model selection rule: Sonnet default; escalate to Opus for high-judgment synthesis, structural recommendations, fork analysis, novel architecture proposals, charter or ADR drafts; drop back to Sonnet for file reads, search, format compliance, summarization. Atlas states which model is in use when switching. The rule has been applied in at least one session and the model-switch disclosures are visible in the session transcript.

**Dependencies:**
Hard dependency on Item 6 (Opus access must be live before this discipline can be practiced, not just documented). The policy can be drafted on Sonnet; it cannot be validated on Sonnet alone.

**First artifact to ship:**
A patch to the relevant charter document (or a new ADR-005 if the scope warrants a standalone decision record) capturing the within-task model selection rule, the escalation triggers, and the disclosure requirement.

**Full approval required?**
Light approval on the rule as written. The rule itself was approved in the approvals log (row 35) as a future patch. The first artifact is executing that already-approved decision. If the drafting reveals the rule is more complex than the approvals-log entry captured — for example, if there are ambiguous cases that require a new policy decision — those ambiguous cases get flagged for Full approval before resolution.

**Opus dependency flag:**
HIGH for validation. The within-task selection rule should be reviewed and approved under Opus once Item 6 is live. A rule about when to use Opus, approved only on Sonnet, is not self-consistent.

---

## Scope confidence

Overall scope: High. The seven items are coherent, non-overlapping, and each has a clear completion criterion. The dependency graph is sound.

Individual items where confidence is below Medium:

Item 6 (Opus access): MEDIUM-LOW confidence on implementation path. Atlas does not know the current state of the Hermes gateway multi-model configuration. The success criterion is clear but the path to it may require David to take actions in system configuration that Atlas cannot inspect from this context. The first session of Substrate Brief work should start with a diagnostic: what does the current gateway config expose, and what change is required? Atlas should not attempt to design the configuration change without inspecting actual gateway state first.

Item 1 (Charter Regression Suite) test case count: MEDIUM confidence on the number 10. That number is a reasonable floor for coverage without being a proxy for completeness. David should treat 10 as a minimum, not a target. The Opus review pass may surface additional categories that require test cases.

Item 4 (Session-Start Manifest) on session discipline: MEDIUM confidence that the manifest will be consistently provided at session start without a reminder mechanism. The manifest's value depends on it being read before substantive work begins. Without a workflow hook (a reminder, a session template, or Atlas proactively asking for it), the manifest risks becoming a document that exists but isn't consulted. This is a human-process dependency that the brief cannot fully solve — flag it for David's attention when Item 4 ships.

---

## Open questions surfaced by this brief

These should be entered into Item 3's register when it ships.

OQ-001: What is the current Hermes gateway model configuration? What change is required to expose Opus? Does David need to take a configuration action, or can Atlas configure this?

OQ-002: Should the within-task model selection rule be a charter patch to an existing document or a new ADR-005? What is the right home for behavioral operating procedures that don't rise to the level of architectural decisions?

OQ-003: What is the intended relationship between the Charter Regression Suite and the existing Paperclip Atlas memo library (frozen per ADR-003)? Should regression test cases reference or extract from Paperclip memos, or treat them as distinct artifacts?

OQ-004: The Layer 2 agent stub in Item 2 requires M6b input. Should the Agent Roles Register explicitly note which roles are placeholder-pending-M6b vs. operative today? Or does including placeholder roles risk premature canonicalization of M6b design decisions not yet made?

---

*End of Substrate Brief v1 — Draft. Awaiting Opus review pass.*
