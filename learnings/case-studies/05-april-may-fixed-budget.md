# Case 05 - Fixed-budget optimization campaign

Observation window: 2026-04-15 through 2026-05-08
Disclosure mode: anonymized
Duration: several concentrated campaigns across several weeks
Application domain: intentionally withheld

## Scope and evidence authority

This campaign had richer experiment control than the March legacy case but no sealed promotion
evaluator. Repeated operational comparisons were adaptive discovery evidence and a way to manage an
incumbent. They were not untouched confirmation. No key result froze evaluator executable, candidate
and control artifacts, and canonical effective configuration under content identity.

The campaign covered training, runtime evaluation, experiment control, and incumbent selection. Search
was intensive, decisive shared-hardware measurements were mostly serialized, and a human selected
causal questions and promotion-worthy evidence.

## Infrastructure timeline

On 2026-04-15, the project had repeatable training, an operational evaluator, manual incumbent changes,
and held-out loss for checkpoint selection. The evaluator remained writable beside the implementation,
while configuration and artifact identity were uneven.

From 2026-04-15 through 2026-04-20, one-hop and multi-lane controllers added fixed-control end-task
comparisons, constrained proposals, automatic incumbent updates, append-only history, deterministic
playoffs, limited retries, persistent replay state, and planner queues. The work also separated
checkpoint replacement sensitivity from early stopping.

From 2026-04-24 through 2026-04-28, model, data, runtime, and replay layers changed rapidly. A gate
repeatedly compared adaptive candidates with a reused incumbent and rejected many regressions. Later
runs disabled that gate, and a supervised ablation sequence tested mechanisms outside a complete
identity bundle.

From 2026-04-29 through 2026-05-08, further gate-disabled campaigns reused out-of-band references. A
later result contradicted a simple transfer assumption from an earlier setting.

By the end, structured run bundles recorded revisions, configurations, paths, logs, and incumbent
state, but not universal dirty-tree, executable, artifact, or loaded-configuration digests. As of
2026-08-10, the harness still lacked hidden or query-limited promotion data, cumulative adaptive-search
accounting, repeated-look correction, and a mandatory promotion gate. It supported disciplined
adaptive discovery, not sealed promotion.

## Main findings

### Separate checkpoint selection, adaptive incumbent selection, and promotion

Held-out loss helped detect unstable training and select a plausible checkpoint within a run. It did
not reliably rank candidates across runs when operational utility also depended on runtime cost, an
outer algorithm, or a changed data regime. Reused end-task comparisons exposed these mismatches but
became adaptive after influencing later candidates.

A surrogate may select a checkpoint, and a reused end-task gate may guide discovery. Final promotion
requires untouched evaluation or a predeclared sequential protocol that accounts for prior looks.

Current status: durable as a workflow rule. Historical candidate rankings require sealed retest.

### Bridge artifact and runtime changes with the unchanged artifact

On 2026-04-24 and 2026-04-28, candidate artifacts were measured across runtime changes. Rerunning the
unchanged earlier artifact on the newer runtime kept timing near its prior result, arguing against the
runtime change as the main cause of one regression.

When a comparison crosses both boundaries, measure old artifact on old runtime, old artifact on new
runtime, and new artifact on new runtime. Add the fourth crossed cell if ambiguity remains. Test
low-level mechanisms at representative shapes because their performance can change with workload size.

Current status: narrowed. The bridge design is durable, but the historical causal claim requires
retest with frozen executable, artifact, and configuration identity.

### Select quality-changing components on fixed-budget utility

Direct quality-and-cost tradeoffs appeared on 2026-04-28, followed by further campaigns on 2026-04-29
and a context-transfer reversal on 2026-05-08. When an outer algorithm consumes a component under a
wall-time or resource budget, quality per call and calls per budget interact.

Throughput, arithmetic count, surrogate loss, and isolated quality are diagnostics. Select by running
the deployed loop at its real budget and in the relevant data-generation regime whenever the component
can change behavior.

Current status: durable as an operational rule. Exact candidate rankings remain adaptive discovery
evidence.

## Model and project impact

Codex GPT-5.4 was directly verified from route metadata from 2026-04-14 through at least 2026-04-25. It
was strong at repository navigation, end-to-end implementation, experiment plumbing, and sustained
tool-driven work. Codex GPT-5.5 was verified on 2026-04-26 and 2026-04-28 and was effective at concrete
execution, counterfactual testing, and repository-state auditing. One session included analysis from
another agent, limiting route-specific attribution.

Claude Opus 4.7 with an extended-context designation was attributed through commit trailers from
2026-04-24 through 2026-05-07. It contributed substantial multi-file implementation and useful
synthesis, but raw route metadata was unavailable. Behavioral claims remain provisional.

The strongest supported assignment is an implementation and measurement operator under frozen
transaction rules, with a separate judgment owner for causal claims and promotion. The workflow
accelerated implementation, rejected surrogate-only improvements, and encouraged cheap
counterfactuals, but did not establish unattended autonomy or sealed promotion.

## Evidence limits

This report omits the project, domain, private paths, internal names, exact metrics, model shapes,
budgets, hardware, prompts, and commits. No favored candidate received untouched promotion with
complete identity. Capacity boundaries, reduced-precision crossover points, search-depth effects, and
controller autonomy remain provisional. The conclusions concern workflow authority and experiment
design, not private outcomes or a general provider ranking.
