# Contributing

Fastlane is intentionally narrow. Contributions should improve delegated
implementation quality, proof integrity, temporal calibration, or installation.

## Good Contributions

- clearer ownership or proof gates;
- stronger anti-false-positive rules;
- reusable case notes from real runs;
- validation improvements;
- installation or plugin packaging improvements;
- examples that show causal proof.

## Out Of Scope

- unrelated coding best-practice packs;
- generic prompt collections;
- unverified performance claims;
- repo-specific memories or private project names;
- background services, telemetry, or credentials.

## Skill Change Rules

- Keep each `SKILL.md` focused and concise.
- Put detailed examples in `references/` when they are not core protocol.
- Add case notes only when the lesson is reusable across repositories.
- Do not claim a workflow is faster unless a measurement or example supports
  the claim.
- Preserve the distinction between parent judgment and worker construction.

## Validation

Before opening a PR, run:

```bash
python3 scripts/validate-skills.py
```

If available, also run:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/fastlane
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/tempofastlane
```

## Pull Request Notes

Include:

- what changed;
- why it belongs in Fastlane or TempoFastlane;
- how you validated it;
- any known limits.
