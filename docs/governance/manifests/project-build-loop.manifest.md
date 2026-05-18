# Manifest: project-build-loop

**Status:** Implementation artifact (the v1 project manifest). Created 2026-05-18.
**Approval class:** L1 Full — a standing capability grant / pre-authorization
surface (gip-spec §7; MV-GIP proposal §17; `../../decisions/approvals-log.md`).

> **THIS FILE GRANTS STANDING AUTHORITY — READ gip-spec §7/§8 FIRST.** The
> Governed Intent Protocol is ratified by
> [ADR-005](../../decisions/ADR-005-governed-intent-protocol.md). A manifest
> is the permission layer: the grant below IS a pre-authorization. It is
> bounded by ceilings and a non-grantable set that always re-gates. No
> agent — Atlas included — may author or widen this grant; only David's
> logged L1 Full enacts or changes it (gip-spec §8 authority-expansion
> invariant). The Decision Protocol skill that consumes this manifest is a
> later, separately-gated stage and does not exist yet.

---

## Schema (exactly the 9 gip-spec §7 fields)

| # | Field | Value |
|---|---|---|
| 1 | `id` | `project-build-loop` |
| 2 | `type` | `project` |
| 3 | `principals_allowed` | `Atlas` (only) |
| 4 | `substrates_allowed` | `hermes` (only real v1 adapter; T3/T4 invoked through Hermes, never directly) |
| 5 | `paths_in_scope` | `docs/**`, repo working tree of DavidOS/FamilyAI/DavidAIStory **excluding** identity/structural paths (`SOUL.md`, `docs/decisions/ADR-*`, `docs/autonomy/**`, `docs/governance/registries/**`, `docs/governance/manifests/**`, `~/.hermes/**`) |
| 6 | `capability_grant` | Reversible, repo-scoped build-loop work at or below L2: action-map Cat 1 (read repo files, L3), Cat 2 (write/modify non-identity repo files, L2), Cat 5 (non-destructive shell, L3), Cat 6 (state-modifying shell within workdir incl. local `git add`/`git commit`, L2), Cat 12a (git push to feature branch, additive, L2). Nothing else is pre-authorized. |
| 7 | `ceilings` | spend_cap = 0 (no spend of any kind); recipient_allowlist = none (no external recipient); irreversibility = never without ask; external_sends = none; credentials_secrets = none; account_access = none. Any breach auto-downgrades the action to L1 (gip-spec §7). |
| 8 | `expiry` | 2026-08-17 (90-day default per ADR-004; repo house convention); review on expiry or on observed drift, whichever first |
| 9 | `decision_log_target` | `docs/governance/decision-log.md` — **DEFERRED / NOT CREATED.** Named here only as the intended append-only structured decision/observability-spine target per gip-spec §11. The log artifact itself is a separate later-gated stage and is **not created by this manifest**; this field records intent, not an existing file. |

## Non-grantable set (NOT a 10th field — binding reference; always re-gates)

Per gip-spec §7 + §8 and ADR-004's canonical approval list, the following
can NEVER be pre-authorized by this or any manifest. They are excluded from
`capability_grant` by construction and always re-gate at the stated rung.
Bound to real `action-map.md` categories / `modifiers.md` rules:

| Non-grantable action | action-map / modifier binding | Re-gates to |
|---|---|---|
| External outreach / messaging / sends | Cat 15 (Send messages/content to external recipients) | L1 Full |
| Spend / money movement / account creation | No action-map category exists (tracked residual R4); ADR-004 canonical list ("spending money", "creating accounts"). Closest adjacent: Cat 14 (authenticated APIs, writes) | L1 Full |
| Legal / privacy conclusions | No action-map category exists (tracked residual R4); ADR-004 canonical list ("legal/privacy conclusions") | L1 Full |
| Edit SOUL.md | Cat 16 | L1 Full |
| Create / revise ADRs | Cat 17 | L1 Full |
| Edit autonomy files (action-map / modifiers / SCHEMA) | Cat 18 | L1 Light (new category) / L1 Full (rung or modifier change or SCHEMA) |
| Edit registries or manifests (incl. this file) | Cat 2 carve-out + gip-spec §8 authority-expansion (identity/structural) | L1 Full |
| Modify Hermes configuration | Cat 19 | L1 Full |
| Memory writes (MEMORY.md) | Cat 8 (base L2) — **elevated to non-grantable by gip-spec §7 C4**; Decision Protocol applies the more restrictive | L1 |
| Personal / health / financial-sensitive data actions | Cat 3c (authenticated reads of David's accounts) / Cat 14 (authenticated writes) | L1 Light (read) / L1 Full (write) |
| Agent activation | gip-spec §8 + anti-goals #9 (named-future stubs only) | L1 Full |
| Workflow creation | ADR-004 canonical list (structural change to DavidOS) | L1 Full |
| /goal runs or adoption | See "Bound future surfaces" below | L1 Full (and not adopted) |
| Manifest grant creation / widening | gip-spec §8 authority-expansion invariant — identity-level, David-only | L1 Full |
| Delete files / destructive shell | Cat 4 / Cat 7 | L1 Full |
| Push to main or any force-push | Cat 12b | L1 Full |
| Any action on an out-of-scope repo | Modifier 3 (Out-of-Scope Repository) | L1 Full (state) / L1 Light (read) |
| Any identity-shaping action by a subagent | Modifier 1 (Subagent Actor) — Cat 16/17/18/19 | L0 (Forbidden) |

Conflict resolution is SCHEMA.md §3: most-restrictive-wins; L0 always wins.
This manifest never lowers a rung below the action-map base; it only
pre-authorizes the §6 `capability_grant` subset and otherwise defers.

## Tracked residual (NOT actioned by this manifest)

- **R4** — `action-map.md` has no explicit spend/money or legal/privacy
  category. This manifest does **not** fix that and does **not** modify
  the autonomy files. Spend/money and legal/privacy-sensitive actions are
  blocked here through the non-grantable set above and the ADR-004
  canonical approval list. R4 is recorded as a tracked residual for a
  possible future, separately-gated action-map proposal — it is named
  here, not resolved here.

## Bound future surfaces (named, NOT enabled)

- **/goal** — a Hermes future command surface (R3). When/if it exists, /goal
  use will be governed as an input bound by this manifest. **/goal is NOT
  enabled, NOT adopted, and CANNOT run under this manifest.** Any future
  /goal use is a separate L1 Full approval and must be explicitly
  manifest-bound at that time. This line records the binding intent only;
  it grants nothing.

## Model-class autonomy invariance (ADR-006)

Model class is autonomy-invariant. Operating on Opus vs Sonnet never
widens rung, approval intensity, granted scope, write authority, or
external-action authority under this manifest (ADR-006 Decision).

## What this manifest does NOT do

It creates no agent, no workflow, no skill, no /goal capability, and no
decision-log file. It does not empower Karrigan, Hustler, Jeff, or Steve —
they remain named-future registry stubs with `execution_authority=none`.
It is consumed by the future Decision Protocol skill (not yet built);
absent that skill, this manifest is a declared, durable grant with no
automated consumer.

## Pointers

- [gip-spec.md](../gip-spec.md) — §7 manifest model, §8 invariants, §11 spine
- [ADR-005](../../decisions/ADR-005-governed-intent-protocol.md) — GIP ratification
- [ADR-006](../../decisions/ADR-006-opus-default-control-plane.md) — model-class invariance
- [action-map.md](../../autonomy/action-map.md) / [modifiers.md](../../autonomy/modifiers.md) — the L3 policy kernel this binds to
- [registries/](../registries/) — inventory layer (who/what exists; grants nothing)
