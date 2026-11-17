# Talking points: linkly

## "How did you generate the short codes?"
The problem: every long URL needs a short, unique code that never collides.
What I chose and why: an auto-incrementing ID encoded in base62. It's guaranteed unique, and six characters covers about 56 billion links.
Trade-off I accepted: codes are guessable in order, which is fine for public links but not for private ones.
What I'd change now: add a random offset or an optional random code for private links.

## "What happens when a link goes viral?"
The problem: thousands of redirects a second, and each one should count as a click.
What I chose and why: the redirect only publishes a click event. A worker batches the events and updates counts once a minute, so redirects never wait on a database lock.
Trade-off I accepted: click counts lag by up to a minute.
What I'd change now: the original code counted inline. I caught the lock contention while reviewing the design and moved it to batched writes.

## "How do expired links work?"
The problem: links can have an expiry date, and an expired link should stop working.
What I chose and why: check expiry at redirect time and return a friendly "this link expired" page.
Trade-off I accepted: expired rows stay in the database.
What I'd change now: never recycle an expired code, since old shared links would point somewhere new.
