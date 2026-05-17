# GIP Spec — Governed Intent Protocol Implementation Reference

> **GIP DIRECTION RATIFIED — THIS SPEC IMPLEMENTS IT, ADDS NO DECISION.**
> The Governed Intent Protocol direction is ratified by
> [ADR-005](../decisions/ADR-005-governed-intent-protocol.md) (2026-05-17,
> L1 Full per [ADR-004](../decisions/ADR-004-workspace-native-approval-mechanism.md);
> `../decisions/approvals-log.md` R1-R6). This document is the operator-usable
> implementation reference. It is an L2 repo-write artifact, not an
> architecture decision.

---

## 1. Purpose & subordination

This is the operator-usable implementation reference for the Governed Intent
Protocol: it consolidates the ADR-005-ratified direction into one executable
normative document, by pointer, introducing no design changes.

**This spec is not the Decision Protocol skill. It defines the contract the
future skill must implement.**

Subordination ranking (highest authority first):

1. [ADR-005](../decisions/ADR-005-governed-intent-protocol.md) — the ratified
   decision (Decision/Consequences, L40-106).
2. [MV-GIP proposal](./proposals/2026-05-17-mv-gip-proposal.md) — the ratified
   design reference (§1-§20).
3. This spec — implements (1) and (2); decides nothing.

Where this spec and a higher authority disagree, the higher authority wins.

## 2. Consolidation principle + contradiction gate

**Consolidation principle.** This spec restructures the ratified GIP
direction into implementation form. It introduces no design changes. Where
it appears to, that is an error to be corrected toward ADR-005 and the MV-GIP
proposal, not a new decision.

**Contradiction gate — default: NOT TRIPPED.** The only channel by which
this spec may diverge from the ratified direction is a concrete internal
contradiction or a high-risk blind spot surfaced during consolidation. The
response is: flag it, scoped, with severity, surface to David — never silent
redesign. Absent that, the proposal and ADR-005 stand verbatim (SOUL.md
§6/§10; ADR-005 "superseded framing"). This spec is not a relitigation
surface.

## 3. Five-layer model

Canonical: MV-GIP proposal [§3](./proposals/2026-05-17-mv-gip-proposal.md).

- **L1 Intent surface** — operator/agent emits a Governed Intent Envelope.
- **L2 Decision Protocol (NEW)** — envelope + manifests + kernel → Decision.
  A skill, not infrastructure (see §7).
- **L3 Policy kernel (EXISTS, preserved)** — action-map / modifiers / SCHEMA;
  the "Hermes mechanism" field reread as abstract "enforcement binding."
- **L4 Substrate adapter seam (NEW, minimal)** — one real adapter: Hermes.
- **L5 Execution + audit (mostly EXISTS)** — Hermes executes; a structured
  decision record is appended (observability spine, §12).

## 4. Governed Intent Envelope

Canonical + rationale: MV-GIP proposal [§4](./proposals/2026-05-17-mv-gip-proposal.md).
Hard cap: 11 fields, safe defaults — a routine action emits a near-empty
envelope. Field-sprawl is the documented failure mode; the cap is the design.

1. `intent` — free text: what is wanted.
2. `principal` — Atlas|David|Karrigan|Hustler|Jeff|Jobs|subagent:<id>|cron:<id> (default Atlas).
3. `action_category` — matched action-map category or "uncategorized".
4. `context_ref` — manifest id(s) or "ad-hoc".
5. `substrate` — hermes (default) | claude-code | codex | ruflo.
6. `resource_class` — repo|filesystem|network|credential|external-recipient|external-representation|identity.
7. `reversibility` — reversible|checkpointed|irreversible.
8. `blast_radius` — self|repo|account|external|external-representation|identity.
9. `side_effects` — none|local-state|external-send|spend|auth-write.
10. `capability_grant` — manifest scope token or "none (ask)".
11. `posture` — conversational|advisory|approval-disciplined (style/cadence
    ONLY; never the rung).

## 5. Context model

Canonical: MV-GIP proposal [§5](./proposals/2026-05-17-mv-gip-proposal.md).
Context is structured INPUT to the Decision Protocol, NOT a modifier.
Dimensions: workflow / skill / script / project / substrate (each may carry
a manifest); `resource_class` (relabels action-map's five domains, not a new
taxonomy); `reversibility` (ADR-004 heuristic, made explicit); `blast_radius`
(Cat 16b made first-class); plus `external_side_effects` and `secrets` flags.
~7 of these already exist implicitly; the model names what the system already
reasons about ad hoc so the decision is consistent and auditable.

## 6. Decision protocol — contract only

Canonical: MV-GIP proposal [§6](./proposals/2026-05-17-mv-gip-proposal.md).

- **Consumes:** envelope + manifests + L3 kernel.
- **Emits:** Decision `{final_rung, intensity, granted_scope,
  structured_citation}`. Citation is an object (category + modifiers +
  manifest id + invariants fired), not line numbers.
- **Procedure (outline):** parse envelope → match category → look up base
  rung → apply modifiers per SCHEMA §3 → evaluate context + manifest grant +
  ceilings → apply invariants (§9) → emit Decision → append decision record
  (§12).

The Decision Protocol is a **skill, authored in the Hermes profile, NOT in
this spec** (see §14). This section specifies its contract only.

## 7. Manifest model

Canonical: MV-GIP proposal [§7](./proposals/2026-05-17-mv-gip-proposal.md).

A manifest = a small declared-context file carrying a scoped capability
grant; the grant IS the pre-authorization (cron pattern, generalized).
Fields: `id | type | principals_allowed | substrates_allowed |
paths_in_scope | capability_grant | ceilings | expiry (ADR-004 90-day
default) | decision_log_target`.

- **Ceilings (mandatory on every grant):** spend cap, recipient allowlist,
  irreversibility=never-without-ask. Any breach auto-downgrades to L1.
- **Non-grantable set** (no manifest may pre-authorize; always re-gates):
  external sends with legal/financial/representational content; spend /
  account creation; legal/privacy conclusions; identity/structural edits;
  **memory writes (Cat 8) — elevated-scrutiny, non-grantable (C4)**.
- v1 populates exactly ONE manifest: the project manifest for the build
  loop. Other manifest types are schema-defined, unpopulated.

## 8. Invariants

Canonical: MV-GIP proposal [§8, §9](./proposals/2026-05-17-mv-gip-proposal.md);
ADR-005 [L42-54](../decisions/ADR-005-governed-intent-protocol.md).

- **Authority-expansion invariant.** No agent — Atlas included — may author
  or widen any agent's capability grant. Creating/widening a grant is
  non-grantable, identity-level, David-only. Atlas may PROPOSE; only David's
  logged L1 Full enacts.
- **Tier-aware decision-direction invariant.** Decisions flow down the tier
  hierarchy only; results/audit flow up. No substrate produces a Decision.
- **C5 — repo is the audit/change substrate, not the governance brain.** No
  repo automation (CI, hooks, bots) may act as a decision-maker.
- **C1 — substrate-portability contract.** Envelope and Decision schema are
  substrate-neutral; substrate-specific enforcement lives only in the L4
  adapter.

## 9. Governed flow

intent → **envelope** (11 fields, §4) → **context** resolution (manifests,
ceilings, §5/§7) → **Decision Protocol** evaluates envelope + context +
kernel + invariants (§6/§8) → emits **Decision** {final_rung, intensity,
granted_scope, structured_citation} → on approval, **substrate/build
handoff**: T1 emits; T2 (Hermes) receives and executes; T3/T4 are invoked
*through* T2 under the Decision, never directly → a structured **decision
record** is appended to the observability spine (append-only, §12).
Decisions flow down the tier hierarchy only; results and audit flow up; no
substrate produces a Decision. (MV-GIP proposal §3, §6, §9, §12.)

## 10. Tool/substrate tier hierarchy

Canonical: MV-GIP proposal [§11](./proposals/2026-05-17-mv-gip-proposal.md);
ADR-005 strategic frame [L30-38](../decisions/ADR-005-governed-intent-protocol.md).

- **T1 DavidOS/Atlas** — control plane — *emit*.
- **T2 Hermes** — execution/orchestration — *receive-only*; the only real v1
  adapter.
- **T3 Claude Code / Codex** — build/dev tools — *receive-only*, invoked
  through T2, no own adapter.
- **T4 Ruflo** — later bounded multi-agent build-execution layer, **NOT the
  governance brain** — *receive-only*.
- **T5 NotebookLM / Obsidian** — knowledge/research resources — *none*.
- **T6 future UI** — reader only — *none*.

Hard rule: T4 can never short-circuit to T1; no substrate produces a
Decision.

## 11. Observability spine

Canonical: MV-GIP proposal [§12](./proposals/2026-05-17-mv-gip-proposal.md);
anti-goals [#4](./anti-goals.md). No governance object is prose-only. Keep
structured: (a) decision record; (b) approval-queue item; (c) manifest;
(d) agent-registry entry; (e) the append-only structured decision/activity
log. v1 commits to the **schema** of this log only. Consumers, dashboards,
and analytics are deferred (anti-goals #4).

## 12. Anti-goals constraints in force

**Constraints in force.** This spec operates inside the fence at
[anti-goals.md](./anti-goals.md) (binding per ADR-005). Specifically:
envelope ≤ 11 fields, safe defaults, additions require an *observed* gap
(#8); agent registry ≤ 8 fields, substrate registry ≤ 6 fields + tier,
neither an identity/credential/CRM layer (#7); the observability spine is a
**schema only** — no consumers, dashboards, or analytics (#4); no
UI/command center (#1); no standing council process (#2); no eval harness
(#3); exactly one real adapter, Hermes — no Claude Code/Codex/Ruflo adapter
build (#6); no per-agent build for Karrigan/Hustler/Jeff/Jobs (#9); no
speculative ADR proliferation (#10). Lifting any constraint is a separate
logged ADR-004 decision (anti-goals.md §"How an anti-goal is lifted").

## 13. Repo / Hermes-profile boundary

**Repo / profile boundary.** This spec lives in the repo
(`docs/governance/gip-spec.md`) and is the durable, diffable reference. The
Decision Protocol is a **skill, not infrastructure**, authored in the Hermes
profile where Hermes loads it — it is **not authored by this spec or this
workstream**. This document specifies the Decision Protocol's contract and
I/O so the future skill is built against a stable target; it stops at that
contract boundary. Cross-reference both directions; author neither side of
the skill here. (MV-GIP proposal §6, §16, §20.)

## 14. Deferred scope

**Deferred (not in this spec, each separately gated).** Agent & substrate
registries; manifests & manifest schema (v1 = one project manifest, later);
the Decision Protocol skill (Hermes profile, after this spec is approved);
BEFORE-bucket action-map fixes 1,3,5,7,16 (independent, own gates); DURING
fixes 2 & 9A; UI, council process, eval harness, dashboards, external
automation, extra adapters, per-agent builds; iZZi generalization
(second-pass, SOUL.md §5). Absence here is deliberate, per the lifecycle
([governance/README.md](./README.md) L41) and anti-goals.md — not omission.
(MV-GIP proposal §16, §19.)

## 15. Implementation-convention notes (subordinate)

The bounded Nemanja digest
([atlas-digest.md](../charter/influences/nemanja-mirkovic-2026-05-14/atlas-digest.md))
is **implementation-quality / operating-model reference input only — not
architecture authority**. Its contradiction gate already returned "no
concrete contradiction; ADR-005 stands" (digest Q7). It MAY inform
implementation convention — e.g. the build/operate handoff (Codex/Claude
Code build durable tooling; Hermes/Atlas operates it), which concretizes the
T1-T4 hierarchy without changing it. It has no authority over ADR-005 or the
proposal. iZZi-generalization items remain second-pass (SOUL.md §5). No
Nemanja reanalysis.

## 16. Pointers index

- [ADR-005 — Governed Intent Protocol](../decisions/ADR-005-governed-intent-protocol.md)
- [MV-GIP proposal (§1-§20)](./proposals/2026-05-17-mv-gip-proposal.md)
- [governance/README.md — lifecycle + tree](./README.md)
- [anti-goals.md — overbuild fence](./anti-goals.md)
- [context-refresh-protocol.md — fetch-before-work](../atlas/context-refresh-protocol.md)

---

*Status: implementation reference. Not in force as a decision — ADR-005 is
the decision. This spec consolidates; it does not decide.*
