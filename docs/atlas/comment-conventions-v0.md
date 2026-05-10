# Atlas Comment-Tag Conventions — v0

**Status:** Draft. Promote to durable on David's `[APPROVAL: policy-change]`.
**Authority:** This file defines the canonical comment-tag taxonomy used by Atlas (and by any future project-lead agent) on Paperclip issue threads. It is the contract that lets David scan threads in seconds and lets heartbeat / parser logic detect approvals without parsing prose.

## 1. Why tags

Free-form comments produce low-signal threads — David has to read every word to find the one approval, the one blocker, the one deliverable. Structured tags let David and Atlas both scan an issue and answer "what's pending here?" in under 30 seconds. Tags also let downstream automation (heartbeat parser, Daily Operating View renderer) detect specific events without prose-parsing.

## 2. The tag set

Eleven tags, lowercase-bracketed, always at the very top of the comment body.

| Tag | Who posts | Purpose |
|---|---|---|
| `[STATUS]` | Atlas | Status update during a long-running issue. Includes Hermes session ID. No action requested. |
| `[QUESTION]` | Atlas | Atlas needs information from David before proceeding. Includes a single concrete question. |
| `[RECOMMENDATION]` | Atlas | Atlas proposes a course of action. Not a request — David may ignore. |
| `[APPROVAL-REQUEST]` | Atlas | Atlas needs an explicit approval before continuing. Body MUST follow the structured block in §3. |
| `[APPROVAL: <kind>]` | David | David grants approval of the matching kind. Comment may otherwise be empty or include constraints/notes. |
| `[REJECT]` | David | David rejects the most recent `[APPROVAL-REQUEST]` on this issue. Comment may include reason. |
| `[DELIVERABLE]` | Atlas | Final output for the issue is shipped. Memo / plan / decision attached as document. |
| `[BLOCKER]` | Atlas | Atlas is blocked and cannot proceed. Includes what's blocking and what unblocks it. |
| `[PROMOTION-REQUEST]` | Atlas | Atlas requests promotion of a `raw/` file to `wiki/`, or `output/` to `archive/` early. |
| `[ATLAS-NOTE]` | Atlas | A non-urgent observation appended to a thread or daily note. Like a margin note. |
| `[ALERT]` | Atlas (or system) | Something needs David's attention right now. Cost spike, heartbeat-loop detected, runtime failure. |

## 3. Structured block for `[APPROVAL-REQUEST]`

Every `[APPROVAL-REQUEST]` comment must include this six-line structured block immediately after the tag, before any free-form prose. The format lets David approve or reject in seconds and lets parser logic match request → approval reliably.

```
[APPROVAL-REQUEST]
kind:           <one of: code-change | policy-change | install | paid-service | credential | production | irreversible | new-agent | wiki-promotion | wiki-edit | archive-promotion>
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
