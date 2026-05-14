# DavidOS Autonomy — Orientation

**Status:** Orientation document for the DavidOS autonomy system. Read this first if you are new to the autonomy artifacts.

---

## What lives here

`docs/autonomy/` contains the canonical sources of truth for how autonomy works in DavidOS.

| File | Purpose |
|---|---|
| `SCHEMA.md` | Canonical definition of the autonomy schema (5 rungs, 10 per-row fields, modifier grammar). Changes to this require an ADR. |
| `action-map.md` | The populated action-category-to-rung table. Every action category in DavidOS has a row here. |
| `modifiers.md` | Actor/context modifier rules. Adjust base rungs from `action-map.md` when specific conditions apply. |
| `README.md` | This file. |

---

## The model in one paragraph

DavidOS autonomy maps **actions to autonomy rungs**, not actors to permissions. For each action category, there is a base rung (L0 Forbidden through L4 Schedules and Acts) defined in `action-map.md`. Modifiers in `modifiers.md` adjust the base rung when specific actors (subagents, scheduled jobs) or contexts (cron execution, restricted scope) apply. The `davidos-router` skill computes the final rung per request by looking up the category and applying matching modifiers. This satisfies P6 (consolidated principle: "Autonomy is configured by category and audited, never assumed") and makes autonomy auditable as data rather than as inferred behavior.

---

## How to use the autonomy system

### As David (operator)

- **To understand what Atlas can do without asking:** Read `action-map.md` and filter for rows with base rung L2, L3, or L4 (subject to any modifiers in `modifiers.md` that apply).
- **To add a new action category:** Add a row to `action-map.md` following the schema in `SCHEMA.md`. Set `Date added` to today, `Added by` to your name, and `Last reviewed` to blank.
- **To change an existing category's rung:** Edit the row in place. Add a Notes entry naming the prior rung and the change date. Update `Last reviewed`.
- **To add a modifier:** Add a row to `modifiers.md` following the modifier schema. Document the reasoning explicitly.
- **To audit current autonomy state:** Grep `action-map.md` for L0 entries to see what is forbidden. Grep for L3 and L4 entries to see what Atlas does silently or on schedule. Read `modifiers.md` to see which actor/context conditions deviate from baseline.

### As Atlas (charter-active agent)

- **To determine if you can take an action:** Identify the action category. Look up the base rung in `action-map.md`. Check `modifiers.md` for any modifier whose "Applies to" matches your current actor and context. Apply the modifier's effect to the base rung. Act according to the final rung.
- **To extend the map when a new action category emerges:** Section 6 of SOUL.md governs this. Treat the new action as advisory by default, surface the gap, and propose a new `action-map.md` row as a Full approval item per ADR-004.
- **To propose changes to existing rows:** Same Full approval mechanism. Do not edit `action-map.md` or `modifiers.md` directly without approval; the autonomy map is identity-level.

### As a future agent or skill

If you are an agent or skill operating in DavidOS that is not Atlas, you inherit the canonical `action-map.md` automatically. Your actor type may be referenced by modifiers (e.g., "Subagent Actor" modifier applies to subagents spawned by Atlas; future modifiers may apply to specific skills or scheduled jobs). If your operating profile requires deviation from the canonical map, that deviation should be expressed as a modifier in `modifiers.md`, not as a separate autonomy file.

---

## Why this structure

The full reasoning is in `docs/audits/preparation/2026-05-13-autonomy-map-design-decisions.md`. In summary:

- **Action category is the primary unit** because David's risk tolerance is action-defined, not actor-defined. The general principle: *map approval policies to the dimension that varies the policy, not to the dimension that varies the actor.*
- **One canonical map with modifiers** because per-agent maps fragment the information model (violating P1), prevent the router from computing risk tier across actors (violating P3), and force duplication of the same category across files (violating P4).
- **Modifiers express actor and context variation** because actor and context are real but secondary to action policy. Modifiers compose with the canonical map without replacing it.

---

## Versioning

Schema version is in `SCHEMA.md` header. Action-map and modifiers do not have version numbers; their version is inferred from git history (and from `Date added` / `Last reviewed` fields per row).

Schema changes (adding rungs, changing fields, changing modifier grammar) require an ADR. Entry-level changes (adding categories, adding modifiers) follow the looser process documented above.

---

## Audit hooks

This structure is designed to support automated audit. The `davidos-autonomy-review` skill (Phase 1) and the `davidos-evaluation` skill (Phase 1) operate on these files directly. Specifically:

- `action-map.md` rows where `Last reviewed` is more than N days old surface for re-evaluation.
- Approval override patterns are counted per category over time; categories with high override rates are flagged for rung re-consideration.
- The structural audit's P6 test grep these files and verifies every row cites a real Hermes mechanism (not just "policy" or "discipline").

---

## See also

- `docs/decisions/ADR-004-workspace-native-approval-mechanism.md` — Light/Full approval intensities, canonical approval list. L1 rungs in the action map reference ADR-004 intensities.
- `docs/audits/preparation/2026-05-13-autonomy-map-design-decisions.md` — full reasoning trail for the schema choices.
- `docs/audits/preparation/2026-05-13-phase1-schema-review-task.md` — Atlas's post-activation task to evaluate the schema design.
- `docs/reference/hermes-operating-knowledge-pack.md` — Hermes configuration knobs referenced in the `Hermes mechanism` field of action-map rows.
- SOUL.md Section 6 — Atlas's operating posture, which references the autonomy system.
