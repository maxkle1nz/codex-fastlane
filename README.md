# Fastlane for Codex

Fastlane is a Codex delegation system for getting more real work out of a
high-reasoning parent model by sending bounded implementation lanes to
`gpt-5.3-codex-spark`.

The parent model keeps judgment. The lane does bounded implementation. Proof
decides whether the result is accepted.

Fastlane is for Codex users who want to move beyond single-agent execution:
more lanes, faster task materialization, more proof, less avoidable rework.

## Why This Exists

High-reasoning Codex sessions are valuable. GPT-5.4 and GPT-5.5 are excellent
as parent agents because they can hold architecture, tradeoffs, integration,
and acceptance criteria. The mistake is spending that judgment on every
mechanical edit, every obvious test patch, and every bounded implementation
slice.

Fastlane turns Codex into a technical manager for its own Spark workers:

- the parent defines the mission, ownership, constraints, and proof contract;
- `gpt-5.3-codex-spark` executes a narrow lane with complete context;
- the parent reviews, hardens, integrates, and verifies before acceptance.

This matters because most agent delegation fails in two places:

- agents overestimate how long pure generation will take;
- agents accept "tests passed" even when the new path was never actually
  exercised.

Fastlane solves the proof problem with a strict delegation contract.
TempoFastlane solves the timing problem with TEMPONIZER: phase-aware
wall-clock calibration that treats measured runtime as truth.

In practice, the goal is not to make Codex reckless. The goal is to let Codex
create more lanes, earlier, with better evidence and less rework.

## Skills

| Skill | Use it when | Core idea |
| --- | --- | --- |
| `fastlane` | You want a disciplined Spark delegation workflow. | Delegate construction to `gpt-5.3-codex-spark`; centralize judgment and final proof in the parent. |
| `tempofastlane` | You want the faster, calibrated lane. | Fastlane plus TEMPONIZER, which corrects inherited time estimates with measured execution time. |

## Spark Lanes

Fastlane uses Codex 5.3 Spark in two lane modes:

- `medium`: for compact, mechanical, pattern-following work where the parent
  has already made the product, architecture, and proof-policy decisions;
- `xhigh`: for coupled implementation, generators, runtime proof, public
  behavior, or tasks where a wrong local choice would create parent rework.

Both modes get the same discipline: complete context, explicit ownership,
forbidden surfaces, repo-native commands, proof criteria, and a required
handoff. The difference is task risk, not prompt quality.

That is the speed engine. Spark can materialize bounded work quickly when the
parent describes the lane precisely and keeps acceptance centralized.

## How The System Works

Fastlane is built around one operating rule:

> Delegate construction; centralize judgment and integration.

The parent agent does not disappear. It becomes more important. It decides what
should be delegated, chooses `medium` or `xhigh`, gives the lane exact context,
prevents scope drift, and rejects weak proof.

Each lane carries:

- a baseline snapshot of the repo state;
- owned files or modules;
- forbidden surfaces;
- exact repo-native verification commands;
- a proof contract that forces the new path to leave an observable signal;
- a handoff that separates actual lane changes from pre-existing dirty files.

That is why Fastlane can make work feel faster without simply lowering the
quality bar. The system saves time by reducing wasted judgment and catching
false positives before they become parent-side rework.

## No Super Prompt Required

Fastlane also helps when you do not have the perfect "super prompt" ready.
Instead of asking the user to fully design the next implementation prompt, the
parent agent uses the protocol to inspect the repo, infer local conventions,
choose the next bounded useful lane, and turn that lane into an implementation
contract.

That claim comes directly from the skills: before spawning Spark, the parent
must inspect enough local context, capture a baseline, discover repo-native
commands, state the mission, assign ownership, define forbidden surfaces, and
set observable acceptance criteria.

Fastlane is not a roadmap oracle. If the task is still unclear, exploratory, or
impossible to isolate into a write scope, the protocol says not to delegate yet.
The promise is narrower and more useful: when the project has an implementable
next phase, Fastlane helps Codex materialize it as a lane with context,
ownership, and proof.

## Install

Ask Codex to install the calibrated lane:

```text
Use $skill-installer to install https://github.com/maxkle1nz/codex-fastlane/tree/main/skills/tempofastlane
```

Ask Codex to install the baseline lane:

```text
Use $skill-installer to install https://github.com/maxkle1nz/codex-fastlane/tree/main/skills/fastlane
```

For repo-local use, copy or symlink the skill folder into your repository:

```bash
mkdir -p .agents/skills
cp -R skills/tempofastlane .agents/skills/
```

Restart Codex if the skill does not appear immediately.

## Quick Start

Ask Codex:

```text
Use $tempofastlane for this bounded implementation. Keep the parent responsible
for architecture, final integration, and proof. Measure Te per phase if feasible.
```

Or use the simpler lane:

```text
Use $fastlane to delegate this bounded implementation slice to Spark. Keep
ownership tight and require causal proof before acceptance.
```

## What Makes It Different

Fastlane is not a prompt pack and not an "autonomous agent" claim. It is an
execution protocol for a specific moment: the parent agent has enough context
to define a bounded slice, but should not spend premium reasoning on mechanical
construction.

TempoFastlane adds the deeper layer: temporal calibration.

Language models often inherit human planning priors from training data. They
describe work in human-scale blocks: minutes, hours, long sequential phases.
Agents do not always operate on that timeline. Some phases are seconds of
generation, batched I/O, or parallel setup.

TEMPONIZER makes the agent name that difference before deciding effort,
parallelism, or whether to iterate:

- classify the work phase as `GEN`, `IO`, `DBG`, or `PAR`;
- treat the inherited estimate as `Tp`, not truth;
- compute a corrected estimate `Tc = alpha(phi) * Tp`;
- measure real execution time as `Te`;
- update future delegation choices from the wall clock.

That is the TEMPONIZER loop: estimate, execute, measure, recalibrate.

The attitude change is the product: the agent stops waiting like a human
planner and starts creating lanes from measured execution reality.

The repo is designed to make those gains measurable. Use `Te` and proof
artifacts instead of asking users to trust a speed claim.

## Proof Contract

A worker handoff is not accepted because it sounds confident. It is accepted
only when the parent can verify the causal signal.

Good proof answers:

- What proves the new code path ran?
- Which artifact contains it?
- Which field, log line, status, screenshot, or output confirms it?
- What could still be masking a false positive?
- Which files were already dirty before the worker started?

Velocity without proof is just faster drift.

See [docs/proof-example.md](docs/proof-example.md) for an illustrative handoff
shape with commands, proof signals, false-positive checks, and `Te` fields.

## Composes With m1nd And L1GHT

Fastlane becomes stronger when the parent has better structural context and
better operational knowledge.

- [`m1nd`](https://github.com/maxkle1nz/m1nd) helps the parent discover code
  structure, neighbors, impact, and risk before assigning a lane.
- [`L1GHT`](https://github.com/maxkle1nz/m1nd) keeps reusable operational
  knowledge and specs available to the parent before delegation.
- Fastlane turns that context into bounded execution with proof.

The combination is simple: discover better, delegate narrower, verify harder.

## Repo Structure

```text
.
+-- .codex-plugin/plugin.json
+-- skills/
|   +-- fastlane/
|   +-- tempofastlane/
+-- docs/
|   +-- launch-plan.md
|   +-- market-map.md
|   +-- positioning.md
+-- examples/
+-- scripts/
```

## Market Position

Most agent-skill repositories are either catalogs, domain packs, or best
practice libraries. Fastlane enters a narrower and more ownable category:

> the delegation control protocol for Codex.

See [docs/market-map.md](docs/market-map.md) for the current landscape and
[docs/positioning.md](docs/positioning.md) for the product narrative.

## Validate

Run the repo-local validator:

```bash
python3 scripts/validate-skills.py
```

If you have Codex's skill creator installed locally, you can also run:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/fastlane
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/tempofastlane
```

## Trust Posture

- No telemetry.
- No secrets.
- No background services.
- No model lock-in beyond the current Spark delegation lane described in the
  skills.
- Public claims must be backed by examples, case notes, or measured proof.

## Sources

- [OpenAI Codex skills documentation](https://developers.openai.com/codex/skills)
- [openai/skills](https://github.com/openai/skills)
- [Agent Skills standard](https://agentskills.io)
