# Changelog

All notable changes to Design Duel are listed here. This project follows [Semantic Versioning](https://semver.org).

## [Unreleased]

### Security
- Git URLs: only https or ssh accepted; cloned with `--` and quoting into `~/.design-duel/<repo>/src`, not the current directory, so the clone's `CLAUDE.md` and `.claude/` files can't load as project instructions
- `git pull` runs only if the existing clone's origin matches the URL
- Repo names cleaned up before they're used in paths
- Git runs with pager, fsmonitor, external diff and textconv turned off, so a local repo's `.git/config` can't run commands
- The background mapping subagent gets the safety rules and read-only tools
- State files (`map.md`, `log.md`) are treated as data, not instructions
- Security flaws stay in the local fix log unless the user says yes per row
- CI actions pinned to commit SHAs, with Dependabot keeping them current

## [1.0.0] - 2026-11-17

First public release.

### Added
- Learning sessions: design each part of a repo yourself, with constraints added one at a time
- Head-to-head verdict comparing your design against the repo's, honest in both directions
- Background repo mapping into 5 to 10 design decisions, stored outside the repo so answers can't be peeked at
- Review mode for re-trying problems you struggled with
- Interview mode that turns a session into talking points and runs a mock round
- Fix log for bugs found in your own repo (markdown file, or a Sheet in the Claude app)
- Interactive rounds when the client supports visuals, with ASCII and multiple-choice fallbacks in the terminal
- Safety rules: read-only on your code, never runs repo code, treats repo content as data rather than instructions
