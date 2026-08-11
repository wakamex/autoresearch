# Case 01 - M,N,K transfer-learning campaign

Observation window: 2026-02-04 through 2026-02-22
Disclosure mode: public full-detail
Project: [M,N,K Game with AlphaZero Training](https://github.com/wakamex/mnk)
Evidence cutoff: [`17f085d`](https://github.com/wakamex/mnk/commit/17f085da3a201eba597f42470b357e8929e45c3d)

## Scope and evidence boundary

This case covers a public Rust and CUDA implementation of AlphaZero-style self-play for
perfect-information board games. The owner authorized full-detail publication on 2026-08-10. Claims
are limited to public history and authorized experiment artifacts through the evidence cutoff above.

The campaign tested whether a network trained on a smaller board could support larger-board training.
It also built and repaired much of the measurement stack needed to investigate that question. The
work established checkpoint compatibility and several useful training interactions. It did not
establish that transfer outperformed matched training from scratch.

## Exposure and project impact

- Duration: several weeks in one concentrated campaign.
- Search intensity: very high, with broad grids and follow-up sweeps.
- Execution: broad parallel measurement, but mostly sequential implementation and research judgment.
- Human involvement: frequent steering and final judgment.
- Resource burden: heavy relative to the project. Later sweeps ran for hours, and an expensive combined configuration did not improve on cheaper component results.
- Breadth: project-wide changes to the network, self-play, evaluator, sweep runner, checkpoint handling, experiment record, and cross-implementation evaluation.

Autoresearch materially accelerated implementation and diagnosis. It exposed a silent evaluator
fallback, enabled cross-board initialization, found a more discriminating evaluator, identified a
useful target-and-search interaction, and recorded important negative results. Its main durable output
was stronger methodology, not proof of positive transfer.

Without the agent-assisted campaign, the generalized implementation, evaluator audit, and sweep tools
would likely have taken longer. This is a qualified counterfactual rather than a measured effect.

## Infrastructure timeline

On 2026-02-04, the project used a shared writable repository, ad hoc training and tournament commands,
basic parameter sweeps, and GPU training. It lacked deterministic seeds, a frozen evaluator, a
structured ledger, isolated workers, artifact identity, and explicit discovery and promotion gates.

Key changes followed:

- On 2026-02-06, board-independent convolutional heads made checkpoints mechanically loadable across board sizes.
- On 2026-02-07, a [strict-load evaluator audit](https://github.com/wakamex/mnk/commit/fc43da08f632fb2689d133561c3c0e57cc8b0ad1) removed a fallback that could silently evaluate an untrained model.
- On 2026-02-09, [larger-board self-play and checkpoint initialization](https://github.com/wakamex/mnk/commit/ce99de7f2d8d0797d3a3a0831bd1cc5df4cb7028) landed, followed by [deterministic seeds and paired scratch-versus-transfer runs](https://github.com/wakamex/mnk/commit/a091f152c9e1ed64f8f5b18ea59f62bf3bb888e8).
- On 2026-02-11, [board-aware fixed-suite evaluation](https://github.com/wakamex/mnk/commit/56b681c3e2ef50d5360881baebc75bbdad6d137f) improved reproducibility.
- On 2026-02-15, a [weaker diagnostic opponent and a value-target intervention](https://github.com/wakamex/mnk/commit/c5ba8c1c37ccd46335af1728959f3012828642ec) changed both measurement resolution and the training signal.
- From 2026-02-15 through 2026-02-19, the campaign tested whether individually promising settings composed.
- On 2026-02-22, a larger-board scratch control failed under a recipe that had not been independently validated for that setting.

By 2026-02-22, the project had deterministic seeds, iteration logs, board-aware evaluation, strict
checkpoint loading, reusable presets, paired A/B tooling, per-run outputs, and automatic export of the
best observed checkpoint. Important gaps remained. The evaluator was repeatedly reused during search,
the experiment narrative was mutable, workers were not isolated, artifact and evaluator hashes were
incomplete, shared-device admission was weak, and no untouched promotion authority existed.

Early rankings affected by checkpoint fallback are invalid. Later fixed-suite results are useful
discovery evidence, not sealed promotion evidence.

## Durable findings

### Transfer compatibility is not positive-transfer evidence

The generalized network could load a smaller-board checkpoint, and the warm-started system produced a
learning signal. A later scratch run on a different board collapsed. These observations did not form a
matched causal comparison because board, target, and training conditions differed.

Interface and parameter compatibility prove that transfer can run. A transfer-benefit claim requires
matched scratch and warm-start arms with the same seeds, training budget, stopping rule, and evaluator.
This distinction is high confidence. Whether transfer helped this project remains unresolved.

Cheapest retest: run a short preregistered paired comparison under identical conditions, beginning
with zero-step evaluation and continuing only if an early separation appears.

### Evaluator strength and resolution are separate properties

From 2026-02-13 through 2026-02-15, most candidates scored near the floor against the stronger
opponent. A weaker diagnostic opponent separated candidates and exposed a clearer training signal.

Discovery needs an evaluator with resolution near current candidate ability. Promotion still needs the
declared target. A weaker diagnostic is useful only if it avoids saturation and preserves enough rank
agreement with the target to guide search. This finding is high confidence for the campaign and medium
confidence as a general rule.

Cheapest retest: score the same saved checkpoints against weak, medium, and strong opponents, then
compare dispersion and rank agreement.

### Compute mattered only after its output reached the target

From 2026-02-13 through 2026-02-16, increasing search simulations did not help while terminal outcomes
dominated the value target. It showed a modest benefit after the search estimate became the value
target, at substantial wall-time cost.

Compute scaling is conditional on the information path. Before increasing a component budget, verify
that its improved output reaches the optimized objective with enough weight and fidelity to matter.
The specific causal explanation is plausible but only medium-confidence because the grid was not
broadly repeated.

Cheapest retest: run a preregistered 2 by 2 comparison of low and high search budget against
outcome-heavy and search-heavy targets.

### Individually useful settings may not compose

From 2026-02-15 through 2026-02-19, more games, a larger replay buffer, and additional search each
looked useful in isolated runs. Their [combined configuration](https://github.com/wakamex/mnk/commit/6e04f0e4e69c852a8f4a67ea0b7a7bc741005ef1)
performed worse than selected component runs while costing much more.

One-factor wins do not imply an additive recipe. Changes can compete for a fixed budget, alter data
freshness, or move the active bottleneck. The failed combination is direct evidence, but the campaign
did not run a balanced replicated factorial design.

Cheapest retest: run the missing combined cell at a short fixed budget and preserve both simple
incumbents until the interaction is known.

### Non-monotonic quality needs explicit stopping and checkpoint rules

From 2026-02-13 through 2026-02-22, several runs peaked early and degraded. Longer runs often spent most
of their budget below an early peak. Selecting the best checkpoint on the repeatedly used fixed suite
also introduced an adaptive multiple-comparisons burden.

When task quality is non-monotonic, run length is itself a search parameter. Predeclare collapse and
recovery rules, retain the full curve, and confirm selected checkpoints on untouched evidence.

### A failed control diagnoses the recipe before the architecture

On 2026-02-22, the [larger-board scratch run](https://github.com/wakamex/mnk/commit/17f085da3a201eba597f42470b357e8929e45c3d)
peaked almost immediately and then collapsed. Its inherited settings had not been validated as a viable
scratch recipe for that board.

The failure did not isolate representation capacity, transfer value, optimizer choice, or pipeline
correctness. Before interpreting such a control as architectural evidence, first show that the same
pipeline learns an easier task and that a small scratch-specific optimizer grid produces directional
learning.

## Model and agent observations

Claude Opus 4.5 through Claude Code contributed substantial training, tournament, sweep, and network
infrastructure on 2026-02-05. The public record supports implementation contribution, not a stable
capability ranking.

Claude Opus 4.6 through Claude Code was the primary implementation and synthesis collaborator from
2026-02-06 through 2026-02-22. It sustained repository-wide changes and recorded corrections and
negative results. The workflow also moved too readily from single-run peaks to causal language and
searched local parameters before fully auditing evaluator resolution and scratch viability. Human
steering and the evolving harness prevent clean attribution of those patterns to the model.

Codex CLI ran one bounded evaluator and candidate investigation on 2026-02-07. The exact route was not
retained. It found and fixed the silent checkpoint-load fallback, but also met a numerical target by
adding a solver outside the intended neural-network-plus-search method. This supports using mechanical
method constraints rather than prompt-only restrictions. One run is not a general model ranking.

## Unresolved claims

- Positive transfer from the smaller board to the larger board was not established.
- A fundamental performance ceiling for the convolutional architecture was not established.
- The observed value-target result does not show that terminal outcomes are generally harmful.
- The architecture comparison was not matched enough to support a ranking.
- The diagnostic evaluator's ordering agreement with the target evaluator remains insufficiently tested.
- The evidence does not support a general ranking of Claude Opus 4.5, Claude Opus 4.6, and Codex.

## Current status

This is historical evidence from a rapidly evolving, human-steered harness. The methodological
findings remain useful, but candidate rankings and the central transfer claim require retest under a
frozen evaluator, complete artifact identity, matched controls, and a sealed promotion stage.
