# Proposal — Minimum Viable Governed Intent Protocol & Context-Governance Layer

**Status:** PROPOSAL — working draft. **NOT APPROVED ARCHITECTURE.**
**Date:** 2026-05-17
**Author:** Atlas (claude-opus-4-7, David-approved Opus governance session)
**Supersedes in scope:** the Part B governance design and Fix 13 framing in
`../../audits/preparation/2026-05-14-atlas-comprehensive-fix-and-governance-proposal.md`

> This document is a working draft. It is **not in force** and does **not**
> represent approved DavidOS architecture until **ADR-005 is created** and
> the corresponding entries are appended to
> `../../decisions/approvals-log.md`. Until both exist, nothing here may be
> implemented. Approval is governed by
> [ADR-004](../../decisions/ADR-004-workspace-native-approval-mechanism.md).

---

## 1. Executive recommendation

Adopt a Governed Intent Protocol (GIP) as a thin wrapper around the
existing v0.1 policy kernel (`docs/autonomy/action-map.md`,
`modifiers.md`, `SCHEMA.md` — all present, verified). Preserve the kernel;
add a context layer, manifests with ceilings, a decision protocol, and a
tier-aware substrate adapter seam with Hermes as the only real v1 adapter.
Validate through one loop: building an AI project/business. Build nothing
speculative. Agents (Karrigan/Hustler/Jeff/Jobs) and tools (Claude
Code/Codex/Ruflo/NotebookLM/Obsidian) are registry entries and invariants
only — zero implementation.

Core judgment: the v0.1 substrate is structurally sound but (a) blind to
workflow/skill/script/project/substrate context and (b) Hermes-welded via
the per-row "Hermes mechanism" field (SCHEMA.md lines 64-71). GIP fixes
both with one pattern already proven in the repo: the cron
"approve-the-actor-once, per-run-doesn't-re-gate" pattern (2026-05-14
proposal Fix 6/Cat 20). Generalize that one pattern; invent nothing else.

## 2. Proposed decision statement (what David approves)

"I approve adopting the Governed Intent Protocol as a thin wrapper around
the existing autonomy kernel, with: an 11-field intent envelope; a context
model; a decision protocol (skill, not infrastructure); a manifest model
with ceilings, a non-grantable category set, and memory writes as an
elevated-scrutiny non-grantable surface; an authority-expansion invariant;
a tier-aware decision-direction invariant; a substrate-portability
contract; the principle that the repo is the audit/change substrate not
the governance brain; an anti-goals fence; an 8-field agent registry; a
6-tier tool/substrate registry; and a structured decision log as the
observability spine. The v0.1 kernel is preserved and explicitly labeled
draft-pre-ADR. ADR-005 ratifies GIP (not v0.1). The AI project/business
build loop is the sole acceptance test for v1."

Intensity: **L1 Full** — standing structural policy (SCHEMA.md §4b;
ADR-004 lines 99-113).

## 3. Layer model

- **L1 Intent surface** — operator/agent emits a Governed Intent Envelope.
- **L2 Decision Protocol (NEW)** — envelope + manifests + kernel →
  Decision (rung, intensity, granted scope, structured citation). This is
  Fix 19's `davidos-router`, promoted from "match a category" to "evaluate
  an envelope." A skill, not infrastructure (2026-05-14 proposal B.5).
- **L3 Policy kernel (EXISTS, preserved)** — action-map / modifiers /
  SCHEMA. The "Hermes mechanism" field is reread as "enforcement binding,"
  resolved by L4.
- **L4 Substrate adapter seam (NEW, minimal)** — one real adapter: Hermes.
  All others registry-only.
- **L5 Execution + audit (mostly EXISTS)** — Hermes executes; a structured
  decision record is appended (the observability spine, §12). The future
  UI is a reader of this log.

### C1 — Substrate-portability contract

The envelope and the Decision schema are **substrate-neutral by
contract**. Substrate-specific enforcement detail lives **only** in the
adapter (L4) — never in the envelope, never in a kernel row. The kernel's
"Hermes mechanism" field is reinterpreted as an abstract "enforcement
binding" that the active adapter resolves. Consequence: Hermes, Claude
Code, Codex, or any future environment can map into the same schema
without a schema change — they supply an adapter, not a new envelope.
This is what makes the control plane tool-agnostic in practice and not
just in aspiration. [reusable]

[reusable] the five-layer split + C1 contract.
[david-specific] the kernel's repo names and the Hermes binding.

## 4. Minimal Governed Intent Envelope (11 fields)

1. `intent` — free text: what is wanted
2. `principal` — Atlas|David|Karrigan|Hustler|Jeff|Jobs|subagent:<id>|cron:<id> (default Atlas)
3. `action_category` — matched action-map category or "uncategorized"
4. `context_ref` — manifest id(s) or "ad-hoc"
5. `substrate` — hermes (default) | claude-code | codex | ruflo
6. `resource_class` — repo|filesystem|network|credential|external-recipient|external-representation|identity
7. `reversibility` — reversible|checkpointed|irreversible
8. `blast_radius` — self|repo|account|external|external-representation|identity
9. `side_effects` — none|local-state|external-send|spend|auth-write
10. `capability_grant` — manifest scope token or "none (ask)"
11. `posture` — conversational|advisory|approval-disciplined (governs
    style/cadence ONLY; never the rung)

Hard cap at 11. Safe defaults → a routine action emits a near-empty
envelope. Field-sprawl is the documented failure mode of every
governance-envelope effort (WS-Security, over-scoped OAuth); the cap is
the design. [reusable] entire envelope. [david-specific] principal enum.

## 5. Context model

Context is structured INPUT to the Decision Protocol, NOT a modifier
(rationale §13). Dimensions: workflow / skill / script / project /
substrate (each can carry a manifest); `resource_class` (maps onto
action-map's existing five domains — relabel, not new taxonomy);
`reversibility` (already implicit in ADR-004 intensity heuristics, made
explicit); `blast_radius` (what Fix 3/Cat 16b gropes toward manually,
made first-class; adds `external-representation` for Jeff); plus
`external_side_effects` and `secrets` flags (promote latent Cat 3c/7/16
concerns).

Key point: ~7 of these already exist implicitly, scattered across
action-map rows + ADR-004 heuristics + SCHEMA §7's deferred list. The
context model names what the system already reasons about ad hoc so the
decision is consistent and auditable. Not new governance — consistent
governance. [reusable]

## 6. Decision protocol outline

A skill (`davidos-router` reframed). Procedure, no runtime plumbing
(2026-05-14 proposal B.5). Steps: parse envelope → match category against
action-map Description fields → look up base rung → apply modifiers per
SCHEMA §3 conflict rules → evaluate context + manifest grant + ceilings →
apply invariants (non-grantable set §7, authority-expansion §8,
decision-direction §9, repo-not-brain C5) → emit Decision
{final_rung, intensity, granted_scope, structured_citation} → append
decision record to the observability spine (§12). Citation is an **object**
(category name + modifiers + manifest id + invariants fired), NOT line
numbers (replaces SCHEMA §4 step 5's brittle line-number string; matches
Fix 12 intent). [reusable] protocol. [david-specific] repo/category
specifics.

## 7. Manifest model — ceilings, non-grantable set, memory elevation

A manifest = small declared-context file carrying a scoped capability
grant. The grant IS the pre-authorization (cron pattern, generalized).
Fields: `id | type (workflow|project|skill|script) | principals_allowed |
substrates_allowed | repos/paths_in_scope | capability_grant | ceilings |
expiry (reuses ADR-004 90-day policy default) | decision_log_target`.

**Ceilings (mandatory on every grant):** spend cap, recipient allowlist,
irreversibility=never-without-ask. Any action exceeding any ceiling
auto-downgrades to L1 — never silent-grant.

**Non-grantable category set** (no manifest may pre-authorize these; they
always re-gate per-action regardless of context):
- external sends with legal/financial/representational content (Cat 15)
- spend / account creation (ADR-004 canonical list line 68)
- legal/privacy conclusions (ADR-004 line 72)
- identity/structural edits (Cat 16/17/18/19)
- **C4 — memory writes (Cat 8).** Memory is an elevated-scrutiny,
  non-grantable surface. A manifest can never silent-grant a memory
  write. Rationale: memory persists cross-session and silently shapes
  every future session's behavior; a blanket grant on memory is a slow
  identity-drift vector. Cat 8's L2 base rung is unchanged for
  interactive use; the change is that **manifests cannot pre-authorize
  it** — memory writes inside an approved context still surface.

This is the Hustler containment primitive: his job is continuous
operation in exactly the external-claims/spend cluster, so a blanket
manifest grant would be a privilege-escalation vector. The set
neutralizes it. [reusable — every multi-agent iZZi customer needs this]

v1 populates exactly ONE manifest: the project manifest for the build
loop. Workflow/skill/script manifest types are schema-defined,
unpopulated. Do not pre-populate.

## 8. Authority-expansion invariant

No agent — Atlas included — may author or widen any agent's capability
grant. Creating/widening a grant is itself non-grantable, identity-level,
David-only, and agent/subagent-forbidden. Generalizes Modifier 1's
load-bearing logic ("identity-shaping work cannot be delegated",
modifiers.md lines 13-19) from subagents to all agents. Atlas may PROPOSE
a grant change; only David's logged L1 Full enacts it. Atlas widening any
grant unilaterally is structurally impossible, not merely discouraged.
Without this, Atlas is one compromised principal away from system-wide
self-expansion. [reusable — core safety invariant]

## 9. Tier-aware decision-direction invariant

Decisions flow down the tier hierarchy only; results/audit flow up.
- T1 control plane (DavidOS/Atlas) = **emit**
- T2 execution/orchestration (Hermes) = **receive-only**
- T3 build/dev tools (Claude Code, Codex) = **receive-only**
- T4 multi-agent build orchestration (Ruflo) = **receive-only**
- T5 knowledge/research (NotebookLM, Obsidian) = **none**
- T6 future UI = **none** (reader only)

A substrate's OUTPUT may become INPUT to a new envelope, but no substrate
may produce a Decision. T4 can never short-circuit to T1. Hard encoding
of "Ruflo is not the governance brain." [reusable]

### C5 — Repo is the audit/change substrate, not the governance brain

The repo/GitHub is where decisions and changes are recorded, diffed, and
audited — the durable change/audit substrate. It does **not** make
governance decisions. No repo automation (CI, hooks, bots) may act as a
decision-maker. Governance decisions are made by the Decision Protocol
and ratified by David via ADR-004; the repo's sole governance role is
durability and auditability. [reusable]

## 10. Minimal agent registry (8 fields)

`id | role | primary_function | posture | default_model_tier |
execution_authority (none|bounded|standard) | allowed_tools_or_substrates
| status (active|named-future)`

Field justification (registry serves ONLY governance, routing, UI labels,
cost/model posture, authority boundaries):
- `id` — routing + log handle
- `role` — one-line UI/citation label
- `primary_function` — what routing keys off to pick the agent
- `posture` — interaction style/cadence; orthogonal to authority
  (resolves the open question at karrigan-intent-capture.md line 96)
- `default_model_tier` — cost posture; Karrigan=higher
  (karrigan-intent-capture.md lines 13,36), others Sonnet per SOUL.md §5
- `execution_authority` — authority-boundary primitive; Karrigan=none initially
- `allowed_tools_or_substrates` — routing + containment
- `status` — only Atlas=active; Karrigan/Hustler/Jeff/Jobs=named-future

Explicitly excluded: identity/SOUL layer, memory, credentials,
relationships, schedules. Governance/routing registry, not a profile
system. [reusable] structure. [david-specific] the five named agents.

## 11. Minimal 6-tier tool/substrate registry

Per entry: `id | tier | role | decision_direction
(emit|receive-only|none) | adapter (hermes=real; all others=none) |
status (active|unimplemented)`

| id | tier | role | dir | adapter | status |
|---|---|---|---|---|---|
| DavidOS/Atlas | T1 | control plane | emit | n/a | active |
| Hermes | T2 | execution/orchestration | receive-only | REAL | active |
| Claude Code | T3 | build/dev tool | receive-only | none | unimplemented |
| Codex | T3 | build/dev tool | receive-only | none | unimplemented |
| Ruflo | T4 | multi-agent build orch (NOT governance brain) | receive-only | none | unimplemented |
| NotebookLM | T5 | research/synthesis resource | none | none | unimplemented |
| Obsidian | T5 | human knowledge/thinking resource | none | none | unimplemented |
| Future UI | T6 | operator command center | none | none | unimplemented |

Only Hermes gets an adapter in v1. T3/T4 are invoked THROUGH T2 under a
Decision — registry entries + an invocation-target concept, not their own
adapter seam. Shrinks v1 scope. [reusable] tier model.

## 12. UI-facing structured objects to preserve now (observability spine, C3)

Do not design the UI. Single rule: **no governance object is prose-only.**
Keep structured from day one so Jobs later designs against a stable
schema:
- (a) decision record (envelope + decision + structured citation)
- (b) approval-queue item (ADR-004 Light/Full request AS an object)
- (c) manifest
- (d) agent-registry entry
- (e) **the observability spine** — an append-only, machine-readable
  structured decision/activity log. **C3:** this is not merely a UI feed;
  it is the system's observability spine — the single durable record from
  which drift detection, approval-fatigue analysis, calibration, and any
  future dashboard are derived. v1 commits to the **schema** of this log
  only. Consumers/tooling/dashboards are deferred per anti-goals.md #4.

Repo evidence the instinct is already correct: `approvals-log.md` is
already a structured table (lines 18-19). Generalize that discipline to
all five objects. [reusable]

## 13. How this resolves Fix 9

Fix 9 **Option A** (split Modifier 3 into 3a state-changing / 3b
read-only), marked **PROVISIONAL**. Reject Option B (conditional clause
in modifier grammar). Reason: conditional/contextual rung logic belongs
in the Decision Protocol (§6), not welded into the closed modifier
grammar (SCHEMA.md lines 101-109; Modifier 3 already overflows it by
branching read/write — 2026-05-14 proposal M2). Option B reopens SCHEMA
(an ADR each time, §5) for every future context condition. Option A is
cheap, unblocks the validator + citation contract, and is cleanly
absorbed: at GIP, 3a/3b collapse into the Decision Protocol's
reversibility/blast_radius evaluation. Notes line on 3a/3b: "provisional
— absorbed by Decision Protocol at GIP." Removes the "undecided" blocker
with a stance; commits nothing GIP must unwind. [inferring — 85%; aligns
with 2026-05-14 proposal author's own 70% lean to A, line 395]

## 14. How this changes Fix 13

Fix 13 originally = ADR-005 retroactively ratifying the v0.1 substrate
(2026-05-14 proposal lines 158-164). **Change:** do NOT ratify v0.1.
ADR-005 instead ratifies GIP (this proposal). v0.1 kernel stays
explicitly labeled "draft, intentionally pre-ADR." One ADR, zero churn.
Resolves the deferred-Fix-13 contradiction: defer ALL SCHEMA-editing
fixes (12/14/15, not just 13) until the GIP ADR; the GIP ADR is the first
and only ADR; nothing rough-draft is frozen. [inferring — 90%]

## 15. Approved fixes — before / during / after

- **BEFORE** (safe, principled, GIP won't unwind): Fix 1 (Cat 3↔5
  contradiction), Fix 3 (Cat 16b identity-adjacent — do EARLY,
  protective), Fix 5 (Cat 3b notes), Fix 7 (date), Fix 16 (Cat 3c/14
  credential note).
- **DURING** (fold into GIP design): Fix 2 (Cat 9 split — do the split,
  defer enforcement rework), Fix 9 (Option A provisional, §13).
- **AFTER** (absorbed/reworked by GIP): Fix 6/8/10/11 (cron contract =
  first manifest instance), Fix 12 (citation → structured object), Fix 14
  (subagent reporting → envelope return contract), Fix 15 (principal →
  envelope field 2), Fix 17 (validator → validate post-GIP schema),
  Fix 13 (→ GIP ADR per §14).

## 16. Exact files to create/change — dependency order (later writes)

Not part of write #1. Recorded for the lifecycle:
1. ADR-005 (GIP adoption + invariants §8/§9/C5 + portability clause C1)
2. `docs/governance/anti-goals.md` *(landed in write #1)*
3. `docs/governance/gip-spec.md`
4. `docs/governance/registries/{agent,substrate}.md`
5. one project manifest instance + manifest SCHEMA
6. `docs/decisions/approvals-log.md` append (desync resolution §18)
7. BEFORE-bucket action-map fixes (1,3,5,7,16) — independent
8. Fix 2 + Fix 9A applied (provisional notes)
Decision Protocol skill: after spec is approved, in the Hermes profile.

## 17. What requires David approval

- This proposal's decision statement (§2): L1 Full
- ADR-005: L1 Full (Cat 17)
- Each manifest grant + ceiling set: L1 Full (pre-authorization)
- Agent/substrate registry creation: L1 Light
- Fixes 2 & 9A (rung-touching): L1 Full (SCHEMA §4b)
- BEFORE-bucket fixes 5,7,16: L1 Light; 1,3 (rung-sensitive): L1 Full
- Authority-expansion + non-grantable set + memory elevation: L1 Full

## 18. What to log to resolve the repo/source-of-truth desync

Append to `approvals-log.md` (later write, on approval — not write #1):
- GOV-1: Opus approved for this governance session (2026-05-17), task named
- GOV-2: prior unlogged Opus session (2026-05-14 proposal authored on
  Opus — that doc's header confirms) logged retroactively
- The fix decision set: before/during/after per §15
- Fix 9 = Option A provisional (§13)
- GIP architecture decision + the corrected 6-tier hierarchy
- Fix 13 reframe: ADR-005 ratifies GIP not v0.1 (§14)

Until this lands the repo is not source-of-truth. High-leverage.

## 19. Explicitly deferred

Hustler revenue/offer logic; Jeff CRM/pipeline/proposal machinery; Jobs
UI build; Karrigan coaching/reactive/scheduled skills; per-agent SOUL
layers; customer-facing legal/compliance workflow; Ruflo/Claude
Code/Codex adapter implementations; NotebookLM/Obsidian integrations;
workflow/skill/script manifest population; observability-spine consumer
tooling/dashboards; full council process; Nemanja (untouched). All named
in registries/anti-goals; none built.

## 20. Repo placement

- **Proposal artifact** (this doc): `docs/governance/proposals/` — a new
  tree, deliberately NOT beside the 2026-05-14 audit-prep proposal.
  Foundational architecture is not an audit byproduct. Tradeoff: one new
  directory; benefit: correct lineage signal and co-location with the
  spec/registries/manifests to come.
- **Approved decision record**: ADR-005 → `docs/decisions/` (existing ADR
  home) + one line in `approvals-log.md`. No new location; established
  pattern.
- **Implementation artifacts**: `docs/governance/` (gip-spec, registries,
  manifests); the Decision Protocol skill in the Hermes profile where
  Hermes loads it. Tradeoff: repo-vs-profile split is unavoidable —
  cross-reference both ways.

[reusable] the proposal → decision → implementation lifecycle separation.
[david-specific] the exact paths.

---

## Status of this proposal

Working draft. **Not in force.** Becomes architecture only when ADR-005
is created and `approvals-log.md` carries the §18 entries. Until then it
is captured here to end the chat-only dependency for the architecture
direction — not to authorize implementation.
