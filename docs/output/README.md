# output/

**Purpose:** final memos, decision records, and deliverables produced for a specific Paperclip issue. The "we shipped this" folder.

**Naming convention:** `<issue-id>-<slug>.md`, e.g. `DAV-17-v1-operating-ui-plan.md`. One file per deliverable. Versioning via filename suffix when needed (`-v0`, `-v1` — never overwrite).

**Write permission:** agents may write here directly **only when explicitly producing a deliverable for an issue**, after the deliverable has been approved as a Paperclip document (key `memo` / `plan` / `decision`). The `[APPROVAL: code-change]` for the originating issue is sufficient — no separate gate to commit the file.

**Auto-archive:** files here are eligible for automatic move to `archive/` 90 days after the originating issue closes. The Daily Operating View "memory freshness" section surfaces eligible candidates; Atlas executes the move without further approval (it's a deterministic, reversible operation logged in git).

**Out of scope here:** working drafts (use `raw/`), durable reference knowledge (use `wiki/` after promotion), Atlas's operating documents (use `atlas/`).
