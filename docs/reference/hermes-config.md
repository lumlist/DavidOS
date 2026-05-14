# Hermes Configuration — DavidOS Runtime

**Status:** Canonical. Referenced by SOUL.md §6 ("Autonomy by category").
**Source of these values:** [Opus Task 4 — Knowledge Pack Integration](../audits/preparation/2026-05-13-task4-knowledge-pack-integration.md).
**Edit policy:** Changes to these values are L1 Full per ADR-004 (they modify Atlas's runtime behavior across all sessions).

---

## Configuration values (active)

These are the Hermes config keys that enforce the autonomy policies described in SOUL.md §6 and the action-map.md rungs.

| Key | Value | Effect |
|---|---|---|
| `approvals.mode` | `smart` | Hermes applies category-aware approval gating based on the action map, not a blanket allow/deny. |
| `skills.guard_agent_created` | `false` | Atlas can create new skills without per-skill approval. **This deliberately overrides Knowledge Pack §H5's recommendation** (which suggested `true`) — David wants skill velocity high during the foundation phase. Revisit if skills proliferate noisily. |
| `checkpoints.enabled` | `true` (`max_snapshots: 20`) | Hermes maintains workspace snapshots so reversible-action recovery is real, not aspirational. Required for the §6 four-condition test to be honest about "reversible OR checkpoint OR redoable." |
| `agent.max_turns` | `150` | Per-session Atlas turn budget. Higher than Hermes default because DavidOS work is research-and-synthesis heavy. |
| `terminal.backend` | `local` | Atlas can run shell commands locally in the workspace. Sensitive paths (e.g., system directories, credential files) are still gated by Hermes's dangerous-command pattern matcher independent of this setting. |
| `display.show_cost` | `true` | Atlas surfaces cost data to David in-session. Supports cost-aware decision-making per SOUL.md §5. |

---

## Deliberate deviation from Knowledge Pack §H5

The Hermes Operating Knowledge Pack (`docs/reference/hermes-operating-knowledge-pack.md` §H5) recommends `skills.guard_agent_created: true` to prevent skill sprawl. **DavidOS overrides this to `false`** as a deliberate decision documented here.

**Reasoning:**
- Foundation phase requires fast iteration on skill design.
- Skill sprawl is a real risk but a slow one — easier to clean up than to undo "I needed to create a skill but had to wait for approval."
- The §7.3 leverage-flag pattern provides a softer drift-detection mechanism (Atlas flags when skill count gets noisy).
- The `davidos-soul-md-audit` skill's Test E (coverage) will surface unused skills over time.

**Re-evaluation trigger:** If skill count exceeds ~15 OR if Atlas creates skills that are duplicative of existing ones, flip this to `true` and review.

---

## Cron context modifier

Per `docs/autonomy/modifiers.md`, scheduled actions running in cron context drop one rung (L2 → L3). This is enforced by the action map; Hermes does not have a separate config key for it.

---

## Related canonical files

- `docs/autonomy/action-map.md` — what action categories exist and their rungs
- `docs/autonomy/modifiers.md` — actor and context modifiers
- `docs/autonomy/SCHEMA.md` — rung definitions and field schema
- `docs/decisions/ADR-004-workspace-native-approval-mechanism.md` — approval intensity scheme
- `docs/reference/hermes-operating-knowledge-pack.md` — full Hermes operating reference (§H5 specifically)
