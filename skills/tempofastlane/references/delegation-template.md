# TempoFastlane Delegation Template

Use this template when spawning a worker. Fill in repo-native paths, commands,
proof fields, and phase estimates discovered locally.

## Worker Mission

You are a bounded implementation worker. Implement only the assigned slice.
You are not alone in the codebase: do not revert unrelated changes, and adapt to
pre-existing dirty state.

## Temporal Calibration

- Expected phases: `GEN`, `IO`, `DBG`, `PAR`.
- Initial inherited estimate (`Tp`): `<state if useful>`.
- Corrected estimate (`Tc = alpha(phi) * Tp`): `<state in smallest unit that fits>`.
- Record measured execution time (`Te`) per phase in your final handoff when
  feasible.

## Baseline

- Repo root: `<absolute path>`
- Branch/status snapshot: `<git status -sb>`
- Relevant dirty files before worker starts: `<list>`
- Existing command names discovered from repo files: `<list>`

## Ownership

Owned files or modules:

- `<path or module>`

Forbidden surfaces:

- `<path or module>`
- unrelated rewrites, branch changes, commits, tags, pushes

## Implementation Goal

`<one paragraph describing the exact desired behavior>`

## Acceptance Criteria

- `<observable behavior>`
- `<proof artifact or structural diff snapshot>`
- `<legacy path still works if applicable>`
- `<new path leaves distinct proof signal if applicable>`

## Verification Commands

Run only commands copied from repo-native scripts/docs or explicitly provided by
the parent:

```bash
<command 1>
<command 2>
```

If a command fails, classify it as `code-failure`, `environment-blocker`, or
`command-error`.

## Final Handoff Required

Return:

- files changed;
- commands run and exact result;
- proof artifacts and exact fields/log lines that prove the new path ran;
- limitations or concerns;
- files already dirty before your work;
- measured `Te` per phase when feasible;
- whether this exposed a reusable TempoFastlane workflow improvement.
