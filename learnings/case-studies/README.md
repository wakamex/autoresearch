# Autoresearch case studies

These are ten chronological reports from campaigns where I used autoresearch. Some describe public
projects in full, some name private projects without publishing their repositories, and others
generalize private work without revealing the project or application.

Each report explains when and how intensively I used autoresearch, what infrastructure existed at the
time, which models did what, what changed because of the work, and which lessons still appear useful.
The case number provides chronological ordering, while the exact dates appear below and inside each
report.

## Chronological reading guide

Effective tokens are uncached-equivalent estimates from retained session records.

<!-- generated-case-studies:start -->
| Case | What happened | Effective tokens | When |
|---|---|---:|---|
| [`01-mnk-transfer.md`](01-mnk-transfer.md) | [M,N,K game research](https://github.com/wakamex/mnk) used a Rust and CUDA AlphaZero system to test whether a smaller-board checkpoint could improve learning on a larger board. The checkpoint loaded successfully, but the campaign never established a benefit over matched scratch training, and several promising settings produced a worse and more expensive combined result. | ~33M | 2026-02-04 to 2026-02-22 |
| [`02-tactics-search.md`](02-tactics-search.md) | [Tactics.md](https://tactics.md/) used autoresearch to develop and tune its hand-written Greedy and Heuristic agents across more than 24 million simulated games, then test learned action search. One learned model reached 86.7% held-out accuracy but scored only 10% against the simpler Greedy agent because useful actions were pruned before deeper evaluation. | ~1.32B | 2026-03-07 to 2026-04-07 |
| [`03-tactics-cpu-optimization.md`](03-tactics-cpu-optimization.md) | [Tactics.md](https://tactics.md/) used Codex to test 102 interventions on the CPU pipeline generating self-play training games, accelerating turn search and quantized neural evaluation while uncovering eight correctness defects. Narrow component benchmarks repeatedly misled; only full-turn replay and end-to-end self-play could distinguish real speedups from changed game behavior. | ~86M | 2026-03-10 to 2026-03-11 |
| [`04-gradient-bang-automation.md`](04-gradient-bang-automation.md) | A [Gradient Bang](https://www.gradient-bang.com/) headless client completed live trading, combat, fleet, and exploration workflows and reached contemporaneous visible ranks of 29 in exploration and 27 in trading. Parallel probe agents then began consuming one another's completion events. | ~47M | 2026-04-14 to 2026-04-16 |
| [`05-tactics-neural-evaluators.md`](05-tactics-neural-evaluators.md) | [Tactics.md](https://tactics.md/) used autoresearch to train neural models that evaluated positions inside its game-tree search, testing architecture size, training targets, quantization, and self-play across 435 result bundles. Under the same 10 millisecond move budget, a model that evaluated each position 73 times more slowly still won because its judgments were better, while the model with the best validation loss played worst among matched candidates. | ~118M | 2026-04-15 to 2026-05-08 |
| [`06-options-market-making-multi-llm.md`](06-options-market-making-multi-llm.md) | Options market-making research used GPT-5.5 for implementation, Gemini 3.5 Flash for candidate generation and reflection, and Fable 5 for judgment and stopping decisions. An independent audit found gaps between the research record and implemented system. One candidate failed a causal correction and its replacement survived bounded validation, but the historical return disappeared in a short fresh window with stronger quote competition. | ~500M | 2026-06-22 to 2026-07-10 |
| [`07-flysim-sim-to-live.md`](07-flysim-sim-to-live.md) | [FlySim](https://github.com/wakamex/flysim) trained flight-control policies in a public JAX simulator, then a private overlay tested a frozen policy in a live external flight application. When a half-second handoff clipped 14% of controls, replaying the exact safety-filtered inputs showed that the simulator underrepresented the live aircraft's roll and yaw response. Retraining fixed the clipping without weakening the live safety limits. | ~240M | 2026-07-08 to 2026-07-27 |
| [`08-strategy-game-multi-model-playtesting.md`](08-strategy-game-multi-model-playtesting.md) | A party-management strategy game used six model families as independent playtesters who managed parties, edited character tactics, and revised strategies against a deterministic battle simulator. Their disagreements prevented premature game-design changes, exposed tool-assisted play that violated the rules, and recorded which mechanics the models described as clear, confusing, or engaging. | ~68M | 2026-08-02 to 2026-08-09 |
| [`09-freetranscribe-gpu-inference.md`](09-freetranscribe-gpu-inference.md) | [FreeTranscribe.org](https://freetranscribe.org/) doubled transcription throughput while sharing one RTX 3090 between live production and autoresearch. Error counts stayed unchanged across 295 broad cases and fell from 105 to 103 on a reviewed long-form set. | ~144M | 2026-08-06 to 2026-08-08 |
| [`10-trading-strategy-search.md`](10-trading-strategy-search.md) | Quantitative-trading autoresearch sustained 46 agent-led research cycles in eight hours, implementing 39 strategies and retaining 35 development results that passed causal-attribution checks while sealed future data stayed untouched. Shared-capital replay mapped the development tradeoff between profit and volume. Gemini 3.6 Flash remained the historical bandit leader after completing 10 of 10 cycles; in a later panel, GPT-5.6 Luna medium received similar internal ratings to Sol medium at under one-twentieth the API-equivalent cost. | ~143M | 2026-08-08 to 2026-08-11 |
<!-- generated-case-studies:end -->

## Website data

[`case-studies.json`](case-studies.json) contains the same metadata in a browser-friendly form. It is
generated from the JSON frontmatter in each report, not maintained separately. A website can load it
directly:

```js
const response = await fetch(
  "https://raw.githubusercontent.com/wakamex/autoresearch/master/learnings/case-studies/case-studies.json",
);
const { cases } = await response.json();
```

The top-level object supplies the collection title, description, latest case date, repository URL,
and aggregate token estimates. Each case supplies `featured_rank` and a `token_estimate` with
processed tokens, effective tokens, and confidence. Effective tokens are an uncached-equivalent
proxy, while processed tokens include cached input. These are rounded estimates from retained local
session records, not provider billing statements. The generator validates this metadata before
publishing either view.

Edit a report's frontmatter, then regenerate both outputs with:

```sh
python3 scripts/generate_case_studies.py
```

Do not edit the table or JSON by hand. CI runs the generator in check mode and fails when either
generated view is stale.

These are practitioner reports, not independent replications. Model observations are conditional on
the calendar period, provider route, prompt, tools, and harness maturity. Calendar and infrastructure
backfills should update both the individual case and this index.

Case-study conclusions are scoped to their recorded infrastructure. Newer evidence does not win merely
because it is newer, but evidence from a more controlled and representative harness should supersede a
conflicting older observation unless the older mechanism is independently reproduced.
