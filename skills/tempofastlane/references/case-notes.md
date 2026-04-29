# TempoFastlane Case Notes

Use this file for reusable lessons observed across TempoFastlane runs. Keep it
universal: no private repo names, no one-off paths, no domain-specific memories.

## Initial Temporal Calibration Note

Workers and parent agents often inherit human-scale planning estimates from
training text. Treat those estimates as `Tp`, not as truth. Before choosing
medium versus xhigh, classify the phase and compute a corrected `Tc`.

**Lesson:** fast generation is not automatically low risk. `GEN` may be cheap
and suited to medium, while a small-looking `DBG` task can deserve xhigh because
parent rework risk is high.

## Integration Gate Note

Fast worker patches often complete the owned slice but omit adjacent wiring:
CLI command registration, schema exposure, fixture updates, docs hooks, adapter
registration, or proof-artifact plumbing.

**Lesson:** the parent gate must include a wiring and hardening pass before
accepting a worker patch.

## Proof-Speed Note

A smoke test that completes quickly is not suspicious by itself. Speed is a
wall-clock measurement correcting TIB. The parent should reject proof only when
the causal signal is weak, masked, or absent.

**Lesson:** evaluate proof content, not duration.

## Update Hygiene

Add a new note only when the pattern appears across runs or is clearly reusable
across repositories. If the lesson should change the protocol itself, propose a
single skill update instead of accumulating duplicate notes.
