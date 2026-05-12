# scripts/archive/

Archived scripts that targeted the now-frozen Paperclip API (see [ADR-003](../../docs/decisions/ADR-003-paperclip-frozen-atlas-memo-library.md)).

Files have the `.paperclip` suffix to make their unavailability obvious. Do not run.

## Files

| File | Original purpose | Why archived |
|---|---|---|
| `session.py.paperclip` | Session-start/end CLI that posted `[SESSION START]` / `[SESSION END]` comments on Paperclip issue DAV-22 | Paperclip API on `127.0.0.1:3100` no longer exists |
| `render-daily-view.py.paperclip` | Generated `docs/daily/today.{md,html}` from Paperclip issue/comment state | Same |
| `session-config.json.paperclip` | Config: Paperclip API base URL, session tracker issue ID, Atlas agent ID | All values are Paperclip-instance-bound |

## Workspace-native replacements

When session lifecycle and daily-view tooling are rebuilt for hermes-workspace, the canonical location will be `scripts/` (new files, not these). Pending ADR-004 (approval mechanism) and Workspace baseline config.

Until then, the live session memo lives at [`docs/sessions/NEXT-SESSION-OPEN.md`](../../docs/sessions/NEXT-SESSION-OPEN.md).
