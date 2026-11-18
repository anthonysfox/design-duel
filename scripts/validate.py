#!/usr/bin/env python3
"""Check that the plugin files and the skill's frontmatter are valid.

Run from the repo root: python3 scripts/validate.py
Exits non-zero and prints every problem it finds.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []


def load_json(rel):
    path = ROOT / rel
    try:
        return json.loads(path.read_text())
    except FileNotFoundError:
        errors.append(f"{rel}: missing")
    except json.JSONDecodeError as e:
        errors.append(f"{rel}: invalid JSON ({e})")
    return None


plugin = load_json(".claude-plugin/plugin.json")
market = load_json(".claude-plugin/marketplace.json")

if plugin:
    for key in ("name", "version", "description"):
        if not plugin.get(key):
            errors.append(f"plugin.json: missing '{key}'")
    if plugin.get("version") and not re.fullmatch(r"\d+\.\d+\.\d+", plugin["version"]):
        errors.append("plugin.json: version must look like 1.2.3")

if market:
    names = [p.get("name") for p in market.get("plugins", [])]
    if plugin and plugin.get("name") not in names:
        errors.append("marketplace.json: doesn't list the plugin named in plugin.json")
    for p in market.get("plugins", []):
        if p.get("source") != "./":
            errors.append(f"marketplace.json: plugin '{p.get('name')}' source must be './' (got {p.get('source')!r})")

changelog = ROOT / "CHANGELOG.md"
if plugin and plugin.get("version") and changelog.exists():
    if f"[{plugin['version']}]" not in changelog.read_text():
        errors.append(f"CHANGELOG.md: no entry for version {plugin['version']}")

skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
if not skills:
    errors.append("skills/: no SKILL.md found")

for skill in skills:
    rel = skill.relative_to(ROOT)
    text = skill.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{rel}: missing frontmatter block")
        continue
    fm = dict(
        (k.strip(), v.strip().strip('"'))
        for k, v in (line.split(":", 1) for line in m.group(1).splitlines() if ":" in line)
    )
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not name:
        errors.append(f"{rel}: frontmatter has no name")
    elif name != skill.parent.name:
        errors.append(f"{rel}: name '{name}' doesn't match folder '{skill.parent.name}'")
    elif not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        errors.append(f"{rel}: name must be lowercase letters, digits and hyphens")
    if not desc:
        errors.append(f"{rel}: frontmatter has no description")
    elif len(desc) > 1024:
        errors.append(f"{rel}: description is over 1024 characters")
    elif "<" in desc or ">" in desc:
        errors.append(f"{rel}: description can't contain angle brackets")

if errors:
    print("Validation failed:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print(f"All good: plugin files valid, {len(skills)} skill(s) checked.")
