# Atlas Comment-Tag Conventions — v0

**Status:** Draft. Promote to durable on David's `[APPROVAL: policy-change]`.
**Authority:** This file defines the canonical comment-tag taxonomy used by Atlas (and by any future project-lead agent) on Paperclip issue threads. It is the contract that lets David scan threads in seconds and lets heartbeat / parser logic detect approvals without parsing prose.

## 1. Why tags

Free-form comments produce low-signal threads — David has to read every word to find the one approval, the one blocker, the one deliverable. Structured tags let David and Atlas both scan an issue and answer "what's pending here?" in under 30 seconds. Tags also let downstream automation (heartbeat parser, Daily Operating View renderer) detect specific events without prose-parsing.

## 2. The tag set

Sixteen tags, lowercase-bracketed, always at the very top of the comment body.

| Tag | Who posts | Purpose |
|---|---|---|
| `[STATUS]` | Atlas | Status update during a long-running issue. Includes Hermes session ID. No action requested. |
| `[QUESTION]` | Atlas | Atlas needs information from David before proceeding. Includes a single concrete question. |
| `[RECOMMENDATION]` | Atlas | Atlas proposes a course of action. Not a request — David may ignore. |
| `[APPROVAL-REQUEST]` | Atlas | Atlas needs an explicit approval before continuing. Body MUST follow the structured block in §3. |
| `[APPROVAL: <kind>]` | David | David grants approval of the matching kind. Comment may otherwise be empty or include constraints/notes. |
| `[REJECT]` | David | David rejects the most recent `[APPROVAL-REQUEST]` on this issue. Comment may include reason. |
| `[DEFER: <YYYY-MM-DD>]` | David | David defers the most recent `[APPROVAL-REQUEST]` until the named date; Atlas re-surfaces it on or after that date. |
| `[REVISION]` | David | David provides scope or direction changes mid-issue. Atlas treats as instruction. |
| `[DELIVERABLE]` | Atlas | Final output for the issue is shipped. Memo / plan / decision attached as document. |
| `[BLOCKER]` | Atlas | Atlas is blocked and cannot proceed. Includes what's blocking and what unblocks it. |
| `[PROMOTION-REQUEST]` | Atlas | Atlas requests promotion of a `raw/` file to `wiki/`, or `output/` to `archive/` early. |
| `[ATLAS-NOTE]` | Atlas | A non-urgent observation appended to a thread or daily note. Like a margin note. |
| `[ALERT]` | Atlas (or system) | Something needs David's attention right now. Cost spike, heartbeat-loop detected, runtime failure. |
| `[SESSION START]` | David (via `scripts/session.py start`) | Marks the start of a working session. Body is the Session Start Submission (top-of-mind, decisions, questions, ideas, considerations). Posted on the session-tracker issue. |
| `[SESSION-START-RESPONSE]` | Atlas | Atlas's response to the most recent `[SESSION START]`. Schema in `davidos-session-workflow-v0.md` §9. |
| `[SESSION END]` | David (via `scripts/session.py end`) | Marks the explicit end of a working session. Body MAY include David's optional notes; empty is valid. Posted on the session-tracker issue. |
| `[SESSION-DEBRIEF]` | Atlas | Atlas's eight-section debrief produced ALWAYS in response to a `[SESSION END]`, regardless of whether David provided notes. Schema in `davidos-session-workflow-v0.md` §8. |
| `[SESSION-START-CORRECTION]` / `[SESSION-END-CORRECTION]` / `[SESSION-DEBRIEF-CORRECTION]` | David or Atlas | Correction to the immediately-prior session artifact (whose file under `docs/sessions/submitted/` is immutable). Cites the corrected line(s) and the fix. |

## 3. Structured block for `[APPROVAL-REQUEST]`

Every `[APPROVAL-REQUEST]` comment must include this six-line structured block immediately after the tag, before any free-form prose. The format lets David approve or reject in seconds and lets parser logic match request → approval reliably.

```
[APPROVAL-REQUEST]
kind:           <one of: code-change | policy-change | install | paid-service | credential | production | irreversible | new-agent | wiki-promotion | wiki-edit | archive-promotion | offline-work | bundle>
what:           <one-line description of the action>
why:            <one-line justification>
risk:           <reversible | low | medium | high | irreversible>
reversibility:  <how to undo it, or "irreversible — explain in body">
expected_cost:  <$0 | $X one-time | $X/month recurring | n/a>
proposed_action: <the exact command, file edit, install, or sequence Atlas will execute on approval>
```

Free-form prose (rationale, alternatives considered, diff snippets) goes BELOW this block.

## 4. Pairing rules

- An `[APPROVAL-REQUEST]` is "pending" until a matching `[APPROVAL: <kind>]` or `[REJECT]` appears later in the same thread. The Daily Operating View "pending approvals" section lists every pending request system-wide.
- `[APPROVAL: <kind>]` matches the most recent unmatched `[APPROVAL-REQUEST]` with the same `kind` on the same issue. If multiple requests of the same kind are pending, David must reference one explicitly (e.g. `[APPROVAL: code-change] (re: comment 4f12...)`).
- Approval is **never** inferred from passive non-objection, from agent-turn continuation, or from David replying with substantive feedback that does not include the bracketed tag. Atlas requires the literal tag to act.
- A `[REJECT]` closes the request without action. Atlas may post a revised `[APPROVAL-REQUEST]` afterwards.
- A `[DEFER: <YYYY-MM-DD>]` closes the request without action and tells Atlas to re-surface it (as a fresh `[APPROVAL-REQUEST]` with the same scope) in the Daily Operating View on or after the deferred-until date.

### 4.1 Session-tag pairing rules

- `[SESSION START]` and `[SESSION END]` are posted only by `scripts/session.py {start,end}` (Stage 2.6+) on the dedicated session-tracker issue. Until that script lands, they may be posted manually by David but always with the same body shape (per the templates in `docs/atlas/templates/session-{start,end-notes}-template.md`).
- A `[SESSION START]` is "open" until the next `[SESSION END]` on the same issue. Only one session may be open at a time. If a `[SESSION START]` arrives while one is already open, Atlas posts a `[SESSION-START-CORRECTION]` flagging the missing `[SESSION END]` and treats the new start as auto-ending the previous session with empty notes.
- Atlas MUST respond to every `[SESSION START]` with exactly one `[SESSION-START-RESPONSE]` and to every `[SESSION END]` with exactly one `[SESSION-DEBRIEF]`. The Debrief is produced regardless of whether David provided notes — David's notes are optional, the Debrief is not.
- `[REVISION]` is paired with the most-recent in-flight scope on the same issue. Atlas treats the revision as instruction immediately; the response goes in a `[STATUS]` or `[DELIVERABLE]` (not a new `[SESSION-START-RESPONSE]`).

## 5. Bundled approvals (David's DAV-17 §2 modification)

Stage 1 (documentation/policy bundle) may be approved as a single `[APPROVAL]` covering multiple low-risk changes. To enable this, an `[APPROVAL-REQUEST]` may use `kind: bundle` with a `bundle_kinds` field listing the constituent kinds, and the body must include the full diff summary inline so David can verify scope.

```
[APPROVAL-REQUEST]
kind:           bundle
bundle_kinds:   policy-change, code-change
what:           Stage 1 documentation/policy bundle (folders, READMEs, 4 policy files, 4 templates)
why:            <reason>
risk:           reversible
reversibility:  git revert
expected_cost:  $0
proposed_action: commit the diff below; no installs, no runtime config, no schedules
```

Bundles are explicitly limited to: documentation, policy drafts, templates, and folder/README scaffolding — i.e. work that is reversible by `git revert` and has no runtime side-effects. Installs, credentials, paid services, runtime/provider changes, scheduling, and new-agent creation may NEVER be bundled.

## 6. Self-amendment

Atlas may propose changes to this convention file via `[APPROVAL-REQUEST] kind: policy-change`. David approves or rejects. The file is versioned by filename suffix (`-v0`, `-v1`); no overwrites.

End of file.
