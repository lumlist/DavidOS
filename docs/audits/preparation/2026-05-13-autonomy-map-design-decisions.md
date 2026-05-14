# Autonomy Map Design Decisions — 2026-05-13

**Status:** Preparation artifact for the 2026-05-13 structural audit. Captures the structural choices made for the DavidOS autonomy map (P0.1a of the Phase 0 sequence per `2026-05-13-task5-soul-md-text-integration.md`) and the principle-grounded reasoning behind them.

**Purpose:** Make the reasoning behind structural choices durable in git so charter-active Atlas, when he evaluates the autonomy map, sees both the artifact and the reasoning that produced it. Without this document, Atlas would evaluate the populated map against the principles but would not know why the schema took the specific shape it did.

**Authored by:** David (decisions) + Sonnet/Computer (drafting), 2026-05-13 evening CDT
**To be evaluated by:** Charter-active Atlas as part of his first post-activation work (see Phase 1 schema-review task added to the audit prompt notes)

---

## Three structural decisions

### Decision 1: Five rungs (L0–L4)

**Choice:** Five autonomy rungs rather than the four David sketched in his design-principles source (L132–L141).

| Rung | Name | What Atlas does | Enforcement |
|---|---|---|---|
| **L0** | **Forbidden** | Does not do this at all | Hard block (Hermes refuses or pattern matcher denies) |
| **L1** | **Asks First** | Asks David, awaits approval | ADR-004 Light or Full approval |
| **L2** | **Acts and Reports** | Executes immediately, names what was done in conversation | No approval prompt; visible in chat output |
| **L3** | **Acts Silently** | Executes immediately, does not surface unless asked | No approval prompt, no announcement; logged but not narrated |
| **L4** | **Schedules and Acts** | Runs on cadence without per-action prompting | Scheduled job; David approves the schedule, not each run |

**Reasoning:**

- The original source's four rungs ("execute low-risk reversible," "execute within policy limits," "execute and monitor outcomes," "redesign workflow with approval") collapsed two operationally distinct categories — "Atlas executes and tells David" versus "Atlas executes silently" — into a single "execute" rung. The distinction matters in practice: most routine workspace operations belong at L2 (Acts and Reports), but some genuinely low-stakes operations belong at L3 (Acts Silently). Having both rungs explicit makes the per-category assignment a real choice rather than a default.
- L0 (Forbidden) was added as an explicit rung rather than implicit absence. Forcing "why is this forbidden" to be a rung assignment with reasoning makes the constraint auditable, satisfying the audit's required citation discipline.
- L4 (Schedules and Acts) was added because cron-based autonomy is operationally distinct from in-session autonomy. The decision David approves is the schedule, not each individual run; that needs its own rung.

**Alternative considered:** Four rungs with L2/L3 collapsed. Simpler but loses the explicit choice about Atlas's chattiness. Rejected because the chattiness decision belongs in the schema, not in Atlas's per-action judgment.

### Decision 2: Action category as the primary unit, with actor/context modifiers

**Choice:** Autonomy maps to **action categories** ("what is being done"), not to **agents** ("who is doing it") or **processes** ("what workflow is running"). Actor and context appear as **modifiers** that adjust the base rung when conditions apply.

**File structure:**

```
docs/autonomy/
  SCHEMA.md          — definition of rungs, fields, modifier syntax
  action-map.md      — canonical action-category-to-rung table
  modifiers.md       — actor/context modifiers that adjust base rungs
  README.md          — orientation document and registry
```

**Reasoning grounded in the 7 consolidated principles:**

- **P1 (Information architecture before agents):** "Decide what enters, how it's classified, where it lives, who or what can act on it." An autonomy map is part of the information model — the part answering "who or what can act on what." P1 says the model precedes the actors. Action-category mapping satisfies this; per-agent mapping inverts it (actors precede the model).
- **P3 (Strong router before more agents):** The router emits "risk tier" and "approval requirement" per request. The router needs a single source of truth for action policy that handles actor-level variation as a modifier, not as a separate lookup table. Per-agent maps fragment the router's evaluation surface.
- **P4 (Every workflow produces a reusable asset; otherwise it's labor):** A map that must be duplicated per agent is a non-reusable asset by design. Per-agent maps fragment the substrate. Action-category mapping with modifiers compounds: new agents inherit the canonical map; modifiers express their deviations.
- **P6 (Autonomy is configured by category and audited, never assumed):** The rewritten P6 (per Opus's Task 4) names "category of action" as the unit of autonomy explicitly. "Per-agent" is not the unit P6 names.

**Alternative considered: Per-agent maps (one autonomy file per agent).** The case for this was "matches how authorization works in adjacent systems (IAM, RBAC)." Rejected because:

- IAM-style authz is identity-permission ("can this user do this thing"), which centralizes actor variation but doesn't centralize action policy. DavidOS needs to centralize action policy because David's risk tolerance is action-defined, not actor-defined.
- DavidOS is single-operator (David is always the principal). Actor variation is execution mechanism, not authorization principal. IAM analogies fail.
- P6 specifically inverts the IAM model by making category the unit. Per-agent maps would violate P6 as stated.

**Alternative considered: One unified map with an "Agent/Process" column.** Rejected because making actor a primary-key column alongside category still treats actor as constitutive rather than modifying. The principle-aligned structure is category as primary key, actor as conditional modifier.

**General principle articulated tonight:** *Map approval policies to the dimension that varies the policy, not to the dimension that varies the actor.* For DavidOS, the dimension that varies the policy is action category, because David's risk tolerance is about actions, not about actors. If a different system had policy variation that tracked more closely with actor identity, per-actor mapping would be right; but that is not DavidOS.

### Decision 3: 10-field per-row schema with audit metadata

**Choice:** Each row in `action-map.md` contains 10 fields:

```
Category: <short name>
Description: <one-line definition>
Default rung: <L0 / L1 / L2 / L3 / L4>
Approval intensity if L1: <Light / Full / N/A>
Hermes mechanism: <which config knob, skill guard, pattern, or scope enforces this>
Notes: <conditions, exceptions, dependencies>
Date added: YYYY-MM-DD
Added by: David | Atlas (with David's approval on YYYY-MM-DD)
Review trigger: <default "on observed drift"; override per category as needed>
Last reviewed: YYYY-MM-DD (blank for v0.1; populated when reviewed)
```

**Reasoning:**

- The first six fields (Category through Notes) are the operational minimum needed to satisfy the audit's P6 test: each row must point at a real Hermes mechanism, and the choices must be auditable per category.
- The last four fields (Date added, Added by, Review trigger, Last reviewed) enable two self-improvement mechanisms David explicitly wants:
  - **Drift detection:** A `davidos-autonomy-review` skill (to be built in Phase 1) can grep the map for rows where "Last reviewed" exceeds a threshold and surface them for re-evaluation.
  - **Authorship audit:** "Added by" lets David distinguish entries he authored from entries Atlas proposed post-activation. The map becomes evolution-traceable.
- "On observed drift" was selected as the default review trigger because v0.1 has insufficient observation to specify per-category triggers. Once Atlas operates against the map for a session or two, he can propose category-specific triggers grounded in observed behavior — satisfying the principle that drift detection should be data-grounded rather than guess-grounded.

**Alternative considered: Lean 6-field schema (drop the audit metadata).** Faster to author v0.1. Rejected because the audit metadata directly enables the self-improvement mechanism David asked about, and the cost of adding the fields at the schema level is much lower than retrofitting them after categories accumulate.

**Alternative considered: Per-category explicit review triggers in v0.1.** Maximizes thoughtfulness but requires David to articulate triggers for ~15–25 categories with no observation to ground the choices. Rejected as premature optimization. Default "on observed drift" lets the data shape the triggers.

---

## How modifiers work (the operational pattern)

The `action-map.md` defines base rungs per action category. `modifiers.md` defines rules that adjust base rungs under specific conditions.

**Example modifier:**

```
Modifier: Cron context
Applies to: Any category when executed by a scheduled job
Effect: Drop rung by one level (L2 becomes L3; L1 requires pre-scheduled approval template)
Reasoning: Cron execution removes the in-the-moment David awareness that L2 assumes
```

**Example modifier:**

```
Modifier: Subagent actor
Applies to: Subagents spawned by Atlas
Categories affected: ADR creation, SOUL.md edits, autonomy map edits, principle modifications
Effect: Forced to L0 regardless of base rung
Reasoning: Identity-shaping work cannot be delegated per Section 6 of SOUL.md
```

The router (P3, to be built as `davidos-router` skill in Phase 1) computes the final rung for each request by:

1. Looking up the action's category in `action-map.md` → base rung
2. Checking `modifiers.md` for any modifier whose conditions apply to this request → adjustment
3. Emitting the final rung

This satisfies the audit's requirement that autonomy decisions be a single computation against a canonical source of truth.

---

## What this structure does not yet address (v0.2 work)

Three things the v0.1 schema deliberately does not capture, called out so future revisions are scoped:

1. **Time-of-day or session-state conditions.** "Atlas can spawn subagents during planning sessions but not during build sessions." Deferred to v0.2 if a real pattern emerges.
2. **Cross-category dependencies.** "Atlas can do X only after Y is done." Deferred to v0.2.
3. **Confidence-threshold conditional rungs.** "Action is L2 if confidence ≥ 90%, else L1." The schema currently uses fixed rungs per category; confidence-conditional rungs would require schema extension.

These are not gaps in v0.1; they are intentional scope bounds.

---

## How Atlas should evaluate this document

When charter-active Atlas reads this document as part of his first post-activation work (the schema-review task added to the audit prompt notes), he should:

1. Confirm or contest each decision (5 rungs, action-category primary key, 10-field schema) against the 7 consolidated principles. Cite specifically.
2. Propose alternatives only if his reasoning differs from the principle-grounded reasoning above. "I would have made the same choice for the same reason" is a valid answer — do not invent disagreements to seem rigorous.
3. Flag any place where the populated map (`action-map.md`) reveals a schema inadequacy that this document did not anticipate.
4. Recommend whether the v0.2 scope-bounded gaps (time-of-day conditions, cross-category dependencies, confidence-threshold rungs) need to be addressed sooner than expected.

The point of this document is not to defend the decisions against revision — it is to make the decisions revisable from a grounded starting point rather than from inference.
