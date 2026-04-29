# Proof Contract Example

This is an illustrative proof contract for a Fastlane handoff. It shows the
shape of evidence the parent should require before accepting a worker lane.

Do not treat the values below as benchmark data. Replace them with measured
commands, artifacts, and `Te` values from a real run.

## Scenario

The parent delegates a bounded validation patch to `gpt-5.3-codex-spark`.

Goal:

- preserve the existing validation path;
- add a new invalid-input guard;
- prove the new guard ran instead of relying on legacy success.

## Parent Lane Contract

Owned files:

- `src/validator.ts`
- `tests/validator.test.ts`

Forbidden surfaces:

- public API names;
- generated artifacts;
- package manager metadata.

Verification commands copied from repo scripts:

```bash
npm test -- validator
npm run typecheck
```

Proof requirements:

- legacy valid input still passes;
- invalid input exercises the new guard;
- test output or proof artifact names the new error code;
- worker reports already-dirty files before its patch.

## Worker Handoff Shape

```text
Files changed:
- src/validator.ts
- tests/validator.test.ts

Already dirty before work:
- README.md

Commands run:
- npm test -- validator: passed
- npm run typecheck: passed

Proof artifact:
- tests/validator.test.ts

Proof signal:
- rejects invalid input with error.code = "INVALID_LANE_INPUT"
- legacy valid input still returns ok = true

False-positive risk checked:
- the new test forces the invalid-input branch;
- the legacy success path cannot satisfy the new assertion;
- no snapshot or fixture masks the new guard.

Measured Te:
- GEN: 42s
- IO: 18s
- DBG: 1m12s
```

## Parent Acceptance

The parent accepts only after independently checking the diff and rerunning the
commands. The key question is not "did tests pass?" but "what proves the new
path ran?"

If no runtime path exists, use a structural diff snapshot instead:

- public signature before/after;
- exported API list before/after;
- fixture shape before/after;
- generated contract before/after.
