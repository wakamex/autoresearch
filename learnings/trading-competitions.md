# Trading-competition autoresearch

Scope: Statistical validation, competition mechanics, execution, risk, and promotion criteria for autonomous trading research.
Case-study basis: None for the competition protocol. Applied trading observations are reported
separately in Cases 03 and 07 under `case-studies/`.
External-review basis: `external-review/README.md`.

## Bottom line

The existing corpus has a strong architecture for autonomous experimentation: fixed evaluators, persistent ledgers, hypothesis trees, isolated branches, keep-or-revert decisions, held-out gates, and explicit research contracts. The main gap was statistical and competition-specific. A trading autoresearch system can follow that architecture perfectly and still select noise, exploit its simulator, or optimize a leaderboard objective that has little relationship to durable trading profit.

For trading competitions, the correct design is a two-objective system:

1. Estimate the probability of placing highly under the exact contest rules and likely opponent field.
2. Refuse strategies whose apparent contest advantage depends on ruinous tail risk, invalid volume, hidden leakage, unrealistic execution, or repeated selection on the confirmation data.

Search should be broad. Evidence should be narrow. Parallel branches, diverse agents, and stepping stones improve discovery, but only sealed, time-ordered, cost-complete tests can promote a candidate.

## Evidence hierarchy

The sources do not deserve equal weight.

| Tier | Source type | Appropriate use |
|---|---|---|
| A | Peer-reviewed or working papers, benchmark documentation, official scoring documentation | Statistical design, evaluation protocol, documented competition-wide results |
| B | Organizer retrospectives and detailed contestant or winner writeups | Competition mechanics, execution failure modes, practical search tactics |
| C | Project READMEs, blog claims, social posts, and curated project lists | Hypothesis generation and implementation patterns only |

Self-reported benchmark scores and winner explanations are not independent validation. Winner writeups are especially survivor-selected. Their engineering lessons can be useful even when their claimed edge cannot be generalized.

## What the original corpus establishes

Across Arbor, Autoresearch Agents, Curie, EurekAgent, MLE-bench, RE-Bench, Prime Agent, Darwin Gödel Machine, the Paradigm challenge writeup, David Gasquez's essays, and the Awesome Autoresearch collection, the recurring high-value principles are:

- Freeze the evaluator, data contract, resource budget, and allowed edit surface before search.
- Keep a complete experiment ledger with hypothesis, change, configuration, code hash, data hash, result, failure reason, and decision.
- Isolate branches so experiments do not contaminate one another.
- Separate discovery from held-out promotion.
- Preserve lineage and useful stepping stones. Greedy selection can discard intermediate ideas that later combine well.
- Make failures legible. Dead-end ledgers and explicit keep-or-revert decisions prevent repeated work.
- Put evaluator and integrity checks outside the agent's writable environment.
- Expect reward hacking. The DGM and Prime Agent accounts show that an agent may exploit the evaluator despite explicit instructions not to cheat.
- Use fresh seeds, resets, and from-scratch branches when the search plateaus.
- Treat public leaderboard feedback as adaptive information, not as an untouched test.

The Paradigm PM challenge is a particularly useful warning. Its winner reports 1,039 variants and more than 2,000 evaluations, used fresh seeds near the end, and still saw a final result below the public leaderboard result. The account also documents simulator-specific exploits and disqualifications. This is strong evidence for search tactics, but also strong evidence that a public score can become an optimization target rather than a measure of general trading ability.

## New statistical lessons

### Ordinary holdout is not enough after adaptive search

The Probability of Backtest Overfitting paper explains why a conventional train-test split can become unreliable when researchers repeatedly choose the best result among many alternatives. Combinatorially symmetric cross-validation estimates how often the in-sample winner falls below the median out of sample and measures performance degradation.

The Deflated Sharpe Ratio corrects an observed Sharpe ratio for multiple selection, sample length, skewness, and kurtosis. Its practical message is more important than any particular formula: all attempted variants contribute to the selection burden. Trials should be planned from investment hypotheses, not generated without limit because compute is cheap.

Consequences for autoresearch:

- Count agent branches, parameter sweeps, prompt revisions, feature choices, market choices, and reruns as trials.
- Record discarded and failed trials, not only successful ones.
- Estimate effective trial count conservatively when trials are correlated.
- Report a selection-adjusted statistic such as DSR and, where the return matrix permits it, PBO through CSCV.
- Never reuse a touched holdout as promotion evidence.
- After two failed interventions at one gate, audit the premise and require a new hypothesis rather than widening the sweep.

### Time order and label overlap matter

Numerai's published benchmark construction is a concrete pattern: walk-forward validation trains only on information available before the prediction, with an explicit purge between training and validation windows. Its current 20-day target example uses 156-era validation chunks and an 8-era purge.

For trading, use expanding or rolling walk-forward evaluation with a purge and, when positions or labels overlap, an embargo. Random cross-validation is inappropriate. Data timestamps must represent when information was actually available, not when it was later recorded or revised.

### Live history is harder to game than a resettable score

Numerai keeps model history permanent and warns users not to overuse validation diagnostics. That design blocks selective deletion of bad rounds. Our ledger should have the same property. A new idea gets a new identity and lineage rather than rewriting the history of the old one.

## New competition lessons

### Winning rank and maximizing expected return are different objectives

The M6 luck and strategy analysis finds that the extreme observed Sharpe ratios were compatible with chance after accounting for the number of teams. In its stylized and bootstrap analyses, optimizing the probability of a high rank produced a different portfolio from maximizing expected Sharpe. The rank-oriented approach improved podium probability while increasing the probability of finishing near the bottom and lowering expected Sharpe.

This is directly relevant whenever prizes depend on relative ranks or a nonlinear points table. A contest simulator must model the field and estimate probabilities of each finishing rank, not merely optimize the expected raw metric. However, the strategy must also pass a predeclared survival veto. A higher podium probability is not acceptable if it comes from an unbounded loss tail or likely account ruin.

### Short competitions are dominated by variance

M6 ran across 12 non-overlapping four-week periods and still found that none of the teams beat its investment benchmark in every month. Only three teams beat the forecasting benchmark in every month, and only 26 of 163 teams completed every period. Its follow-up luck analysis found no sufficient evidence that the extreme Sharpe ratios exceeded what chance could produce across the field.

A 48-hour contest result is therefore weak evidence of persistent alpha. It can still be the correct prize objective, but internal evaluation must use many historical or replayed 48-hour windows and report a distribution:

- Median, lower decile, and upper decile net P&L
- Probability of loss and probability of breaching the loss cap
- Gross legitimate filled notional
- Fees, funding, rebates, slippage, and adverse-selection cost
- Maximum inventory, margin utilization, drawdown, and liquidation frequency
- Uptime, rejected orders, stale-data time, and recovery behavior
- Simulated probability of each finishing rank under plausible opponent fields

### Forecast quality is not trading value

The M6 competition found almost no overall relationship between forecasting and investment performance. Its strongest forecasting teams often formed inefficient portfolios, while strong investment teams had mixed forecast accuracy. The HEFTcom energy competition similarly found that decision-making under uncertainty was about as important as forecast skill. Its strategic bidding improvements were economically comparable to a large forecast-accuracy improvement.

The practical unit of research is therefore the complete policy:

data -> state estimate -> fair value or forecast -> position target -> order choice -> fill -> inventory and risk response -> net result

Signal-only studies cannot promote a trading strategy. A signal should be evaluated by its incremental value after position sizing, execution, and risk management.

### Execution edge can dominate model edge

The UChicago winner's market-making account attributes much of its advantage to trading more aggressively while managing position limits and inventory better than competitors. Its useful components are fair value, competitive quoting, inventory fade, book-aware edge, and live observability.

The 2026 UChicago account provides the counterexample. Its fair-value model reportedly remained accurate, but fixed order sizes, market-order slippage, thinner books, costly unwinds, and a non-adaptive edge threshold degraded the result. This supports layer-specific diagnosis: when the model remains calibrated but realized P&L fails, test execution before changing the signal.

Human parameter tuning in those simulator contests is not transferable to an unattended contest. The equivalent controls must be deterministic, bounded, tested, and observable before the run.

### Volume is not free

Hummingbot's Gate.io retrospective reports $10.2 million of volume and $4,991 of exchange fees, or about 4.9 basis points of fees per dollar of reported volume in aggregate. The actual cash prize pool was $1,279.20 after a misunderstanding about an advertised maximum. This does not estimate the economics of a new event, but it demonstrates two mandatory checks:

- Independently reconstruct the complete fee, rebate, reward, and eligibility function.
- Optimize net prize-adjusted value, not volume in isolation.

Volume that pays more in fees and adverse selection than it earns in spread, rebates, P&L points, and expected prize value is not an edge. Self-trading, wash volume, or other invalid activity must be impossible by construction.

### Live competition design improves integrity

M6 and HEFTcom used repeated live submissions. HEFTcom notes that live operation prevented future-data leakage and exposed missing data, technical failures, and unexpected events. It also shows the burden: even capable teams struggled early or missed submissions. Reliability is part of performance, not an implementation detail.

## Recommended trading-competition autoresearch protocol

### Phase 0 - Mechanism audit

Before strategy work, write a research contract containing:

- Exact scoring and rank conversion
- Eligible venues, markets, instruments, and order types
- Starting capital, leverage, margin, liquidation, and final valuation rules
- Fee and rebate tier actually loaded on the contest account
- Funding, borrow, gas, and settlement rules
- Volume attribution and excluded activity
- Runtime, forced close behavior, and human-intervention policy
- Submission limits and whether entries compete independently
- Safety limits and disqualification conditions

Unresolved rules become explicit scenarios or blockers. They do not become favorable assumptions.

### Phase 1 - Baseline and cheapest falsification

Build the simplest valid baseline and test the premise before adding complexity. Examples include passive inventory-constrained quoting, buy-and-hold, flat/no-trade, and a simple directional rule. Include all costs. If the proposed mechanism cannot beat the relevant simple baseline under optimistic but plausible execution, stop that branch.

### Phase 2 - Discovery

Use parallel, isolated branches and a hypothesis tree. Each experiment changes one causal factor unless an interaction is the declared hypothesis. Discovery may use many walk-forward windows, but every trial is logged and contributes to the multiple-testing count.

Retain candidates on a Pareto frontier rather than collapsing everything prematurely into one score. The core axes are net P&L, legitimate volume, downside risk, and reliability. A contest-points estimate may be shown, but uncertain opponent normalization should not hide raw economics.

### Phase 3 - Sealed promotion

Promote only against untouched, time-ordered windows that match the contest horizon. Predeclare thresholds for median net P&L, lower-tail loss, drawdown, volume, and failure rate. Report DSR and PBO where applicable. Use several seeds for stochastic components and resample whole market blocks rather than individual ticks.

Discovery results cannot become promotion evidence. If a confirmation window informs another change, it moves into the development set and a new sealed window is required.

### Phase 4 - Execution replay

Replay event-level books where available. Model or measure:

- Queue position and maker fill probability
- Partial fills and cancel latency
- Taker slippage and book impact
- Rate limits, websocket gaps, clock skew, reconnects, and duplicate events
- Minimum order sizes, precision, balances, and margin reservations
- Funding, fees, rebates, borrow, gas, and forced final liquidation
- Competition from other makers and changing liquidity through the run

Bar-based fills are discovery evidence only unless the strategy is genuinely insensitive to intrabar path and queue mechanics.

### Phase 5 - Forward validation

Run shadow, paper, and then minimum-size live tests without manual rescue. Use the same deployment path, account permissions, configuration, and monitoring intended for the contest. Persist the loaded configuration and code hash, not merely the intended files.

### Phase 6 - Freeze and rehearsal

Freeze code, model, dependencies, configuration, and risk limits. Rehearse at least one full contest-duration run. The runtime should have a single order writer, idempotent recovery, stale-data guards, bounded inventory, kill conditions, and an auditable event log.

## Promotion card

Every proposed finalist should fit on one promotion card:

| Field | Required evidence |
|---|---|
| Mechanism | Why the edge should exist and who pays for it |
| Search burden | All variants and effective independent-trial estimate |
| Data | Source, availability timestamps, hashes, gaps, and exclusions |
| Validation | Walk-forward schedule, purge, embargo, sealed windows, and seeds |
| Economics | Net P&L, volume, fees, rebates, funding, slippage, and final close |
| Risk | Drawdown, loss probability, liquidation, inventory, and scenario shocks |
| Rank | Podium probability across plausible opponent fields and score mappings |
| Reliability | Full-duration uptime, recovery tests, rejected orders, and stale time |
| Integrity | Evaluator isolation and proof that scoreable volume and fills are valid |
| Decision | Promote, revise under a new hypothesis, or stop |

## Stop and reset rules

- Give each hypothesis an attempt limit, time limit, and scope-escape condition before it starts.
- After two failed interventions at the same gate, audit the premise and require a materially new hypothesis.
- Stop a branch whose best case fails after realistic fees or whose edge disappears under a modest execution perturbation.
- Reset from scratch when a branch plateaus and accumulated complexity no longer has an ablation-supported contribution.
- Do not promote because budget is exhausted or the public leaderboard looks favorable.
- Preserve failed experiments and weak ancestors. They remain useful for avoiding repeats and for future recombination.

## Evidence map

The public evidence inventory, source contributions, and attribution limits are maintained in
[`external-review/`](external-review/README.md).
