# Fastlane Example Prompt

```text
Use $fastlane for this bounded implementation.

Goal:
Add the missing validation for <feature> without changing the public API.

Parent constraints:
- Parent owns architecture, final integration, and acceptance.
- Worker owns only the files listed below.
- Do not commit, push, or edit unrelated files.

Owned files:
- <path>
- <path>

Verification:
- Use the existing repo command: <command copied from package.json/Makefile/docs>
- Legacy behavior must still pass.
- New behavior must leave a distinct proof signal: <field/log/output>.

Handoff:
Return files changed, commands run, proof artifact paths, exact proof signal,
limitations, already-dirty files, and any possible false-positive risk.
```
