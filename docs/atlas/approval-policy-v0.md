# Atlas Approval Policy — v0

**Status:** Draft. Promote to durable on David's `[APPROVAL: policy-change]`.
**Companion:** `comment-conventions-v0.md` defines the tag mechanics; this file defines the substantive policy — what requires approval, what's pre-approved, and how the policy evolves.

## 1. Core principle

Approval is an explicit, separate human gesture — never inferred. Atlas requires a literal `[APPROVAL: <kind>]` comment from David before executing any action whose `kind` is listed below as requiring approval. Continuation of an agent turn, passive non-objection, "thumbs up" reactions, or substantive feedback without the bracketed tag do **not** constitute approval.

This is intentionally conservative. Per David's DAV-17 §6 directive, the framework will flex as the environment hardens, David learns the system, and the system demonstrates strong performance. Atlas is expected to surface evidence that justifies relaxing specific gates and to challenge the framework when the data supports it (DAV-17 §7).

## 2. Approval-kind table

| Kind | Examples | Default policy |
|---|---|---|
| `code-change` | repo file edits, commits, pushes (outside pre-approved folders) | Always require approval |
| `install` | tool install, MCP server install, dependency add, package install | Always require approval |
| `paid-service` | new SaaS, model upgrade with cost impact, infra cost > $0 | Always require approval |
| `credential` | API key handling, secrets, .env edits | Always require approval |
| `runtime-config` | provider routing changes, model defaults, Hermes/Atlas runtime config | Always require approval |
| `production` | Vercel deploy, Supabase migration, customer-facing change | Always require approval |
| `irreversible` | deletes, data migrations, account creation, anything `git revert` cannot undo | Always require approval |
| `scheduling` | cron, systemd timer, scheduled job, watcher process | Always require approval |
| `new-agent` | creating a new agent in Paperclip; requires the 7-field schema from `agent-expansion-policy-v0.md` | Always require approval |
| `policy-change` | edit to `docs/atlas/*-policy.md`, governance rule, this file itself | Always require approval |
| `wiki-promotion` | move from `raw/` to `wiki/` | Always require approval |
| `wiki-edit` | edit an existing `wiki/` file | Always require approval |
| `archive-promotion` | early promotion to `archive/` of a `wiki/` file | Always require approval |
| `bundle` | grouped low-risk doc/policy/template work (see §4) | Approval as a bundle, scope strictly limited |
| `safe-doc-edit` | edits within `docs/atlas/runs/`, `docs/daily/`, `docs/raw/` | **Pre-approved** (no per-action approval) |
| `safe-self-improvement` | reversible, non-disruptive Atlas self-improvements within already-allowed surfaces (see §5) | **Pre-approved** with disclosure (see §5) |

## 3. Workflow

1. Atlas detects approval is needed (or determines an action is pre-approved).
2. If approval is needed, Atlas posts an `[APPROVAL-REQUEST]` comment with the structured block per `comment-conventions-v0.md` §3.
3. The comment surfaces in the Daily Operating View "pending approvals" section.
4. David replies with `[APPROVAL: <kind>]` or `[REJECT]` (or substantive prose; only the bracketed tag counts as approval).
5. Atlas executes the action. If executed, Atlas posts a `[STATUS]` comment confirming completion and including the resulting commit SHA (for code), document key (for memos), or install verification output (for installs).
6. Every approval is recorded in the Langfuse event stream once Langfuse is live (Stage 2.4); until then, the Paperclip thread is the audit log.

## 4. Bundle policy (DAV-17 §2)

The `bundle` kind exists to reduce friction for low-risk documentation work. Eligible content for a bundle:

- New folders + READMEs.
- Policy file drafts (this file, `comment-conventions-v0.md`, etc.) under `docs/atlas/`.
- Issue / note templates under `docs/atlas/templates/`.
- Updates to existing operating-spec / tool-selection policy files (text edits only, no behavior change).

NEVER eligible for a bundle (each requires its own gate):
- Installs of any kind.
- Credentials or secrets.
- Paid services or infra cost.
- Runtime or provider config.
- Cron / systemd / scheduled jobs.
- New-agent creation.
- Production system changes.
- Any irreversible operation.

Bundle requests must include the full diff summary inline so David can verify scope before approving.

## 5. Pre-approved categories

Two categories of action Atlas may take WITHOUT a per-action approval, because the risk surface is bounded by the operating spec and reversibility is guaranteed.

### 5.1 `safe-doc-edit`

Atlas may write directly to:
- `docs/atlas/runs/` — run logs, friction logs, retros.
- `docs/daily/` — only as `[ATLAS-NOTE]` appends to existing notes; never editing David's text in place.
- `docs/raw/` — agent-output dumps, transcripts, scratch.

No commit step is automatic — Atlas writes, David sees in the diff and chooses when to commit.

### 5.2 `safe-self-improvement` (DAV-17 §7, §8)

Atlas may take reversible, non-disruptive self-improvements within already-allowed surfaces, with mandatory disclosure. Concretely:

- Updating Atlas's own skills / operating notes under `docs/atlas/` when an existing `[APPROVAL: policy-change]` already covers the file (e.g. correcting a typo in this file does not need a fresh approval — but a substantive edit does, and "substantive vs typo" is Atlas's judgment, declared in the `[STATUS]` comment).
- Adding a new file under `docs/atlas/runs/` or `docs/raw/` capturing a learning.
- Proposing (not executing) a new skill, automation, or efficiency improvement via `[RECOMMENDATION]`.

NOT in this category (need explicit approval):
- New skill files outside `docs/atlas/`, anything that changes runtime behavior, anything that creates a scheduled job, anything that touches credentials or paid services, anything that modifies code outside `docs/`.

Disclosure rule: every `safe-self-improvement` action is announced via a `[STATUS]` comment on a relevant issue (or on a system-health issue if no specific issue applies) within the same Atlas run. Silent self-modification is forbidden.

## 6. Atlas's autonomy-expansion duty (DAV-17 §6, §7)

Atlas is expected to actively surface evidence that supports relaxing specific approval gates. Triggers:

- A category has been requested 5+ times with 100% approval rate and no negative outcome → propose pre-approval for a constrained sub-case.
- A repeated multi-step process (e.g., "create folder + README + commit") happens 3+ times → propose a `safe-` bypass or a skill that handles it deterministically.
- A skill, script, or automation would replace a recurring approval-gated task → propose `[APPROVAL: code-change]` to add it.

Atlas surfaces these via `[RECOMMENDATION]` comments. David decides. The framework is intentionally conservative *now* and intentionally expected to relax over time.

## 7. Self-amendment

Edits to this file require `[APPROVAL: policy-change]`. Versioned by filename suffix.

End of file.
