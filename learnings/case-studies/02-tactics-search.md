# Case 02 - Tactics.md policy and action-node search

Observation window: 2026-03-07 through 2026-04-07
Disclosure mode: named detailed, private repository
Project: [Tactics.md](https://tactics.md/), a private turn-based tactics game played on a hex grid

The repository and primary artifacts belong to another party and remain private. This is an
authorized practitioner account of my work, not independently reproducible public evidence. The
repository owner approved publication of the project name and detailed results on 2026-08-10. This
report describes results and implementation mechanics without reproducing repository content.

## What the campaigns covered

The first campaign developed and optimized two interpretable, hand-written agents. Greedy selected
locally strong actions, while Heuristic planned and scored coordinated full turns. The work progressed
from scalar tuning against an unstable reference to frozen candidate-versus-control evaluation,
fixed-matchup diagnosis, random-team gates, protected regression cases, Bayesian optimization,
population ranking, and bounded MCTS ablations.

The second campaign, from 2026-04-05 through 2026-04-07, tested action-node search. Instead of making a
complete turn one search edge, it represented moves, attacks, abilities, and ending the turn as
separate edges. Learned policy and value components attempted to control the much larger frontier.

Both campaigns were intensive and frequently human-steered. The March 10-12 Greedy ledger alone
contains 455 experiments: 406 discards, 47 keeps, and 2 crashes. Numeric entries account for more than
24 million simulated games. The action-node campaign produced 235 commits in about 42 hours, but that
count includes infrastructure, artifacts, and recovery attempts rather than 235 independent ideas.

## Infrastructure and evidence authority

The campaigns began in a shared worker-writable repository with manually launched measurements and an
ambiguous comparison baseline. They added separate candidate and frozen-control configurations,
deterministic seeds, staged sample sizes, confidence reporting, bidirectional fixed matchups, action
traces, environment-removal counterfactuals, protected cases, saved checkpoints, and retained negative
results.

The standard Greedy promotion run used 100,000 random-team games. Runs of 200, 1,000, and 5,000 games
served as smoke, shortlist, and local-confirmation stages. Later tools added parameter search,
Bradley-Terry population ranking, full-system comparisons, search counters, and component benchmarks.

The evaluator still remained writable by the worker. Fixed and randomized populations were repeatedly
reused, execution and recovery were mostly manual, and no sealed promotion set or independent
promotion owner existed. The results below are strong adaptive development evidence, not untouched
confirmation.

## What happened

### Narrow wins frequently failed the population gate

Fixed matchups made failures legible, but also invited overfitting. One rule that rewarded screened,
maximum-range positions improved its motivating matchups to 56.0% and 51.0%. The 1,000-game random-team
gate then scored only 49.0%, and one protected matchup fell to 30.6%. Narrowing the rule removed some
collateral damage but also reduced the apparent lift to noise.

The useful pattern was a motivating case, neighboring cases, and then a representative population.
Fixed cases remained diagnostic microscopes and regression canaries, not promotion surfaces.

### Automated tuning revised the policy theory

Making Heuristic's scoring terms configurable allowed bounded Bayesian searches over related families.
A 40-iteration search found that a unit able to move and attack needed full attack credit rather than
a discounted proxy. The resulting configuration scored 55.1% over 50,000 games against Greedy, about
+35 Elo under that evaluator.

Target-priority tuning produced the larger surprise. The hand-written policy strongly prioritized
healers. Independent searches instead ranked high-damage units first and healers much lower. A later
configuration reached about +105.5 Elo against Greedy. Further expensive tuning changed many weights
but added only about 3.4 Elo, showing both the value of theory revision and the onset of diminishing
returns. These exact values were adaptively selected and are campaign evidence, not reusable policy
settings.

### Candidate breadth mattered more than a sophisticated evaluator

Shallow policy MCTS tested candidate count, rollout count, depth, response evaluation, pre-ranking,
and several leaf evaluators. Heuristic alone measured about +102 Elo against Greedy at 725 games per
second. The strongest tested MCTS configuration measured about +263 Elo but only 2.5 games per second;
a configuration within 8 Elo of it ran about twice as fast.

The clearest new gain came from generating genuinely different full-turn candidates. Extra
pre-ranking added cost without a demonstrated strength gain. A learned NNUE leaf could be actively
harmful when the candidate generator omitted useful plans. More evaluation could not repair a frontier
that never admitted the right action.

### Learned targets improved while actual play collapsed

The action-node campaign trained a 4,005-slot primitive-action policy head and a value head from
self-play. Offline metrics often improved sharply without stronger play. In the clearest collapse, a
round with only draw outcomes reached 86.70% held-out policy top-1 accuracy while the learned agent
scored 10.0% against Greedy.

A larger continuation generated 1,313,492 positions. Its best saved learned-search checkpoint scored
41.2% against searched Greedy over 40 games and 7.5% against plain Greedy. Increasing data, frontier
width, depth, exploration, and nominal time did not make the learned frontier competitive. The model
was becoming better at predicting targets produced by the narrowing process it controlled.

Offline fit therefore needed separate gates for target entropy, outcome diversity, frontier recall,
and end-to-end playing strength.

### Full breadth changed the failure diagnosis

A simpler reference searched the complete legal action buffer with hand-written ordering and a basic
health-plus-material leaf evaluator. Its positive internal results showed that primitive action-node
search could work when useful actions were not discarded before deeper evaluation. The branch then
made full breadth an explicit control.

This did not validate the learned architecture or reproduce the reference under sealed conditions. It
relocated the main hypothesis from “action-node search is broken” to “top-K target generation and
frontier recall are broken.” Before abandoning an expressive search architecture, the cheapest useful
counterfactual was to remove learned truncation.

### A stale executable invalidated the first performance narrative

The component benchmark used five fixed tactical situations. Its wrapper rebuilt only when the
optimized executable was absent, so source edits could be followed by timings from an older binary.
The apparent initial optimization chain was discarded.

After forcing a fresh build, the valid baseline reset to 42,995 nodes per second. A one-factor sequence
then reached 128,425 nodes per second, a 2.987x component improvement. One intermediate change
regressed, and later profiling showed that some general search bookkeeping bought no pruning in this
exact depth-one regime.

The final throughput number remains adaptively reused component evidence. It was not confirmed as a
playing-strength improvement or under deeper search. Deterministic fixtures are not reproducible
evidence when the executed artifact is unknown.

## Model and agent observations

Claude Opus 4.6 was attributed to simulator, Greedy, mechanics-parity, and early search work during
March. Claude Sonnet 4.6 contributed bounded evaluator and alternative-policy changes in early April,
including corrections to forest damage and capped-game accounting. The record supports substantial
implementation contribution but not stable model rankings or weaknesses because exact provider routes
and prompt configurations were not retained.

The action-node campaign's coding-agent route was not preserved. At the role level, it showed very high
implementation throughput, detailed negative-result preservation, prolonged tuning around a failing
learned frontier, late skepticism about artifact identity, and repeated relaunch attempts without
first isolating the orchestration failure. These are workflow observations, not attributable model
traits.

## Project impact and limits

Autoresearch materially improved the interpretable agents, built a stronger evaluation method,
overturned several plausible policy assumptions, rejected brittle local fixes, exposed a
self-reinforcing learned-target failure, and prevented stale binary timings from becoming accepted
performance evidence. Without it, these changes likely would have arrived more slowly and more
scenario-specific rules might have survived. A stricter family stop policy could also have reached
several conclusions with much less search.

The private repository prevents independent inspection. Exact optimized parameters and candidate
rankings were adaptively selected. The learned-frontier result does not prove learned pruning is
generally inferior, the 2.987x component result does not establish stronger play, and no quantitative
claim about autonomous throughput, agent parallelism, or model superiority is supported.
