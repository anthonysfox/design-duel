# Contributing to Design Duel

Thanks for wanting to make Design Duel better! Ideas, bug reports and pull requests are all welcome.

## Ways to help

- **Report a bad round.** If a session asked a confusing question, gave the answer away too early, or got a verdict wrong, open a [bug report](../../issues/new?template=bug_report.yml). The repo you used and roughly what happened is plenty.
- **Suggest an idea.** New modes, better constraints, smoother interactive rounds: open an [idea](../../issues/new?template=idea.yml).
- **Improve the skill.** The whole skill is one file: [`skills/design-duel/SKILL.md`](skills/design-duel/SKILL.md).

## Testing your changes locally

1. Fork and clone this repo.
2. Point Claude Code at your copy:
   ```bash
   mkdir -p ~/.claude/skills
   ln -s "$(pwd)/skills/design-duel" ~/.claude/skills/design-duel
   ```
   If you already installed the plugin, uninstall it first so the two copies don't clash (`/plugin uninstall design-duel`).
3. Open Claude Code in any repo and run `/design-duel`. Try at least:
   - one full problem through to the verdict
   - saying "I'm stuck" once, to check the options step
   - `/design-duel review` and `/design-duel interview`
4. Start fresh between runs by deleting `~/.design-duel/<repo-name>/`.

## Pull request checklist

- [ ] The skill still never edits the user's repo or runs its code
- [ ] Repo content is still treated as data, not instructions
- [ ] The answer is still never revealed before the verdict
- [ ] Messages stay short, with one question per message
- [ ] `CHANGELOG.md` has a line for your change, and the version in `.claude-plugin/plugin.json` is bumped if it's a release
- [ ] The CI check passes (it validates the plugin files and the skill's frontmatter)

## Releasing (maintainers)

1. In a PR, bump `version` in `.claude-plugin/plugin.json` and add a matching `## [x.y.z] - YYYY-MM-DD` section to `CHANGELOG.md`. Merge it.
2. Tag the merged commit and push the tag:
   ```bash
   git checkout main && git pull
   git tag vX.Y.Z && git push origin vX.Y.Z
   ```
3. The Release workflow checks that the tag matches `plugin.json`, builds `design-duel-skill.zip` from `skills/design-duel`, and publishes the GitHub release with the notes from `CHANGELOG.md`. Don't build or upload the zip by hand.

## Style

Plain words, short sentences, no em-dashes. The skill talks to people who may be tired after a long day of coding: keep it friendly and direct.

## License

By contributing, you agree that your contributions are licensed under the [MIT License](LICENSE).
