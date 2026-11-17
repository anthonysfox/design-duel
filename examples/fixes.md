# Fix log: linkly

| Fix | Priority | Status | Where | Why it matters | Found in | Added |
| --- | --- | --- | --- | --- | --- | --- |
| Move click counting out of the redirect path into batched writes | High | To do | src/routes/redirect.ts, src/db/clicks.ts | Every redirect locks the same row, so a viral link slows down every visitor | Design Duel D2 | 2026-11-12 |
| Return 404 instead of 500 when a code isn't found | Medium | Done | src/routes/redirect.ts | Unknown codes currently crash the handler and page the on-call | Design Duel D1 | 2026-11-12 |
| Never reuse codes from expired links | High | In progress | src/db/links.ts, migrations/ | A recycled code sends old shared links to a stranger's URL | Design Duel D3 | 2026-11-13 |
| Remove the unused `hash` column | Low | To do | migrations/, src/db/schema.ts | Left over from an earlier design and never read | Design Duel D1 | 2026-11-12 |
