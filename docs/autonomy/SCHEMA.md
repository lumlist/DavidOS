# DavidOS Autonomy Schema

**Status:** Canonical schema for all autonomy maps in DavidOS. Authored 2026-05-13 evening. Version 1.0.

**Purpose:** Defines the autonomy rungs, the per-row fields for the action map, and the modifier syntax. Every autonomy artifact in `docs/autonomy/` conforms to this schema. Changes to this schema require an ADR (currently ADR-005 minimum) and the explicit Full approval per ADR-004.

**Companion files:**
- `action-map.md` — the populated action-category-to-rung table conforming to this schema
- `modifiers.md` — the actor/context modifier rules conforming to this schema
- `README.md` — orientation document

**Reasoning trail:** See `docs/audits/preparation/2026-05-13-autonomy-map-design-decisions.md` for the principle-grounded reasoning behind every choice in this schema.

---

## 1. The Five Rungs

Each action category in `action-map.md` has a **base rung** drawn from this five-rung ladder. Rungs are ordered by increasing autonomy.

| Rung | Name | What the actor does | Enforcement mechanism |
|---|---|---|---|
| **L0** | **Forbidden** | Does not do this at all. | Hard block. Hermes refuses the operation, or its pattern matcher denies it, or the request is rejected at the router. |
| **L1** | **Asks First** | Asks David before doing. Awaits explicit approval. | ADR-004 Light or Full approval format; `approvals.mode` runtime prompt. |
| **L2** | **Acts and Reports** | Executes immediately. Names what was done in conversation so David is aware. | No approval prompt. Visible in chat output. |
| **L3** | **Acts Silently** | Executes immediately. Does not surface in conversation unless asked. | No approval prompt. No announcement. Logged but not narrated. |
| **L4** | **Schedules and Acts** | Runs on cadence without per-action prompting. | Scheduled job. David approves the schedule once; individual runs do not gate. |

### Notes on rung selection

- L0 entries must specify *why* the action is forbidden. "Forbidden" is a deliberate constraint, not a default.
- L1 entries must specify the approval intensity (Light or Full per ADR-004).
- L2 vs L3 is the chattiness choice. Default to L2 unless the action is so routine that reporting it adds noise.
- L4 is for cron-style autonomy. The schedule itself is the approval surface, not individual runs.

---

## 2. Per-Row Schema (10 Fields)

Every row in `action-map.md` contains these ten fields, in this order:

```
Category: <short name, 2-6 words, declarative>
Description: <one-line definition; what the action is, concretely>
Base rung: <L0 | L1 | L2 | L3 | L4>
Approval intensity if L1: <Light | Full | N/A>
Hermes mechanism: <specific config knob, skill guard, pattern matcher, scope, or ADR-004 line that enforces this rung>
Notes: <conditions, exceptions, dependencies; or "—" if none>
Date added: <YYYY-MM-DD>
Added by: <David | Atlas (with David's approval on YYYY-MM-DD)>
Review trigger: <default "on observed drift"; override per category as needed>
Last reviewed: <YYYY-MM-DD; blank for v0.1 initial entries>
```

### Field definitions

**Category** — Short declarative name. Examples: "Read repo files," "Spawn subagent for research," "Push to git remote." Avoid jargon; the category should be intelligible to David without a glossary.

**Description** — One sentence defining the action concretely. The test: another agent reading this description should be able to recognize a specific request as an instance of this category. Examples: "Reading any file in DavidOS, FamilyAI, or DavidAIStory repos" or "Executing `git push` to a remote branch (any branch, any remote)."

**Base rung** — One of L0, L1, L2, L3, L4. The default autonomy for this category absent modifier conditions.

**Approval intensity if L1** — Light or Full per ADR-004. N/A if base rung is not L1. If a modifier downgrades a non-L1 action to L1, the modifier specifies the intensity.

**Hermes mechanism** — The specific enforcement. Acceptable forms:
- `approvals.mode: smart + ADR-004 canonical list L66-L75`
- `skills.guard_agent_created: true`
- `terminal.cwd scope + repo-scope principle (SOUL.md §5)`
- `Hermes dangerous-command pattern matcher`
- Combination of the above

Unacceptable: "policy" or "discipline" without naming a real mechanism. If the rung depends on chat-time discipline rather than a config or pattern, the row is not yet operational and should be flagged in Notes.

**Notes** — Conditions, exceptions, dependencies. Examples: "Outside-repo reads require L1 Light per repo-scope principle" or "Subagent-spawned variants forced to L0 by the Subagent Actor modifier." Use "—" if no notes apply.

**Date added** — When the row was added to the map. Initial v0.1 entries use 2026-05-13.

**Added by** — Authorship trace. Either `David` (for v0.1 entries David authored) or `Atlas (with David's approval on YYYY-MM-DD)` (for entries Atlas proposed post-activation that David approved). Distinguishes operator-authored entries from Atlas-extended entries.

**Review trigger** — Condition that should trigger a re-evaluation of this row's rung. Default for v0.1: `on observed drift` (meaning: when behavior diverges from the configured rung, re-evaluate). Per-category overrides as observation accumulates. Examples of override values: `quarterly`, `on cost spike`, `never (rung is fixed by policy)`, `on overflow of approval queue`.

**Last reviewed** — Date the row was most recently evaluated and confirmed. Blank for v0.1 initial entries. Populated by the `davidos-autonomy-review` skill (to be built in Phase 1) or by explicit David action.

---

## 3. Modifier Schema

`modifiers.md` defines rules that adjust base rungs when specific actor or context conditions apply. Modifiers do not override the schema; they compose with it.

### Per-modifier schema (7 fields)

```
Modifier: <short name>
Applies to: <actor or context condition that triggers this modifier>
Categories affected: <"any" or comma-separated list of category names; or rule like "any category in [list]">
Effect: <how the base rung is adjusted; or what the override rung is>
Reasoning: <why this modifier exists; ground in principles or ADRs>
Date added: <YYYY-MM-DD>
Added by: <David | Atlas (with David's approval on YYYY-MM-DD)>
```

### Effect grammar

Modifier effects use a small grammar:

- `Drop rung by N` — Lower the base rung by N levels (e.g., L2 becomes L3; L1 becomes L0).
- `Raise rung by N` — Raise the base rung by N levels (e.g., L3 becomes L2; L2 becomes L1).
- `Force to <rung>` — Override the base rung entirely (e.g., `Force to L0` regardless of base).
- `Force approval intensity <Light|Full>` — Used when modifier changes a base L1's intensity without changing the rung.
- Combinations using "and": `Drop rung by 1 and Force approval intensity Full`.

### Modifier conflict resolution

When two modifiers apply to the same request:

1. **Most restrictive wins.** If one modifier raises a rung and another lowers it, the higher (more restrictive) result holds.
2. **L0 always wins.** Any modifier that forces L0 overrides any other modifier.
3. **Document conflicts.** If two modifiers conflict in ways the above rules don't cleanly resolve, the affected row in `action-map.md` should add a Notes entry naming the conflict and the resolution rule applied.

---

## 4. How the Router Uses This Schema

The `davidos-router` skill (to be built in Phase 1 per P3) computes the final rung for each incoming request:

1. Identify the action category by matching the request against `action-map.md` Description fields.
2. Look up the base rung in the matched row.
3. Iterate `modifiers.md` for any modifier whose "Applies to" condition is satisfied by the current actor and context.
4. Apply each matching modifier's Effect to the base rung, using the conflict resolution rules above.
5. Emit the final rung along with citation: "Category X (action-map.md L42), modifiers Y and Z applied (modifiers.md L18, L31), final rung Lk with approval intensity I."

The citation is part of the router's contract — every routing decision is auditable.

---

## 5. Schema Evolution

Changes to this schema (rungs, fields, modifier grammar) are identity-level. They require:

1. An ADR proposing the change with reasoning
2. Full approval per ADR-004
3. A migration plan for existing rows in `action-map.md` and `modifiers.md`

Changes to entries *within* the schema (adding categories, adding modifiers) follow the looser process documented in `README.md`.

---

## 6. Audit Hooks

This schema is designed to support automated audit. Specifically:

- The `davidos-autonomy-review` skill (Phase 1) can grep `action-map.md` for rows where `Last reviewed` exceeds a threshold, surfacing them for re-evaluation.
- The `davidos-evaluation` skill (Phase 1) can count approval overrides per category over time and propose rung changes when patterns emerge.
- The structural audit's P6 test can grep `action-map.md` and verify every row's `Hermes mechanism` field cites a real enforcement mechanism (not just "policy").

The schema makes these audits possible without any additional infrastructure. The fields are the hooks.

---

## 7. Out of scope for v1.0 (deferred to v2.0)

Three things this schema deliberately does not capture. Documented here so future revisions are scoped:

1. **Time-of-day or session-state conditions.** "Atlas can spawn subagents during planning sessions but not during build sessions." The modifier grammar does not currently express time or session conditions.

2. **Cross-category dependencies.** "Atlas can do X only after Y is done." The schema currently treats each category as independent.

3. **Confidence-threshold conditional rungs.** "Action is L2 if confidence ≥ 90%, else L1." The schema currently uses fixed base rungs; confidence-conditional rungs would require either modifier-level expression or schema extension.

If a real operational need emerges for any of these, propose a v2.0 schema revision via ADR.
