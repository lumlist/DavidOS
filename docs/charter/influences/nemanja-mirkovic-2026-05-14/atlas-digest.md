# Atlas Digest — Nemanja Mirkovic source (2026-05-14)

Provenance: bounded Atlas digest of "15 Hermes Agent use cases I wish I tried sooner" (Nemanja Mirkovic, 2026-05-14). Raw materials and full inventory: see `INDEX.md` in this directory.

## Status

Nemanja is implementation-quality and operating-model reference input — not ratified architecture. ADR-005 remains the approved architecture direction. The GIP proposal remains the ratified design reference. This digest does not reopen or modify either.

## Implementation-improvement list (prioritized, sequenced)

GIP-implementation refinements only — not design changes. Recommended order: 1 → 2 → 3 → 4 → 5 → 6. Effort S/M/L · Leverage H/M/L.

1. Adopt the build/operate handoff convention in GIP implementation: Codex/Claude Code build durable tooling; Hermes/Atlas operates it. Effort S · Leverage H. Strongest, best-evidenced takeaway; directly actionable.
2. Sequence GIP implementation to ship a recurring push-digest/triage agent first (lowest integration, highest retention). Effort S · Leverage H.
3. Add a standing data-scoping pre-flight to operating discipline (sibling to fetch-before-work). Effort S · Leverage M.
4. Specify a self-improving rating loop as a standard pattern for recurring-output agents. Effort M · Leverage M.
5. Define the command-center surface as push-digest + low-friction ingest, not query-only. Effort M · Leverage M. Confidence-limited; may warrant the two named screenshots before acting.
6. Note council-as-context convergence with the existing multi-model-council source — cross-reference, don't duplicate. Effort S · Leverage L.

## Q7 finding — contradiction / blind-spot gate

No concrete contradiction with ADR-005 or GIP. The operator/builder thesis is complementary to the ratified direction. ADR-005 stands; GIP was not reopened. One low-severity, framing-mitigated blind spot: single-practitioner anecdotal source with several self-described untested use cases — do not elevate to validated pattern.

## Reusable iZZi shortlist — second-pass / not-now

No action this session (SOUL.md §5: generalization is second-pass).

- Uniform agent-employee spec schema (INPUTS/PROCESSING/OUTPUTS/outcome + category tag).
- Build-vs-operate handoff as a customer-onboarding heuristic.
- Self-improving rating loop as a productizable agent feature.

---

Digest only — not an ADR, governance file, approvals-log entry, or implementation plan.
