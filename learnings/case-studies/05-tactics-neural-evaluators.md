---
{
  "case": 5,
  "title": "Tactics.md neural evaluator optimization",
  "started": "2026-04-15",
  "ended": "2026-05-08",
  "featured_rank": 1,
  "summary_markdown": "[Tactics.md](https://tactics.md/) used autoresearch to train neural models that evaluated positions inside its game-tree search, testing architecture size, training targets, quantization, and self-play across 435 result bundles. Under the same 10 millisecond move budget, a model that evaluated each position 73 times more slowly still won because its judgments were better, while the model with the best validation loss played worst among matched candidates."
}
---

# Case 05 - Tactics.md neural evaluator optimization

Observation window: 2026-04-15 through 2026-05-08
Disclosure mode: named detailed, private repository
Duration: several intensive campaigns across several weeks
Project: [Tactics.md](https://tactics.md/), a private turn-based tactics game played on a hex grid

The repository and primary artifacts belong to another party and remain private. This is an
authorized practitioner account of my work, not independently reproducible public evidence. The
repository owner approved publication of the project name and detailed results on 2026-08-10.

## What was optimized

The project trained neural action-value models and used them as leaf evaluators in game-tree search.
The deployment question was not which network predicted held-out targets best. It was which network
produced the strongest play when every move received the same 10 millisecond search budget.

Unlike Case 02, this campaign did not develop the action-node search architecture. It optimized the
models that scored positions at the leaves of an existing search loop, including model shape, target
weighting, quantization, training data, and inference cost.

The evidence store contains 435 structured result bundles plus manual ablations and out-of-band
matches. This is cumulative adaptive search burden, not 435 independent confirmations. Highlighted
comparisons usually ran 5,000 games for about eight minutes; some self-play cycles generated 100,000
games and ran for about an hour. Decisive measurements were mostly serialized, and human steering
selected the causal questions and promotion-worthy evidence.

## Infrastructure and evidence authority

On 2026-04-15, Tactics.md had repeatable GPU training and an operational game evaluator, but checkpoint
selection centered on held-out loss and incumbent changes were mostly manual. The evaluator remained
writable beside the implementation.

From 2026-04-15 through 2026-04-20, one-hop and multi-lane controllers added fixed-control matches,
constrained proposals, append-only history, automatic incumbent updates, deterministic playoffs,
limited retries, persistent replay state, and planner queues. The workflow separated early stopping
and checkpoint choice within a run from the decision to replace an incumbent.

From 2026-04-24 onward, the campaign added architecture and feature ablations, quantization-aware
training, int8 kernels, and repeated challenger-versus-incumbent gates. One enabled gate rejected 13
consecutive self-play candidates at roughly -4 to -9 Elo. Later studies deliberately disabled the
gate and advanced every cycle, using a reused reference for out-of-band checks.

The resulting system supported disciplined adaptive discovery, not sealed promotion. It had no hidden
or query-limited final set, repeated-look correction, or complete content identity for evaluator,
candidate, control, and loaded configuration. No favored historical candidate received untouched
promotion evidence.

## What happened

### A much slower evaluator still won under the fixed budget

The main reference used a 2,560-wide sparse embedding and 1,280/192 hidden layers. Compact candidates
used a 128-wide embedding and 16/32 hidden layers. A middle design widened only the embedding to 1,280
while keeping the small hidden trunk.

| Candidate | Elo against reference | Nodes per move | Nanoseconds per leaf |
|---|---:|---:|---:|
| Compact 128/16/32 | -123.3 | 2,919 | 675 |
| Wide embedding 1,280/16/32 | -62.0 | 2,683 | 677 |
| Reference 2,560/1,280/192 | 0 | 168 | 49,246 |

The reference was about 73 times slower per leaf and searched far fewer nodes, yet still won by 62 Elo
under the same 10 millisecond move budget. Evaluation quality outweighed throughput. A fixed-node
benchmark would have answered a different question from the deployed loop.

Widening the embedding from 128 to 1,280 recovered 61 Elo at almost unchanged leaf cost, but the next
doubling to 2,560 lost about 6 Elo. Doubling the hidden layers improved validation loss while leaving
playing strength nearly flat and increasing leaf cost by 49%. The first gain justified continuing the
sweep; the first reversal prevented “width is dominant” from becoming an unlimited scaling rule.

### The best validation loss selected the worst playing model

Three int8 models used the same 1,280/16/32 architecture and training budget. Only the weight placed on
the final game result changed:

| Final-result weight | Best validation loss | Elo against reference | Nanoseconds per leaf |
|---:|---:|---:|---:|
| 0.0 | 0.4094 | -61.2 | 870 |
| 0.5 | 0.4066 | -59.0 | 872 |
| 1.0 | 0.4041 | -86.6 | 871 |

The 1.0 setting had the best held-out loss and the worst playing strength. Held-out loss remained
useful for detecting unstable training and selecting a checkpoint within one run. It did not have
authority to rank models across runs when runtime and an outer search determined actual utility.

### Int8 performance reversed with model shape

At a large production-like hidden shape, the new int8 path was roughly three times faster than the
previous leaf evaluator. At the narrow 1,280/16/32 shape, quantization-aware training preserved playing
strength but int8 inference was 29% slower than fp32. Packing, dispatch, and per-row dequantization
overhead were poorly amortized.

The decision was not “int8 works” or “int8 fails.” It was to retain int8 for shapes where the real
kernel and workload demonstrated value. Low-level optimizations needed representative shapes.

### An unchanged artifact isolated a runtime change

A candidate model was measured after pairwise accumulator work had also changed the runtime. On
2026-04-28, the unchanged earlier fp32 model was rerun on the newer engine. It measured 666 ns per leaf
and -60.4 Elo, close to its earlier 677 ns and -62.0 Elo result.

That bridge argued against the shared runtime change as the main cause of a candidate-specific
regression. It was still only a local counterfactual because executable and artifact hashes were not
fully frozen. When both artifact and runtime change, the unchanged artifact on the new runtime is the
cheapest crossed cell.

### A fixed-data recipe failed under self-play

A compact recipe tuned on a fixed teacher corpus reached about -44 Elo against the reference, better
than the wide single-shot model. The same architecture and recipe then started from random weights and
trained for 15 self-play cycles. It scored -128.2 Elo at cycle 5, -124.6 at cycle 10, and -133.6 at
cycle 15. An older compact self-play recipe had reached -54.4 after 17 cycles.

The recipe ranking reversed when the model generated its own data. This changed the diagnosis from a
simple optimizer or architecture question to an interaction among initialization, optimization, and
data regime.

## Model and agent observations

Codex GPT-5.4 was directly verified from route metadata from 2026-04-14 through at least 2026-04-25.
It was strong at repository navigation, end-to-end implementation, controller construction, and
experiment plumbing. Codex GPT-5.5 was verified on 2026-04-26 and 2026-04-28 and was effective at
concrete execution, counterfactual testing, and repository-state auditing. One session included
analysis supplied by another agent, limiting causal attribution.

Claude Opus 4.7 with a 1M-context designation appeared in 28 co-author trailers from 2026-04-24 through
2026-05-07. It contributed substantial implementation and useful synthesis. One attributed analysis
turned the first width gain into an overly confident dominance claim; the next experiment preserved
speed but lost strength. Raw route metadata was unavailable, so this remains trailer-attributed rather
than transcript-verified behavior.

The strongest supported role assignment is an implementation and measurement operator under frozen
transaction rules, with a separate judgment owner responsible for causal claims and promotion.

## Project impact and limits

The workflow redirected work toward useful embedding capacity, prevented monotonic width scaling,
rejected a target setting favored by validation loss, limited int8 deployment to suitable shapes, and
exposed a fixed-data versus self-play reversal. Without the rapid counterfactual sequence, the project
likely would have spent longer optimizing surrogate loss, scaling width, or blaming shared runtime
code for a shape-specific kernel regression.

Readers cannot inspect the private code, models, run bundles, or match records. Exact rankings remain
adaptive development evidence, capacity and int8 crossover points are unresolved, and the self-play
failure did not isolate data quality from initialization and optimizer interactions.
