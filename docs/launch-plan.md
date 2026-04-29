# Launch Plan

## Goal

Launch the repo as a focused "delegation control protocol" for Codex skills:
installable, proof-aware, and easy to explain.

## Pre-Launch Checklist

- [ ] Confirm the publishing owner is `maxkle1nz`; update URLs if needed.
- [ ] Confirm final repo slug, preferably `codex-fastlane`.
- [ ] Run `python3 scripts/validate-skills.py`.
- [ ] Run Codex skill validation for both skill folders if available.
- [x] Add an illustrative proof contract example.
- [ ] Add one real anonymized case note showing a false-positive caught by the
      parent gate.
- [ ] Add one real anonymized TempoFastlane case note showing `Tp`, `Tc`, and
      `Te`.
- [ ] Create the GitHub repo with the recommended topics in
      [docs/positioning.md](positioning.md).
- [ ] Use a concise repo description:
      `Proof-gated Spark delegation skills for Codex, with TEMPONIZER wall-clock calibration.`

## Day-Zero README Order

1. One-line promise.
2. Why the problem exists.
3. Fastlane vs TempoFastlane table.
4. Install commands.
5. Quick start prompt.
6. Proof contract.
7. Market position.
8. Trust posture.

The first screen should answer: what is this, why does it exist, how do I use
it, and why should I trust it?

## Suggested Announcement

```text
I published Fastlane for Codex: two Agent Skills for delegating bounded
implementation work without giving up parent-side proof.

Fastlane gives Codex a strict worker delegation protocol.
TempoFastlane adds TEMPONIZER: phase-aware wall-clock calibration for `Tp`,
`Tc`, and measured `Te`.

The point is not "let the agent run wild." The point is faster bounded
construction while the parent keeps architecture, integration, and final proof.

Repo: https://github.com/maxkle1nz/codex-fastlane
```

## First Issues To Seed

- Add real-world proof artifact examples.
- Add a `Tp`/`Tc`/`Te` benchmark log template.
- Add cross-agent compatibility notes.
- Add more case notes from generator, frontend, and test-repair runs.
- Package as an installable Codex plugin once the public plugin path is final.

## Contribution Strategy

Accept contributions that improve the protocol, examples, validation, or
case-note quality.

Avoid turning the repo into a general skill catalog. Every addition should
answer at least one of these:

- Does it improve delegation quality?
- Does it reduce false-positive acceptance?
- Does it improve temporal calibration?
- Does it make installation or validation easier?

## Success Metrics

Early:

- stars from Codex users;
- issues asking for case notes or templates;
- forks installing the skills repo-locally;
- mentions in "agent skills" and Codex community lists.

Quality:

- examples include causal proof;
- no public claim exceeds available evidence;
- contributors understand the parent-gate model;
- TempoFastlane notes include measured wall-clock data when feasible.
