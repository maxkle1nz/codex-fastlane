#!/usr/bin/env python3
"""Validate the Fastlane skill repo without third-party dependencies."""

from __future__ import annotations

import json
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
REQUIRED_SKILLS = {
    "fastlane": "Fastlane",
    "tempofastlane": "TempoFastlane",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: pathlib.Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing required file: {path.relative_to(ROOT)}")


def parse_frontmatter(path: pathlib.Path) -> dict[str, str]:
    text = read_text(path)
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)} must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(f"{path.relative_to(ROOT)} must close YAML frontmatter")

    raw = text[4:end]
    fields: dict[str, str] = {}
    current: str | None = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        match = re.match(r"^([a-zA-Z_][a-zA-Z0-9_-]*):\s*(.*)$", line)
        if match:
            current = match.group(1)
            value = match.group(2).strip()
            if value in {">-", "|-"}:
                fields[current] = ""
            else:
                fields[current] = value.strip('"').strip("'")
            continue
        if current and line.startswith("  "):
            fields[current] = (fields[current] + " " + line.strip()).strip()
            continue
        fail(f"unsupported frontmatter line in {path.relative_to(ROOT)}: {line}")
    return fields


def validate_skill(name: str, display_name: str) -> None:
    skill_dir = ROOT / "skills" / name
    if not skill_dir.is_dir():
        fail(f"missing skill directory: skills/{name}")

    frontmatter = parse_frontmatter(skill_dir / "SKILL.md")
    if frontmatter.get("name") != name:
        fail(f"skills/{name}/SKILL.md has wrong name")
    if not frontmatter.get("description"):
        fail(f"skills/{name}/SKILL.md needs a description")

    agent_yaml = read_text(skill_dir / "agents" / "openai.yaml")
    for needle in [
        f'display_name: "{display_name}"',
        "short_description:",
        "default_prompt:",
        "allow_implicit_invocation:",
    ]:
        if needle not in agent_yaml:
            fail(f"skills/{name}/agents/openai.yaml missing {needle}")

    for ref in ["case-notes.md", "delegation-template.md"]:
        if not (skill_dir / "references" / ref).is_file():
            fail(f"skills/{name}/references/{ref} is missing")


def validate_plugin() -> None:
    manifest_path = ROOT / ".codex-plugin" / "plugin.json"
    try:
        manifest = json.loads(read_text(manifest_path))
    except json.JSONDecodeError as exc:
        fail(f".codex-plugin/plugin.json is invalid JSON: {exc}")

    if manifest.get("name") != "codex-fastlane":
        fail(".codex-plugin/plugin.json name must be codex-fastlane")
    if manifest.get("skills") != "./skills/":
        fail(".codex-plugin/plugin.json must point skills to ./skills/")
    prompts = manifest.get("interface", {}).get("defaultPrompt", [])
    if len(prompts) > 3:
        fail("plugin defaultPrompt must contain at most 3 entries")
    for prompt in prompts:
        if len(prompt) > 128:
            fail(f"plugin defaultPrompt entry exceeds 128 chars: {prompt}")


def main() -> None:
    backups = list(ROOT.glob("skills/**/*.bak*"))
    if backups:
        fail("backup files found under skills/: " + ", ".join(str(p) for p in backups))

    for name, display_name in REQUIRED_SKILLS.items():
        validate_skill(name, display_name)
    validate_plugin()
    print("Fastlane skill repo validation passed.")


if __name__ == "__main__":
    main()
