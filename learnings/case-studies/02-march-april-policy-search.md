# Case 02 - Policy and search optimization

Status: reviewed
Reviewed: 2026-08-10
Observation window: 2026-03-07 through 2026-04-07
Disclosure mode: anonymized

## Scope and evidence boundary

This case combines two consecutive campaigns in one private project. The first improved an
interpretable sequential policy through targeted diagnosis, population evaluation, parameter search,
and bounded search ablations. The second tested a finer-grained learned search architecture, rejected
its learned frontier, introduced a full-breadth control, and optimized the verified control path.

Evidence was reconstructed from version history, research notes, benchmark records, run summaries,
and retained artifacts. The evaluator remained worker-writable, measurements and orchestration were
mostly manual, and discovery surfaces were reused adaptively. The findings are practitioner evidence,
not independent replication or sealed promotion results.

## Exposure and project impact

- Duration: one month of concentrated implementation, evaluation, diagnosis, and optimization.
- Search intensity: very high, spanning many local variants, broad stochastic comparisons, parameter-search batches, population rankings, learned-component runs, and compiled benchmarks.
- Execution: primarily serial reasoning and measurement, with internal simulation parallelism and limited concurrent long-running work.
- Human involvement: frequent steering and final promotion judgment.
- Resource burden: heavy relative to the project.
- Breadth: policy scoring, action generation, scenario diagnostics, population evaluation, training, search architecture, benchmark tooling, caches, and hot-path implementation.

The campaign materially improved the policy and its research method. It rejected many brittle local
fixes, corrected evaluator mismatches, exposed self-reinforcing learned targets, and prevented stale
binary measurements from becoming accepted optimization evidence. The strongest result was better
causal attribution and evaluation discipline rather than one final parameter vector or promoted
learned architecture.

Without this workflow, locally attractive rules would likely have accumulated, the learned-search
failure might have been attributed to the entire architecture, and stale executable timings might
have remained trusted. A stricter family stop policy could probably have reached several conclusions
with less search.

## Infrastructure timeline

On 2026-03-07, the project had a fast simulator and a hand-written policy, but comparisons still used
an unstable or ambiguous reference. Work ran in a shared writable checkout without disposable workers,
a persistent orchestrator, a sealed evaluator, artifact attestation, automated recovery, or an
independent promotion owner.

From 2026-03-10, the campaign used separate candidate and frozen-control configurations with a direct
head-to-head command and confidence reporting. It then added fixed-scenario diagnostics, bidirectional
runs, action traces, environment-removal counterfactuals, randomized-population gates, protected
regression cases, and explicit keep-or-revert decisions.

Late in March and early in April, policy terms became parameter-driven. Bounded Bayesian searches over
related families, direct ablations, and population ranking were used to generate hypotheses. Search
components were exposed as separate controls so candidate diversity, pre-ranking, response evaluation,
depth, and leaf scoring could be compared under a fixed budget.

From 2026-04-05 through 2026-04-07, a linked fine-grained search campaign trained a learned frontier and
evaluation components. Offline fit improved while end-to-end behavior remained weak and sometimes
collapsed. A model-free full-breadth control relocated the failure from the overall architecture to
premature truncation and target generation.

The final phase added component and full-system comparisons, saved checkpoints, per-round summaries,
search counters, correctness tests, and a shared performance benchmark. An audit found that the
benchmark wrapper could reuse an old executable after source edits. The earlier timing chain was
discarded, the wrapper was changed to force a fresh optimized build, and one-factor measurement
restarted from a new baseline.

At the end, the project had much stronger diagnosis, evaluation, and research memory, but still lacked
worker isolation, an append-only transaction ledger, complete executable and configuration identity,
general recovery, progress-freshness monitoring, and sealed promotion authority.

## Durable findings

### A fixed case is a microscope, not a promotion surface

Narrow scenarios exposed mechanisms quickly, but candidates that improved one case often failed on
neighboring cases or the randomized population. Repeated exposure also turned fixed scenarios into
local tuning surfaces.

Use a three-stage path: motivating case, preregistered neighboring transfer ring, then representative
population gate. Retain solved cases as regression constraints rather than optimizing only their
aggregate score. This finding was repeated throughout the March campaign and is high confidence under
the recorded harness.

### Remove one mechanic before editing the policy

Matched scenario runs with one environmental mechanic disabled often determined whether the failure
belonged to core action preference or to a later interaction. Some visually plausible trace fixes
changed a decision without improving the outcome.

Before adding another policy rule, remove or freeze one suspected causal layer and require outcome
movement. The counterfactual may identify an interaction rather than a sole cause, so reintroduce the
mechanic in one controlled step before closing the diagnosis.

### Reachability and behavior should precede another verbal variant

Many differently described proposals were inert, unreachable, strict subsets, or behaviorally
equivalent on the tested population. Manual notes exposed the pattern only after substantial local
search.

After one or two failed variants at the same surface, compare branch counters and canonical action
traces before another full evaluation. Natural-language diversity is not causal diversity. Behavioral
equivalence remains population-specific and should compress work rather than prove universal identity.

### Automated tuning is a theory-revision tool

Parameter search overturned intuitive priority assumptions and identified sensitive action-sequencing
terms. The useful result was the qualitative direction and interaction, not the optimizer's exact best
point on an adaptively reused objective.

Use independent starts and direct ablations to validate qualitative findings. Treat the selected point
as discovery evidence until fresh confirmation, and test composition before combining winners from
sequentially optimized parameter families.

### Candidate coverage can dominate added evaluation depth

The clearest search gain came from generating genuinely different full-action candidates. Extra
pre-ranking added cost without demonstrated benefit, and a more sophisticated evaluator could not help
when the candidate path omitted useful alternatives.

At a fixed wall-time budget, measure useful behavioral coverage before paying for deeper evaluation.
Cross candidate breadth and evaluation depth explicitly rather than assuming either dominates.

### Self-generated targets can improve while behavior collapses

From 2026-04-05 through 2026-04-07, learned components became better at predicting targets generated
by their own search process while end-to-end behavior stayed weak and outcome diversity narrowed.
Increasing depth, width, exploration, or inference time did not reliably repair the outer loop.

Offline fit establishes agreement with generated targets, not deployed utility. Keep a fixed
full-system control in every round and gate on target entropy, outcome diversity, or visited-state
coverage when the model shapes the future data it consumes.

### A full-breadth control can relocate the failure layer

After repeated learned-frontier interventions failed, a simple full-breadth control showed that the
underlying fine-grained architecture remained viable. The missing good branch was often discarded
before deeper search could evaluate it.

Before rejecting an expressive architecture, remove learned pruning and run the cheapest matched
high-recall control that fits the budget. If it works, frontier recall and downstream search quality
become separate hypotheses. Full breadth is a diagnostic, not automatically the final design.

### The benchmark wrapper is part of the artifact

A benchmark that rebuilt only when its executable was absent reused stale code after source edits.
The resulting timing sequence did not measure the claimed candidates and was discarded.

Bind source, build policy, executable, effective configuration, and workload manifest in one result.
Always rebuilding is one solution; a verified content-addressed build is another. Deterministic input
fixtures do not compensate for unknown executable identity.

## Model and agent observations

Claude Opus 4.6 was attributed to early simulator, policy, mechanics-parity, and search implementation
during March 2026. The record supports broad multi-file implementation and useful negative-result
preservation, but not a stable model-specific weakness. Provider route and prompt configuration were
not retained.

Claude Sonnet 4.6 was attributed to bounded evaluator and alternative-policy implementation in early
April 2026. It contributed useful evaluator corrections and cross-platform changes, but too few
interventions exist for a behavioral ranking.

Much of the focused optimization work lacks reliable model-route metadata. The role-level evidence
supports high implementation throughput under human judgment. It also shows prolonged local search,
late artifact-identity skepticism, and repeated relaunches without first diagnosing the orchestration
layer. These are workflow observations, not clean model traits.

## Unresolved claims

- Exact optimized parameters were adaptively selected and are not transferable conclusions.
- The learned-frontier failure does not establish that learned pruning is generally inferior.
- Component throughput improvements were not sealed as representative end-to-end gains.
- Fixed-fixture performance gains require confirmation on additional regimes.
- The information-efficiency benefit of the large negative-result archive was not measured.
- No quantitative claim about autonomy, agent parallelism, or model superiority is supported.

## Current status

This is historical evidence from a highly intensive but manually governed campaign. Its strongest
conclusions concern diagnosis, evidence authority, and information paths. Candidate rankings and
architecture choices should be retested under frozen evaluators, complete identity capture, explicit
attempt budgets, and sealed confirmation.
