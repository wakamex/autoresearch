# Case 10 - Adaptive quantitative-trading strategy search

Observation window: 2026-08-08 through 2026-08-10
Disclosure mode: anonymized
Duration: three calendar days, with roughly two days of substantive research
Application domain: quantitative trading; project identity and asset class withheld

## What was researched

The campaign searched over rules for a quantitative trading strategy using time-ordered historical
data. It tested low thousands of related policy variants across nearly one hundred batches, compared
candidate families, examined whether combinations added genuinely different behavior, and reserved a
sealed future period that discovery runs were forbidden to inspect. No candidate reached that final
promotion test.

The practical questions were whether a proposed rule still worked after realistic costs, whether
apparently different variants actually produced different trades, whether combining strategies added
diversification, and whether a long-running agent was continuously testing useful hypotheses.

## Exposure

- Usage pattern: one concentrated campaign with repeated experimental batches and follow-up audits.
- Project phases: exploration, implementation, optimization, validation, and deployment preparation.
- Search intensity: very high.
- Parallelism: primarily sequential execution with limited parallel proposal work.
- Human involvement: frequent steering, especially for research direction, premise audits, and resource allocation.
- Resource intensity: heavy relative to the project.
- Breadth: project-wide methodology spanning data contracts, evaluators, search, research memory, orchestration, and decision review.
- Decision influence: critical to several major decisions.

## Infrastructure context

The campaign began on 2026-08-08 with a basic deterministic harness, a small append-only ledger, and
useful artifact hashes, but no isolated workers, persistent conductor, sealed promotion route, general
recovery, or progress-freshness monitor. By 2026-08-10 it had disposable worktrees, strict manifests,
structured transaction and campaign records, causal replay, explicit evidence labels, a reserved
sealed epoch, and bounded recovery on the strict path.

The high-throughput path still used a shared repository, evaluators remained worker-editable, and the
rolling agent session acted as director. The sealed epoch remained untouched and no promotion run
occurred. A 2026-08-10 comparison found that a separate newer harness had stronger persistent
orchestration, admission, recovery, and promotion controls, so continuity and model-behavior claims
from this campaign require retest under that infrastructure.

## Project impact

The contribution was mixed but important. Autoresearch produced key falsifications, stronger
validation, reusable evaluation infrastructure, and a more defensible decision process. Raw autonomous
throughput was lower than elapsed time and resource use suggested because work sometimes shifted toward
waiting, supporting machinery, or nearby variants.

Without autoresearch, systematic comparison would likely have been slower and favorable assumptions
might have survived longer. Without frequent human steering, the same workflow likely would have spent
more time on local optimization and infrastructure. This counterfactual is plausible but unmeasured.

## Main findings

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

### Thousands of variants may still represent the same few ideas

Many tuned strategies were minor variations that made nearly the same trades. Counting them as
independent ideas would have made one crowded family look artificially diverse. Grouping candidates by
mechanism and actual behavior revealed the smaller set of distinct approaches worth combining, though
the exact allocation among them remained unstable.

### Telling an agent to work for hours does not keep it doing research

Asking the agent to keep working for a long duration did not make it continuously test hypotheses. It
sometimes waited despite having usable evidence or treated setup work as research progress. The loop
needed an explicit queue of runnable experiments and a concrete reason whenever it stopped.

### Build a tool only when a specific experiment needs it

Supporting tools were valuable but could become the default activity. Requiring every proposed tool
to name the experiment it would unblock kept the campaign focused without weakening integrity checks.

## Model observation

Codex was fast and effective at repository inspection, bounded evaluator and tooling implementation,
structured artifacts, deterministic validation, and failure attribution. It was weaker at sustaining
broad autonomous search without steering and tended toward infrastructure, waiting, and nearby
variants. The best role was bounded implementation and batch execution under an explicit queue,
infrastructure gates, and periodic judgment-owner review.

Evidence strength is medium because exposure was intensive but short and had no controlled
within-project model comparison.

Current status: implementation strengths remain supported, while autonomy, waiting, and throughput
weaknesses require retest under a persistent conductor. The exact underlying model route was withheld
because it was not a public model name.

## Provisional findings

- Soft family attractiveness with a small exploration floor may preserve reversibility better than permanent closure.
- Scheduled unrestricted ideation may counter local search, but its causal value was not established.
- Exact allocation and regularization rules need more untouched transitions before promotion.

## Evidence limits

This is an anonymized practitioner report, not independent replication. Exact metrics, counts,
configuration values, project identity, application details, and the private model-route identifier
are omitted. Candidate results were discovery or development evidence, and no sealed promotion result
was produced.
