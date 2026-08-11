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
| [`02-tactics-search.md`](02-tactics-search.md) | Tactics.md evaluated interpretable agents across more than 24 million simulated games. In one learned-search round, 86.7% held-out policy top-1 accuracy on all-draw targets still translated to only 10% against Greedy. Full-breadth search showed that useful actions were being pruned before deeper evaluation. | ~1,300 words | 2026-03-07 to 2026-04-07 |
| [`03-tactics-performance.md`](03-tactics-performance.md) | Five Tactics.md benchmark runs varied by only 0.52%, but they measured different random workloads. The campaign found eight correctness and exactness defects, while a 13% microbenchmark win became a 3.7% end-to-end regression. | ~1,000 words | 2026-03-10 to 2026-03-11 |
| [`04-gradient-bang-automation.md`](04-gradient-bang-automation.md) | A Gradient Bang headless client completed live trading, combat, fleet, and exploration workflows and reached contemporaneous visible ranks of 29 in exploration and 27 in trading. Parallel probe agents then began consuming one another's completion events. | ~1,350 words | 2026-04-14 to 2026-04-16 |
| [`05-tactics-fixed-budget-models.md`](05-tactics-fixed-budget-models.md) | A Tactics.md leaf evaluator that was 73 times slower still won by 62 Elo under the same 10 millisecond move budget. Among three otherwise matched models, the one with the best validation loss produced the worst playing strength. | ~1,200 words | 2026-04-15 to 2026-05-08 |
| [`06-llm-governance.md`](06-llm-governance.md) | Different LLMs were useful for proposing, implementing, judging, and auditing. A scarce high-capability model produced its clearest value in judgment, but cross-model agreement still did not count as validation. | ~1,250 words | 2026-06-22 to 2026-07-10 |
| [`07-sim-to-live-orchestration.md`](07-sim-to-live-orchestration.md) | A live failure looked like an interface problem. Exact replay located a model-coverage gap, allowing the live safety boundary to remain intact. | ~900 words | 2026-07-08 to 2026-07-27 |
| [`08-multi-agent-playtesting.md`](08-multi-agent-playtesting.md) | Six model families independently playtested the same system. Their disagreements prevented wrong-layer changes, exposed invalid tool-assisted evidence, and showed why unanimous AI feedback still could not validate human experience. | ~1,500 words | 2026-08-02 to 2026-08-09 |
| [`09-freetranscribe-gpu-inference.md`](09-freetranscribe-gpu-inference.md) | FreeTranscribe.org doubled transcription throughput with fewer errors while sharing one RTX 3090 between live production and autoresearch. | ~1,500 words | 2026-08-06 to 2026-08-08 |
| [`10-adaptive-search.md`](10-adaptive-search.md) | A corrected runtime setting changed the research premise, many supposedly different candidates behaved identically, and a long-running campaign still failed to schedule useful work continuously. | ~750 words | 2026-08-08 to 2026-08-10 |

These are practitioner reports, not independent replications. Model observations are conditional on
the calendar period, provider route, prompt, tools, and harness maturity. Calendar and infrastructure
backfills should update both the individual case and this index.

Case-study conclusions are scoped to their recorded infrastructure. Newer evidence does not win merely
because it is newer, but evidence from a more controlled and representative harness should supersede a
conflicting older observation unless the older mechanism is independently reproduced.
