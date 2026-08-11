# Autoresearch case studies

These are ten chronological reports from campaigns where I used autoresearch. Some describe public
projects in full, some name private projects without publishing their repositories, and others
generalize private work without revealing the project or application.

Each report explains when and how intensively I used autoresearch, what infrastructure existed at the
time, which models did what, what changed because of the work, and which lessons still appear useful.
The case number provides chronological ordering, while the exact dates appear below and inside each
report.

## Chronological reading guide

Lengths are approximate and exclude this index.

| Case | What happened | Length | When |
|---|---|---:|---|
| [`01-mnk-transfer.md`](01-mnk-transfer.md) | In a Rust and CUDA AlphaZero system for M,N,K games, a smaller-board checkpoint loaded into a larger-board network, but the campaign never established a benefit over matched scratch training. Several promising settings also produced a worse and more expensive combined result. | ~1,400 words | 2026-02-04 to 2026-02-22 |
| [`02-tactics-search.md`](02-tactics-search.md) | Autoresearch developed and tuned Tactics.md's hand-written Greedy and Heuristic agents across more than 24 million simulated games, then tested learned action search. One learned model reached 86.7% held-out accuracy but won only 10% against the simpler Greedy agent because useful actions were pruned before deeper evaluation. | ~1,300 words | 2026-03-07 to 2026-04-07 |
| [`03-tactics-cpu-optimization.md`](03-tactics-cpu-optimization.md) | Over two days, Codex tested 102 engine interventions on the CPU pipeline generating training games for a hex-grid tactics AI, accelerating turn search and quantized neural evaluation while uncovering eight correctness defects. Local benchmarks repeatedly misled; only full-turn replay and end-to-end self-play could distinguish real speedups from changed game behavior. | ~1,000 words | 2026-03-10 to 2026-03-11 |
| [`04-gradient-bang-automation.md`](04-gradient-bang-automation.md) | A Gradient Bang headless client completed live trading, combat, fleet, and exploration workflows and reached contemporaneous visible ranks of 29 in exploration and 27 in trading. Parallel probe agents then began consuming one another's completion events. | ~1,350 words | 2026-04-14 to 2026-04-16 |
| [`05-tactics-neural-evaluators.md`](05-tactics-neural-evaluators.md) | Autoresearch trained neural models to evaluate positions inside a hex-grid tactics AI, testing architecture size, training targets, quantization, and self-play across 435 result bundles. Under the same 10 millisecond move budget, a model that evaluated each position 73 times more slowly still won because its judgments were better, while the model with the best validation loss played worst among matched candidates. | ~1,200 words | 2026-04-15 to 2026-05-08 |
| [`06-multi-llm-trading-research.md`](06-multi-llm-trading-research.md) | Six LLM routes helped build and operate an automated trading-research loop. An independent GPT-5.6-sol audit read the raw experiment record, recovered omitted phases, found reproducibility gaps and proposals mistaken for implemented work, and reduced deployment optimism. Later causal corrections invalidated the leading results, showing why agreement among models was not validation. | ~1,250 words | 2026-06-22 to 2026-07-10 |
| [`07-flysim-sim-to-live.md`](07-flysim-sim-to-live.md) | FlySim trained flight-control policies in a public JAX simulator, then a private overlay tested a frozen policy in a live external flight application. When a half-second handoff clipped 14% of controls, replaying the exact safety-filtered inputs showed that the simulator underrepresented the live aircraft's roll and yaw response. Retraining fixed the clipping without weakening the live safety limits. | ~1,000 words | 2026-07-08 to 2026-07-27 |
| [`08-multi-model-game-playtesting.md`](08-multi-model-game-playtesting.md) | Six model families independently managed parties, edited character tactics, and revised strategies against a deterministic battle simulator. Their disagreements prevented premature game-design changes and exposed tool-assisted play that violated the rules, but even unanimous AI feedback could not show whether human players would understand or enjoy the game. | ~1,700 words | 2026-08-02 to 2026-08-09 |
| [`09-freetranscribe-gpu-inference.md`](09-freetranscribe-gpu-inference.md) | FreeTranscribe.org doubled transcription throughput with fewer errors while sharing one RTX 3090 between live production and autoresearch. | ~1,500 words | 2026-08-06 to 2026-08-08 |
| [`10-trading-strategy-search.md`](10-trading-strategy-search.md) | Autoresearch tested low thousands of quantitative-trading rules across nearly one hundred batches while reserving a sealed future period for final evaluation. Real deployment costs overturned the leading results, many supposedly different strategies made the same trades, and the long-running agent sometimes stopped researching even while its process remained alive. | ~950 words | 2026-08-08 to 2026-08-10 |

These are practitioner reports, not independent replications. Model observations are conditional on
the calendar period, provider route, prompt, tools, and harness maturity. Calendar and infrastructure
backfills should update both the individual case and this index.

Case-study conclusions are scoped to their recorded infrastructure. Newer evidence does not win merely
because it is newer, but evidence from a more controlled and representative harness should supersede a
conflicting older observation unless the older mechanism is independently reproduced.
