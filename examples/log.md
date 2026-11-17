# Design Duel log: linkly

## D1. Turning a long URL into a short code (2026-11-12)
verdict: tie (matched the repo's design)
struggled with: started with hashing the URL and taking the first 6 characters. The "two URLs collide" constraint moved them to a counter encoded in base62.
found on their own: base62 to keep codes short, a unique index on the code column
review: no

## D2. Counting clicks without slowing redirects (2026-11-12)
verdict: yours
struggled with: first answer was updating the click count inside the redirect request. The "viral link gets 2,000 clicks a second" constraint showed row lock contention.
found on their own: write click events to a queue and batch the counts every minute
better than the repo: yes. The repo increments the counter inline on every redirect, which locks the same row under load. Batched counting fixes it.
review: yes

## D3. Handling links that expire (2026-11-13)
verdict: repo's
struggled with: proposed a cron job that deletes expired rows. Didn't consider that a deleted code can be reissued and point an old shared link somewhere new.
found on their own: checking expiry at redirect time
review: yes

Pattern to work on: thinking about what happens under heavy load before designing the happy path.
