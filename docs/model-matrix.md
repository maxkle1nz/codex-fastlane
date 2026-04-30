# Model Matrix

Last reviewed: 2026-04-30.

Fastlane chooses the worker that protects the parent agent's cognitive budget.
The parent may run on a frontier model such as `gpt-5.5` with high or xhigh
reasoning, but it should not spend that premium reasoning on routine code
construction when a bounded lane can do the work under contract.

## Parent Cognitive Budget Rule

The parent is the manager of the work, not the default typist.

Keep the parent focused on:

- translating the human idea into the next useful mission;
- architecture, decomposition, and risk calls;
- lane selection and model/effort choice;
- proof contract design;
- integration, hardening, and final acceptance;
- synthesis back to the human.

Delegate code construction when:

- the write scope can be owned by a lane;
- the existing pattern is discoverable;
- commands or proof artifacts can be named;
- the parent can cheaply verify the returned diff.

Let the parent write code only when the edit is smaller than the delegation
overhead, the lane cannot be isolated, or the parent is repairing an integration
gap discovered during final proof.

## Lane Router

Before spawning a Fastlane, classify the work:

| Signal | Ask |
| --- | --- |
| `scope` | Is the write set exact, narrow, and owned? |
| `risk` | Would a wrong local choice create parent rework? |
| `proof` | Can the lane leave causal evidence that the new path ran? |
| `phase` | Is the work mostly `GEN`, `IO`, `DBG`, or `PAR`? |
| `context` | Does the worker need broad repo history or only embedded context? |
| `surface` | Is this code, docs/copy, research, audit, or integration? |

Then choose the smallest capable lane. Escalate model or effort only when proof
difficulty, ambiguity, or parent rework risk demands it.

## Recommended Lanes

| Lane | Default model/effort | Best for | Avoid when |
| --- | --- | --- | --- |
| `parent` | `gpt-5.5` high/xhigh, fallback `gpt-5.4` xhigh | Human intent synthesis, architecture, decomposition, final proof, integration judgment. | Routine implementation that can be scoped as a worker contract. |
| `coder` | `gpt-5.3-codex` medium/high | Code-only implementation, focused refactors, debugging, tests, repo-native patches. | Broad product ambiguity or non-code research. |
| `spark` | `gpt-5.3-codex-spark` medium/xhigh | Near-instant text-only iteration, compact patches, fast proof fixes when Spark is available. | Tasks needing broad tool use, long context, or stable production pricing. |
| `fastworker` | `gpt-5.4` low or `gpt-5.4-mini` medium | Low-risk mechanical work, file scans, simple edits, support lanes, repeated small tasks. | Architecture, subtle proof, security, or cross-module debugging. |
| `auditer` | `gpt-5.4` high or `gpt-5.5` high | Review, edge cases, security-oriented checks, proof-gap hunting. | Pure construction where a coder lane is cheaper. |
| `researcher` | `gpt-5.5` medium/high, fallback `gpt-5.4` high | Internet research, docs verification, multi-source synthesis, benchmark updates. | Simple local repo scans. |
| `creative` | `gpt-5.4` low/medium, escalate to `gpt-5.5` for high-stakes synthesis | README copy, launch language, product framing, examples, naming, UX text. | Claims that require measurement or engineering proof. |
| `integrator` | Parent-owned; optionally assisted by `gpt-5.3-codex` high | Wiring worker patches into adjacent systems after proof review. | Replacing the parent acceptance gate. |

## Selection Rules

Use `gpt-5.3-codex` for bounded code when Spark is not needed. It is the
default `coder` lane for substantial code-only work because the model is
specialized for agentic coding, and because keeping code construction out of
the parent protects the parent session's premium reasoning budget.

Use `gpt-5.3-codex-spark` when latency matters more than breadth and the task
is compact enough for a near-instant text-only lane. Treat Spark as a research
preview lane: useful, fast, and contract-bound, but not the only Fastlane
worker.

Use `gpt-5.4` low for well-scoped tasks when speed and cost matter and the
parent has already made the decisions. Use `gpt-5.4-mini` when a separate
subagent should scan, summarize, or support the parent cheaply.

Use `gpt-5.5` for the parent or for rare worker lanes with high ambiguity,
research depth, computer use, long-context synthesis, or expensive failure
modes. Do not spend `gpt-5.5` xhigh on routine edits unless delegation overhead
would exceed the edit itself.

## Lane Record

Every Fastlane handoff should make model choice inspectable:

```text
Lane type: coder
Model: gpt-5.3-codex
Effort: medium
Why this lane: bounded code-only patch; existing pattern found; proof command exists.
Escalate if: proof gap, broad rewrite, missing architecture, or repeated guessed commands.
Tp/Tc/Te: <inherited estimate> / <corrected estimate> / <measured wall clock>
Parent cost protected: <what the parent did not spend premium reasoning writing>
```

## Evidence Discipline

Public model benchmarks guide lane defaults; they do not replace local proof.
Record per-lane `model`, `effort`, `Tp`, `Tc`, `Te`, accepted-on-first-pass,
parent rework, proof artifacts, and final acceptance outcome. Over time, this
becomes the repo's own operational benchmark.

Known limits:

- Public evals usually run in research environments and may differ from
  production Codex behavior.
- Reasoning-effort comparisons are not always published for every model.
- `gpt-5.3-codex-spark` is a research preview and its pricing is not final.
- Fastlane should never claim "best model" without a linked measurement for
  the task class.

## Sources

- [Codex Models](https://developers.openai.com/codex/models)
- [Codex Subagents](https://developers.openai.com/codex/concepts/subagents)
- [Codex Best Practices](https://developers.openai.com/codex/learn/best-practices)
- [GPT-5.3-Codex model page](https://developers.openai.com/api/docs/models/gpt-5.3-codex)
- [Introducing GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex/)
- [Introducing GPT-5.4](https://openai.com/index/introducing-gpt-5-4/)
- [Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)
- [Codex rate card](https://help.openai.com/en/articles/20001106-codex-rate-card)
