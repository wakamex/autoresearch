# Autoresearch case studies

These are ten chronological reports from projects where I used autoresearch. Some describe public
projects in full; others generalize private work without revealing the project or application.

Each report explains when and how intensively I used autoresearch, what infrastructure existed at the
time, which models did what, what changed because of the work, and which lessons still appear useful.
The case number provides chronological ordering, while the exact dates appear below and inside each
report.

## Chronological reading guide

Lengths are approximate and exclude this index.

| Case | What happened | Length | When |
|---|---|---:|---|
| [`01-february-transfer-learning.md`](01-february-transfer-learning.md) | A pretrained model transferred cleanly, but the campaign never established that it beat matched training from scratch. Several individually promising settings also produced a worse and more expensive combined result. | ~1,400 words | 2026-02-04 to 2026-02-22 |
| [`02-march-april-policy-search.md`](02-march-april-policy-search.md) | A learned search component improved at predicting its own targets while end-to-end behavior remained weak or collapsed. A simple full-breadth control located the failure in premature truncation and target generation. | ~1,400 words | 2026-03-07 to 2026-04-07 |
| [`03-mid-march-performance.md`](03-mid-march-performance.md) | Several local speedups disappeared or reversed after controlling the workload and checking the complete stateful operation. | ~800 words | 2026-03-10 to 2026-03-11 |
| [`04-mid-april-headless-automation.md`](04-mid-april-headless-automation.md) | Parallel agents were consuming one another's completion events. Reliable live automation required binding every action and observation to the correct transaction. | ~1,350 words | 2026-04-14 to 2026-04-16 |
| [`05-april-may-fixed-budget.md`](05-april-may-fixed-budget.md) | A component that looked better in isolation was not always the best use of a fixed compute budget. Repeated operational evaluation could select an incumbent but could not provide fresh promotion evidence. | ~800 words | 2026-04-15 to 2026-05-08 |
| [`06-june-july-governance.md`](06-june-july-governance.md) | Different LLMs were useful for proposing, implementing, judging, and auditing. A scarce high-capability model produced its clearest value in judgment, but cross-model agreement still did not count as validation. | ~1,250 words | 2026-06-22 to 2026-07-10 |
| [`07-july-sim-to-live-transfer.md`](07-july-sim-to-live-transfer.md) | A live failure looked like an interface problem. Exact replay located a model-coverage gap, allowing the live safety boundary to remain intact. | ~900 words | 2026-07-08 to 2026-07-27 |
| [`08-early-august-model-evaluation.md`](08-early-august-model-evaluation.md) | AI evaluators found real wording and evidence problems, but their broader product judgments changed with prompt framing, tool access, provider state, and reused fixtures. | ~1,050 words | 2026-08-02 to 2026-08-09 |
| [`09-early-august-production-optimization.md`](09-early-august-production-optimization.md) | Research and production safely shared one accelerator. The subtler failure was a healthy agent process that had stopped producing research progress. | ~1,250 words | 2026-08-06 to 2026-08-08 |
| [`10-early-august-adaptive-search.md`](10-early-august-adaptive-search.md) | A corrected runtime setting changed the research premise, many supposedly different candidates behaved identically, and a long-running campaign still failed to schedule useful work continuously. | ~750 words | 2026-08-08 to 2026-08-10 |

These are practitioner reports, not independent replications. Model observations are conditional on
the calendar period, provider route, prompt, tools, and harness maturity. Calendar and infrastructure
backfills should update both the individual case and this index.

Case-study conclusions are scoped to their recorded infrastructure. Newer evidence does not win merely
because it is newer, but evidence from a more controlled and representative harness should supersede a
conflicting older observation unless the older mechanism is independently reproduced.
