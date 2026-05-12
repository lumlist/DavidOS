# DavidOS Session Workflow & Hosted Operating View — v0

Source approval: David's `[APPROVAL: bundle]` on DAV-17 at 2026-05-10T10:25:43Z, bundle named **Stage 2.5 — Session Workflow Foundation**.
Author: Atlas
Status: **Durable.** This file replaces the prior draft `davidos-session-workflow-design-v0.md`. Future substantive revisions require `[APPROVAL: policy-change]` and a new versioned filename (`-v1`, `-v2`, …) — no in-place overwrite.

## Vocabulary (definitive)

- **Session Start Submission** — David's structured submission at the *beginning* of a working session, replying to the prior Session Debrief and adding top-of-mind context, decisions to make, questions, ideas, considerations.
- **Session End** — David's explicit gesture to close the working session. Triggers Atlas to produce the Session Debrief. Notes from David are *optional*, not required.
- **Session Debrief** — Atlas's concise response after a Session End. Eight required sections, listed in §"Session Debrief schema" below.
- **Offline Work Approval Queue** — Queue of `offline-work` items Atlas has recommended; approved, rejected, or deferred outside an active session.
- **Parking Lot** — Raw ideas / questions / concerns / considerations / observations awaiting routing. May be authored by David, Atlas, or any other agent. Not active work, not durable memory.
- **Visual Proposal** — Prototype image, diagram, flowchart, or wireframe Atlas attaches to a recommendation when it would materially improve David's understanding or decision quality. Atlas prefers the cheapest acceptable rendering method (ASCII / Mermaid / SVG before pixel-art generators).

## Lifecycle at a glance

```
                     ┌───────────────────────────────────┐
                     │  David starts a working session   │
                     └────────────┬──────────────────────┘
                                  │
                                  ▼
        docs/sessions/drafts/session-start-draft.md   (template-driven)
                                  │
                       (David runs scripts/session.py start)
                                  │
        ┌─────────────────────────┴─────────────────────────┐
        │                                                   │
        ▼                                                   ▼
docs/sessions/submitted/         Paperclip [SESSION START] comment
<ts>-session-start.md            on session-tracker issue
        │                                                   │
        └─────────────────────────┬─────────────────────────┘
                                  ▼
                Atlas heartbeat picks it up; reads prior
                Session Debrief; produces Session-Start
                Recommendation.
                                  │
                                  ▼
              [SESSION-START-RESPONSE] comment + 1+ proposed
              actions (active work / new issue / parking lot
              entries / deeper dive / first-action suggestion).
                                  │
                                  ▼
        ┌───────────── working session in progress ─────────────┐
        │                                                       │
        │   • David edits docs/sessions/drafts/session-end-     │
        │     draft.md as ideas come up (OPTIONAL).             │
        │   • Atlas does not poll the draft.                    │
        │   • Daily Operating View shows "Session active"       │
        │     banner.                                           │
        │   • David or Atlas may add Parking Lot items at any   │
        │     time (different sections by source).              │
        │                                                       │
        └───────────────────────┬───────────────────────────────┘
                                ▼
                David runs scripts/session.py end
                (any draft notes are passed; no draft = no notes)
                                │
                                ▼
docs/sessions/submitted/<ts>-session-end.md   +
Paperclip [SESSION END] comment with David's optional notes
                                │
                                ▼
        Atlas heartbeat picks it up; ALWAYS produces a Session
        Debrief regardless of whether David submitted notes.
                                │
                                ▼
docs/sessions/submitted/<ts>-debrief.md   +
[SESSION-DEBRIEF] comment with the 8 required sections
                                │
                                ▼
        ┌───── if Debrief recommends offline work ──────┐
        │                                               │
        ▼                                               ▼
docs/sessions/offline-queue/   one [APPROVAL-REQUEST]
<date>-<slug>.md               kind: offline-work per item
status: pending                on the session-tracker issue
        │                                               │
        └────────────────────────┬──────────────────────┘
                                 ▼
        Between sessions: David replies on each
        [APPROVAL: offline-work] / [REJECT] / [DEFER].
        Atlas updates the file's status header. Atlas
        executes only when status flips to `approved`.
```

The diagram is the v0 visual proposal embedded in this memo per §"Visual proposals." More elaborate visuals (e.g., a full UI wireframe for sub-stage A) are deferred until that sub-stage is on-deck.

## 1. Implementation path (v0.1)

The Stage 2.5 commit lands the *foundation*: vocabulary, storage, conventions, templates, policies. **No executable code in this commit.** A separate `[APPROVAL-REQUEST]` follows for the smallest test-today implementation step.

### Storage layout

```
docs/
  sessions/                          # NEW folder — agents may write per the rules in memory-curation-policy
    drafts/
      session-start-draft.md         # current Session Start Draft (overwritten each session)
      session-end-draft.md           # current Session End Draft (OPTIONAL — empty is valid)
      parking-lot.md                 # rolling Parking Lot file with sections by source (David / Atlas / agent-name)
    submitted/
      <YYYY-MM-DDTHH-MM>-session-start.md
      <YYYY-MM-DDTHH-MM>-session-end.md
      <YYYY-MM-DDTHH-MM>-debrief.md
    offline-queue/
      <YYYY-MM-DD>-<short-slug>.md   # one file per offline-work request; status header indicates state
```

Why a dedicated `docs/sessions/` folder rather than reusing `docs/raw/` or `docs/daily/`:
- Workflow artifacts with a specific lifecycle deserve their own gate: nothing in `sessions/` is durable memory until promoted.
- Keeps `raw/` for general scratch and `daily/` for the daily-note template + Daily Operating View output.

### Control flow (file-and-Paperclip-only — no scripts in Stage 2.5)

The full executable flow uses `scripts/session.py start|end`. The script itself is **not** in this commit; this memo specifies its behavior so the future implementation has a clear contract.

**On Session Start (David-initiated):**
1. David fills `docs/sessions/drafts/session-start-draft.md` from the template. Edits in any markdown editor.
2. David runs `scripts/session.py start` (Stage 2.6+):
   - Validates non-empty.
   - Copies to `docs/sessions/submitted/<timestamp>-session-start.md` (immutable archive).
   - Posts `[SESSION START]` comment on the session-tracker issue.
   - Resets `session-start-draft.md` to blank template.
3. Atlas heartbeat picks up the new `[SESSION START]` and produces a `[SESSION-START-RESPONSE]` per §"Session-Start Recommendation schema" below.

**During the session:**
4. David optionally edits `docs/sessions/drafts/session-end-draft.md` whenever inspiration strikes. Atlas does NOT read the draft during the session.
5. The Daily Operating View (after Stage 2.6 renderer update) shows a "Session active since HH:MM" banner with a one-click link to the session-end-draft path.
6. David or Atlas may add to `parking-lot.md` at any time. Each entry includes a `source:` field (David / Atlas / `<agent-slug>`).

**On Session End (David-initiated):**
7. David runs `scripts/session.py end`. The script:
   - Reads the current draft (if any). Empty draft is *valid* — David is not required to write a debrief.
   - Copies to `docs/sessions/submitted/<timestamp>-session-end.md`.
   - Posts `[SESSION END]` comment on the session-tracker issue, including any draft content as "David's optional notes" (clearly delimited).
   - Resets `session-end-draft.md` to blank template.
8. Atlas heartbeat ALWAYS produces a Session Debrief on a `[SESSION END]` — regardless of whether David provided notes. The Debrief reads:
   - All Atlas/agent activity since the matching `[SESSION START]`.
   - The session-start submission (for context).
   - David's optional notes (if any).
   - The current Daily Operating View.
   - Parking Lot deltas during the session.
9. Atlas writes the Debrief to `docs/sessions/submitted/<timestamp>-debrief.md` and posts `[SESSION-DEBRIEF]` on the session-tracker issue.
10. If the Debrief recommends offline work, Atlas writes one file per item to `docs/sessions/offline-queue/` with `status: pending`, and posts an `[APPROVAL-REQUEST] kind: offline-work` per item.

**Extended-away handling (David's mod #3):**
- If David's Session End notes (or the `[SESSION END]` body) include the phrase "stepping away for <N> hours" or similar, Atlas treats it as an *extended-away* signal when N ≥ 10.
- The Session Debrief's §8 "Security/cost/memory if David steps away 10+ hours" is then populated with concrete recommendations (see schema below). Otherwise §8 may be a one-line "n/a (short-away)".
- Atlas may also infer extended-away from prolonged inactivity even without an explicit signal — but only as a `[RECOMMENDATION]`, not a unilateral lockdown.

**Offline Work Approval Queue (between sessions):**
11. David replies on each request with `[APPROVAL: offline-work]`, `[REJECT]`, or `[DEFER: <YYYY-MM-DD>]`. Atlas updates the file's `status:` header.
12. Daily Operating View "Pending approvals" section auto-includes `offline-work` items because they're already `[APPROVAL-REQUEST]`s with a `kind:`.

**Parking Lot:**
13. `docs/sessions/drafts/parking-lot.md` has three labeled sections: `## David` / `## Atlas` / `## Other agents`. Each entry: `- <YYYY-MM-DD HH:MM> | <category> | <text>`. Categories: idea / question / concern / consideration / observation.
14. David may add to any section; in practice writes to `## David`. Atlas appends to `## Atlas`. Other agents (when commissioned) append to `## Other agents` with their own subsection per agent slug.
15. Atlas may surface high-value items in the Daily Operating View "Atlas recommendations" section as proposed-routing candidates, but acts on none of them without explicit `[APPROVAL: <kind>]`.
16. Filtering "mine only" is supported by the file structure (David reads only `## David`). The Daily Operating View renderer (Stage 2.6+) will offer a per-source filter.

### Templates created in this commit

- `docs/atlas/templates/session-start-template.md` — sections: Reply to last debrief / Top of mind / Decisions I want help with / Questions / Ideas / Considerations or concerns.
- `docs/atlas/templates/session-end-notes-template.md` — sections: optional notes for Atlas (matches David's [REVISION] §"Session End Draft fields"), but explicitly labeled as optional. Empty submission is valid.
- `docs/atlas/templates/parking-lot-template.md` — three top-level sections (David / Atlas / Other agents), entry format documented inline.
- `docs/atlas/templates/offline-work-item-template.md` — frontmatter (`status: pending`, `requested_at`, `kind`, `source: Atlas|<agent-slug>`), body sections: what / why / risk / reversibility / expected_cost / proposed_action.

### Files NOT in Stage 2.5

- `scripts/session.py` (Stage 2.6 — separate `code-change` gate).
- Daily Operating View renderer update for session banners + offline-queue surfacing (Stage 2.6 — separate `code-change` gate).
- Any localhost HTTP endpoint, hosted UI, DNS, auth, scheduling, Obsidian-MCP, Langfuse, Tailscale, Caddy, Paperclip-write-API expansion, or new agent — each their own future gate.

## 2. Hosted Daily Operating View — longer-term architecture

Three sub-stages, each its own gate:

| Sub-stage | Goal | Approval surface |
|---|---|---|
| A — Local-only static viewer with in-page form | David hits `http://localhost:<port>/today.html` in any browser; Start/End-session buttons write to draft files via stdlib `http.server` + custom handler. | `code-change` for the script. |
| B — Tailscale-fronted multi-device | Same surface, accessible from any device on David's Tailnet. Auth via Tailnet membership, no public exposure. | `install` (Tailscale or equivalent), maybe `paid-service` if any cost. |
| C — Public on David's unused domain | Caddy + Cloudflare Tunnel back to the local box, signed-token or single-account-OAuth auth. | `install` (Caddy/Tunnel), `credential` (signing key), `paid-service` (any infra cost), `production` (customer-facing implications), `policy-change` for new `hosted-deployment` approval-kind. |

Architectural invariants across all three sub-stages:

- **Repo is the source of truth.** Hosted UI never holds state; reads/writes files (or, eventually, Paperclip API).
- **No new database.** `docs/sessions/**` is the database.
- **Stateless backend.** Every request reads files, writes files.
- **Single-tenant.** Customer-facing iZZi mode is out of scope here.

## 3. Storage model — drafts NEVER active memory

| Class | Path | Atlas may read? | Treat as instruction? | Promoted via |
|---|---|---|---|---|
| Active instruction | Paperclip issue description; Paperclip comments tagged `[APPROVAL-REQUEST]` / `[APPROVAL: ...]` / `[REVISION]` / `[BLOCKER]` / `[SESSION START]` / `[SESSION END]` | Yes | **Yes** | n/a |
| Active memory | `docs/wiki/`, `docs/output/`, `docs/atlas/*-policy-v*.md`, `docs/atlas/atlas-operating-spec.md`, this file | Yes | **Yes** | n/a |
| Submitted session input | `docs/sessions/submitted/*-session-start.md`, `*-session-end.md`, `*-debrief.md` | Yes | The Debrief is durable Atlas-output; Session Start/End submissions become instructions only via the matching Atlas response | n/a (immutable archive) |
| Draft (non-instruction) | `docs/sessions/drafts/session-{start,end}-draft.md` | **No during a session** — Atlas only reads via the helper script's atomic copy step | **No** | helper script (David-initiated) |
| Parking Lot | `docs/sessions/drafts/parking-lot.md` | Yes (read; surface in Daily Operating View) | **No** | `[PROMOTION-REQUEST]` per item; David approves; Atlas routes |
| Offline-queue item | `docs/sessions/offline-queue/*.md` with `status: pending` | Yes | **No** until status is `approved` | `[APPROVAL: offline-work]` flips status |
| Raw scratch | `docs/raw/` | Yes | **No** (informational only) | `[PROMOTION-REQUEST]` to `wiki/` |

Three behavioral rules locked into `approval-policy-v0.md` in this commit:

1. **Drafts are inert.** Atlas never reads `docs/sessions/drafts/session-*-draft.md` during normal operation. Heartbeats do not poll draft files.
2. **Parking Lot is observation, not direction.** Atlas may surface items as routing candidates in the Daily Operating View; never acts on them without explicit promotion approval. Agent-submitted items are *suggestions*, never durable memory or active work.
3. **Offline-queue items are pending until approved.** Atlas reads them and may pre-research within `safe-doc-edit` bounds, but does not execute the proposed action until `status: approved`.

## 4. Promotion process

A Parking Lot, Session Start, or Session End item can be promoted to one of seven destinations. Same shape for each: Atlas proposes routing → David approves → Atlas executes.

| Destination | Approval-kind | Atlas action on approval |
|---|---|---|
| Active work (open Paperclip issue, assigned to Atlas) | `code-change` (Paperclip issue creation) | Create issue with item content as seed description; remove line from `parking-lot.md`. |
| New Paperclip issue (unassigned, parked) | `code-change` | Same as above with `assigneeAgentId: null`. |
| Durable memory — `wiki/` entry | `wiki-promotion` | Author wiki file; remove parking-lot line. |
| Deeper dive | `code-change` | Create Paperclip issue with Domain Deep Dive Request template pre-filled; assign Atlas. |
| Skill | `policy-change` | Draft skill under `docs/atlas/skills/`; post for `[APPROVAL: policy-change]`. No auto-promote. |
| Automation | `code-change` (+ maybe `scheduling`) | Draft script; post `[APPROVAL-REQUEST] kind: code-change`. |
| Ignore / defer | n/a | Mark line `[ignored]` or `[deferred-until: YYYY-MM-DD]` in `parking-lot.md`. |

Promotion is **batched** in the Session Debrief's `## Promotion candidates` section so David approves once with `[APPROVAL: bundle]` instead of 50 individual requests per session. Per-line constraints in the approval are honored.

## 5. Daily Operating View Builder — role NOW, agent later

**Role NOW** (executed by Atlas/Hermes). The role is real; the work in v0.1 / sub-stage A is small enough that a dedicated agent is premature and would spend most of its budget context-switching.

**Agent commission triggers** (at least 3 of 4):
- 30+ session cycles of v0.1 use.
- Sub-stage B/C work in flight.
- Weekly Builder-role load > ~4 hours.
- Atlas's other duties context-switching cost is measurable.

**v0 spec sketch** (NOT a creation request — pre-thinking only). Full 7-field spec per `agent-expansion-policy-v0.md` §2 to be filled when the trigger fires:

- **Role:** owns Daily Operating View end-to-end. Triages `daily-view`-labeled issues; implements approved improvements; runs sub-stage migrations under per-stage approval. Reports to Atlas; does not own policy decisions.
- **Guardrails:** inherited from policy + role-specific (no edits outside its allow-list; never originates approval-kinds or comment-tags).
- **Permissions:** projects: `[DavidOS / Personal AI Workspace]`; labels: `[daily-view, session-workflow, offline-queue]`; folders: `[scripts/, docs/sessions/, docs/daily/, docs/atlas/templates/, docs/atlas/install-briefs/]`; pre-approved kinds: `[safe-doc-edit]`.
- **Memory boundaries:** reads all policies + this memo + spec; writes only in permission folders; owns `docs/atlas/agents/daily-view-builder/`; read-only access to `docs/atlas/` root.
- **Runtime validation:** synthetic test issue → no-op render → `[STATUS]`; identity correctly resolved by comment route (or documented mitigation); allow-list enforcement verified by attempted out-of-bounds writes failing loudly; OTel tagging verified post-Langfuse.
- **Approval policy:** inherits Atlas's at same strictness; MORE strict on `policy-change` (Builder may not originate), `new-agent` (Builder may not propose), `paid-service`/`install`. Identical otherwise.
- **Success metrics (30-day cadence):** ≥1 daily-view improvement shipped per 7-day window when there are open `daily-view` issues; 0 out-of-allow-list incidents; 0 unauthorized policy/agent originations. Kill: 14-day window with no shipped improvements + 1+ open `daily-view` issues; or any single signal-2/3 incident.

## 6. Paperclip API write-path investigation/fix

Three phases:

### Phase 1 — Reproduce (no code changes, ~30 min)
- Atlas writes a small repro under `docs/atlas/runs/<date>-paperclip-comment-route-bug-repro.md` (pre-approved `safe-doc-edit`).
- Documents endpoint, headers sent, response received, the resulting comment record's `authorUserId: "local-board"` despite `X-Paperclip-Agent-Id` header.
- Confirms scope: documents/issues/projects/runs APIs all attribute the agent correctly. Only the comment route is buggy.

### Phase 2 — Propose fix (issue + diff sketch, no Paperclip source edits)
- Atlas opens a dedicated issue (proposed under "AI Workspace Diagnostic Service" or as a new top-level): "Paperclip comment-route ignores X-Paperclip-Agent-Id in local_trusted mode."
- Description: repro, root cause analysis, proposed diff sketch (TypeScript pseudocode only — Atlas does not have approval to edit Paperclip source).
- David decides: fix himself, hand to a Paperclip maintainer, or grant Atlas a fresh `code-change` gate covering Paperclip source edits.

### Phase 3 — Live-with-mitigation enhancement (optional, ~1 hour, `code-change` gate)
- If David accepts the mitigation indefinitely: add a small auto-`[ATLAS-NOTE]` automation that, when productivity-monitor flags fire on a known-loop-mitigated issue, posts a one-line `[STATUS]` referencing the persistent false-positive memo. Reduces human cost of the mitigation.

Recommendation: do Phase 1+2 immediately (cheap, generates artifact). Defer Phase 3 until David picks fix-vs-mitigate.

## 7. Visual proposals (David's [REVISION] mod #4)

When discussing complex design / architecture / workflow / UI / implementation changes, Atlas proactively produces a prototype image, diagram, flowchart, or wireframe when it would materially improve David's understanding or decision quality. Atlas prefers the cheapest acceptable rendering:

| Need | Preferred method | Avoid unless richer is needed |
|---|---|---|
| Lifecycle / sequence flow | ASCII art (this memo's §"Lifecycle at a glance"), or Mermaid in a markdown code block | Pixel-art generators, screenshot-based diagrams |
| Architecture diagram | Mermaid `flowchart`, simple SVG with inline CSS | Full design-tool exports |
| UI wireframe | ASCII boxes + labels; or simple SVG via stdlib templating | Figma export, generated images |
| Decision tree | Markdown nested list; Mermaid `graph LR` | Rich infographics |
| Data shape | Markdown table + JSON snippet | Real screenshots |
| State machine | Mermaid `stateDiagram` | Custom diagram editors |

Rules:
- Visuals are **proposals**, not durable memory. They live in the same memo / comment / debrief as their context.
- If a richer visual is needed (e.g., real screenshot, brand mock), Atlas posts a `[RECOMMENDATION]` saying so and asks for `[APPROVAL: code-change]` to invoke a heavier tool.
- All visuals are reproducible from the memo's text — anyone reading the markdown later should not need an external image to understand the design.
- Cost discipline: prefer ASCII first, Mermaid second, SVG third, generated images last and only with approval.

The lifecycle ASCII diagram in §"Lifecycle at a glance" of this memo is the v0 example.

## 8. Session Debrief schema

Every Session Debrief produced by Atlas in response to a `[SESSION END]` includes these eight sections, in this order:

1. **What should stay top of mind** — durable threads David should not let drop.
2. **Decisions / work to prioritize next** — the next 1-3 concrete items.
3. **Open questions, ideas, or concerns to process** — items needing more thought.
4. **Recommended deeper dives** — Domain Deep Dive candidates with one-line scope.
5. **Work Atlas will do while David is offline, if any** — explicit list with proposed-actions; each item generates an `[APPROVAL-REQUEST] kind: offline-work`.
6. **Priorities for the next working session** — 2-4 items.
7. **Suggested first prompt for next session** — a one-paragraph drop-in for `session-start-draft.md`.
8. **Security, cost, and memory considerations if David steps away 10+ hours** — concrete recommendations covering:
   - Credentials at risk and mitigation (e.g., rotate / restrict / revoke).
   - Cost cap recommendations (e.g., pause non-essential agents, lower model tier, hard spend cap).
   - Memory hygiene (e.g., flush Parking Lot to durable wiki, archive completed `output/` files).
   - Offline-work scope: which items in the Offline Work Approval Queue are safe to leave Atlas executing autonomously vs. should be paused until return.
   - Heartbeat-loop watchdog: explicit decision on whether Atlas continues silent stand-down or pauses heartbeats entirely.

If David's `[SESSION END]` doesn't signal extended-away (or omits a duration), §8 is rendered as one line: `n/a — short-away`.

## 9. Session-Start Recommendation schema

Every Atlas response to a `[SESSION START]` (`[SESSION-START-RESPONSE]`) includes:

1. **Acknowledgment of David's submission** — one paragraph.
2. **Routing recommendations**, one per substantive item in the submission, each labeled:
   - `→ active work` (Atlas will pick up now, or David should)
   - `→ new Paperclip issue` (proposed title + project + assignee)
   - `→ Parking Lot` (proposed source + category)
   - `→ deeper dive` (proposed scope + effort level)
   - `→ ignored or challenged as distraction` (Atlas's reasoning for why this isn't worth pursuing now)
3. **Recommended first action for the session** — one concrete next step.
4. **Atlas-side flags** — anything Atlas wants David to know about its own state (open approvals, blockers, etc.).

## 10. Run control — Stage 2.5 commit specifics

Stage 2.5 is exactly: docs + policy + templates + folder scaffold. No scripts, no installs, no scheduling, no agent commissioned, no Paperclip-write-API expansion.

Files committed in Stage 2.5:

| Path | Action | Source |
|---|---|---|
| `docs/atlas/davidos-session-workflow-v0.md` | new (this file) | promotion of prior draft |
| `docs/sessions/drafts/README.md` | new | scaffold |
| `docs/sessions/submitted/README.md` | new | scaffold |
| `docs/sessions/offline-queue/README.md` | new | scaffold |
| `docs/atlas/templates/session-start-template.md` | new | template |
| `docs/atlas/templates/session-end-notes-template.md` | new | template |
| `docs/atlas/templates/parking-lot-template.md` | new | template |
| `docs/atlas/templates/offline-work-item-template.md` | new | template |
| `docs/atlas/comment-conventions-v0.md` | edit | adds `[SESSION START]`, `[SESSION END]`, `[SESSION-START-RESPONSE]`, `[SESSION-DEBRIEF]` tags |
| `docs/atlas/approval-policy-v0.md` | edit | adds `offline-work` and `wiki-edit-from-promotion` kinds; adds `safe-visual-proposal` pre-approved category; adds bundle pattern note for Stage 2.5 precedent |
| `docs/atlas/memory-curation-policy-v0.md` | edit | adds `docs/sessions/` rules to folder layout and write-permission table |

Verification after commit: `[STATUS]` with SHA, `git log -1 --stat`, `git status --short`. No artifacts left untracked except the auto-regenerable `docs/daily/today.{html,md}` and `docs/daily/<today>.md` template stub.

End of file.
