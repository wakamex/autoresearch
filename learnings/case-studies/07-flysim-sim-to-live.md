# Case 07 - FlySim flight control from simulation to a live application

Observation window: 2026-07-08 through 2026-07-27
Disclosure mode: public FlySim evidence plus an authorized private transfer account
Duration: several concentrated campaigns across several weeks
Application domain: flight dynamics, reinforcement learning, and live flight-control transfer

## Scope and evidence authority

The public project is [FlySim](https://github.com/wakamex/flysim), a flight-dynamics and
reinforcement-learning system. It contains the simulator, observation and action contracts, policy
training, and reproducible simulation results. A private overlay connected frozen FlySim policies to
an unnamed external flight application through runtime observation, safety supervision, delivered-
input tracking, and bounded live tests. The overlay and live evidence remain private.

FlySim exposed four flight controls and a 185-value observation containing the current aircraft state,
recent applied controls, and delayed input. Its public JAX simulator ran physics every 5 milliseconds
and the policy every 20 milliseconds. The campaign trained policies to cross target sequences while
respecting limits on speed, tilt, height, contact, abrupt controls, and safety events.

This case is about validating the same frozen policy across simulation and a live external runtime. It
is not transfer learning where a model continues learning in the live application.

The harness changed substantially during the window. Work on 2026-07-08 and 2026-07-09 was manually
launched in a shared mutable tree. From 2026-07-10 onward, the project progressively added predeclared
gates, artifact identity, protected final evidence, and staged promotion. These boundaries were
procedural rather than technically isolated, and human judgment retained promotion authority.

## Infrastructure timeline

On 2026-07-08, the project lacked a uniform ledger, exclusion map, isolated workers, persistent
orchestration, and freshness monitoring. Discovery, confirmation, and promotion were inconsistently
separated.

From 2026-07-10 through 2026-07-12, the project added complexity guardrails, a canonical runtime path,
predeclared gates, separate selection and protected-final stages, frozen-artifact checks, fresh-process
validation, a staged sim-to-live ladder, and dependency ordering.

From 2026-07-24 through 2026-07-26, correctness, performance, and task-validity gates preceded
accelerated learning. A bounded recovery program separated diagnostic discovery from fresh promotion,
retained failed families, and required portable-artifact parity plus mechanically non-acting live
validation.

On 2026-07-27, exact-state orchestration replaced time-based readiness. Intrusive observation gained a
safe scheduling contract, an observation-only counterfactual preceded promotion, and the result
received complexity and stale-path audits.

By the end, major runs used predeclared manifests, configuration and artifact identity, explicit
evidence labels, bounded budgets, fresh-process confirmation, protected final evidence, deterministic
rejection gates, and retained negative results. Shared-resource admission, freshness monitoring, and
blocked-state handling remained manual. A 2026-08-10 review found no newer source evidence.

## Main findings

### Use extra simulation speed to test more assumptions

From 2026-07-24 through 2026-07-25, an accelerated implementation exceeded its performance requirement
while preserving declared semantics, yet the downstream learning gate still failed. Bounded campaigns
localized the problem to exploration, visited-state coverage, and convergence assumptions rather than
runtime throughput.

A speedup changes which experiments are affordable, not the credibility of a downstream claim. Spend
the windfall on independent seeds, protected cases, premise tests, or shorter iteration cycles unless
speed changes the semantic mechanism, data exposure, or deployed budget.

Current status: current as of 2026-08-10.

### After repeated failures, test the premise layer by layer

After several plausible interventions failed at the same gate, cheaper diagnostics tested task
reachability, representation, initial exploration, visited-state coverage, and convergence. Each
removed one causal layer, and the eventual intervention addressed the observed coverage mismatch.

Current status: current but workload-dependent. A successful reachability or offline-fit test
establishes only its own layer.

### Replay exactly what the live system received before loosening safety limits

On 2026-07-11, a bounded 0.5-second live handoff returned safely but clipped 14% of its control
samples. Rather than giving the policy wider control authority, the project replayed the same preceding
history and the controls actually delivered after safety filtering inside FlySim. The simulated
aircraft moved much less than the live aircraft, especially in roll and yaw, locating the failure in
the simulator's dynamics coverage rather than the adapter or safety boundary.

Only the simulator's dynamics randomization range changed. After retraining, the same live boundary
recorded zero clipping. Two later three-target live runs completed without clipped, invalid, late, or
floor-contact events and returned to a safe landing. A later full-course attempt still stopped safely,
so the campaign did not claim complete live transfer.

Persist the post-safety inputs actually delivered, timing, state, configuration, and artifact identity.
Replay can distinguish model coverage from adapter or runtime behavior, though hidden state or
nondeterminism may leave it underdetermined. Locating the layer does not identify the right replacement.

Current status: current and infrastructure-dependent as of 2026-08-10.

### Drive automation from observed state, not sleep timers

On 2026-07-27, exact state predicates replaced fixed delays. Fresh processes showed that one
intermediate state was optional. An explicit branch let the launcher omit an inapplicable action,
whereas a linear state machine could wait indefinitely or act from stale state.

Authorize each action from its observed source state, represent optional and transient branches, and
fail unknown states with a timeout and captured evidence.

Current status: current for introspectable stateful automation.

### Read-only instrumentation can still hang the system

On 2026-07-27, a semantically read-only observer could hang when invoked from an unsafe runtime
context. The corrected design restricted observation conditions, preserved runtime control behavior,
bounded attempts, detached cleanly, and passed observation-only tests before promotion.

Instrumentation needs separate contracts for what it reads and when it is safe to read. Concrete safe
points remain runtime-specific.

Current status: narrowed as of 2026-08-10.

## Model and project impact

Codex was the primary repository inspector, implementation worker, experiment runner, diagnostician,
and evidence recorder from 2026-07-08 through 2026-07-27. Its exact route was not retained. It was
effective at unfamiliar-code navigation, executable contracts, multi-step implementation,
counterfactual execution, and layer-specific diagnosis. Early path proliferation, optimistic
infrastructure premises, and enabling work without a scientific dependency were recurring weaknesses.

This role observation requires retest because the harness changed, steering was frequent, and no
matched model comparison existed. The workflow materially accelerated implementation and diagnosis,
but its largest value came from evidence boundaries, causal replay, and retained failures rather than
proposal volume. It does not establish unattended autonomy.

## Evidence limits

Public FlySim claims are inspectable in its repository. The external application, private adapter,
runtime inspection, input delivery, live recordings, and operational details remain unavailable to
readers. Private results are authorized practitioner evidence, not independently reproducible public
evidence. The successful correction demonstrates one local coverage failure, not a general learning-
algorithm ranking. Quantitative orchestration gains and parallel-agent speedups were not established.
