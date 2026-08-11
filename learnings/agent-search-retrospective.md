# Agent-search retrospective

Scope: General workflow lessons about autonomous search, research memory, evaluation, and role specialization.
Case-study basis: All published reports under `case-studies/`.
External-review basis: `external-review/README.md`.
Evidence boundary: This is aggregate synthesis. Private project records are intentionally excluded.

## Model and role observations

These observations come from multiple applied workflows. Application details are omitted here even
when a supporting case study is public. The observations are useful for role assignment, but should
not be read as general model rankings. Model behavior, product routing, and pricing can also change
over time.

- From 2026-07-02 through 2026-07-10, Fable 5 through Claude Code was most useful as the judgment layer. It sharpened research
  briefs, designed targeted and canned experiments, audited apparent passes, managed transitions
  between research phases, and identified methodology problems. It was slower and more constrained,
  so it was most valuable for direction and review rather than high-volume candidate generation.
- On 2026-02-05, Claude Opus 4.5 through Claude Code contributed substantial multi-file training,
  evaluation, sweep, and model infrastructure. The public history supports implementation contribution,
  but does not isolate a stable behavioral strength or weakness from human direction and the evolving harness.
- From 2026-02-06 through 2026-02-22, Claude Opus 4.6 through Claude Code sustained repository-wide
  implementation and research synthesis, including explicit corrections and negative-result reporting.
  The joint workflow also moved too readily from single-run peaks to causal language and searched local
  settings before fully auditing evaluator resolution and control viability. These are workflow findings,
  not clean model traits.
- In a separate March 2026 campaign, Claude Opus 4.6 was attributed to broad simulator, policy,
  mechanics-parity, and search implementation. The record independently supports repository-wide
  implementation under deterministic tests, but retained route and interaction evidence remains too
  weak for a stable behavioral characterization.
- In early April 2026, Claude Sonnet 4.6 was attributed to bounded alternative-policy and evaluator
  implementation, including corrections to simulator semantics and outcome accounting. The sample is
  too small and jointly directed to support a model ranking.
- On 2026-02-07, one bounded Codex CLI campaign found a consequential silent evaluator fallback and
  implemented stricter checks. It also satisfied a numerical target through a method outside the intended
  primary approach, showing why method constraints need mechanical enforcement. The exact model route was
  not retained, and one campaign cannot establish a recurring model weakness.
- Codex was the main high-throughput implementation worker. It explored quickly, produced usable
  candidates, inspected unfamiliar repositories effectively, built bounded evaluators and data tools,
  produced structured artifacts, added deterministic validation, and traced failures to concrete
  software layers. Its recurring weaknesses were recombining nearby ideas, orbiting known optima,
  treating supporting infrastructure as campaign progress, and sometimes waiting for more evidence
  when valid experiments could already run. In a bounded participant role, it also showed careful
  multi-turn theory revision and causal review, but was slower than flash-oriented routes and
  eventually shifted toward local optimization on a fixed population. In systems optimization work,
  Codex was also effective at finding concrete evaluator escapes and revising an overbroad quality gate
  after counterexamples. Separate sessions did not make its outputs independent once they shared the
  same ledger and framing. In a 2026-03-10 to 2026-03-11 performance campaign, it implemented structural and local
  changes quickly, diagnosed benchmark defects, and built targeted profiles, but needed human help to
  close exhausted families and distinguish local exactness from complete stateful correctness. That
  campaign began with basic manual infrastructure, so these weaknesses should not be attributed to the
  model alone.
- Codex GPT-5.4 was directly verified from route metadata from 2026-04-14 through at least 2026-04-25
  in another campaign. It was strong at repository navigation, end-to-end implementation, structured
  experiment plumbing, and sustained tool-driven work. The evidence supports its implementation role
  more strongly than any stable behavioral weakness because the code, evaluator, and campaign state
  changed during long sessions.
- Codex GPT-5.5 was directly verified on 2026-04-26 and 2026-04-28 in that campaign. It was effective
  at source and log inspection, concrete counterfactual execution, and repository-state auditing. One
  session included user-supplied analysis from another agent, so causal narratives from that session
  cannot all be attributed to Codex. No stable route-specific weakness was established.
- Claude Opus 4.7 with an extended-context designation was attributed through commit trailers from
  2026-04-24 through 2026-05-07. The record supports substantial multi-file implementation, while an
  attributed dialogue supports useful synthesis and diagnostic proposals. Raw route metadata was not
  retained, so behavioral claims, including premature extrapolation beyond the identity controls,
  remain provisional.
- Codex with the recorded `gpt-5.6-luna` participant route showed careful multi-turn theory revision
  and causal review on 2026-08-08, but eventually shifted toward local optimization on a fixed
  population. This was discovery evidence under audited rather than enforced no-tools behavior.
- From 2026-06-29 through 2026-07-10, Gemini 3.5 Flash through Agy was unreliable for direct candidate generation, with frequent empty,
  malformed, or failing outputs. It was occasionally useful for diversity because its reflections
  proposed ideas that the stronger implementation workers had not considered.
- On 2026-07-10, GPT-5.6-sol through Codex was valuable as an independent outside auditor. It found missing evidence and gaps
  between evaluation conditions and the intended live workflow that the primary judgment model had
  not identified.
- On 2026-06-22, an independent comparison among Claude Opus 4.8 with Haiku 4.5 subagents, Fugu Ultra,
  and GPT-5.5 found Claude strongest for the initial conceptual and methodological proposal, Fugu most
  concrete for implementation, and GPT-5.5 strongest at concise synthesis and lineage checking. That
  result concerned research design, not promotion evidence or a general capability ranking.
- From 2026-08-04 through 2026-08-08, Gemini through Agy using `gemini-3.6-flash-low` was fast and useful for inexpensive breadth, wording preflights, concise
  reflection, and recognizing local exhaustion. It tended to remain near one theory and sometimes
  offered causal explanations that did not match the supplied sequence. Exact variant, runner
  defaults, prompting, and enforced tool restrictions materially affect this assessment.
- From 2026-08-03 through 2026-08-08, DeepSeek v4 Flash routes through Hermes and OpenCode were useful for cost-conscious adversarial review, recovering from failed
  hypotheses, and separating broad outcomes from unresolved causal sequence. It made overly strong
  readiness judgments when the intended presentation channel was underspecified and required strict
  output normalization.
- From 2026-08-06 through 2026-08-08, Cursor Composer 2.5 found consequential configurations and produced useful critique quickly, but an
  available tool channel invalidated its use as a blind participant. It fits tool-using exploration or
  implementation unless the runner can enforce and audit a no-tools contract.
- From 2026-08-07 through 2026-08-08, Grok Build 0.1 maintained coherent hypotheses across turns and offered useful independent criticism, but
  could spend several attempts around a stable local configuration. Provider-state health should be
  verified before interpreting startup failures as model evidence.
- On 2026-08-08, Devin SWE 1.7 sustained long-horizon hypothesis revision and reproduced a surprising
  interaction before reporting it. Its main observed limitation was latency rather than a stable
  reasoning failure, making it better suited to deeper sequential investigation than broad throughput.

The useful unit is therefore a role, not a universally best model. The observed division of labor was
high-throughput models for implementation search, a stronger judgment model for experiment design and
triage, a different model for occasional hypothesis diversity, an independent model for adversarial
audits, and deterministic code as the final judge.

## Anonymized exposure snapshots

One contribution ran from 2026-08-08 through 2026-08-10 as a short, concentrated campaign. Usage was very
intensive and covered the research workflow broadly, with primarily sequential execution, limited
parallel proposal work, and frequent human steering. Autoresearch materially improved falsification,
validation infrastructure, and decision quality, but its raw autonomous throughput was lower than
the elapsed time and resource use suggested. Without active direction, time drifted toward local
variants, waiting, and supporting machinery. The overall contribution was mixed but important rather
than uniformly productive.

This exposure supports claims about Codex implementation strength and orchestration failure modes,
but the short observation period and absence of a within-project model comparison limit any broader
ranking claim.

A second contribution ran from 2026-08-02 through 2026-08-09 as one highly concentrated campaign.
Search intensity was very high, resource use was moderate relative to the project, and the workflow
spanned evaluator design, bounded search, interface comprehension, causal diagnosis, and multi-provider
orchestration. It progressed from design-only manual work to a deterministic simulator, exact replay,
versioned artifacts, canonical traces, multi-turn participant records, exact-session checks, private
provider state, and tool-call audits. Evaluators remained worker-writable, orchestration and judgment
remained manual, and there was no sealed model-ranking or product-level promotion authority.

The main value of this second contribution was faster implementation and diagnosis, stronger
validation, and prevention of premature mechanism changes through cheap counterfactuals, exact replay,
causal traces, and explicit evidence boundaries. Its model observations are route-specific discovery
evidence, and its predictions about human experience are not human validation.

A third contribution ran from 2026-08-06 through 2026-08-08 as a very high-intensity campaign spanning
exploration, implementation, optimization, validation, deployment preparation, and limited
post-deployment verification. Measurements were primarily sequential while proposal, design, and
review work used limited parallelism. Human steering and a persistent judgment owner remained central.
The harness grew from manual controls around a live resident accelerator into isolated transactions,
structured ledgers, production-owned admission, bounded recovery, artifact identity, explicit evidence
labels, and one narrow sealed-promotion route.

This third contribution produced important performance discoveries, prevented weakly authorized
changes, and strengthened recovery and evaluation infrastructure. Its largest value came from causal
falsification, adversarial evaluation, and retained research memory rather than uninterrupted
autonomous throughput. A 2026-08-10 review found that runtime isolation had improved, but the conductor
was inactive and progress freshness, named blocked states, and a general sealed-promotion interface
remained absent. Current Codex configuration was not treated as evidence of the route used during the
campaign.

A fourth contribution covered one intensive campaign from 2026-03-10 through 2026-03-11. It began with manually launched sessions, a
worker-writable evaluator, uncontrolled workload randomness, few timing repetitions, informal
discovery and promotion rules, and no structured ledger or automated recovery. During the campaign it
added seeded workload signatures, repeated statistics, processor isolation, child-process accounting,
stage microprofiles, complete stateful transaction checks, an append-only experiment log, and explicit
promotion rules. Recovery, evaluator protection, artifact identity, resource admission, and progress
monitoring remained manual or absent. The campaign produced meaningful performance and correctness
improvements, but frequent human steering remained necessary.

This fourth contribution is legacy evidence from a substantially less mature harness. Its observations
about workload identity and transaction-level correctness remain useful because they were causally
tested. Its observations about autonomy, throughput, search continuity, and Codex limitations should
be retested before application to a current orchestrated system. A late-April 2026 snapshot showed
structured run bundles, persistent controllers, richer recovery, and clearer discovery and promotion
state, superseding the March harness description while leaving some evaluator identity, resource
admission, and progress-freshness gaps unresolved.

A fifth contribution covered several concentrated, tightly supervised campaigns from 2026-04-15
through 2026-05-08. Search intensity and resource use were very high. The work spanned training,
runtime evaluation, experiment control, and incumbent selection. The harness grew from manual runs and
uneven identity capture into file-driven controllers, structured run bundles, append-only history,
explicit incumbent state, and deterministic gate rules. It still lacked a sealed promotion evaluator,
complete executable and artifact identity, cumulative search-burden accounting, and an independent
promotion owner.

This fifth contribution materially improved implementation speed, validation, and causal
falsification. Its repeatedly reused operational gate provided adaptive discovery and incumbent
management, not sealed promotion evidence. Durable lessons concern separating checkpoint selection
from promotion, bridging artifact and runtime changes with the unchanged artifact, and selecting
quality-changing components on fixed-budget end-to-end utility. Historical candidate rankings and
route-specific behavioral weaknesses require stronger retests.

A sixth contribution covered several concentrated campaigns from 2026-07-08 through 2026-07-27.
Search intensity and resource use were very high, while reasoning, implementation, and measurement
were mostly sequential. The harness progressed from manually launched probes in a shared mutable tree
to predeclared manifests, protected final evidence, exact artifact identity, fresh-process validation,
bounded recovery, a dependency-ordered queue, canonical commands, and complexity audits. Evaluators
remained worker-editable, resource admission and progress monitoring remained manual, and a human
retained promotion authority.

This sixth contribution materially accelerated implementation and diagnosis, but its strongest value
was causal falsification, exact transfer replay, protected evidence, and retained failure history. It
showed that a performance windfall should fund more falsification, that repeated failures benefit from
a layer-discriminating premise tree, and that external automation needs explicit state branches and a
safe scheduling contract for intrusive observation. Its Codex role observation requires retest because
the exact route was not retained and the harness changed substantially during the window.

A seventh contribution covered multi-model research from 2026-06-22 through 2026-07-10, with a
lifecycle recheck on 2026-08-10. It began with manual writable worktrees and independent design
proposals, then added a uniform runner, isolated scratch spaces, a read-only hash-guarded evaluator,
transactional restore-on-failure, structured diaries, exclusion maps, reflections, deduplication,
staged evaluation, and an explicit judgment layer. Internal time-based validation was repeatedly reused,
so it never became untouched promotion evidence.

This seventh contribution supports allocating scarce strong-model quota to judgment, evaluating
candidate reliability separately from reflection value, and giving independent audits a separate
primary-evidence path and authority. Its August recheck found that stronger causal inputs and newer
evidence had weakened or invalidated the strongest application claims. The durable result is therefore
methodology and role specialization, not a promoted application outcome.

## Repeated patterns

### Convergence can mean orbiting

Multiple workers may repeatedly rediscover the same narrow region or even equivalent candidates. This supports local robustness only when the attempts began from meaningfully independent contexts. Otherwise it is evidence that the search is anchored in one basin.

Track exact patch identity, behavioral signatures, and mechanism families. Use explicit exclusions and periodic fresh-start prompts to distinguish independent confirmation from repetition.

### Reflections compound better than raw proposals

The durable research memory is why a change was attempted, which mechanism it tested, what the result falsified, and what should happen next. Later workers can reuse these takeaways without inheriting an entire growing conversation.

Persist structured reflections alongside results. Share them during exploitation cycles, while occasionally withholding the current framing from a fresh worker to test for anchoring.

### Output reliability and research value are separate axes

A route that frequently fails an exact candidate contract may still contribute a valuable mechanism
summary, adversarial alternative, or diversity injection. Measure valid-output rate separately from
blinded information value. Keep unreliable routes outside the critical execution path, and test them
through bounded reflection tasks before discarding them entirely.

### Independent audits need independent evidence paths

A different model name does not make an audit independent. The auditor should begin from primary
records, inspect a broader scope than the actor's synthesis, and have authority to downgrade or block
claims. Let the actor verify concrete catches afterward, while treating overlapping scores and shared
framing as possible anchoring rather than independent confirmation.

### Negative results need reopening conditions

A failed mechanism is not a timeless fact. Its outcome may depend on representation, layout, call
structure, toolchain, or another architectural prerequisite. A bare exclusion can either permit
wasteful repetition or incorrectly block a valid retry after the surrounding structure changes.

Record the failure layer and the specific prerequisite whose change would justify reopening the
family. Under unchanged conditions, close exact or behaviorally equivalent retries. After a named
prerequisite changes, rerun the unchanged candidate first to test whether the predicted interaction is
real.

### Shared context correlates search

Workers readily copy the latest promising explanation. This accelerates exploitation but reduces effective diversity. More agents do not imply more independent hypotheses when they share the same framing and champion.

Separate proposal generation where useful, label mechanism families, and measure diversity by causal ideas rather than worker count.

### Reasoning and measurement need separate schedulers

Independent proposal generation, code inspection, and adversarial review can run in parallel while
measurements on a contested device remain serialized. This can reduce design and review wall time, but
does not increase measurement throughput.

Choose agent parallelism from the backlog of genuinely independent reasoning tasks, not from device
availability or unused agent quota. Shared framing can still correlate the work, and synthesis remains
a serial judgment step. Parallel external actions also need exclusive observation lanes or
identity-safe demultiplexing; separate targets do not prevent workers from consuming one another's
events on a shared stream.

### Compress correlated candidates before downstream selection

A large candidate set can contain many close siblings whose multiplicity looks like diversity. Before
combining or allocating among candidates, collapse exact and behaviorally near-duplicate variants.
Retain a representative leader per causal mechanism and admit additional members only when they add a
distinct outcome pattern, constraint response, risk profile, or Pareto-frontier role.

Treat concentrated allocations as provisional until they remain stable across several untouched
transitions, and compare them against a simple allocation over the representative set. This is a
qualified practitioner observation: representative compression was useful, but the exact selection
and regularization rule remains under-validated.

### Workers prefer reparameterization

Without active research direction, workers tend to revisit thresholds, weights, gates, and local combinations. Truly different mechanisms rarely emerge merely because the loop runs longer.

After bounded local attempts, require a new mechanism, a targeted counterfactual, or a fresh derivation from the problem constraints.

### A generated pass is not trustworthy

Apparent wins can come from evaluator mistakes, stale artifacts, ignored configuration, path-dependent test behavior, held-out leakage, or insufficient stress testing. More capable models remain vulnerable because the failure is usually in system authority rather than proposal quality.

Every important pass needs deterministic reproduction, effective-configuration and artifact hashes, a baseline rerun, and adversarial review proportional to the claim.

### Evaluator hardening can become another search surface

Each evaluator check expands or modifies the trusted computing base. Closing one stale-artifact,
identity, schema, or recomputation escape does not establish authority over the full claim. A complex
evaluator can accumulate caller-controlled admission, unchecked derived values, runtime impersonation,
permissive types, and replace-between-inspection races.

After repeated integrity failures, stop adding isolated checks and audit the premise. Prefer a smaller
runner-owned program, closed inputs, exact environment binding, single-open verification, and a narrow
claim surface that can be attacked with canned adversarial cases.

### AI subjects are comprehension probes, not human substitutes

Bounded, tool-audited language models can cheaply test wording precision, available controls, report
legibility, valid choice formation, and whether supplied evidence supports theory revision. Their
procedural behavior can be reproduced and checked against the same interface.

Their confident predictions about human understanding, usability, enjoyment, or retention remain
conditional on prompt framing and are not human validation. Coding agents with repository access are
also not blind participants. Keep mechanized outcomes and subjective experience claims under separate
evidence authorities.

### Distinguish the product channel from the diagnostic channel

An evaluator may consume a compact machine-oriented report even when the intended user experiences a
different interface. Without an explicit presentation contract, reviewers can misattribute report
reading burden to the product or infer that a presentation change repairs a deeper mechanism problem.

Record the experienced interface as part of the effective evaluator configuration. Keep default
summaries compact and make causal traces optional diagnostic evidence rather than the assumed product
experience.

### Nominal variety may compile to the same behavior

Differently named or described policies can reach the same branches and produce equivalent decisions
on the declared population. Repeatedly editing a mechanism against such a population cannot separate a
mechanics defect from a sampling or reachability defect.

Before intervening again at a failed gate, compare compiled structures, reachable branches, event
signatures, and canonical behavior traces. Add a matched one-factor counterfactual designed to
discriminate the suspected mechanism. Equivalence remains population-specific rather than universal.

### Fixed fixtures gradually become local-tuning surfaces

Repeated adaptive exposure to a small deterministic population can shift a campaign from discovering
new mechanisms toward parameter changes and fixture-specific tuning. The transition is gradual, so a
fixed round limit is a poor stopping rule.

Track the arrival rate of new causal mechanism families. Preserve fixed fixtures for regression and
promotion, but move discovery to a provenance-preserving variation when additional fixed-fixture
rounds stop producing independent information. A practical transfer ladder is the motivating fixture,
a preregistered ring of adjacent cases, and then the representative population gate.

### Canned experiments improve information efficiency

Bounded experiments with a fixed hypothesis, locked inputs, and explicit exit criteria often produce more information per unit of compute than open-ended requests to find something better. Broad search remains useful for discovery, but it should feed precise experiments rather than replace them.

### Premise audits need discriminatory tests

After repeated failures at one gate, broad reflection is less useful than a small tree of tests that
separate evaluator and task feasibility, representation, data or visited-state coverage, optimization,
and local parameter choice. Each diagnostic should state which layer it can falsify and which stronger
claim it cannot establish. Preserve the tree so later interventions remain attributable. For a search
system with learned or heuristic truncation, a matched full-breadth or high-recall control is often the
cheapest test of whether good branches are being discarded before evaluation.

### Infrastructure needs a scientific dependency claim

Implementation-capable agents can make supporting machinery the default response even when useful
experiments are already runnable. Every proposed tool should therefore name the experiment it
unblocks, the missing capability, the smallest implementation that closes the gap, and a stop
condition. Mandatory integrity, safety, and recovery controls remain prerequisites, but speculative
infrastructure should not be confused with scientific progress.

### Elapsed time is not a scheduler

A long-duration instruction does not ensure continuous research. An unattended workflow can wait for
more evidence, over-invest in setup, or remain idle despite having valid bounded experiments available.
A work-conserving queue should distinguish hypothesis work, necessary enabling work, blocked time, and
unexplained idle time. It must not authorize reuse of sealed evidence, low-value experiment spam, or
unsafe actions merely to stay busy.

### Process liveness is not campaign liveness

A healthy execution service and a live conductor process do not prove that research is continuing. The
queue may be empty, the managed loop may be inactive, or an older process may remain alive without
producing transactions.

Monitor progress freshness and require a bounded transition to a ledgered result, valid queued or
running work, or an explicit blocked-state record. Distinguish justified waiting for production,
budget, or evidence integrity from unexplained idle state.

### Automatic synthesis can dilute judgment

Automatic in-loop synthesis through the Claude provider, which at the time routed to Fable, was less
effective than asking Fable to operate explicitly as the judgment layer. Automatic summarization can
overwrite a stronger hand-curated brief or prematurely turn tentative observations into policy.
Workers should emit structured results and takeaways, while an explicit judgment owner curates the
active research brief and closes exhausted families.

## Provisional hypotheses

The following observations are promising enough to preserve but do not yet have enough independent
evidence for promotion into durable principles. They are research questions, not operating rules.

### Soft family attractiveness may preserve useful reversibility

Replacing permanent binary family closure with a continuously updated attractiveness score may keep
weak but potentially recombinable branches available. A small exploration floor could preserve
optionality while concentrating most resources on stronger families.

The current evidence does not show whether this produces new discoveries or merely keeps exhausted
branches alive. Test it against explicit family closure under matched experiment budgets. Compare new
mechanisms discovered, repeated dead ends, resource concentration, and confirmed promotions.

### Scheduled unrestricted ideation may counter local search

Periodic prompts that ignore the current candidate family and generate mechanisms from first
principles may broaden search after workers begin producing mostly local combinations.

The observed workflow still generated many nearby ideas, so the causal value of a fixed ideation
cadence is unresolved. Compare scheduled fresh ideation with trigger-based resets under matched
proposal and evaluation budgets. Measure mechanism diversity and confirmed value rather than raw idea
count.

### Exact allocation and regularization rules remain under-validated

Compressing correlated candidates before downstream selection is already useful as a qualified
workflow lesson. The stronger claim that a particular concentration limit, shrinkage rule, or resource
allocation proportion transfers across settings is not established.

Freeze candidate representatives and competing allocation rules before several untouched transitions.
Compare them with a simple equal allocation and report stability, turnover, protected-case failures,
and the predeclared objective. Do not tune the rule repeatedly against the same transitions.

### Optional causal traces may improve diagnosis

On-demand chronological traces may help reviewers answer causal questions without making dense
evidence the default interface. It is not yet established whether access to a trace improves the next
decision or merely produces longer explanations. Test this with matched reviewers and score the next
diagnosis, not response length.

### Seeded fixture variation may restore discovery diversity

Changing one provenance-preserving content factor while holding language, evaluator, and reports fixed
may restore novel mechanism discovery after a fixed population is exhausted. It may instead create a
larger memorization surface. Compare matched fixed and varied blocks by new mechanism families and
confirmed downstream value.

### Cross-model disagreement may not be independent evidence

Different answers across model routes may reflect genuine hypothesis diversity, but may also arise
from provider scaffolding, prompt sensitivity, tool availability, or shared training priors. Treat
model count as a weak proxy for independent evidence until the causal framing and execution boundary
are controlled.

### Filesystem recovery may replace a durable registry in narrow settings

A deterministic filesystem namespace may be sufficient for bounded-attempt, single-host recovery,
reducing the need for a separate durable operation registry. The design was counterexample-tested but
not validated in the live path. Distributed storage, concurrency, or unbounded attempts may reverse
the tradeoff. Test crash, retry, duplicate delivery, and cleanup semantics before promotion.

### Compatible-work batching needs live admission evidence

Batching compatible work improved throughput in controlled discovery, but production admission,
waiting policy, recovery, and delivery semantics were not validated. Treat batching as a discovery
result until the exact production scheduler passes injected arrivals, timeouts, crashes, and partial
delivery cases.

### Judgment-owner adjudication has a limited evidence boundary

Direct orchestrator review may be sufficient for objective output disagreements when a frozen quality
contract and complete evidence are available. It does not establish that model review can replace
human-subject evidence or subjective product validation. Compare independent adjudication and retain
uncertainty rather than forcing a binary decision.

### Parallel-agent speedup remains unquantified

Parallel proposal and review work appeared to reduce wall time, but no matched serial baseline was run.
Measure completed usable artifacts, distinct mechanisms, duplicated work, synthesis time, and total
agent resources before claiming a quantitative speedup.

## Privacy and evidence boundary

This document intentionally omits project names, instruments, venues, implementation languages,
proprietary metrics, exact result counts, and paths to private records. It retains model names because
their role-specific strengths and weaknesses are part of the transferable workflow evidence. Claims
based on anonymized experience should be treated as practitioner evidence rather than independent
replication.
