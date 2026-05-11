# Parking Lot

Initialized from `docs/atlas/templates/parking-lot-template.md` (Stage 2.6).

Each entry is a single bullet line: `- <YYYY-MM-DD HH:MM> | <category> | <text>`

Categories: `idea` | `question` | `concern` | `consideration` | `observation`.

---

## David

(David's items. Free-form append. David may also tag items `[promote: <destination>]` to suggest routing — Atlas surfaces these in the next Session Debrief's promotion-candidates section.)

## Atlas

(Atlas-authored items. Each entry must include the originating context in the text — e.g., a wake-id, an issue reference, or "from session 2026-05-12T09-00 debrief". Atlas-submitted items are SUGGESTIONS only; never durable memory or active work without explicit `[APPROVAL: <kind>]`.)

## Other agents

(Items submitted by agents other than Atlas. Each agent gets its own H3 subsection with its slug, e.g.:

### daily-view-builder

- 2026-05-15 14:32 | observation | <text>

These are also suggestions only.)

---

Filtering rules:

- David reads "mine only" by viewing only `## David`.
- Daily Operating View renderer (Stage 2.6+) offers a per-source filter so all four views (David / Atlas / Other agents / All) are one click apart.
- Atlas does not move items between sections. If an item needs re-attribution, the original entry stays and a corrective note is appended.

Promotion:

- Items are promoted via the Session Debrief's `## Promotion candidates` section, batched per session, approved with `[APPROVAL: bundle]` (or `[REJECT]` per item via inline annotations). Atlas executes approved promotions and removes the corresponding lines from `parking-lot.md`. Deferred items get a `[deferred-until: YYYY-MM-DD]` tag.
