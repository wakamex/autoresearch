# Case 10 - Adaptive quantitative-trading strategy search

Observation window: 2026-08-08 through 2026-08-11
Disclosure mode: anonymized
Duration: four calendar days, including one concentrated eight-hour campaign
Application domain: quantitative trading; project identity and asset class withheld

## What was researched

The campaign searched over rules for a quantitative trading strategy using time-ordered historical
data. Its first phase tested low thousands of related variants across nearly one hundred batches. Its
latest phase changed the unit of work: each model cycle had to propose one causal mechanism, implement
one complete strategy, and evaluate it once across the full market panel. Future data remained
untouched for final testing.

The practical questions were whether a proposed rule still worked after realistic costs, whether
apparently different variants actually produced different trades, whether combining strategies added
diversification, and whether a long-running agent was continuously testing useful hypotheses.

## Exposure

- Usage pattern: one concentrated campaign with repeated experimental batches and follow-up audits.
- Project phases: exploration, implementation, optimization, portfolio evaluation, validation design, and deployment preparation.
- Search intensity: very high.
- Parallelism: primarily sequential execution with limited parallel proposal work.
- Human involvement: frequent steering, especially for research direction, premise audits, and resource allocation.
- Resource intensity: heavy relative to the project, with exact token and route-cost accounting in the latest panel.
- Breadth: project-wide methodology spanning data contracts, evaluators, search, research memory, orchestration, and decision review.
- Decision influence: critical to several major decisions.

## Infrastructure context

The campaign began on 2026-08-08 with a basic deterministic harness, a small append-only ledger, and
useful artifact hashes, but no isolated workers, persistent conductor, sealed promotion route, general
recovery, or progress-freshness monitor. By 2026-08-10 it had disposable worktrees, strict manifests,
structured transaction and campaign records, causal replay, explicit evidence labels, a reserved
sealed epoch, and bounded recovery on the strict path.

On 2026-08-11, the campaign froze one synchronized multi-market development snapshot, added a shared
portfolio budget and deterministic event ordering, and gave strategy agents isolated worktrees. A
seeded route scheduler balanced exploitation with random exploration and starvation
protection. The eight-hour campaign completed 46 route cycles, implemented 39 strategies, and retained
35 causally valid results. It included 12 new mechanisms and 16 interactions or portfolio-aware
policies, with no infrastructure-only batch.

The evaluator remained worker-editable and the rolling agent session still acted as director. The
sealed future period remained untouched and no promotion run occurred.

## Project impact

Autoresearch built a reproducible evaluation pipeline, searched broadly, exposed false premises, and
then improved its own research method. Replacing nearby parameter variants with mechanism-first cycles
produced clearer strategy diversity. Shared-capital replay found one slightly positive selective
controller and several distinct tradeoffs between profit and trading volume that independent
per-market tests had hidden.

The latest no-wait contract also sustained continuous useful work across 46 route cycles. This
superseded the early impression that Codex could not maintain broad search, while confirming that a
duration request alone was not enough.

## Main findings

### Replay strategies against the resources they actually share

The earlier evaluator gave every market an independent capacity limit. Every normal-sized strategy
remained negative after costs under that assumption. The August 11 evaluator instead merged markets in
receive-time order and made them compete for one portfolio budget. Under that shared budget, one
selective controller became slightly positive while retaining about 41% of baseline volume. Several
other strategies formed useful intermediate PnL-volume tradeoffs.

Independent component tests can explain mechanisms, but they do not establish a feasible portfolio
when components compete for capital, inventory, risk, or another shared resource.

### Search for different mechanisms, not thousands of nearby settings

The first campaign explored low thousands of correlated variants. The later campaign ran 46
mechanism-first cycles and retained 35 valid results, including new mechanisms and portfolio-aware
interactions. One learned controller combined with a causal asymmetry controller to reduce the fixed
baseline loss by about 55% and beat both declared parents.

Behavior signatures and exact-parent comparisons made the evidence easier to interpret. Parameter
tuning still had value after a mechanism worked, but it no longer counted as independent research
diversity.

### Allocate model routes by research yield and cost

The latest 20-cycle GPT-5.6 panel treated each model and effort combination as a separate choice. Luna
medium and Sol medium both completed every assigned cycle with similar research ratings. Luna medium
was faster and cost about $0.16 in API-equivalent usage per valid result, compared with about $3.40 for
Sol medium. Sol still produced distinct valuable strategies that a cheapest-only policy could have
missed.

The practical allocation was to exploit the inexpensive reliable route while reserving exploration
for more expensive routes. Quality, completion rate, wall time, and cost remained separate measures.

### Real deployment settings can invalidate the whole search

A documented default cost setting was later replaced by the value actually loaded for deployment.
Rerunning unchanged representative strategies under the real setting overturned much of their
apparent viability and changed the research direction. Earlier results remained valid only for their
recorded hypothetical costs.

Premise-sensitive configuration should therefore be observed before broad search where possible. When
it changes, replay a compact unchanged representative set before continuing.

### A scenario name must include every setting that can change behavior

Changing one cost in a saved report did not reproduce the full deployment scenario because another
path-dependent cost was still baked into the original trades. Repricing old results is valid only when
the strategy would make the same decisions and every affected quantity was saved. Otherwise rerun the
strategy under the complete scenario.

### Similar-looking strategies should be grouped before combining them

Many tuned strategies were minor variations that made nearly the same trades. Counting them as
independent ideas would have made one crowded family look artificially diverse. Grouping candidates by
mechanism and actual behavior revealed the smaller set of distinct approaches worth combining. The
latest mechanism-first campaign confirmed this diagnosis while producing clearer diversity.

### Telling an agent to work for hours does not keep it doing research

Asking the agent to keep working for a long duration did not initially make it continuously test
hypotheses. An explicit no-wait contract, route scheduler, bounded failures, atomic results, and a
required closeout report later sustained 46 cycles. The problem was the operating contract, not an
inherent inability of Codex to continue research.

### Build a tool only when a specific experiment needs it

Supporting tools were valuable but could become the default activity. Requiring every proposed tool
to name the experiment it would unblock kept the campaign focused without weakening integrity checks.

## Model observations

The latest panel compared GPT-5.6 Luna at medium and xhigh effort, Sol at medium and xhigh effort, and
Terra at high effort through the same AOP harness. Successful Luna and Sol cycles received similar
research ratings, but completion, time, and API-equivalent cost differed materially. Luna medium was
the best observed exploitation route. Sol remained useful for exploration because its more expensive
cycles produced important strategies. Terra produced one strong result but two no-result cycles.

Across routes, Codex remained effective at repository inspection, deterministic evaluator work,
causal experiment plumbing, and bounded implementation. The explicit no-wait campaign superseded the
earlier claim that it could not sustain broad search. Route rankings remain tied to the recorded model,
effort, harness, prompt, caching, and pricing.

## Provisional findings

- Soft family attractiveness with a small exploration floor may preserve reversibility better than permanent closure.
- Scheduled unrestricted ideation may counter local search, but its causal value was not established.
- Exact allocation and regularization rules need more untouched transitions before promotion.

## Evidence limits

This is an anonymized practitioner report, not independent replication. It retains generic campaign
counts, public model routes, and API-equivalent cost comparisons while omitting project identity,
asset class, instruments, markets, private configurations, and strategy details. Candidate results
used adaptively reused development data; future final-test data remained untouched.
