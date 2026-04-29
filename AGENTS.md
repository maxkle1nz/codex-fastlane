# Repository Instructions

This repository publishes Fastlane and TempoFastlane as Codex Agent Skills.

## Public Voice

- Use maintainer language, not assistant language.
- Prefer concrete claims: bounded delegation, parent-side verification, causal
  proof, wall-clock calibration.
- Do not claim "best", "production-ready", or "faster than X" without a linked
  measurement or example.
- Treat TEMPONIZER as a public protocol concept: explain enough to be useful,
  but do not turn the README into a speculative benchmark page.

## Skill Layout

- Skills live under `skills/<skill-name>/`.
- Each skill must contain `SKILL.md`.
- Optional skill resources belong in `references/`, `scripts/`, `assets/`, or
  `agents/`.
- Do not add README files inside individual skill folders.
- Keep long examples out of `SKILL.md` when a reference file would work.

## Validation

Run before reporting a repo change complete:

```bash
python3 scripts/validate-skills.py
```

When the local Codex skill creator is available, also run:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/fastlane
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/tempofastlane
```

## Git Safety

- Do not commit, tag, push, or publish without explicit maintainer approval.
- Preserve unrelated dirty state.
- Keep public messages short, concrete, and evidence-aware.
