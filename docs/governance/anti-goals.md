# DavidOS Anti-Goals — Overbuild Prevention Fence

**Status:** Normative constraint artifact. Created 2026-05-17.
**Approval class:** L1 Light (standing constraint; not pure documentation).

> **GIP DIRECTION RATIFIED — THIS FENCE IS IN FORCE.** The Governed
> Intent Protocol direction is ratified by
> [ADR-005](../decisions/ADR-005-governed-intent-protocol.md) (2026-05-17,
> L1 Full per [ADR-004](../decisions/ADR-004-workspace-native-approval-mechanism.md);
> `approvals-log.md` R1-R6). This anti-goals fence is therefore **active
> and binding** on all governance work. Implementation artifacts (spec,
> registries, manifests, Decision Protocol skill) remain separately
> gated; each must be justified against this fence before it is built.

---

## Why this file exists

Every governance/system effort overbuilds. The failure mode is building
the comprehensive apparatus before the cheapest version has been observed
in use. This file is the explicit fence. Any proposal to build something
on this list must first justify *why the anti-goal no longer applies* —
the burden is on the build, not on the restraint.

This is grounded in SOUL.md §5 (anti-overengineering: "Default to the
smallest viable shape. Add complexity only when justified by observed
friction") and the iZZi customer-zero principle (generalization is a
second-pass concern).

[reusable] Every future iZZi customer will overbuild the same way. An
anti-goals fence generalizes cleanly; the *structure* of this file is a
reusable template. The *specific entries* are partly DavidOS-specific.

## Anti-goals (what DavidOS will NOT build now)

1. **No custom UI / operator command center.** The future UI (Jobs's
   domain) is deferred. Only the structured data objects it will one day
   read are preserved. No inbox, queue, dashboard, or view is built now.

2. **No full council process as a standing mechanism.** Council *output*
   is valid validation input. Institutionalizing a recurring council
   process, council tooling, or a council artifact pipeline is deferred.

3. **No heavy evaluation harness.** No regression-suite automation, no
   eval framework, no scored behavioral battery beyond what SOUL.md §10
   already defines. The cheapest manual check first.

4. **No complex dashboard or observability tooling.** The observability
   spine is a *schema* (a structured decision log). Consumers, dashboards,
   visualizations, and analytics on top of it are deferred until the log
   has accumulated enough to show what is worth surfacing.

5. **No external automation.** No outbound bots, scheduled external
   sends, CI-driven actions, or webhook-triggered agent runs as part of
   governance v1.

6. **No multi-substrate adapter build-out.** Exactly one real adapter
   (Hermes, the current execution/orchestration substrate). Claude Code,
   Codex, Ruflo are registry entries with no implementation. Building
   adapters for substrates not yet in use is the premature-abstraction
   trap.

7. **No registry sprawl.** The agent registry is capped at 8 fields; the
   substrate/tool registry at 6 fields + tier. Neither becomes an agent
   identity/profile system, a credential store, or a relationship/CRM
   layer.

8. **No envelope sprawl.** The Governed Intent Envelope is capped at 11
   fields with safe defaults. Field additions require explicit
   justification against an observed gap, not a hypothetical one.

9. **No premature per-agent build.** Karrigan, Hustler, Jeff, Jobs exist
   only as named-future registry stubs. Their coaching / revenue / BD /
   UI logic is not designed or built in governance v1.

10. **No speculative ADR proliferation.** One ADR (ADR-005) ratifies the
    GIP direction. The v0.1 kernel stays explicitly labeled
    draft-pre-ADR. Rough-draft policy is not frozen into ADRs.

## How an anti-goal is lifted

An anti-goal is removed only when (a) observed operational friction makes
its absence more expensive than the build, AND (b) David approves lifting
it via the normal ADR-004 surface. Lifting an anti-goal is itself a
logged decision, not a silent drift.
