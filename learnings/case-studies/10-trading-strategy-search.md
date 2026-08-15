---
{
  "case": 10,
  "title": "Adaptive quantitative-trading strategy search",
  "started": "2026-08-08",
  "ended": "2026-08-11",
  "featured_rank": 3,
  "token_estimate": {"processed_tokens": 1150000000, "effective_tokens": 143000000, "confidence": "high"},
  "summary_markdown": "Quantitative-trading autoresearch sustained 46 agent-led research cycles in eight hours, implementing 39 strategies and retaining 35 development results that passed causal-attribution checks while sealed future data stayed untouched. Shared-capital replay mapped the development tradeoff between profit and volume. Gemini 3.6 Flash remained the historical bandit leader after completing 10 of 10 cycles; in a later panel, GPT-5.6 Luna medium received similar internal ratings to Sol medium at under one-twentieth the API-equivalent cost."
}
---

# Case 10 - Adaptive quantitative-trading strategy search

Observation window: 2026-08-08 through 2026-08-11
Disclosure mode: anonymized
Duration: four calendar days, including one concentrated eight-hour campaign
Application domain: quantitative trading; project identity and asset class withheld

## What was researched

The campaign searched over rules for a quantitative trading strategy using time-ordered historical
data. Its first phase tested low thousands of related variants across nearly one hundred batches. Its
latest phase changed the unit of work: each model cycle had to propose one causal mechanism, implement
one complete strategy, and evaluate it once across the full market panel. A labeled sealed future
period remained untouched for a later final test.

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
protection. The eight-hour campaign completed 46 research cycles and implemented 39 strategies. Of 36
full-panel evaluations, 35 passed the campaign's causal-attribution checks; one was excluded after its
action timing violated the declared delay. The campaign included 12 new mechanisms and 16 interactions
or portfolio-aware policies, with no infrastructure-only batch.

The evaluator remained worker-editable and the rolling agent session still acted as director. The
sealed future period remained untouched and no promotion run occurred.

## Project impact

Autoresearch built a reproducible evaluation pipeline, searched broadly, exposed false premises, and
then improved its own research method. The early phase tested low thousands of correlated variants.
The later 46-cycle phase instead implemented 11 established-family variants, 12 new mechanisms, and 16
interactions or portfolio-aware policies. It retained losses, one causally invalid evaluation, one
duplicate, and nine cycles without an evaluation rather than presenting only successful work.

Shared-capital replay then mapped several tradeoffs between profit and trading volume under one
portfolio budget. One newly implemented selective controller was slightly positive on the reused
development snapshot. This was a useful discovery result, not evidence of deployable profitability.

The latest no-wait contract sustained the full eight-hour campaign through 46 research cycles with no
infrastructure-only batch. This superseded the early impression that Codex could not maintain broad
search, while confirming that a duration request alone was not enough.

## Main findings

### Replay strategies against the resources they actually share

The earlier evaluator gave every market an independent capacity limit even though deployment would use
one portfolio budget. Those results were useful mechanism tests, but they could not represent a
feasible combined portfolio. The August 11 evaluator corrected that mismatch by merging all markets in
receive-time order and rejecting inventory-increasing fills that exceeded one shared budget.

The campaign did not rerun one unchanged strategy under both capacity models. After correcting the
evaluator, it implemented new shared-capital strategies and compared them with a fixed baseline on the
same frozen, adaptively reused development snapshot. One selective controller was slightly positive
while the matched fixed baseline was negative, but the controller retained only about 41% of the
baseline volume. Other shared-capital strategies mapped intermediate profit-volume tradeoffs.

This supports the controller-versus-baseline comparison under the shared evaluator. It does not show
that the evaluator correction caused profitability, that the result will persist, or that deployable
alpha was discovered.

### Search for different mechanisms, not thousands of nearby settings

The first campaign explored low thousands of correlated variants. The later campaign ran 46
mechanism-first cycles, implemented 39 strategies, and retained 35 development results that passed its
causal-attribution checks. One interaction reduced the fixed baseline loss by about 55% and beat both
declared parents on the reused development snapshot.

Behavior signatures and exact-parent comparisons made the evidence easier to interpret. Parameter
tuning still had value after a mechanism worked, but it no longer counted as independent research
diversity.

### Allocate model routes by research yield and cost

The initial mixed-route phase gave Gemini 3.6 Flash medium ten cycles. It completed all ten and received
an 89.2 mean internal rating. Its final Beta-posterior mean was 0.78, the highest among active and
retired routes at the end of all 46 cycles. The route was retired from eligibility when the campaign
deliberately switched to a GPT-5.6-only panel, not because the scheduler rejected it. It therefore
remained the historical bandit leader but did not compete for later allocations.

The later adaptive panel treated each model and effort combination as a separate route:

| GPT-5.6 route | Cycles | Results passing checks | Mean internal rating | API-equivalent cost per result |
|---|---:|---:|---:|---:|
| Luna medium | 3 | 3 | 92.0 | $0.16 |
| Luna xhigh | 6 | 5 | 81.0 | $0.19 |
| Sol medium | 4 | 4 | 94.0 | $3.40 |
| Sol xhigh | 4 | 4 | 93.5 | $3.91 |
| Terra high | 3 | 1 | 44.3 | $3.30 |

After each deterministic evaluation, the rolling Codex director assigned the internal rating using a
fixed 100-point rubric covering contract compliance, causal clarity, behavioral novelty, experiment
design, information gain, and efficiency. Ratings included capped penalties for no-result cycles.
They were not blinded to route identity or outcome.

AOP estimated API-equivalent cost from recorded input, cached-input, and output tokens using the
published model prices retained with each run; cached input used its recorded lower price. The routes
used subscription authentication, so actual marginal charges were unknown. These figures are neither
invoices nor total campaign costs, and they do not price local evaluation or director work.

Within this small adaptive panel, Luna medium and Sol medium completed every assigned cycle and
received similar internal ratings. Luna medium was faster and cost about $0.16 per retained result,
compared with about $3.40 for Sol medium. Sol xhigh still produced distinct useful strategies. The
practical allocation was therefore to exploit the inexpensive reliable route while reserving some
exploration for expensive routes.

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

Gemini 3.6 Flash completed ten of ten cycles and remained the historical bandit leader at closeout with
a 0.78 posterior mean, although it was no longer active. Luna medium offered the best observed
combination of completion, internal rating, time, and API-equivalent cost in the later GPT-5.6 panel.
Sol medium had the highest mean internal rating, and Sol xhigh contributed distinct useful strategies.
Terra high produced one result that passed the checks and two no-result cycles.

These are adaptive allocation observations, not a matched or blinded model benchmark. They are bound
to the 20-cycle panel's models, effort levels, harness revision, fresh-author prompt, task sequence,
caching, and prices recorded on 2026-08-11. Across routes, Codex remained effective at repository
inspection, deterministic evaluator work, causal experiment plumbing, and bounded implementation. The
explicit no-wait campaign superseded the earlier claim that it could not sustain broad search.

## Provisional findings

- Soft family attractiveness with a small exploration floor may preserve reversibility better than permanent closure.
- Scheduled unrestricted ideation may counter local search, but its causal value was not established.
- Exact allocation and regularization rules need more untouched transitions before promotion.

## Evidence limits

This is an anonymized practitioner report, not independent replication. It retains generic campaign
counts, public model routes, and API-equivalent cost comparisons while omitting project identity,
asset class, instruments, markets, private configurations, and strategy details.

All strategy findings came from one frozen development snapshot that was adaptively reused as later
hypotheses responded to earlier results. The slightly positive controller was observed on that surface
and does not establish expected live returns. The evaluator remained worker-editable. The sealed future
period remained untouched, no promotion or final-test run occurred, and no strategy was selected for
deployment.

The model-route panel was small, adaptive, and internally rated without blinding. API-equivalent costs
priced recorded model-token usage under published prices and caching, not actual subscription charges,
local compute, orchestration, or the human owner's time.
