# Durable autoresearch principles

Scope: Cross-domain principles that survived comparison across autonomous research systems, trading competitions, and GPU-backed optimization.
Case-study basis: All published reports under `case-studies/`.
External-review basis: `external-review/README.md`.
Synthesis dependencies: `trading-competitions.md`, `gpu-optimization.md`, and `agent-search-retrospective.md`.

## Research authority

- Freeze the evaluator, data contract, resource budget, allowed edit surface, and promotion rules before search.
- Keep the evaluator and integrity checks outside the worker's writable environment.
- Let workers propose and measure. Give one explicit judgment owner responsibility for promotion, family closure, and evaluator audits.
- Use deterministic code, not an LLM judgment, as the final authority wherever the outcome can be mechanically checked.
- Use multi-model panels as independent diagnostic participants, not voting committees. Give each route the same frozen primary evidence in a separate session, preserve its trajectory, and synthesize only after collection.
- Allocate model routes by observed role rather than one aggregate score. Track protocol compliance, distinct causal hypotheses, verified catches, latency, and cost separately.
- Treat unconstrained optimization as a ceiling and expressivity diagnostic unless it is explicitly authorized to control the product. When authored or interpretable policy matters, declare the higher-level decisions an optimizer must preserve and test those invariants exactly.
- Freeze the interface experienced by an evaluator separately from optional diagnostic instrumentation. Criticism of a machine-oriented report is not automatically evidence about the intended product experience.

## Experiment transactions

- Start every experiment with a mechanism, one declared causal factor, a baseline, a success gate, a failure gate, and a wall-time or compute limit.
- Falsify the premise with the cheapest valid counterfactual before adding complexity.
- Change one causal factor unless an interaction is the declared hypothesis.
- Do not assume that one-factor improvements compose. Before promoting a combined recipe, run the cheapest crossed cell that tests the interaction and retain the simpler incumbents.
- Record the exact patch, effective configuration, code and data hashes, result, failure layer, decision, and runtime.
- Treat unknown options, ignored configuration, stale artifacts, and evaluator mismatches as hard failures.
- Treat premise-sensitive loaded settings as experimental inputs. If a provisional value is replaced by an observed one, replay a compact unchanged representative set before continuing search and preserve earlier artifacts under their original configuration.
- A scenario label binds the complete effective configuration. Reuse an old artifact under changed settings only when behavior is invariant and every affected term can be reconstructed from persisted sufficient statistics; otherwise rerun the scenario.

## Discovery and promotion

- Label discovery and promotion runs before execution. Discovery evidence cannot silently become promotion evidence.
- Use fixed failures as causal microscopes, not promotion surfaces. After a motivating case, test a preregistered ring of adjacent cases before the representative population or sealed gate.
- Keep discovery, adaptively reused internal validation, sealed promotion, and deployment authorization as distinct states. A pass label should identify both its evidence source and the authority that issued it.
- Keep checkpoint selection, adaptive incumbent selection, and sealed promotion as distinct authorities when they answer different questions. A training surrogate may select a checkpoint and a reused operational gate may guide search, but final promotion requires untouched or multiplicity-aware evidence.
- Treat architectural or interface compatibility as an engineering gate, not evidence of positive transfer. A transfer-benefit claim needs matched source-initialized and scratch controls under the same budget, seeds, stopping rule, and evaluator.
- Search broadly through isolated branches, diverse mechanisms, and occasional fresh starts.
- Promote narrowly through untouched confirmation data, fresh processes, realistic costs, and predeclared regression limits.
- Preserve promising stepping stones when greedy keep-or-revert would erase useful diversity.
- Count failed, discarded, and correlated variants in the search burden rather than reporting only survivors.

## Research memory

- Resume from structured external state, not a growing chat transcript.
- Keep an append-only experiment ledger and a concise curated synthesis of breakthroughs, exhausted families, exclusions, and unresolved questions.
- Preserve negative results so later workers do not repeat them.
- Record a negative result's failure layer, surrounding structure, and named reopening condition. Close equivalent retries, but reconsider the mechanism when a prerequisite that changes its predicted cost or behavior has materially changed.
- Deduplicate exact patches and compare behavioral signatures so repeated discovery is not mistaken for independent confirmation.
- Compare compiled structures, reachable branches, and canonical behavior traces before treating differently named policies as independent evidence. Semantic variety that collapses to the same behavior cannot diagnose a mechanism.
- Share accumulated takeaways during exploitation cycles, but use blinded fresh-start cycles to test for anchoring.

## Evidence lifecycle

- Bind practitioner findings to their observation window, model route, evaluator authority, and harness capabilities.
- Treat a major infrastructure change as a possible scope break. Rerun the cheapest relevant counterfactual before applying an older negative result to the new system.
- Newer evidence does not win by date alone. Prefer evidence with stronger controls, closer workload match, clearer causal attribution, and independent confirmation.
- When newer controlled evidence conflicts with an older observation, mark the older lesson superseded, narrowed, or still unresolved rather than silently averaging them.
- Do not use behavior observed under manual sessions, worker-writable evaluators, uncontrolled workloads, or missing ledgers as a current capability claim after those limitations have been removed.

## Measurement and diagnosis

- Match validation to the actual uncertainty: timing noise, stochastic seeds, temporal dependence, distribution shift, execution realism, or agent variance.
- When a learned component influences the targets or states it later consumes, gate on representative outer-loop utility and behavioral diversity. Better fit to self-generated targets can accompany a narrowing or degenerate behavior distribution.
- Measure evaluator resolution separately from validity and difficulty. Discovery needs enough dispersion near current candidate ability, while promotion remains tied to the declared target and untouched evidence.
- Verify workload identity before estimating timing variance. Repeated timings measure one runtime distribution only when setup, operation mix, outputs, and relevant stochastic progression describe the same work.
- Report distributions and protected-case regressions rather than a single best aggregate score.
- Require exact output parity only when the declared mechanism promises unchanged semantics. For semantics-affecting changes, use a frozen operation-specific quality contract, protected-case limits, deterministic reruns, and recorded adjudication of every new disagreement.
- Attribute failure to one layer before editing. If a model remains calibrated while realized performance fails, investigate execution before changing the model.
- When transfer fails at an interface or safety boundary, replay the exact leading transaction in both environments before changing the boundary. Persist the inputs actually delivered after safety handling, plus timing and artifact identity, rather than only the model's proposed inputs.
- Verify the effective loaded configuration, executable or artifact hash, evaluator hash, and workload manifest in every result.
- When a comparison crosses both an artifact change and a runtime change, first rerun the unchanged artifact on the new runtime. Use the remaining crossed cell if that bridge does not isolate the responsible layer, and bind every cell to executable, artifact, and effective-configuration identity.
- When a component is consumed by an outer loop under a fixed resource budget, select on end-to-end utility in the representative data regime. Per-call quality, throughput, arithmetic count, surrogate loss, and work completed are diagnostics unless they have been shown to preserve the same ranking.
- When candidates will share capital, capacity, inventory, risk, or another finite resource, replay them together under that shared constraint. Independent component results can explain mechanisms but cannot establish the feasible combined outcome.
- For stateful or stochastic software, place the correctness gate at the smallest complete transaction after which all externally relevant outputs, state, ordering effects, and stochastic position can be compared. Local parity alone may miss downstream semantic changes.
- Use AI evaluators as inexpensive probes of language precision, available controls, evidence legibility, and theory revision. Treat cross-family disagreement as a reason to test the failure layer, and agreement as a triage signal rather than validation. Do not treat predictions of human understanding, usability, enjoyment, or retention as human evidence.
- Treat absence from a bounded, paginated, cached, or locally centered view as unknown rather than novel. Expand or recenter the query before spending resources on an inferred boundary.

## Search policy and stopping

- Optimize information gained per constrained resource, not raw experiment count.
- Before scaling a component's compute budget, verify that its improved output reaches the optimized objective with enough weight and fidelity to matter. When another intervention changes that information path, retest the budget as an explicit interaction.
- Treat an unexpected compute or throughput windfall as budget for more falsification, protected-case validation, and shorter feedback cycles. It does not increase confidence in a downstream scientific claim unless speed is part of the declared semantic mechanism.
- Prefer targeted falsification and bounded sweeps to endless local parameter tuning.
- Build infrastructure only for a named experiment that cannot otherwise run. State the missing capability, implement the smallest valid bridge, and keep infrastructure progress separate from evidence for the hypothesis.
- Before automating a presentation layer, trace one representative action to its semantic transaction and compare postconditions. A browser may host a required transport without being the correct action API.
- After two failed interventions at one gate, audit the premise and require a new hypothesis.
- Turn a premise audit into a discriminatory test tree where possible. Test evaluator and task feasibility, representation, data or visited-state coverage, and optimization before returning to local parameters, while recording what each diagnostic can and cannot prove.
- Before rejecting a search architecture after repeated pruning failures, run the cheapest matched full-breadth or high-recall control that fits the budget. If it works, treat frontier recall and downstream evaluation as separate hypotheses.
- Stop a family when independent variants fail, gains remain below the noise floor, or improvements only transfer to benchmark-specific cases.
- When quality is non-monotonic, treat run length and checkpoint choice as adaptive search decisions. Predeclare collapse and recovery rules, retain the complete curve, and confirm the selected checkpoint on untouched or multiplicity-aware evidence.
- Reset from scratch when accumulated complexity plateaus without ablation-supported value.
- Do not promote merely because the budget is exhausted or a public score looks favorable.

## Operational validation

- Test the orchestration machinery with deliberate failures before unattended campaigns: timeout, crash, malformed output, stale cache, interrupted build, and resume.
- Treat acknowledgement, operation start, terminal event, and changed postcondition as separate authorities. Bind completion to the newly observed operation identity and use state polling only when the transition is unique and the read is fresh.
- Bound processes, clean up orphans, isolate mutable state, and restore a known baseline after failure.
- For stateful external automation, authorize each action from an observed source state and represent optional or transient branches explicitly. Time may bound a wait but must not establish readiness; unknown states should fail closed with captured evidence.
- Give intrusive instrumentation separate semantic and scheduling contracts. A read-only probe can still deadlock or perturb its target, so declare safe observation conditions, control-signal behavior, timeouts, detach semantics, and an observation-only counterfactual before granting it authority.
- Treat evaluator complexity as trusted-computing-base growth. Prefer runner-owned fixed programs, closed input schemas, single-open artifact verification, exact environment binding, and finite checks on raw and derived values. Repeated integrity escapes should trigger simplification rather than another local check.
- For stateful agent evaluations, include task-private mutable provider state, exact terminal session identity, and the complete tool trajectory in the integrity contract. Fail closed on resume mismatch or forbidden tool use, and never retroactively promote a noncompliant run.
- Serialize evaluation where shared resources would distort measurements.
- Give parallel external transactions exclusive observation lanes or identity-safe demultiplexing. Independent targets are not independent measurements when workers can consume one another's events.
- When production and research share a stateful accelerator, let the production scheduler admit research as a bounded lowest-priority transaction. One authority should own admission, deadlines, cleanup, and restoration; repository isolation or a file lock does not establish device ownership.
- Give unattended campaigns a work-conserving contract: while a valid bounded experiment can run on available evidence, select, execute, and record the next batch. Waiting requires a named blocked gate and proof that no useful experiment can proceed without contaminating protected evidence.
- Monitor campaign progress separately from service and process health. A healthy unattended campaign has a recent ledgered result, valid queued or running work, or a named blocked gate; a live idle process is not evidence of continuing research.
- Prove at least one rejection, one neutral result, and one valid promotion end to end before starting a long campaign.
