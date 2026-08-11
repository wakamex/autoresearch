---
{
  "case": 3,
  "title": "Tactics.md CPU self-play optimization",
  "started": "2026-03-10",
  "ended": "2026-03-11",
  "summary_markdown": "[Tactics.md](https://tactics.md/) used Codex to test 102 interventions on the CPU pipeline generating self-play training games, accelerating turn search and quantized neural evaluation while uncovering eight correctness defects. Narrow component benchmarks repeatedly misled; only full-turn replay and end-to-end self-play could distinguish real speedups from changed game behavior."
}
---

# Case 03 - Tactics.md CPU self-play optimization

Observation window: 2026-03-10 through 2026-03-11
Disclosure mode: named detailed, private repository
Duration: two calendar days in one nearly continuous campaign
Project: [Tactics.md](https://tactics.md/), a private turn-based tactics game played on a hex grid

The repository and primary artifacts belong to another party and remain private. This is an
authorized practitioner account of my work, not independently reproducible public evidence. The
repository owner approved publication of the project name and detailed results on 2026-08-10.

## What was optimized

The campaign optimized Tactics.md's CPU-based Rust turn-search and quantized neural evaluation path
used to generate self-play data. The representative benchmark ran actual game setup, terrain, legal
action generation, candidate-turn search, child-state mutation, QNNUE evaluation, automatic turn
transitions, and training-position production.

The ledger contains 102 entries over roughly 21 hours: 48 keeps, 52 discards, one neutral result, and
one scaffolding change. Keeps included correctness and profiling infrastructure, so they are not 48
independent speedups. Work was mostly sequential, manually launched, resource-intensive, and
frequently human-steered.

This is a legacy-harness case. The evaluator and implementation shared a writable repository, artifact
identity and recovery were incomplete, and no persistent orchestrator or sealed promotion route
existed. Its performance and model behavior should not be treated as a current autoresearch baseline.

## Infrastructure changes

The starting benchmark accepted a seed, but terrain setup still used operating-system randomness.
Timing relied on a few manual runs, and correctness tests focused on individual actions or neural
evaluations rather than a complete searched turn.

By 2026-03-11, the campaign had seeded terrain, stable event signatures, warm-up and repeated-run
statistics, processor affinity, child-process CPU accounting, host-noise warnings, and microprofiles
for QNNUE, move generation, and turn transitions. Exactness checks compared dense features, scalar and
SIMD evaluators, and one complete candidate turn including selected actions, final state, automatic
turn-end effects, event signature, and final RNG position.

An append-only experiment log retained mechanisms and verdicts. Microprofiles were explicitly for
discovery, while the self-play generation workload controlled promotion. Evaluation, cleanup,
restoration, and final judgment remained manual.

## What happened

### Stable timings concealed different workloads

Before the terrain RNG fix, five runs averaged 7.508 seconds with only 0.52% timing variation. That
looked precise, but key event counts varied by thousands. After deterministic setup, the event
signature became constant even though timing variation increased to 1.62%.

The nominal runtime also fell to 7.034 seconds, but that was not a clean speedup because the executed
workload changed. The useful result was workload identity. More repetitions of the original benchmark
would only have measured a mixture of different games more precisely.

### Several large component-level wins failed end to end

The campaign retained substantial paired improvements against immediate controls:

| Change | Representative end-to-end result |
|---|---:|
| Reuse an already-scored child evaluation | 6.834s to 6.328s, -7.40% |
| Replace hash-based movement reachability with indexed masks | 5.872s to 5.550s, -5.48% |
| Cache duplicate one-ply turn orders | 1.489s to 1.303s, -12.49% |
| Streamline and fuse QNNUE row work | 5.362s to 4.078s, -23.94% |
| Add the first exact x86 SIMD QNNUE path | 4.138s to 2.426s, -41.37% |
| Promote the corrected AVX2 bundle | 6.330s to 5.710s, -9.79% |

These percentages cannot be compounded because commands, engine state, and harness controls changed.
The campaign did not preserve one frozen start-to-end comparison.

Several attractive screens also failed promotion. Preallocating movement output improved its cached
microbenchmark by 12.99% but regressed the pinned full workload by 3.74%. An aligned AVX2 layout won
2.31% in the isolated evaluator benchmark and was exactly neutral end to end. Removing a target lookup
almost halved one named bucket while total runtime regressed 0.35%. The component measurements
explained mechanisms; none had
promotion authority.

### Exactness belonged at the complete candidate-turn boundary

The campaign found eight correctness and exactness defects. They included missing sparse model
features, hidden terrain randomness, unstable feature ordering, stale evaluation after an action
automatically ended a turn, component-level parity that missed search-level floating-point drift, and
a SIMD indexing error.

Several candidates passed action-level or evaluator-level checks but changed later search behavior
through ordering, accumulated floating-point differences, automatic transitions, or RNG consumption.
The strongest oracle began from the same midgame and RNG state, searched the same unit order, applied
all turn-end effects, and compared actions, final state, score, events, and RNG position.

### Negative results needed reopening conditions

The log prevented immediate repetition of failed ideas, but also showed why a permanent rejection was
too strong. A mechanism rejected under one representation could become useful after state layout,
access patterns, or the active hotspot changed. A useful negative result therefore recorded the
failure layer, surrounding structure, and the condition that would justify another test.

## Model and project impact

Codex was the primary repository analyst, implementation worker, experiment runner, profiler author,
and log maintainer. The exact model route was not recorded. It was effective at unfamiliar Rust code,
low-level and structural optimization, parity tests, profiler construction, and benchmark-defect
diagnosis. It needed human help to close exhausted families, continue beyond local completion, and
recognize when component-level exactness was weaker than full-turn correctness.

Later Tactics.md controllers had structured run bundles, persistent queues, better checkpoint
preservation, and clearer evidence labels. The March autonomy and role observations require retest
under that infrastructure.

The campaign accelerated the self-play generation path, changed the dominant hotspot several times,
found serious correctness defects, and prevented many microbenchmark-only candidates from being
promoted. Without it, full-state cloning, duplicate evaluation, hash-heavy move generation, and scalar
kernel work likely would have survived longer. No matched human-only campaign exists, and the missing
frozen start-to-end result prevents a defensible cumulative speedup claim.

## Evidence limits

Readers cannot inspect the private implementation, ledger, benchmark output, or retained artifacts.
The exact paired comparisons are development evidence from a changing harness. Processor affinity did
not replace formal resource admission, the evaluator remained worker-writable, and continuous
unattended operation was not demonstrated.
