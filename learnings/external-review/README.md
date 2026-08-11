# External autoresearch review

Scope: Public evidence, source contributions, and attribution limits behind the autoresearch methodology synthesis.
Evidence boundary: External public sources only. Applied project evidence belongs under `../case-studies/`.

This document is the public evidence map for the learnings in this repository. It links directly to
primary public sources rather than republishing local copies. Private project records are excluded;
general workflow observations derived from them are synthesized separately in
[`agent-search-retrospective.md`](../agent-search-retrospective.md).

Raw source snapshots used during review are retained locally under `.local/source-archive/`. That
directory is ignored and is not part of the public evidence package.

## Evidence hierarchy

| Tier | Evidence type | Appropriate use |
|---|---|---|
| A | Peer-reviewed papers, working papers, benchmark documentation, and official scoring documentation | Statistical design, evaluation protocol, and documented aggregate results |
| B | First-party system documentation, organizer retrospectives, and detailed contestant writeups | Architecture, operating practice, competition mechanics, and failure modes |
| C | Project READMEs, first-party blogs, and self-reported benchmark results | Implementation patterns and hypothesis generation |
| D | Social posts and curated catalogs | Discovery leads and concise practitioner observations |

Self-reported results are not independent replication. Winner accounts are survivor-selected. Their
engineering lessons may be useful even when their claimed performance does not generalize.

## Core autoresearch evidence

| Public source | Evidence type | Main contribution |
|---|---|---|
| [Karpathy Autoresearch](https://github.com/karpathy/autoresearch) | Project documentation | Minimal fixed-budget loop, protected preparation code, mutable training implementation, and keep-or-revert decisions |
| [Paradigm Prediction Market Challenge writeup](https://github.com/ryanli-me/paradigm-pm-challenge/blob/main/WRITEUP.md) | Winner writeup | Broad parallel search, repeated evaluation, fresh seeds, shared learnings, resets, and simulator-exploitation warnings |
| [Awesome Autoresearch](https://github.com/yibie/awesome-autoresearch) | Curated catalog | Broad inventory of implementations and adjacent practices; useful for source discovery rather than validation |
| [OpenAI MLE-bench](https://github.com/openai/mle-bench) | Benchmark documentation | Repeated agent seeds, resource normalization, protected solutions, and comparability limitations |
| [EurekAgent](https://github.com/THU-Team-Eureka/EurekAgent) | Project documentation | Permission, artifact, budget, and human-interface engineering with a private evaluator |
| [Arbor](https://github.com/RUC-NLPIR/Arbor) | Project documentation | Coordinator and executor separation, hypothesis trees, fresh worktrees, and held-out merge decisions |
| [RE-Bench](https://github.com/METR/RE-Bench) | Benchmark documentation | Standardized bounded research tasks and benchmark-contamination protection |
| [Darwin Gödel Machine](https://github.com/jennyzzt/dgm) | Project documentation | Archive-based self-improvement, stepping stones, generated-code risk, and preserved lineage |
| [Sakana AI on Darwin Gödel Machine](https://sakana.ai/dgm/) | First-party article | Open-ended search, transferable improvements, diversity, and evaluator exploitation |
| [Curie](https://github.com/Just-Curieous/Curie) | Project documentation | End-to-end experiment rigor, verification, reproducibility, and durable reports |
| [Autoresearch for Agents](https://github.com/hwchase17/autoresearch-agents) | Project documentation | Small direct adaptation of mutable implementation and fixed evaluator boundaries |
| [Prime Agent announcement](https://x.com/PrimeIntellect/status/2085094906603897057) | First-party social thread | Concise architecture and evaluation claims for persistent agent sessions |
| [Prime Agent article](https://www.primeintellect.ai/blog/prime-agent) | First-party article | Persistent context, multi-agent communication, continual harness refinement, and reward-hacking evidence |
| [David Gasquez on autoresearch](https://x.com/davidgasquez/status/2030946939836022886) | First-party social post | Compact claim connecting autoresearch loops to benchmarkable competition work |
| [LLM Friendly Projects](https://davidgasquez.com/llm-friendly-projects) | First-party article | Inspectable pipelines, logs, temporary workspaces, and experiment tracking |
| [Transparent and Effective ML Competitions](https://davidgasquez.com/steering-ais/) | First-party article | Transparent evaluation, reproducibility, Goodhart risk, and identity concerns |

## Trading and statistical evidence

| Public source | Evidence type | Main contribution |
|---|---|---|
| [The Probability of Backtest Overfitting](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf) | Paper | Combinatorially symmetric cross-validation, selection overfitting, and performance degradation |
| [The Deflated Sharpe Ratio](https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf) | Paper | Correction for multiple selection, sample length, skewness, and kurtosis |
| [M6 Investment Challenge: Luck and Strategy](https://arxiv.org/pdf/2412.04490) | Paper | Luck across a competitor field and the difference between rank optimization and expected performance |
| [The M6 Forecasting Competition](https://arxiv.org/pdf/2310.13357) | Paper | Repeated live evaluation, simple baselines, and weak linkage between forecast and investment performance |
| [Hybrid Renewable Energy Forecasting and Trading Competition](https://arxiv.org/pdf/2507.01579) | Paper | Forecast value versus decision value, live reliability, and operational burden |
| [Numerai tournament scoring](https://docs.numer.ai/numerai-tournament/scoring) | Official documentation | Permanent live history and warnings against repeated validation use |
| [Numerai walk-forward models](https://docs.numer.ai/numerai-tournament/models) | Official documentation | Time-ordered validation and published purge construction |
| [Building a Futures Market Making Bot](https://tianyi.io/post/chicago1/) | Contestant writeup | Fair value, competitive execution, inventory response, and observability |
| [UChicago Trading Competition 2026](https://www.cs.utexas.edu/~kavish/blog/uchicago-trading-competition-2026.html) | Contestant writeup | Execution-regime failure despite a reportedly stable predictive model |
| [Gate.io Trading Competition Retrospective](https://hummingbot.org/blog/gateio-trading-competition-results-and-retrospective/) | Organizer retrospective | Fee burden, reward-rule verification, and the difference between volume and net value |

## Attribution cautions

- The Paradigm writeup documents independent parallel agents, but does not establish that every worker
  used a Git worktree, a fresh provider session, or an append-only learning file.
- Karpathy Autoresearch, the Paradigm challenge, and OpenAI MLE-bench are separate projects and should
  not be conflated.
- The David Gasquez social post is a compact application claim, not a detailed run report.
- Public leaderboard results and winner explanations are adaptive and survivor-selected evidence.
- Project READMEs establish intended architecture and reported behavior, not independent reliability.
- Validation methods should match the actual uncertainty rather than copying seed counts or holdout
  structures mechanically from another domain.

## Review method

Repository sources were reviewed at pinned revisions. Web extractions were checked at the beginning,
middle, and end for correct content and reading order. PDF conversions were checked for title,
authors, page order, midpoint, ending, references, and page count. A dynamic page that returned
unrelated content was rejected rather than retained as evidence.

The public bibliography points to current canonical sources. Exact local snapshots and their hashes
remain local research artifacts rather than published repository content.
