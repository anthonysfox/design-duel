# Security policy

Design Duel is a set of instructions that an AI agent follows while it reads code you point it at. A problem in those instructions can let a hostile repo steer the agent, so please report it privately.

## Reporting

Use GitHub's **Report a vulnerability** button on the Security tab of this repo (private vulnerability reporting). Please don't open a public issue for security problems.

Useful to include:
- the repo or file contents that triggered the behavior (a minimal reproduction is ideal)
- what the agent did, such as running a command, fetching a URL, or writing outside `~/.design-duel/`
- the client and version you were using

## In scope

- Prompt injection from repo content, commit messages or state files that gets past the skill's safety rules
- The skill running repo code, editing the repo, or writing outside `~/.design-duel/`
- Unsafe git commands or clone handling
- Problems in this repo's CI or validation script

## Supported versions

Only the latest release on `main` gets fixes.
