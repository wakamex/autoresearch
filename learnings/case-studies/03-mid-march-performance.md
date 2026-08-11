# Case 03 - Stateful performance campaign

Observation window: 2026-03-10 through 2026-03-11
Disclosure mode: anonymized
Duration: two calendar days in one continuous intensive campaign
Application domain: intentionally withheld

## Scope and maturity

This was a short, intensive legacy campaign. It predates the evaluator isolation, artifact identity,
resource admission, recovery, monitoring, and structured promotion machinery used in later workflows.
Its causally tested findings remain useful, but its autonomy, throughput, and model behavior are not a
baseline for current autoresearch systems.

The campaign covered implementation, optimization, and validation across several components of one
performance-critical subsystem. Work was mostly sequential, resource-intensive, and frequently
human-steered. Autoresearch materially influenced promotion and rejection decisions.

## Infrastructure timeline

On 2026-03-10, the project began with correctness tests, a representative end-to-end benchmark,
lightweight profiling, manually launched sessions, hidden workload randomness, and few timing
repetitions. The evaluator and implementation shared a worker-writable repository. Discovery and
promotion were separated only informally.

Across 2026-03-10 and 2026-03-11, the campaign added seeded workloads with stable event signatures,
warm-up and repeated-run statistics, processor pinning, child-process accounting, host-noise warnings,
and reusable microprofiles. Correctness coverage expanded to complete stateful reference transactions,
including stochastic-state progression. An append-only log recorded mechanisms and verdicts, while
explicit rules required end-to-end confirmation and retained human promotion authority.

Workload-variance failures appeared before deterministic setup on 2026-03-10. Stateful correctness
gaps appeared across both days. Specialized profiles and structural changes on 2026-03-11 showed why
local performance and prior negative results could change meaning after the surrounding representation
changed.

The ending harness still lacked immutable evaluators, content-identified artifacts, formal resource
admission, automated progress monitoring, and automated recovery. By late April 2026, newer workflows
had structured run bundles, richer metadata, append-only indexes, persistent controllers, and better
checkpoint preservation. Those improvements supersede the March harness, not the findings below.

## Main findings

### Verify workload identity before estimating timing variance

Repeated wall-clock measurements initially showed modest dispersion while operation counts varied.
Longer runs would have measured different workloads, not the runtime noise of one workload. Routing
setup through the declared seed stabilized the operation signature and made small comparisons more
credible.

Fresh baseline processes should agree on a compact operation signature, output digest, and relevant
stochastic state before repetition count is used to estimate measurement noise.

Current status: durable. Richer run metadata still does not universally prove workload identity.

### Test exactness at the complete stateful transaction boundary

Several candidates passed local output checks but changed downstream behavior through ordering,
randomness consumption, terminal handling, or state carried across adjacent decisions. A complete
reference transaction caught differences that isolated operation tests missed.

The right correctness boundary is the smallest transaction after which all externally relevant state,
selected outputs, workload signatures, and stochastic position can be compared. Local tests are useful
diagnostics but insufficient promotion authority for stateful changes.

Current status: durable.

### Use local profiles for discovery and the end-to-end workload for promotion

Some changes improved an isolated hot path but were neutral or slower in the complete workload. Other
structural changes improved the aggregate while a named profile bucket stayed flat because the removed
duplicate work had occurred outside that bucket.

Profiles and microbenchmarks answer mechanism questions. Promotion belongs to the representative
end-to-end objective unless the local primitive is itself the shipped objective.

Current status: durable.

### Record failure prerequisites, not only verdicts

The experiment log prevented immediate repetition of neutral and regressed variants. It also showed
that a mechanism rejected under one representation could become useful after a structural change
altered its overhead and access pattern.

A negative result should record its failure layer, surrounding structure, and named reopening
condition. A new worker or elapsed time is not a reopening condition.

Current status: narrowed. Structured run bundles supersede the original Markdown log, while the
storage-independent rule remains durable.

## Model and project impact

Codex was the primary implementation worker, repository analyst, experiment runner, profiler author,
and research-log maintainer. The exact model route was not recorded. It was effective at unfamiliar
code inspection, concrete low-level and structural changes, targeted parity tests, benchmark-defect
diagnosis, and bounded experiments. It needed human help to close exhausted families, sustain work,
and distinguish local exactness from complete stateful correctness.

This role assessment requires retest under modern persistent controllers and stronger promotion
contracts. The campaign had no matched model comparison.

The workflow accelerated implementation, found correctness defects, and prevented noisy,
microbenchmark-only, or locally exact candidates from being presented as end-to-end improvements.
Without it, the project likely would have repeated more local variants and trusted timings from
nonidentical workloads. That counterfactual is reasoned, not experimentally matched.

## Evidence limits

This report omits project identity, domain, commands, metrics, operation counts, gains, implementation
details, and environment identity. The short window and changing harness limit claims about autonomy,
family closure, evaluator authority, and Codex behavior. Processor pinning did not replace resource
admission, continuous unattended operation was not demonstrated, and no architectural rewrite or
ideation cadence received matched end-to-end confirmation.
