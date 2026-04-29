# TempoFastlane Example Prompt

```text
Use $tempofastlane for this bounded implementation.

Goal:
Implement <slice> while keeping the parent responsible for architecture,
integration, hardening, and final proof.

Temporal calibration:
- Phase guess: <GEN|IO|DBG|PAR>
- Inherited estimate Tp: <state if useful>
- Corrected estimate Tc: apply the current alpha(phi) prior
- Record measured Te per phase in the handoff if feasible

Ownership:
- Owned files: <paths>
- Forbidden surfaces: <paths or modules>
- Do not commit, push, or rewrite unrelated code.

Proof:
- Legacy path still works: <command and expected signal>
- New path is forced: <command/setup and expected signal>
- If proof cannot be causal, provide a structural diff snapshot.

Handoff:
Return changed files, commands, proof fields/log lines, limitations,
already-dirty files, Te measurements, and whether this run revealed a reusable
TempoFastlane improvement.
```
