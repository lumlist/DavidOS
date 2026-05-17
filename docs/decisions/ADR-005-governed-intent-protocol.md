# ADR-005: governed-intent-protocol

**Date:** 2026-05-17
**Status:** Accepted
**Deciders:** David Izzard

## Context

The v0.1 autonomy substrate (`docs/autonomy/action-map.md`,
`modifiers.md`, `SCHEMA.md` — all present) governs action *category*,
*actor*, *schedule*, and *scope*, but is blind to workflow / skill /
script / project / substrate context and is welded to Hermes via the
per-row "Hermes mechanism" field (`SCHEMA.md` lines 64-71). The
2026-05-14 comprehensive proposal
(`docs/audits/preparation/2026-05-14-atlas-comprehensive-fix-and-governance-proposal.md`,
commit b8c2732, authored on claude-opus-4-7) produced 16 fix proposals
and a Part B governance design. Its Fix 13 proposed an ADR-005 that would
**retroactively ratify the v0.1 substrate**.

A subsequent multi-turn analysis arc (2026-05-17, this session, on
David-approved Opus) plus two external council reviews converged
independently on a different conclusion: the correct core abstraction is
a structured Governed Intent object that wraps — rather than ratifies —
the v0.1 kernel. That arc produced the working-draft proposal at
`docs/governance/proposals/2026-05-17-mv-gip-proposal.md` (committed in
Write #1, commit 69fd8f9, as a **proposal-only capture, explicitly not
approved architecture**). Write #1 deliberately created no decision
record; this ADR is that record.

The strategic frame: DavidOS is a tool-agnostic AIOS control plane, not a
single-purpose Project Build product. Hermes is the current
execution/orchestration substrate; Claude Code/Codex are preferred
build/dev tools; Ruflo is a future bounded multi-agent build-execution
layer (not a governance brain); NotebookLM/Obsidian are
knowledge/research resources; a future UI is the operator command center.
Future agents (Karrigan/Hustler/Jeff/Jobs) are represented as registry
stubs and invariants only. The AI project/business build loop is the sole
v1 acceptance test.

## Decision

Adopt the Governed Intent Protocol (GIP) as a thin wrapper around the
existing v0.1 autonomy kernel — an 11-field intent envelope, a context
model, a decision protocol (skill, not infrastructure), a manifest model
with ceilings and a non-grantable category set (including memory writes
as an elevated-scrutiny non-grantable surface), an authority-expansion
invariant, a tier-aware decision-direction invariant, a
substrate-portability contract, the principle that the repo is the
audit/change substrate not the governance brain, an anti-goals fence, an
8-field agent registry, a 6-tier tool/substrate registry, and a
structured decision log as the observability spine — with the v0.1 kernel
preserved and explicitly labeled draft-pre-ADR, Hermes as the only real
v1 substrate adapter, and the AI project/business build loop as the sole
v1 acceptance test. This ADR ratifies the GIP **direction**; the spec,
registries, manifests, and Decision Protocol skill are later lifecycle
stages, each gated on their own approvals.

## Rationale

- **Alternative A — ratify v0.1 (the original Fix 13).** Rejected: it
  freezes a substrate already known to have 19 audit findings and a
  structural blind spot (context), and welds governance to Hermes. See
  "Superseded framing" below.
- **Alternative B — extend the modifier grammar for context (Fix 9
  Option B).** Rejected: pushes conditional/contextual logic into the
  closed modifier grammar (`SCHEMA.md` lines 101-109), forcing a SCHEMA
  ADR for every future context condition. Context belongs in the Decision
  Protocol, not the grammar.
- **Primary factor.** Two independent analyses (Atlas + external council)
  converged on the structured-intent-object abstraction. The pattern
  reuses one already proven in-repo (the cron "approve-the-actor-once"
  pattern, 2026-05-14 proposal Fix 6/Cat 20) rather than inventing new
  machinery.
- **Cost / risk trade-off.** We accept one new wrapper layer and a small
  ceremony tax; the manifest grant-once-execute-many model offsets it.
  Approval-fatigue *detection* is a deliberate, named deferred gap.
- **Reversibility.** High at this stage. This ADR ratifies a direction
  and a proposal document; no implementation exists yet. Reversal cost is
  editing this ADR and the proposal — no code, no migration.

## Consequences

- **New things that need to exist (later, separately gated):** ADR-005
  (this file); the GIP spec; the agent and substrate registries; the
  manifest schema + one project-manifest instance; the Decision Protocol
  skill (in the Hermes profile). None are created by this ADR.
- **Superseded framing.** The 2026-05-14 proposal's Fix 13 (ADR-005
  ratifies the v0.1 substrate) is **explicitly superseded**. ADR-005
  ratifies GIP, NOT v0.1. The v0.1 kernel remains in force operationally
  but is explicitly labeled "draft, intentionally pre-ADR." This
  superseded position is recorded deliberately (here and in
  `approvals-log.md` R2) so it is not re-litigated (SOUL.md §6, §10).
- **Fix sequencing.** Approved-fix triage adopted: BEFORE = 1,3,5,7,16;
  DURING = 2, 9A; AFTER = 6,8,10,11,12,14,15,17,13. Fix 9 resolved as
  Option A (split Modifier 3 into 3a/3b), provisional, absorbed by the
  Decision Protocol at GIP. Per-fix application is logged when each fix
  is applied — not by this ADR.
- **Write #1 status.** Commit 69fd8f9 (`docs/governance/` tree) was a
  proposal-only capture and **not approved architecture**. This ADR plus
  the `approvals-log.md` R1-R6 entries move the GIP *direction* into
  force; the governance-tree banners are reconciled to point here.
- **Downstream.** Future agents/tools remain registry stubs; no agent or
  adapter is built. The iZZi customer-zero generalization is second-pass.
- **ADR index.** `docs/decisions/README.md` should gain an ADR-005 row;
  that index update is outside this Write's approved scope and is flagged
  as a required follow-up rather than performed silently.

## Re-evaluation triggers

- The GIP wrapper adds ceremony that materially slows the build loop
  without the manifest model offsetting it.
- Approval fatigue sets in before the (deferred) fatigue signal exists
  and bad approvals get logged as good.
- The envelope or a registry needs to exceed its field cap to express a
  real observed need (not a hypothetical one).
- A second iZZi customer onboards and the David-specific assumptions
  prove un-generalizable.

Default review window: **2026-08-17** (90 days) unless triggers fire
first.

## Related

- ADR-004 — workspace-native approval mechanism (the approval surface
  this ADR was approved through)
- `docs/governance/proposals/2026-05-17-mv-gip-proposal.md` — the
  ratified proposal (full §1-§20 detail)
- `docs/governance/anti-goals.md` — the overbuild fence this ADR operates
  within
- `docs/governance/README.md` — governance-tree orientation + lifecycle
- `docs/audits/preparation/2026-05-14-atlas-comprehensive-fix-and-governance-proposal.md`
  — superseded in governance scope (Fix 13 framing)
- `docs/decisions/approvals-log.md` — entries R1-R6 indexing this decision
