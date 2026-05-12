# Registries Research — Findings and Recommendations

*Research conducted: 2026-05-12. Sources: live reads of lumlist/DavidOS, lumlist/familyAI, lumlist/DavidAIStory, NousResearch/hermes-agent, outsourc-e/hermes-workspace; web research on multi-agent architectures and multi-tenancy patterns.*

---

## Executive Summary

1. **The hypothesis is mostly right, but two registries are missing and one needs scope expansion.** The seven proposed registries are individually justified, but the repo evidence reveals two implied-but-uncaptured registers: a **Decisions Index** (ADRs exist but the open/pending decision surface that precedes them doesn't) and an **Agent Roles / Capabilities Register** (the vision doc has eight empty agent role stubs — this gap is explicitly flagged in the repo audit as "the single most visible gap"). The Forks Register is less obviously urgent than these two.

2. **Hermes provides three substrate concepts worth borrowing directly:** the `MEMORY.md`/`USER.md` split (behavioral memory vs. factual user profile), the curator's `last_run_at` + lifecycle-state pattern (registries need freshness signals, not just content), and the context compressor's structured handoff prefix (every registry read should treat prior content as "reference only, not active instruction").

3. **Cursor Memory Bank is the closest external analog for Atlas's session-substrate pattern** — its `activeContext.md` + `progress.md` + `systemPatterns.md` hierarchy maps almost exactly onto what Atlas needs at session start. The key difference: Cursor's memory bank is project-scoped; Atlas's substrate is system-scoped across all active workstreams.

4. **Multi-tenancy is already implicit in the data.** Every existing register uses David-specific content but generic shape. The tenant isolation risk is concrete: Hermes profiles already support isolated `~/.hermes/profiles/<name>/` with separate `MEMORY.md`, `USER.md`, and `skills/` — DavidOS registries should mirror this isolation boundary. The highest leakage risk in a future multi-tenant DavidOS is the Atlas Observations register (per-session reflection content is deeply personal and must be tenant-namespaced before any sharing).

5. **The intake-to-handoff design brief should add one structural requirement not in the current hypothesis:** every registry entry needs a `source` field recording which session or agent created it. This is the most common multi-tenancy gap in early-stage personal AI systems and costs nothing to add now.

---

## Track 1: What the Repos Imply

### Existing Registries (with format details)

#### 1. Project Registry — `docs/project-registry.md`
**Shape:** Two markdown tables — Active Projects (Project | Type | Status | Goal | Current Phase | Next Decision | Active Tools | Review Date) and Business Idea Pipeline (Idea | Status | Why It Might Matter | Next Step | Confidence).

**Writer:** David (with Atlas able to propose updates). The registry appears to have been written once and not updated since the Paperclip → hermes-workspace migration — the "Active Tools" column still references ChatGPT and VPS, not Atlas/Hermes in the current stack, and "Current Phase" is pre-ADR terminology.

**Freshness signal:** None. The repo audit explicitly flags stale docs as a problem; the Project Registry is one of them.

**What's missing from the current shape:** No `tenant_id` field (critical for iZZi), no `assigned_agent` column (Atlas vs. Hermes vs. ChatGPT), no `last_updated` column. The "Next Decision" column is doing double-duty — it should be a foreign key pointer to the Decisions/Open Questions register, not a freetext field.

#### 2. Approvals Log — `docs/decisions/approvals-log.md`
**Shape:** Single append-only markdown table (Date | Intensity | Topic | Decision | Expires | Link). Nine entries as of 2026-05-11, all from the first real session under the new stack.

**Writer:** Atlas appends at session end. David is not expected to write to this file directly.

**Strongest design in the current registry set.** The two-intensity model (Light vs. Full), explicit expiry, and link to the source ADR or debrief is the right shape. ADR-004 specifies re-evaluation triggers when the log exceeds ~50 entries.

**What's missing:** No `tenant_id`, no `approver` field (there's only one approver today but the schema will need it for iZZi). The "Revocations and modifications" section is currently empty — revocations should appear as new rows per ADR-004, but the template doesn't enforce a `revocation_of` foreign key.

#### 3. ADR Index — `docs/decisions/README.md`
This is functionally a registry even though it's not named one. Columns: ADR number | short title | date | status. Currently has four entries plus one pending.

**The gap:** ADRs capture *made* decisions. The open question surface that *precedes* ADRs is scattered. FamilyAI (`docs/product/08-decision-log.md`) has explicit `D-009` through `D-014` pending items with `Status: Pending` and `Decision Gate` fields — this is the richer decision-tracking pattern. DavidOS has no equivalent. Open decisions surface in session debriefs, NEXT-SESSION-OPEN.md, and the parking lot — three different places with no unified index.

#### 4. Customer-Zero Patterns — `docs/atlas/customer-zero-patterns.md`
**Shape:** Append-only, dated observations from Atlas at session end. No entries yet — the file was created with a "first entries will appear at end of the session in which this file is created" note.

**Writer:** Atlas at session end. David reviews and curates.

**Design note:** The empty state is an honest placeholder, not a gap. The shape is correct.

---

### Implied but Uncaptured Registries (with evidence)

#### Implied 1: Agent Roles / Capabilities Register
**Evidence:** `david-ai-workspace-v0.md` has eight agent role stubs (Chief of Staff, Research, Product Strategy, GTM, Personal Life Admin, Health and Fitness, Finance/Admin, Tooling and Automation) that are 100% empty — no Purpose, Responsibilities, or Approval-required fields. The repo audit (`docs/atlas/audit/repo-audit-2026-05-11.md`) explicitly calls this "the single most visible gap relative to the vision principle."

`docs/atlas/identity/atlas-agent-record.json` shows the shape for one agent (id, name, role, title, capabilities, adapterType, adapterConfig, runtimeConfig, permissions, status). This is the right data shape for an agent register. Only Atlas has this record. Other agents have no structured record anywhere in the repos.

**Why it earns its keep:** Atlas needs to know at session start which agents exist, what they can and can't do, and which are active vs. paused. The absence of this register means Atlas reconstructs agent capability from context every session. This is the same problem ADR-004 solved for approvals.

#### Implied 2: Decisions / Open Questions Unified Surface
**Evidence:** `docs/sessions/NEXT-SESSION-OPEN.md` contains open threads (M6b research, ADR-004 charter update, Hermes update). `docs/sessions/drafts/parking-lot.md` is designed for ideas and observations. `docs/daily-dashboard-v0.md` has "Decisions Needed" and "Waiting on Me" tables. `docs/daily-command-center.md` has a "Decisions Needed" table. None of these are the same file. 

FamilyAI has the right model: `docs/product/08-decision-log.md` tracks decisions with `Status: Pending`, `Decision Gate:`, `Who Decides:`, `Alternatives:`, and `Risks Accepted:` fields — then routes closed items to ADRs in `docs/adrs/`. DavidOS has ADRs but not the upstream register that feeds them.

**Why it earns its keep:** Open questions currently have no canonical home. They appear in session debriefs, parking lot, and NEXT-SESSION-OPEN, but there's no single file Atlas can read to know "what's unresolved." This is also the riskiest gap for continuity — if Atlas misses an open question, it either re-asks it (wastes David's time) or assumes it was resolved (creates silent drift).

#### Implied 3: Cost / Spend Register
**Evidence:** The Opus cost incident (2026-05-10, ~$72 in an uncontrolled loop) is documented in `docs/story/01-founder-timeline.md`. The OpenRouter daily cap reduction is captured in `docs/sessions/submitted/2026-05-11T03-27-debrief.md` as an open action. `docs/tool-stack-inventory.md` has a "Keep / Test / Drop" column but no cost column. `docs/decisions/approvals-log.md` has Light/Full intensity but no cost-ceiling enforcement.

ADR-004's approval mechanism requires approval for spending, but there's no register tracking actual spend vs. budget. The Hermes insights engine (`agent/insights.py`) tracks `estimated_cost`, `actual_cost`, `billing_provider`, `total_tokens` per session in its SQLite state DB — this data exists but isn't surfaced into DavidOS docs.

**Assessment:** Less urgent than the two above. The approvals log covers the gate; a spend register would add a trailing ledger. Include as a section inside the Atlas Observations register rather than a standalone register — flag when session spend exceeds a threshold.

#### Implied 4: Tool Stack Decisions (beyond inventory)
**Evidence:** `docs/tool-stack-inventory.md` has a Keep/Test/Drop column but no rationale or date column. Decisions to pause OpenRouter, freeze Paperclip, and switch to Anthropic OAuth are documented in ADRs and session debriefs — but the *current operative state* of the tool stack (which tools are active today, which are paused, which are deprecated) requires reading multiple ADRs. The tool stack inventory is not regenerated after each ADR; it has stale content.

**Assessment:** Not a separate register — fold into Project Registry as a "Tool Stack" table or ensure the tool stack inventory is updated as part of session-end hygiene.

---

### Format / Structure Observations

1. **Append-only with links to source** (Approvals Log) is the strongest pattern in the current set. It degrades gracefully as it grows and remains auditable.
2. **Free-form markdown tables** (Project Registry, daily dashboards) work for human reading but are brittle for Atlas to parse — column headings don't enforce data types. At scale, these will need YAML frontmatter or structured JSON equivalents (Hermes `atlas-agent-record.json` is the right direction for machine-readable records).
3. **Template-driven drafts** (session-start/end templates, parking-lot template) are the right mechanism for Atlas-authored content, but the templates need a `session_id` and `author` field to maintain source provenance.
4. **The FamilyAI `docs/product/08-decision-log.md` pattern** (numbered decisions, explicit pending items, `Who Decides`, `Decision Gate`) is more operationally useful than DavidOS's current approach and should be adopted for the Open Questions / Decisions Register.

---

## Track 2: Hermes Substrate Concepts Worth Borrowing

### 1. MEMORY.md / USER.md Split
Hermes maintains two foundational memory files per profile:
- `memories/MEMORY.md` — agent-curated behavioral patterns, learned preferences, recurrent instructions
- `memories/USER.md` — factual user profile (who the user is, professional background, current priorities)

The `hermes_cli/profiles.py` `_CLONE_SUBDIR_FILES` list shows these are the two files copied when forking a profile — they are the minimum viable identity substrate.

**DavidOS equivalent:** `docs/context-packs.md` contains both factual profile content and behavioral preferences in one file. Splitting into:
- `docs/atlas/substrate/user-profile.md` — factual (David's background, current priorities, sensitive boundaries)
- `docs/atlas/substrate/behavioral-patterns.md` — Atlas-learned patterns (communication preferences, decision-making style, recurring corrections)

...would make it easier for Atlas to update behavioral patterns without touching stable factual content, and maps cleanly to a multi-tenant shape where `user-profile.md` is tenant-specific and `behavioral-patterns.md` is agent-maintained.

### 2. Curator State Pattern
`agent/curator.py` tracks: `last_run_at`, `last_run_duration_seconds`, `last_run_summary`, `run_count`, `paused`, `last_report_path`.

The curator fires based on inactivity (idle >2 hours, last run >7 days ago). This is a **freshness-signal pattern**: the curator doesn't just store content — it stores metadata *about when it last operated on that content*.

**DavidOS application:** Every register should have a `last_reviewed_at` header and an `auto-stale-after` value. The Approvals Log already has expiry dates per entry; the Project Registry and Open Questions Register should have the same. Atlas should surface registers approaching their stale date at session start (the same way ADR-004 requires surfacing approaching expiry on policy approvals).

### 3. Context Compressor Handoff Prefix
`agent/context_compressor.py` injects this prefix before summarized context:

> `"[CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions..."`

**DavidOS application:** Every register that Atlas reads at session start should have an equivalent framing — "this is operating context, not an active instruction list." The Atlas Operating Spec already has session-start context refresh protocol (`docs/atlas/context-refresh-protocol.md`) but doesn't specify *how Atlas should frame registry content to itself*. Adding this explicit framing prevents Atlas from treating stale registry entries as current directives.

### 4. Skills Lifecycle States
The curator manages skills through lifecycle states: active → stale (30+ days unused) → archived (90+ days). The `skills/index-cache/` provides a machine-readable index.

**DavidOS application:** The Customer-Zero Patterns register (`docs/atlas/customer-zero-patterns.md`) will accumulate entries that become stale as iZZi evolves. Adopting the same lifecycle (active → stale → promoted/archived) with a curator-equivalent review at defined intervals prevents the patterns register from becoming a graveyard of outdated observations.

### 5. Insights Engine Categories
`agent/insights.py` tracks: total_sessions, total_messages, total_tool_calls, total_input_tokens, total_output_tokens, estimated_cost, actual_cost, avg_session_duration, model_breakdown, platform_breakdown, tool_usage_patterns, skill_usage.

**DavidOS application:** The Atlas Observations register could include a structured section at session end that mirrors the Hermes insights categories (session length, tools used, decisions made, approvals logged, friction patterns). This makes the observations register machine-readable for trend detection, not just human-readable narrative.

### 6. Profile Isolation Architecture
`hermes_cli/profiles.py` creates fully isolated profile directories: `~/.hermes/profiles/<name>/` with own `config.yaml`, `.env`, `memories/`, `sessions/`, `skills/`, `home/`. The `_PROFILE_DIRS` list shows every directory is bootstrapped per-profile.

**DavidOS application:** The repo-as-substrate pattern mirrors this — each iZZi customer's DavidOS fork would be a separate repo with the same directory structure, David-specific content replaced with tenant-specific content. The risk is repos that have David-specific content hardcoded in paths or file bodies. Registry files with `tenant_id: david` in their YAML frontmatter can be validated in CI to ensure no tenant-specific strings appear in generic template files.

---

## Track 3: Comparable Tools Patterns

### Cursor Memory Bank
The Cursor Memory Bank ([gist](https://gist.github.com/ipenywis/1bdb541c3a612dbac4a14e1e3f4341ab)) uses six core files with explicit dependency hierarchy:

```
projectbrief.md → productContext.md, systemPatterns.md, techContext.md
                → activeContext.md → progress.md
```

| Cursor File | DavidOS Equivalent | Notes |
|---|---|---|
| `projectbrief.md` | `david-ai-workspace-v0.md` | Vision doc; correct |
| `productContext.md` | `docs/context-packs.md` (FamilyAI section) | Exists but not structured to this purpose |
| `systemPatterns.md` | `docs/decisions/` (ADR directory) | ADRs capture this, but read-time is high |
| `techContext.md` | `docs/tool-stack-inventory.md` | Exists, often stale |
| `activeContext.md` | `docs/sessions/NEXT-SESSION-OPEN.md` | Functionally equivalent; rename would improve clarity |
| `progress.md` | `docs/project-registry.md` | Partial; Project Registry doesn't track "what works" |

The critical missing analog: Cursor reads ALL memory bank files at the start of EVERY task — no exceptions. DavidOS's `docs/atlas/context-refresh-protocol.md` defines three refresh levels (Quick/Workstream/MajorDecision) but doesn't mandate a minimum read list. The registry list being designed tonight should become a mandated minimum read list for Atlas at Level 1 (Quick State Check).

### Devin / Cursor Operating Pattern
Devin maintains context in a fully externalized agent environment — the substrate is the task definition and environment state, not a structured registry. Cursor keeps context in the editor state, which is ephemeral. Neither has a durable structured registry equivalent to DavidOS's approach.

**Assessment:** DavidOS's registry-as-substrate pattern is *more sophisticated* than either Devin or Cursor for long-running, multi-workstream operation. This is a genuine DavidOS design advantage — don't flatten it toward Cursor's simpler memory bank.

### LangGraph State Object
LangGraph uses a central `TypedDict` state object (`AgentState`) that passes through all graph nodes. Fields include `messages`, `shared_knowledge`, task-specific fields. The state object is the "registry" in LangGraph terms — everything an agent needs to know is in this object at the start of each node's execution.

**DavidOS equivalent:** The session-start registry read is equivalent to loading the LangGraph state. The structural difference is that LangGraph state is in-memory and ephemeral; DavidOS registries are file-based and durable across sessions. Both are correct for their contexts.

### CrewAI Crew Context
CrewAI agents share a `CrewContext` that is implicitly passed between agents in a crew. The context includes task outputs, shared knowledge, and crew-level state. There is no explicit registry concept — context is emergent from task execution.

**Assessment:** CrewAI's implicit context is a design pattern to avoid for DavidOS. When Atlas delegates to Hermes, the explicit delegation packet (`docs/atlas/context-refresh-protocol.md` §"Delegation Context Packet") is the right approach — explicit over implicit.

### Google ADK Context Stack
[Google ADK](https://developers.googleblog.com/architecting-efficient-context-aware-multi-agent-framework-for-production/) describes a "context stack" that separates:
- **Session state** — ephemeral, per-turn
- **User state** — persistent, per-user preferences and history
- **App state** — shared across users, application-wide configuration
- **Agent memory** — long-term patterns and learned behaviors

**DavidOS application:** This four-layer taxonomy is a better mental model than a flat list of registries. The proposed DavidOS registries map as:
- Session state → `docs/sessions/NEXT-SESSION-OPEN.md` + Parking Lot
- User state → `docs/context-packs.md` + Atlas Observations
- App state → Approvals Log + Project Registry + ADR Index
- Agent memory → Customer-Zero Patterns + Atlas behavioral-patterns substrate

### Mem0 / Honcho Memory Patterns
Mem0 ([arxiv.org](https://arxiv.org/abs/2504.19413)) stores explicit facts extracted from conversations; Honcho stores implicit behavioral patterns derived from repeated interactions. Both use `user_id` scoping for multi-tenancy.

**DavidOS application:** The Atlas Observations register is closer to Honcho's implicit pattern model than Mem0's explicit fact model. Atlas's session-end structured reflections should capture *patterns* (recurring friction types, recurrent decision themes, correction patterns) not just facts. The observations register should have a `pattern_type` field alongside the narrative.

---

## Track 4: Multi-Tenancy Patterns

### Data Shape: Implicit Tenant Keys
The [AWS multi-tenant agentic AI guide](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/introduction.html) (Aaron Sempf & Tod Golding, July 2025) recommends propagating tenant context via JWT through all agent calls. For file-based registries (DavidOS's approach), the equivalent is a `tenant_id` field in YAML frontmatter on every register file, plus a `tenant_id` column in every markdown table.

**Minimal implementation for DavidOS today:**
```yaml
---
tenant_id: david-izzard
registry: project-registry
schema_version: 1
last_reviewed: 2026-05-12
---
```

This YAML frontmatter costs nothing to add now and makes tenant identity explicit. When the second iZZi customer onboards, they fork the repo template, change `tenant_id`, and no David-specific content bleeds into their instance.

### Agent Memory Isolation
Per Mem0's [security best practices](https://mem0.ai/blog/ai-memory-security-best-practices) (2026), the minimum viable multi-tenant memory isolation requires:
- Per-user memory namespacing (queries only search within the authenticated user's memory scope)
- Per-session isolation for ephemeral working context
- Role-based access control for read/write/delete on memory stores

For DavidOS file-based registries, isolation is enforced at the repo boundary (each tenant is a separate repo). The risk is Atlas reading from the wrong registry if it has access to multiple tenant repos simultaneously. The mitigation is the `tenant_id` header check: Atlas should validate that the `tenant_id` in the register matches the current session's tenant before loading.

### Context Contamination Risk: Atlas Observations
The Atlas Observations register (`docs/atlas/observations/`) is the highest-risk register for multi-tenancy because it contains deeply personal session-end reflections. The [Lumenova multi-agent governance guide](https://www.lumenova.ai/blog/taming-complexity-governing-multi-agent-systems-guide/) identifies "identity/credential leakage/theft risks" as a primary MAS risk category.

**Mitigation:** Atlas Observations entries must have `tenant_id` in every entry header, and the register must be excluded from any pattern-aggregation process that runs across tenant boundaries. Customer-Zero Patterns (`docs/atlas/customer-zero-patterns.md`) is the explicit abstraction layer where personal observations are promoted to generic patterns — only the promoted, anonymized patterns should be shared.

### Per-Tenant Configuration Pattern
AWS ADK recommends `tenant personas` that shape how an agent integrates tenant context — tenant-specific memory, knowledge, tools, and guardrails. For DavidOS, the equivalent is the agent record (`docs/workspace/agents/atlas.agent.json`) plus the behavioral patterns substrate. These two files together define the tenant-specific agent persona.

**Structured for many:** The `atlas.agent.json` schema (id, name, role, capabilities, adapterConfig, runtimeConfig, permissions) is already generic. The David-specific content is in the `capabilities` field body text and the `adapterConfig.model` value. A multi-tenant template would parameterize these fields.

### Pooled vs. Siloed Model Decision
For iZZi's first additional customer:
- **Siloed (separate repos):** Maximum isolation, zero risk of cross-tenant contamination, easy mental model. Cost: operational overhead scales linearly with customers. This is the right choice for the first 10 tenants.
- **Pooled (shared registry server with tenant_id scoping):** Appropriate at 50+ tenants. Requires a proper database layer (Supabase) to replace file-based registries. The FamilyAI schema (with `workspace_id` as the tenant key, RLS policies, and audit events) is the right template for this transition.

**Recommendation:** Stay siloed (separate repos) for DavidOS's first 10 iZZi customers. Add `tenant_id` frontmatter now as a zero-cost preparation step.

### Noisy Neighbor in Personal AI Context
The multi-tenancy noisy neighbor risk in personal AI is not compute contention — it's *cognitive contamination* of Atlas's context. If Atlas loads context from two tenant repos in the same session, it risks applying David's behavioral patterns to another tenant's session. The mitigation is the same as the memory isolation rule: validate `tenant_id` matches session context before loading any register.

---

## Synthesis: Recommended Registry List

### Updated Registry Set (8 registries)

The original hypothesis proposed 7 registries. Based on research findings:
- Add: **Agent Roles / Capabilities Register** (strongly implied by repo gaps)
- Add: **Decisions / Open Questions Register** (replaces the vague "Forks Register" as more foundational)
- Rename: Forks Register → include fork/decision-branch tracking within the Decisions Register
- Keep all 6 original registries with format refinements noted below

---

#### Registry 1: Project Registry

**Purpose:** Tracks active projects, ideas pipeline, and agent-supported workstreams. Atlas reads this first at session start to understand current workstream context.

**Format (revised):**
```yaml
---
tenant_id: david-izzard
registry: project-registry
schema_version: 2
last_reviewed: YYYY-MM-DD
---
```

Table columns: Project | Type | Status | Goal | Current Phase | Next Decision (link to Decisions Register) | Assigned Agent | Last Updated | Review Date

**Owner/Writer:** David owns. Atlas may propose updates at session end via `[APPROVAL: wiki-edit]`.

**Why it earns its keep:** Without this, Atlas cannot know which workstreams are active without reading all session debriefs. One-file-open to understand the entire operating landscape.

**Multi-tenancy notes:** `tenant_id` in frontmatter. "Assigned Agent" column separates tenant-specific agent assignments from generic project types.

**Gap to close:** Remove freetext "Next Decision" in favor of a link to a Decisions Register entry ID. Add `Assigned Agent` column. Add `last_updated` column.

---

#### Registry 2: Approvals Log

**Purpose:** Durable append-only record of every approval — what was authorized, when, at what intensity, with what expiry. Atlas reads at session start to know what's already authorized.

**Format:** Current format per ADR-004 is correct. Additions recommended:
- Add `approver` column (currently always "David" but needs to be explicit for multi-tenancy)
- Add `revocation_of` column (NULL for new entries, foreign key for revocations)

**Owner/Writer:** Atlas appends at session end. David may revoke by adding a new row.

**Why it earns its keep:** Without this, Atlas re-asks approval for already-approved patterns. ADR-004 documents this clearly. The log has already proven its value after only one session.

**Multi-tenancy notes:** `tenant_id` in frontmatter. `approver` column identifies the human principal per tenant.

---

#### Registry 3: Decisions / Open Questions Register

**(New. Replaces the proposed "Forks Register" as more foundational.)**

**Purpose:** Single canonical surface for (a) open questions not yet escalated to ADRs, (b) decisions pending David's input, and (c) fork points where a decision is needed before work can branch. The FamilyAI `docs/product/08-decision-log.md` is the proven format.

**Format:**
```
D-NNN  Status: Pending | Resolved | Deferred
Decision/Question: <what needs to be decided>
Context: <why this matters now>
Options: A | B | C
Recommendation: <Atlas recommendation, if any>
Decision Gate: <what unblocks if resolved>
Who Decides: David | Atlas | Technical
Expires: YYYY-MM-DD or n/a
Link to ADR: n/a | ADR-NNN (when resolved and escalated)
```

Resolved items link to the ADR they generated; pending items are Atlas's primary read at session start for "what decisions does David need to make today."

**Owner/Writer:** Atlas creates entries when a decision surface is identified. David resolves or defers. Resolved items are closed and linked to their ADR.

**Why it earns its keep:** Open questions currently appear in 4+ different places in the DavidOS repos (NEXT-SESSION-OPEN.md, session debriefs, parking lot, daily dashboards). This register consolidates them. It also captures the "fork" concept from the original hypothesis — a decision fork IS an open question.

**Multi-tenancy notes:** `tenant_id` in frontmatter. `Who Decides` column supports future role delegation.

**Note on Forks Register:** The original "Forks Register" hypothesis (track soft-fork/compound-fork/time-pressured-fork status) is useful but secondary. Fork status is a *dimension* of a decision (what kind of decision is this?) not a separate register. Add a `fork_type` field to the Decisions Register: `none | soft | compound | time-pressured`.

---

#### Registry 4: Risks Register

**(New as proposed.)**

**Purpose:** Known risks with likelihood/impact/mitigation/owner. The `docs/diagnostic-loop-v0.md` has a section on Approval and Risk but no durable register. The FamilyAI `docs/product/11-strategy-critique.md` has risk language scattered through it. Neither is a structured register.

**Format:**
```
R-NNN  Status: Open | Mitigated | Accepted | Closed
Risk: <one-line description>
Category: Technical | Business | Security | Compliance | Operational
Likelihood: High | Medium | Low
Impact: High | Medium | Low
Mitigation: <what is being done>
Owner: David | Atlas | TBD
Next Review: YYYY-MM-DD
Source: <session or debrief that surfaced this>
```

**Owner/Writer:** Atlas identifies during session work and documents at session end. David reviews and sets Owner/Next Review.

**Why it earns its keep:** The Opus cost incident (2026-05-10) should have been a Risks Register entry the moment model routing was configured. The `docs/diagnostic-loop-v0.md` Approval and Risk section has the right diagnostic questions but no place to persist the answers. Without a register, risks are re-discovered every session.

**Multi-tenancy notes:** `tenant_id` in frontmatter. Risk categories and format are generic; risk content is tenant-specific.

---

#### Registry 5: Agent Roles / Capabilities Register

**(New — implied by repo gaps.)**

**Purpose:** Canonical record of all agents in the DavidOS stack: what they can do, what requires approval, what model/adapter they use, and their current status. The vision doc's empty agent role stubs (`david-ai-workspace-v0.md`) should be populated here.

**Format (YAML, one file per agent OR a structured markdown table):**
The `docs/atlas/identity/atlas-agent-record.json` is the right machine-readable shape. For Atlas's session-start reading, a single human-readable markdown file is better:

```
## Agent: Atlas
Role: Chief Systems Advisor
Status: Active | Paused
Model: anthropic/claude-sonnet-4.6
Adapter: hermes_local
May do without approval: [list]
Requires approval for: [list]
Reads at session start: [registry list]
Writes at session end: [registry list]
Agent record: docs/workspace/agents/atlas.agent.json
Last updated: YYYY-MM-DD
```

**Owner/Writer:** David configures. Atlas updates its own record under `safe-self-improvement` permissions. New agent registration requires `[APPROVAL: install]`.

**Why it earns its keep:** Atlas currently cannot tell David "here are all active agents and their capabilities" without reading scattered files. When a second agent is added (e.g., a daily-view-builder or a FamilyAI research agent), the register becomes essential for Atlas to route work correctly.

**Multi-tenancy notes:** `tenant_id` in frontmatter. Model configurations are tenant-specific; role definitions and approval gates are generic templates.

---

#### Registry 6: Atlas Observations Register

**(New as proposed — `docs/atlas/observations/`.)**

**Purpose:** Session-end structured reflections by Atlas for self-improvement loop. Captures patterns, not just narrative.

**Format (per entry, one file per session or one append-only file):**
```yaml
---
session_id: 2026-05-12T04-00
tenant_id: david-izzard
author: atlas
---

## Session Summary
<2-3 sentence narrative>

## Patterns Observed
- pattern_type: friction | correction | workflow | decision
  description: <what happened>
  recurrence: first | recurring | resolved
  
## Decisions Supported
<list of Decisions Register entries touched>

## Approvals Logged
<list of Approvals Log entries added>

## Risks Surfaced
<list of Risks Register entries added>

## Recommendations for Next Session
<bulleted list>

## Customer-Zero Signal
<if any pattern here generalizes to iZZi customers, note it — this feeds customer-zero-patterns.md>
```

**Owner/Writer:** Atlas writes at session end. David reviews. High-value patterns are promoted to `docs/atlas/customer-zero-patterns.md`.

**Why it earns its keep:** Currently Atlas produces session debriefs in `docs/sessions/submitted/` but these are narrative, not structured for machine reading. The structured observations register enables trend detection across sessions (recurring friction patterns, improving approval discipline, model cost trends).

**Multi-tenancy notes:** `tenant_id` in every entry. The explicit `customer-zero-signal` field is the abstraction boundary — only promoted, anonymized signals cross tenant boundaries.

---

#### Registry 7: Customer-Zero Patterns

**Purpose:** Reusable patterns harvested from DavidOS for future iZZi customers. The abstraction boundary between David-specific experience and generic iZZi template.

**Format:** Current shape in `docs/atlas/customer-zero-patterns.md` is correct (append-only, dated). Add structured metadata per pattern:
```
## Pattern: [name]
Date: YYYY-MM-DD
Source session: <session_id>
Category: Governance | Workflow | Registry | Agent | Security | Cost
Applicability: Universal | Solo-Founder | Non-Technical-Operator | Small-Business
Promoted from Atlas Observations: <entry ref>
Status: Draft | Reviewed | Canonical
```

**Owner/Writer:** Atlas proposes at session end from Observations Register. David reviews and promotes to Reviewed/Canonical.

**Why it earns its keep:** This is iZZi's product IP accumulation mechanism. Every session David operates DavidOS, Atlas can harvest 1-3 patterns. After 50 sessions, the Canonical patterns list is the basis for iZZi's playbook. Without a structured register (vs. narrative notes), this IP doesn't accumulate in a usable form.

**Multi-tenancy notes:** Customer-Zero Patterns are intentionally *abstracted away from tenant-specific content*. They should contain no David-specific data — only generic patterns. This is the designed information flow: Atlas Observations (tenant-specific) → Customer-Zero Patterns (generic, reusable).

---

#### Registry 8: Atlas Substrate / Session-Start Bundle

**(Not in original hypothesis — structural recommendation, not a new register.)**

**Purpose:** The ordered list of files Atlas MUST read at every session start — equivalent to Cursor Memory Bank's mandatory read list. Not a registry itself, but a formal registry manifest.

**Format:**
```markdown
# Atlas Session-Start Substrate

Required reads (Level 1 — Quick State Check):
1. docs/decisions/approvals-log.md — what's authorized
2. docs/sessions/NEXT-SESSION-OPEN.md — active threads
3. docs/project-registry.md — workstream state
4. docs/workspace/agents/atlas.agent.json — own capabilities/constraints
5. docs/atlas/substrate/user-profile.md — tenant identity
6. docs/atlas/substrate/behavioral-patterns.md — learned preferences

Required reads (Level 2 — Workstream Context):
[+ registry for whichever workstream is being entered]

Required reads (Level 3 — Major Decision):
[+ Decisions Register + Risks Register + ADR directory]
```

This manifest transforms the registry list from "files Atlas might read" to "files Atlas must read." It should live at `docs/atlas/session-start-substrate.md`.

---

## Patterns We Should NOT Adopt

### 1. Cursor Memory Bank Hierarchy (directly)
Cursor Memory Bank assumes a single-project scope with a clear `projectbrief.md` at the root. DavidOS operates across 3+ active workstreams simultaneously (DavidOS, FamilyAI, DavidAIStory, iZZi Builder Services). Forcing all context into one hierarchy creates a false single-project framing. **Adopt the concept (mandatory read list, explicit file dependency hierarchy) but not the single-hierarchy structure.**

### 2. LangGraph-style In-Memory State
LangGraph's state machine pattern is correct for structured workflows but requires all state to fit in a `TypedDict` passed through nodes. DavidOS's state (open questions, risks, approvals, patterns) is durable and cross-session — it can't be an in-memory object. **Do not attempt to implement a runtime state graph for DavidOS registries. File-based markdown with YAML frontmatter is the right substrate for the current scale.**

### 3. Mem0 for Atlas Memory
Mem0's explicit-fact extraction architecture (49% temporal retrieval accuracy on LongMemEval) is weaker than Honcho's dialectic/implicit-pattern architecture for the DavidOS use case. Atlas needs to infer patterns from repeated corrections and preferences, not just store explicit facts. **If upgrading Hermes's memory backend, evaluate Honcho or Hindsight over Mem0.** This is a Hermes-level decision, not a DavidOS registry decision — flag for ADR-005 consideration.

### 4. CrewAI Implicit Context
CrewAI passes context implicitly between agents. For DavidOS, where Atlas delegates to Hermes, the delegation context packet (`docs/atlas/context-refresh-protocol.md` §"Delegation Context Packet") is the established explicit pattern. **Do not replace explicit delegation packets with implicit context passing — it creates exactly the context contamination risk identified in Track 4.**

### 5. Blackboard Pattern for Multi-Agent Communication
The event-driven blackboard pattern (Confluent, 2025) works well for distributed agent systems with many concurrent producers and consumers. DavidOS currently has one primary agent (Atlas) with occasional Hermes delegation. **The blackboard pattern is overengineered for the current scale. Revisit at 5+ concurrent agents.**

### 6. ADR-for-everything
FamilyAI's decision-log approach (D-NNN with Status: Pending) is better for open questions than creating an ADR for every question. ADRs should remain the output of a decision, not the tracking mechanism for open questions. **Keep ADRs as formal records of resolved decisions; use the Decisions Register for unresolved questions.**

---

## Open Questions for Atlas Next Session

1. **Session-Start Substrate formalization:** Should `docs/atlas/session-start-substrate.md` be created as a formal file that Atlas is instructed to read first in every session? This is a 30-minute implementation task — propose in next session with `[APPROVAL: wiki-edit]`.

2. **Decisions Register vs. existing structures:** Three places currently track open decisions (NEXT-SESSION-OPEN.md, parking lot, daily dashboard). Consolidating into a Decisions Register creates migration work. Does David want to migrate existing open items, or does the Decisions Register start fresh from the next session? Suggest: start fresh, with NEXT-SESSION-OPEN.md as an index that points to D-NNN entries.

3. **Agent Roles Register urgency:** The eight empty agent role stubs in `david-ai-workspace-v0.md` represent a known gap. Should populating the Agent Roles Register be a Priority 1 task in the next session, or does it wait until more agents exist beyond Atlas? Atlas can draft all eight agent profiles in one session based on the vision doc intent — propose as offline-queue item.

4. **`tenant_id` frontmatter rollout:** Adding YAML frontmatter to 7 registry files is a 15-minute task. Propose as part of next session's hygiene pass — include in `docs/sessions/REPO-HYGIENE-CHECKLIST.md`.

5. **Atlas Observations format validation:** The proposed observations format (YAML-prefixed entries with `pattern_type` structured field) is a design hypothesis. It should be stress-tested against one session's worth of real data before being formalized. **Do not promote to durable policy until 3 sessions of use — capture first observations in the existing session debrief format, then structure from patterns.**

6. **FamilyAI registry alignment:** FamilyAI has the richer Decisions Register pattern (`docs/product/08-decision-log.md` with D-NNN, Status, Decision Gate, Who Decides) while DavidOS does not. Should DavidOS adopt the FamilyAI format verbatim, or should a shared template be created that both repos reference? This is an iZZi customer-zero question — the answer becomes the iZZi Decisions Register template.

7. **When does the Risks Register justify its maintenance cost?** The proposed Risks Register earns its keep when David operates multiple concurrent projects with cross-cutting risks (e.g., a security decision in DavidOS affects FamilyAI). Today DavidOS has 2 active projects. At 4+, the cross-project risk surface becomes non-trivial. **Propose as a "create now, minimal maintenance" register — Atlas adds one entry per session, no more.**

---

*Report compiled by: Perplexity Computer subagent*
*Repos read: lumlist/DavidOS (HEAD ~1493b6e), lumlist/familyAI, lumlist/DavidAIStory, NousResearch/hermes-agent, outsourc-e/hermes-workspace*
*External sources: AWS Prescriptive Guidance on Multi-Tenant Agentic AI (July 2025), Mem0 Security Best Practices, Cursor Memory Bank gist, Lumenova MAS Governance Guide, dev.to multi-tenant agents article*
