# DavidOS Autonomy Modifiers — v0.1

**Status:** Canonical actor and context modifiers for DavidOS. Authored 2026-05-14 by David (operator) with Sonnet/Computer drafting support. Conforms to the schema at `SCHEMA.md`.

**Version:** 0.1 (initial population, pre-activation)

**Purpose:** Modifiers adjust the base rungs in `action-map.md` when specific actor or context conditions apply. The action map defines the canonical autonomy by action category; modifiers express how that autonomy changes under particular conditions. The `davidos-router` skill (Phase 1) computes the final rung by applying matching modifiers to base rungs per the conflict resolution rules in `SCHEMA.md` §3.

**Companion files:** `SCHEMA.md` (modifier schema and grammar), `action-map.md` (canonical action categories), `README.md` (orientation).

---

## Modifier 1: Subagent Actor

- **Modifier:** Subagent Actor
- **Applies to:** Any action performed by a subagent spawned by Atlas (or by a future subagent of a subagent, recursively)
- **Categories affected:** 16 (Edit SOUL.md), 17 (Create or revise ADRs), 18 (Edit autonomy map or modifiers), 19 (Modify Hermes configuration)
- **Effect:** Force to L0 (Forbidden) regardless of base rung
- **Reasoning:** Identity-shaping work cannot be delegated. Per SOUL.md §6 "Participating in structural decisions," identity- or values-shaped decisions are David's alone; this modifier extends that principle to forbid identity-shaping work being performed by subagents, even if Atlas himself has the autonomy to propose changes. Subagents are scope-bounded delegates of Atlas; they inherit his autonomy on operational categories but cannot reach into identity-level files. This is the load-bearing safety property of the subagent delegation pattern.
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)

---

## Modifier 2: Cron Context

- **Modifier:** Cron Context
- **Applies to:** Any action executed by a scheduled job (cron) rather than by Atlas in an interactive session
- **Categories affected:** Any category at base rung L2 (Acts and Reports), with one exception (see Notes)
- **Effect:** Drop rung by 1 (L2 becomes L3 — Acts Silently)
- **Reasoning:** Cron execution removes the in-the-moment David awareness that L2 assumes. When Atlas executes interactively, "Acts and Reports" means David sees the report in the conversation immediately. When a cron job runs at 3 AM, there is no chat surface to report into — the report would land in a log that David checks asynchronously. The principled response is to drop scheduled L2 actions to L3 (silent execution) and rely on the schedule-approval mechanism (Category 15 Notes, L4 schedule policy) as the upstream approval surface. The cron schedule was approved; the per-run execution doesn't add information by being announced.
- **Notes:** Exception — Category 15 (Send messages or content to external recipients) does NOT drop to a lower rung under cron context. External sends always require the L1 Full review of the actual content, and the schedule approval includes the content. The Cron Context modifier does not lower the rung for outbound message content.
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)

---

## Modifier 3: Out-of-Scope Repository

- **Modifier:** Out-of-Scope Repository
- **Applies to:** Any action targeting a repository or directory outside DavidOS, FamilyAI, or DavidAIStory (e.g., `izzi-foundation`, `Aion`, `Jobs`, `Skeptic`, or any other repo or path)
- **Categories affected:** 1 (Read repo files), 2 (Write or modify files in repo workspace), 4 (Delete files), 6 (Run state-modifying shell commands), 7 (Run destructive or sensitive shell commands)
- **Effect:** Force to L1 Full for any action that would modify state; force to L1 Light for read-only actions
- **Reasoning:** SOUL.md §5 ("Repo scope" principle) explicitly bounds Atlas's operations to the three named repos. This modifier enforces that boundary in the autonomy layer: if Atlas attempts to act on an out-of-scope repository, the action requires explicit approval — Light for reads, Full for state changes. The principle could be encoded as a hard L0 forbid, but L1 with explicit reasoning is more useful: David may have a legitimate one-off need (e.g., reading a file from an old repo to migrate something into DavidOS), and the L1 approval surface lets that happen consciously rather than blocking it absolutely.
- **Notes:** This modifier overlaps with Category 3 (Local filesystem reads outside repo scope) which is already L1 Light by default. The redundancy is intentional — the modifier covers state-changing operations against out-of-scope repos that aren't covered by Category 3.
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)

---

## Conflict resolution

Per `SCHEMA.md` §3, when multiple modifiers apply to the same request:

1. **Most restrictive wins.** If one modifier raises a rung and another lowers it, the higher (more restrictive) result holds.
2. **L0 always wins.** Any modifier that forces L0 overrides any other modifier.
3. **Document conflicts in `action-map.md` Notes** if the above rules don't cleanly resolve a specific case.

Example conflict resolution:

- A subagent spawned by Atlas runs on a cron schedule and attempts to edit SOUL.md.
- Modifier 1 (Subagent Actor) applies → Force to L0.
- Modifier 2 (Cron Context) applies → Drop rung by 1.
- Final rung: L0 (Modifier 1 wins by the "L0 always wins" rule).

---

## How modifiers evolve

- **Adding a modifier:** Atlas proposes the full modifier row per the schema with reasoning. David approves at L1 Full per Category 18 (modifier additions or changes). Approved modifiers are added with `Added by: Atlas (with David's approval on YYYY-MM-DD)`.
- **Modifying an existing modifier:** Full approval per Category 18. Modifier changes affect multiple action categories at once and are high-leverage by definition.
- **Removing a modifier:** Full approval per Category 18, with explicit reasoning for why the modifier is no longer needed.

---

## v0.2 candidates (not yet adopted)

Patterns that may warrant modifiers in v0.2 once we observe operation:

- **Karrigan Actor modifier** — when Karrigan is built (post-audit per `2026-05-14-karrigan-intent-capture.md`), he likely needs modifiers governing his higher-model defaults for reasoning tasks and his conversational vs. approval-disciplined posture.
- **High-frequency feature-branch push modifier** — if Category 12a reporting becomes noise, a modifier could drop force-push-to-own-branch from 12b's L1 Full to L2 (creating an effective 12c without splitting the category row).
- **Authenticated connector per-service modifiers** — when David first wires a connector (Gmail, Notion, etc.), per-service modifiers should refine Category 14's behavior. E.g., "Gmail read-only after approval at L3" — silent reads after the connector is wired.
- **Temp file cleanup modifier** — recursive delete in `/tmp/` (Category 4) could be modified to L2 if temp cleanup is routine.

These are flags, not commitments. The pattern is: observe the working motions for a few weeks, see what creates friction or risk, propose targeted modifiers.
