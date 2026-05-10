# DavidOS Session Workflow & Hosted Operating View — v0 Design Memo

Issue: DAV-17 [REVISION] from David at 2026-05-10T09:08:04Z
Author: Atlas
Status: Design / recommendation only. Nothing implemented. Draft saved at this path; not in `wiki/`, not durable policy yet.

## Vocabulary in this memo (matches David's [REVISION])

- **Session Start Submission** — David's structured submission at the *beginning* of a working session, replying to the prior Session Debrief and adding top-of-mind context, decisions to make, questions, ideas, considerations.
- **Session End Draft** — In-session, draftable closeout context. *Not* an instruction. Saves during the session; can be edited while referencing the Daily Operating View.
- **Session End Submission** — The Session End Draft becomes the submitted `[SESSION END]` request when David explicitly closes the working session.
- **Session Debrief** — Atlas's concise response to a Session End Submission.
- **Offline Work Approval Queue** — Queue of `offline-work` items Atlas has recommended; approved, rejected, or deferred outside an active session.
- **Parking Lot** — Raw ideas / questions / concerns / considerations awaiting routing. Not active work, not durable memory.

These five terms (plus Session Debrief) replace any earlier use of "daily note," "intake," or "submission" inside the v1 Daily Operating View domain.

## Output 1 — Safest v0.1 implementation path

The v0.1 surface is **file-and-Paperclip-only**. No hosted UI yet, no backend service, no DNS, no auth, no Paperclip-write API beyond what's already approved. The whole workflow lives in two places: the repo (for drafts) and Paperclip issue threads (for submissions and approvals).

### Storage layout (all under `docs/`, no new top-level directories)

```
docs/
  sessions/                          # NEW folder — agents may write freely; not durable memory
    drafts/
      session-start-draft.md         # current Session Start Draft (overwritten each session)
      session-end-draft.md           # current Session End Draft (overwritten each session)
      parking-lot.md                 # rolling Parking Lot file (append-only by David; Atlas may edit only via [PROMOTION-REQUEST])
    submitted/
      YYYY-MM-DDTHH-MM-session-start.md  # immutable archive of each submitted Session Start
      YYYY-MM-DDTHH-MM-session-end.md    # immutable archive of each submitted Session End
      YYYY-MM-DDTHH-MM-debrief.md        # Atlas's Session Debrief output
    offline-queue/
      YYYY-MM-DD-<short-slug>.md     # one file per offline-work request; status header indicates state
```

Why a new `docs/sessions/` folder rather than reusing `docs/raw/` or `docs/daily/`:
- These are *workflow artifacts* with a specific lifecycle, not raw notes or daily journals. They deserve a folder of their own so the curation gates apply uniformly: nothing in `sessions/` is ever durable memory until promoted.
- Keeps `docs/raw/` available for general scratch/transcripts/ad-hoc inputs, and keeps `docs/daily/` reserved for the daily-note template and Daily Operating View output.

The new folder does NOT need a separate `[APPROVAL: code-change]` for creation — it's the same shape (folder + README + curation rules) as the Stage 1 bundle. But it deserves a small bundled approval with the README content and a one-line update to `memory-curation-policy-v0.md` so the rules are explicit. See output #7.

### v0.1 control flow

**On Session Start (David-initiated):**
1. David fills `docs/sessions/drafts/session-start-draft.md` from the template (described below). Edits in any markdown editor.
2. David runs a tiny CLI helper (proposed name: `scripts/session.py start`) which:
   - Copies `session-start-draft.md` to `docs/sessions/submitted/<timestamp>-session-start.md` (immutable).
   - Posts a `[SESSION START]` comment on a designated session-tracker issue (proposed: a single open issue per active project, or one company-level "Active session" issue). Body = the submission's content.
   - Clears `session-start-draft.md` to the blank template for next time.
3. Atlas's heartbeat picks up the new `[SESSION START]` comment, reads the latest Session End Submission + Session Debrief on file (if any), and produces the Session-Start Recommendation per David's [REVISION] §1 ("active work / Paperclip issue / Parking Lot / deeper dive / ignored or challenged / first action") as a `[SESSION-START-RESPONSE]` comment on the same session-tracker issue.

**During the session:**
4. David edits `docs/sessions/drafts/session-end-draft.md` whenever inspiration strikes. The file is *just a draft*. Atlas does not read it during the session.
5. The Daily Operating View renders a small banner indicating "Session active since HH:MM" (read from the most recent `[SESSION START]` comment) and includes a link to the Session End Draft template path so David can open it with one click.

**On Session End (David-initiated):**
6. David runs `scripts/session.py end`. The script:
   - Validates the draft has at least one non-empty section.
   - Copies to `docs/sessions/submitted/<timestamp>-session-end.md`.
   - Posts a `[SESSION END]` comment on the session-tracker issue.
   - Clears `session-end-draft.md` to blank template.
7. Atlas's heartbeat picks up the `[SESSION END]`, produces the Session Debrief per David's [REVISION] §1 ("stay top of mind / next priorities / open questions / deeper dives / offline work / next-session priorities / suggested first prompt"), writes it to `docs/sessions/submitted/<timestamp>-debrief.md`, and posts as `[SESSION-DEBRIEF]` comment on the session-tracker issue.
8. If the Debrief recommends offline work, Atlas writes one file per item to `docs/sessions/offline-queue/` with a status header (`status: pending`) and posts an `[APPROVAL-REQUEST] kind: offline-work` per item on the session-tracker issue (or on the relevant project issue if the offline work is project-specific).

**Offline Work Approval Queue (between sessions):**
9. David replies on each request with `[APPROVAL: offline-work]`, `[REJECT]`, or `[DEFER]`. Atlas updates the file's status header and acts only on `[APPROVAL: offline-work]`.
10. The Daily Operating View's "Pending approvals" section already lists `[APPROVAL-REQUEST]` items by kind; offline-work items show up there automatically once we add `offline-work` and `offline-work-approved/rejected/deferred` to the approval-policy table (output #7).

**Parking Lot:**
11. `docs/sessions/drafts/parking-lot.md` is append-only by David; Atlas may not edit it directly. Atlas may *propose* a routing decision (active work / new issue / wiki / deeper dive / skill / automation / ignore) for any Parking Lot item via `[PROMOTION-REQUEST]` referencing the line. David approves with `[APPROVAL: <appropriate-kind>]` and Atlas executes the routing, removing the line from `parking-lot.md` after.

### What v0.1 specifically does NOT include

- No hosted web surface (deferred to output #2's longer-term architecture).
- No Paperclip-write APIs beyond comments + documents (already exercised; same surface).
- No persistent backend, no auth, no DNS, no domain hosting.
- No automatic pickup of edits to draft files (drafts are inert until David explicitly submits via the helper script).
- No agent (Daily Operating View Builder remains a *role* in v0.1; see output #5).

### Templates (each ~30 lines, lives in `docs/atlas/templates/`)

- `session-start-template.md` — sections: Reply to last debrief / Top of mind / Decisions I want help with / Questions / Ideas / Considerations or concerns.
- `session-end-template.md` — exactly David's [REVISION] §"Session End Draft fields" verbatim.
- `parking-lot-template.md` — line format: `- YYYY-MM-DD HH:MM | <category> | <text>`. Categories: idea / question / concern / consideration / observation. Atlas reads but never edits.
- `offline-work-item-template.md` — frontmatter: `status: pending|approved|rejected|deferred|completed`, `requested_at`, `kind`, body sections: what / why / risk / reversibility / expected_cost / proposed_action.

### v0.1 effort estimate

- Storage layout + READMEs: ~30 min (bundled with output #7's approval).
- `scripts/session.py` start/end commands: ~3-4 hours of code (stdlib only, mirrors `render-daily-view.py` patterns).
- 4 templates: ~30 min.
- Update Daily Operating View renderer to surface `[SESSION START]` / `[SESSION END]` / offline-work pending: ~2 hours.
- Update `comment-conventions-v0.md` with new tags (`[SESSION START]`, `[SESSION END]`, `[SESSION-START-RESPONSE]`, `[SESSION-DEBRIEF]`, `offline-work` approval-kind): ~30 min.

Total: ~7-8 hours, all `code-change` + `policy-change` gates, all reversible. No installs, no hosted, no auth, no scheduling.

## Output 2 — Longer-term hosted Daily Operating View architecture

David's hosted direction (from the [REVISION]):
- Simple web surface accessible without terminal or ChatGPT.
- Start Session button with draftable form.
- Inline Session End Draft editable while referencing the operating view.
- End Session submission button.
- Offline Work Approval Queue available outside active sessions.
- Links to Paperclip, DavidOS files/Obsidian, later Langfuse.

The right shape is **a static-first site that reads/writes to a thin local backend, deployed on the unused domain**, evolving in three sub-stages so each piece earns its own approval gate.

### Sub-stage A — Local-only static viewer (no domain, no backend)

- Re-render the v0 Daily Operating View at a localhost-only HTTP endpoint (e.g., `python3 -m http.server` against `docs/daily/`) so David can hit it from a browser tab without opening Obsidian or terminal.
- Add a small `<form>` block in the rendered page that POSTs to a *local-only* CGI-ish endpoint (still stdlib only — `http.server` with a custom handler) which writes to the draft files. No public exposure.
- Effort: ~4-6 hours. Approval gate: `code-change` for the script, `scheduling` only if we want it auto-launched at boot (we wouldn't in this sub-stage — David runs it manually).
- Deliverable: David can hit `http://localhost:<port>/today.html` in a browser, click "Start Session," fill a form, click submit. The form writes to `docs/sessions/drafts/session-start-draft.md` and triggers the same `scripts/session.py start` flow as v0.1.

### Sub-stage B — Caddy/Tailscale-fronted local surface (still no public domain)

- Front the local surface with a reverse proxy that's only reachable via Tailscale (or a similar VPN) so David can hit it from any device on his Tailnet without exposing it to the public internet. No DNS changes against the unused domain yet.
- Approval gates: `install` (Caddy or Tailscale serve), `paid-service` if the chosen tool has any cost (Tailscale free tier is sufficient at this scale).
- Why this sub-stage exists: it's the safest way to get David multi-device access without auth complexity. Tailscale handles auth via the Tailnet membership.

### Sub-stage C — Public hosted on David's unused domain

- Only when sub-stages A and B have proven the workflow over 30+ session cycles.
- Architecture: same static page, fronted by Caddy on a small VM (or Cloudflare Tunnel back to the local box, no VM needed). Auth via a single-user signed token (David-only), or via OAuth with a single allowlisted account (David's).
- Approval gates required (each separate): `install` (Caddy/Tunnel), `credential` (signing key), `paid-service` (any infra cost), `production` (anything customer-facing in the iZZi sense), `policy-change` (a new `hosted-deployment` approval-kind to govern future deploys).
- Why deferred this far: every step adds risk surface. Sub-stage A solves the actual painpoint (a click-to-submit UI for the workflow) with zero new infra and zero new auth. The hosted form factor is desirable but not on the critical path.

### Architectural invariants across all three sub-stages

- **Repo is the source of truth.** The hosted UI never holds state — it always reads from and writes to files in the repo (or, eventually, posts to the Paperclip API). If the hosted UI disappeared tomorrow, the workflow continues via the v0.1 file-and-CLI flow.
- **No new database.** `docs/sessions/**` *is* the database.
- **Stateless backend.** Every request reads files, writes files. No in-memory session state.
- **Single-tenant.** Customer-facing iZZi mode is out of scope for this surface; it gets its own architecture later.

## Output 3 — Storage model so drafts and parking lot are NOT treated as active memory

The rule is enforced by **folder location + curation policy**, not by software. Restating cleanly:

| Class | Path | Atlas may read? | Atlas may treat as instruction? | Promoted via |
|---|---|---|---|---|
| Active instruction | Paperclip issue description; Paperclip comment with `[APPROVAL-REQUEST]` / `[APPROVAL: ...]` / `[REVISION]` / `[BLOCKER]` | Yes | **Yes** | n/a |
| Active memory | `docs/wiki/`, `docs/output/`, `docs/atlas/*-policy-v*.md`, `docs/atlas/atlas-operating-spec.md` | Yes | **Yes** (these are durable rules / reference) | n/a |
| Submitted session input | `docs/sessions/submitted/*-session-start.md`, `*-session-end.md`, `*-debrief.md` | Yes | **Yes for the Debrief**; Session Start/End submissions become instructions only via the matching Atlas response which translates them into concrete actions or queue entries | n/a (immutable archive) |
| Draft (non-instruction) | `docs/sessions/drafts/session-start-draft.md`, `session-end-draft.md` | **No during a session** (Atlas treats as inert until the helper script copies to `submitted/`) | **No** | The helper script (David-initiated) |
| Parking Lot (non-instruction) | `docs/sessions/drafts/parking-lot.md` | Yes (read-only, may surface in Daily Operating View) | **No** | `[PROMOTION-REQUEST]` per item; David approves; Atlas routes to the chosen destination |
| Offline-queue item (request) | `docs/sessions/offline-queue/*.md` with `status: pending` | Yes | **No** until status is `approved` | `[APPROVAL: offline-work]` flips status to `approved`; only then does Atlas act |
| Raw scratch | `docs/raw/` | Yes | **No** (raw is informational input only) | `[PROMOTION-REQUEST]` to `wiki/` |

Three behavioral rules added to `approval-policy-v0.md` (small `policy-change`, see output #7):

1. **Drafts are inert.** Atlas never reads `docs/sessions/drafts/session-*-draft.md` during normal operation. The only mechanism that converts a draft into instruction is the helper script's atomic copy + post step, which David runs. Heartbeat wakes do not poll draft files.
2. **Parking Lot is observation, not direction.** Atlas may surface Parking Lot items in the Daily Operating View "Atlas recommendations" section (with the line text and a routing recommendation), but does not act on Parking Lot items without David's explicit promotion approval.
3. **Offline-queue items are pending until approved.** Atlas reads them, may even prepare for them (e.g., research that's pre-approved as `safe-doc-edit`), but does not execute the proposed action until the file's `status:` header shows `approved`.

## Output 4 — Promotion process

A Parking Lot item, Session Start submission item, or Session End submission item can be promoted to one of seven destinations. The promotion process is the same in shape for each: Atlas proposes routing → David approves → Atlas executes. Only the executing action and the relevant approval-kind differ.

| Destination | Approval-kind | Atlas action on approval |
|---|---|---|
| Active work (open Paperclip issue; assign to Atlas) | `code-change` (issue creation is a write to Paperclip — counts as code-change in v0; we should propose a `paperclip-issue` or simply `routing` kind in approval-policy v1) | Atlas creates the issue via Paperclip API with the parking-lot line as the seed description, removes the line from `parking-lot.md`. |
| New Paperclip issue (unassigned, parked for future triage) | same | Same as above but `assigneeAgentId: null`. |
| Durable memory — `wiki/` entry | `wiki-promotion` | Atlas creates the wiki file with the parking-lot line + any context Atlas synthesizes, removes the line. |
| Deeper dive | `code-change` (creates a Paperclip issue with `Domain Deep Dive Request` template pre-filled) | Atlas creates the issue, sets the Domain Deep Dive description, assigns Atlas. |
| Skill | `policy-change` (new skill = new operating procedure) | Atlas writes a draft skill under `docs/atlas/skills/` and posts it for `[APPROVAL: policy-change]` (no auto-promote). |
| Automation | `code-change` (script) + maybe `scheduling` | Atlas drafts the script, posts an `[APPROVAL-REQUEST] kind: code-change`. |
| Ignore / defer | none | Atlas marks the line `[ignored]` or `[deferred-until: YYYY-MM-DD]` in `parking-lot.md`. |

The mechanics:

1. Atlas posts a `[PROMOTION-REQUEST]` comment on the session-tracker issue with the source line, the proposed destination, the proposed `approval-kind`, and the rationale (3-5 sentences max).
2. David replies with `[APPROVAL: <kind>]` or `[REJECT]` or `[DEFER]`.
3. Atlas executes; updates the parking-lot file; posts a `[STATUS]` confirming.

Two important discipline rules:

- Atlas **batches** Parking Lot promotion requests in the Session Debrief — not as 50 separate `[APPROVAL-REQUEST]` comments per session. The Debrief contains a `## Promotion candidates` section listing each line + proposed destination; David approves the whole batch with `[APPROVAL: bundle]` (with optional per-line constraints) just like the Stage 1 doc/policy bundle.
- The session-tracker issue (proposed) becomes the audit trail. One issue per project (or one company-level), kept open indefinitely; status stays `in_progress`; the comment thread is the session log.

## Output 5 — Daily Operating View Builder role / agent question

David asked specifically: define a Daily Operating View Builder *role* now? Make it an agent later? Address safety, guardrails, permissions, memory boundaries, runtime validation, success metrics.

**Recommendation: define as a role NOW (executed by Atlas/Hermes), defer agent commission.** Rationale:

The role is real and durable: someone owns developing and optimizing David's UI surface. But the work in v0.1 and through sub-stage A is small, infrequent, and tightly coupled to other Atlas decisions (curation policy updates, comment-convention extensions, etc.). A dedicated agent at this scale would spend most of its budget context-switching to read Atlas's policies and would still need Atlas to approve most of its decisions — net negative on efficiency, with the added risk that a half-utilized agent atrophies and degrades.

When to commission as an agent (the kill-the-role-trigger):
- v0.1 has been in regular use for 30+ session cycles (probably ~2 months calendar time at typical rhythm).
- The role's workload has grown to include sub-stage B/C decisions (deployment, auth, multi-device), Langfuse-derived metric design, and per-project Daily Operating View customization.
- The total weekly time spent by Atlas on Builder-role work exceeds ~4 hours and is causing context-switching cost on Atlas's other duties.

When that trigger fires, Atlas posts an `[APPROVAL-REQUEST] kind: new-agent` with the 7-field spec from `agent-expansion-policy-v0.md` already populated. Below is the v0 draft of that spec so David can review the shape now and pre-think it.

### v0 spec sketch (NOT a creation request — pre-thinking only)

**Role:** Daily Operating View Builder — owns the Daily Operating View surface end-to-end. Triages all surface-related issues (issues labeled `daily-view`), implements approved improvements, runs sub-stage migrations (A → B → C) under explicit per-stage approval, owns the rendering script, owns the session-workflow scripts, owns the offline-queue mechanics. Reports to Atlas; does not own policy decisions (those remain Atlas).

**Guardrails (inherited + role-specific):**
- All inherited from `agent-expansion-policy-v0.md` §2.2.
- Never modifies anything outside `scripts/`, `docs/sessions/`, `docs/daily/`, `docs/atlas/templates/`, `docs/atlas/install-briefs/`, and the renderer-related test fixtures (when those exist).
- Never originates a new approval-kind or comment-convention tag — proposes them via `[RECOMMENDATION]` to Atlas; Atlas decides.

**Permissions:**
- `projects: [DavidOS / Personal AI Workspace]`
- `labels: [daily-view, session-workflow, offline-queue]`
- `folders: [scripts/, docs/sessions/, docs/daily/, docs/atlas/templates/, docs/atlas/install-briefs/]`
- `apis: [Paperclip — read all, write comments+documents on issues with the labels above]`
- `pre-approved kinds: [safe-doc-edit]` (within the folder allow-list)

**Memory boundaries:**
- Reads: all of `docs/atlas/*-policy-v*.md`, `docs/atlas/atlas-operating-spec.md`, the v1 plan + revised plan, the session workflow design memo (this file once durable), the comment conventions.
- Writes: only within its permission folders.
- Owns subfolder `docs/atlas/agents/daily-view-builder/` for its operating notes.
- Read-only access to `docs/atlas/` root (does not edit Atlas's self-knowledge).

**Runtime validation:**
- Synthetic test issue: a no-op `daily-view`-labeled issue requesting a render-only change. Builder picks it up, runs the renderer, posts a `[STATUS]` with the diff (no commit). Verifies the agent's identity is correctly resolved by the comment route (or the documented mitigation is in place).
- Verifies the agent is using its permission allow-list (attempted writes outside the allow-list should fail loudly, not silently).
- OTel span tagging verified once Langfuse is live.

**Approval policy:**
- Inherits Atlas's approval policy at the same strictness for all kinds touching the role's permission folders.
- Inherits MORE strict policy on: `policy-change` (the Builder may never originate one — Atlas does), `new-agent` (Builder may not propose new agents), `paid-service`/`install` (any sub-stage B/C work needs explicit per-action gates).
- Identical: `code-change` within the allow-list (still per-action gates), `safe-doc-edit` pre-approved within the allow-list.

**Success metrics (30-day cadence):**
- Signal 1: ≥1 daily-view-related improvement shipped per 7-day window when there are open `daily-view`-labeled issues.
- Signal 2: 0 incidents where the Builder wrote outside its allow-list.
- Signal 3: 0 incidents where Builder originated a policy or new-agent proposal.
- Kill criterion: 14-day window with no shipped improvements AND 1+ open `daily-view`-labeled issues; OR any single incident in Signals 2/3.

## Output 6 — How Atlas should investigate and eventually fix the Paperclip API/write path

Per memory, the upstream bug: in `local_trusted` deployment mode, `POST /api/issues/:id/comments` ignores the `X-Paperclip-Agent-Id` header and resolves the actor as `actorType:"user", actorId:"local-board"`. Downstream, the `selfComment` guard at `routes/issues.ts L3264` then mis-attributes wakes, and the heartbeat reopen gate at `heartbeat.ts L8170-8176` reopens issues marked `done`/`cancelled`. Atlas has been mitigating by never marking issues `done` or `cancelled`.

David's [REVISION] explicitly asks Atlas to evaluate fixing or safely using this rather than avoiding it indefinitely. Recommendation:

### Phase 1 — Confirm the bug is reproducible and scoped (no code changes)

- Atlas writes a small repro script under `docs/atlas/runs/` (pre-approved `safe-doc-edit`) that posts a single test comment with the header set, then reads it back, confirming the actorType/actorId mismatch. Documents the exact endpoint, headers sent, response received, and the resulting comment record.
- Confirms the bug surface is *only* the comment route. Documents/issues/projects/runs APIs all behave correctly (Atlas has used them this run; documents PUT correctly attributes the agent).
- Effort: ~30 min. Approval gate: `safe-doc-edit` (pre-approved).

### Phase 2 — Propose the fix (issue + diff design, no code changes to Paperclip itself)

- Atlas opens a Paperclip issue (proposed identifier: a new issue under "AI Workspace Diagnostic Service" project or directly assigned to David) titled "Paperclip comment-route ignores X-Paperclip-Agent-Id in local_trusted mode."
- Description includes: repro, root cause analysis, proposed diff sketch (without writing actual TypeScript — Atlas does not have approval to edit Paperclip source), risk assessment.
- David decides whether to fix it himself, hand it to a Paperclip maintainer, or assign it to Atlas with a fresh `code-change` gate covering Paperclip source edits (which would be a major scope expansion — Atlas currently does not write to Paperclip's repo at all).
- Effort: ~2 hours. Approval gate: `code-change` for the issue creation (or just post on DAV-17 as a recommendation).

### Phase 3 — Live with the bug safely, OR fix it, depending on David

The DO-not-mark-done mitigation works. It costs us: spurious productivity flags (DAV-18, DAV-19), `local-board` attribution on agent comments, and confusion about who said what in long threads. None of these are catastrophic. Atlas can keep operating this way indefinitely.

If David wants the fix: the diff is small (the comment route handler should check for `X-Paperclip-Agent-Id` and resolve the actor accordingly when in `local_trusted` mode). If David wants Atlas to do the fix: that requires `code-change` on Paperclip source, which is a new scope and a bigger gate than anything else we've approved so far.

If David wants to live with the mitigation: we should add a small `[ATLAS-NOTE]` automation that, when the productivity-monitor flags fire on a known-loop-mitigated issue (DAV-1, any future `[DELIVERABLE]`-shipped issue still at `in_progress`), Atlas auto-posts a one-line `[STATUS]` referencing the persistent false-positive memo. This reduces the human cost of the mitigation. Effort: ~1 hour, `code-change` gate.

**My recommendation:** Phase 1 and Phase 2 immediately (they're cheap and they generate the artifact David needs to make a decision). Phase 3 deferred until David picks a path. None of this needs to happen this wake.

## Output 7 — Exact next approval request

The smallest possible next gate. Keeps momentum but stays narrowly scoped to design-stage work, no implementation:

```
[APPROVAL-REQUEST]
kind:           bundle
bundle_kinds:   policy-change, code-change
what:           Stage 3a — session-workflow design durable + storage scaffold. Promote this design memo
                to docs/atlas/davidos-session-workflow-v0.md. Add docs/sessions/{drafts,submitted,offline-queue}/
                folders with READMEs. Update memory-curation-policy-v0.md with the §"docs/sessions/" rules.
                Update comment-conventions-v0.md to add five new tags ([SESSION START], [SESSION END],
                [SESSION-START-RESPONSE], [SESSION-DEBRIEF]) and one new approval-kind (offline-work)
                in approval-policy-v0.md. Add four templates under docs/atlas/templates/.
why:            Lock in the vocabulary and storage rules from David's [REVISION] before any executable
                code is written. This is the same shape as the Stage 1 documentation/policy bundle —
                docs and policy only, no scripts, no installs, no schedules.
risk:           reversible
reversibility:  git revert of the single commit. No runtime side-effects. Drafts folder being empty is
                safe.
expected_cost:  $0
proposed_action: commit ~12 files (3 folder READMEs, 4 templates, 1 design memo promoted, 3 policy file
                edits) in a single commit titled "Stage 3a: session-workflow design and storage scaffold
                (DAV-17)".
```

After Stage 3a is committed, the *next* request would be Stage 3b — `scripts/session.py` and the renderer update — under a separate `code-change` gate. We don't ask for that yet.

Specifically NOT in Stage 3a (each its own future gate):
- `scripts/session.py` (Stage 3b — `code-change`).
- Renderer update for session banners + offline-queue surfacing (Stage 3c — `code-change`).
- Any localhost HTTP endpoint (sub-stage A — `code-change`).
- Any Tailscale/Caddy work (sub-stage B — `install` + `paid-service`).
- Hosted on the unused domain (sub-stage C — multiple gates).
- Daily Operating View Builder agent commission (deferred per output #5).
- Paperclip API repro / fix issue creation (output #6 Phase 1-2 — `safe-doc-edit` + `code-change`).

Atlas may interleave the Paperclip-API-investigation Phase 1 file (output #6) with Stage 3a if David approves both in the same comment, but not unilaterally.

## Where this leaves us

David asked for a design / recommendation, no implementation. This memo is the design. The next move is David's:

- Approve the Stage 3a bundle as-is → Atlas writes the durable docs and policy edits.
- Modify the design first → Atlas iterates this memo.
- Reject the whole shape → Atlas regroups.

Run control: nothing executed this wake beyond writing this memo to disk and (separately) attaching it as a Paperclip document on DAV-17. DAV-17 status remains `in_progress`. No other issues touched. The previously-approved Stage 1 (commit 7170ce0) and Stage 2 (commit 5c63fae) work remains durable; this memo extends but does not modify either.
