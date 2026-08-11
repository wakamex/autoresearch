# Case 08 - Multi-model playtesting for a strategy game

Observation window: 2026-08-02 through 2026-08-09
Disclosure mode: anonymized
Duration: eight calendar days in one highly concentrated campaign
Application domain: private party-management strategy game

## What the models playtested

The project was an early party-management game in which a manager assembles characters with different
abilities, equipment, and tactics, then submits a plan to a deterministic battle simulator. It had a
headless Rust mechanics laboratory and a small local manager interface, not a production game client.

LLMs acted as independent game managers. They chose parties, edited ordered character rule cards,
played repeated deterministic matchups, inspected compact battle reports, revised their theories, and
proposed the next experiment. They could change only choices intended for a player; deterministic code
owned battle resolution and checked whether every submitted plan was legal.

## Exposure

- Usage pattern: several concentrated and repeated campaigns.
- Project phases: exploration, implementation, optimization, and validation.
- Search intensity: very high.
- Parallelism: independent model-family playtests could run concurrently; adjudication and synthesis were serialized.
- Human involvement: frequent steering.
- Resource intensity: moderate relative to the project.
- Breadth: evaluator design, bounded search, interface comprehension, causal diagnostics, and multi-provider orchestration.
- Decision influence: important.

## Starting infrastructure

On 2026-08-02, the project had design documents but no executable domain harness. There was no
deterministic evaluator, structured ledger, exclusion map, isolated worker, persistent orchestrator,
recovery protocol, artifact identity, shared-resource admission, progress monitor, blocked-state
contract, or sealed promotion authority. The worker and future evaluator shared one writable
repository, sessions were manual, and the human owner held judgment authority.

## Ending and current infrastructure

By 2026-08-09, the project had a deterministic simulator, exact enumeration, bounded search,
profiling, deterministic replay, canonical traces, exhaustive regression tests, versioned interfaces,
run manifests, hashes, effective configuration identity, and a curated research record. AI-subject
campaigns used repeatable scripts, exact-session resume, per-turn provenance, timeout handling,
immutable run records, and tool-call audits. Several stateful routes gained task-private mutable state
and cleanup during the window.

The evaluator remained worker-writable, launch and judgment remained manual, and there was no single
append-only machine ledger, persistent work-conserving orchestrator, progress-freshness monitor, named
blocked state, or sealed promotion evaluator. As reviewed on 2026-08-10, the external runner had gained
stronger private-state and immutable-record controls, but these could not retroactively repair earlier
agent-mode or tool-capable trajectories.

Most results were discovery or diagnosis. Narrow deterministic changes used versioned regression gates,
but known populations were reused and no untouched or multiplicity-aware product-level promotion
authority existed. There was no human-subject evidence or sealed model ranking.

## Project impact

From 2026-08-06 through 2026-08-08, six model routes independently played the same frozen version of
the game. Each manager kept its own session, made party and tactics choices, saw the resulting battles,
and revised its theory without seeing another model's decisions. The simulator decided what happened,
session logs revealed forbidden tool use, and the human owner decided which findings could change the
game.

The panel changed what the project investigated, what it left alone, and what it explained more
clearly. It prevented premature rules changes, rejected a strong result produced with forbidden tools,
prompted clearer battle explanations, and helped assign cheap models to routine play and slower models
to deeper review. Its value came from different mistakes and explanations, not suggestion count or a
majority vote.

No matched single-agent branch was run. The campaign therefore shows that cross-family review affected
decisions, but not that it beat one strong agent under equal cost and time. The human synthesizer may
also have been the main source of the improvement.

## Main findings

### Run models separately and compare explanations, not votes

Each family received the same frozen interface and deterministic feedback in a separate session. On
2026-08-06, three families chose different initial plans and proposed different follow-up experiments.
Longer trajectories on 2026-08-07 disagreed about whether one control was dominant, inert, or simply
poorly explained. Six routes on 2026-08-08 again found distinct useful theories, including a
counterintuitive interaction reproduced by a long-horizon participant.

The useful output was the spread of falsifiable mechanisms. Deterministic replay established what
happened; disagreement revealed where the evidence or presentation could not support one diagnosis.
A vote would have discarded that information, and model count was not evidence weight.

Current status: qualified method. It requires frozen evidence, independent sessions, deterministic or
well-controlled outcomes, retained trajectories, and one explicit judgment owner. Shared training
priors, prompts, and fixtures mean different families are not statistically independent samples.

### Use fast models for breadth and slower models for deeper play

No route dominated compliance, breadth, causal depth, latency, and cost. Fast routes were useful for
cheap breadth and wording preflights. Slower routes were better suited to sequential investigation.
Occasional higher-cost routes could add sharper criticism without producing better adaptive play. A
semantically useful tool-capable route failed the blind-participant contract entirely.

The campaign used a small matched comparison to retain a cheaper route for routine throughput and a
more expensive route only for occasional review. This was a local allocation decision, not a general
model ranking.

Current status: promising and route-specific. Track valid compliance, distinct causal hypotheses,
verified catches, latency, and cost separately.

### When models disagree, test what they disagree about

Conflicting reviews separated mechanism behavior, strategy expressivity, evidence presentation,
evaluator integrity, and participant misunderstanding. In one case, changing only the presentation
channel revised a strong criticism without changing system behavior. In another, disagreement led the
project to expose existing causal evidence before adding requested features.

Current status: durable workflow guidance. When reviewers disagree, change one layer at a time and run
the cheapest counterfactual that distinguishes their explanations.

### AI playtests do not show whether humans will enjoy the game

Models formed hypotheses, revised them after evidence, detected ambiguous wording, and explained
causal tradeoffs. Their predictions about human experience changed with prompt framing and presentation.
Even unanimous AI feedback remained a correlated prediction from reused fixtures, not evidence about
people.

Current status: durable but qualified. AI playtesting can preflight comprehension and prioritize human
tests. It cannot validate usability, enjoyment, retention, or population behavior.

### Show playtesters the game view, not a developer report

Reviewers initially consumed compact machine-oriented reports and attributed report-reading burden to
the intended experience. Clarifying the presentation contract changed their diagnosis without changing
behavior. The experienced interface is part of evaluator configuration.

Current status: durable. The stronger claim that optional traces improve the next decision remains
provisional.

### A search oracle may find strategies players cannot actually express

An unconstrained search found behavior outside the authored policy population. A bounded resolver later
recovered useful local behavior while preserving protected higher-level decisions. Optimizers should be
treated as diagnostic ceilings unless granted explicit authority.

Current status: durable as an authority rule. The specific bounded resolver remains scoped discovery
evidence.

### Differently named strategies may behave identically

Several differently named policies produced equivalent decisions on the tested population. The
population could not distinguish a mechanism defect from a reachability or sampling defect. Compiled
structures, reachable branches, and canonical traces should be compared before further intervention.

Current status: durable within a declared population. The source population's negative result does not
transfer to materially different fixtures.

### Tool use and broken sessions can invalidate a playtest

Some apparent participant failures originated in runtime state, authentication lifecycle, or session
continuity. Another completed trajectory violated the no-tools protocol. Provider state, terminal
session identity, and tool history therefore belong to evaluator integrity.

Current status: durable operational guidance. Repaired provider failures are superseded as model
evidence, and prompt-only no-tools compliance remains narrower than enforced isolation.

### Stop tuning the same fixed roster after new ideas dry up

Repeated exposure to a small deterministic population gradually shifted proposals toward parameter
changes and fixture-specific tuning. Fixed fixtures remained useful for regression and promotion, but
discovery needed provenance-preserving variation once new mechanism generation declined.

Current status: qualified and durable as a stopping lesson. Whether seeded variation restores
independent discovery remains untested.

## Model observations

- Gemini through Agy using `gemini-3.6-flash-low` was fast and useful for inexpensive breadth, wording preflights, concise reflection, and recognizing local exhaustion. Its no-tools behavior was audited but not enforced by participant mode.
- DeepSeek through Hermes and OpenCode using recorded DeepSeek v4 Flash routes was useful for cost-conscious adversarial review and recovery from failed hypotheses. Cross-provider comparisons were not controlled.
- Cursor Composer 2.5 found consequential configurations and useful critiques, but an audited tool call invalidated its use as blind-participant evidence.
- Codex implementation sessions lacked exact route metadata. A bounded participant manifest recorded `gpt-5.6-luna`; it showed careful multi-turn theory revision but eventually shifted toward local optimization on the fixed population.
- Grok Build 0.1 maintained coherent hypotheses and useful criticism in participant mode, but could remain around a stable local configuration. Its agent-mode trajectory was rejected as blind evidence after tool use.
- Grok 4.5 produced one sharper but more expensive review. The sample was too small and its participant resume too unreliable for a durable ranking claim.
- Devin SWE 1.7 sustained long-horizon revision and reproduced a surprising interaction, with latency as its main observed limitation.

These are qualified role observations from small adaptive samples, not model rankings. Provider route,
prompt, tools, state isolation, and harness maturity materially affect them. No sealed model-ranking
authority existed.

## Provisional findings

- Optional causal traces may improve the next diagnosis, but may only increase explanation length.
- Seeded fixture variation may restore discovery diversity or merely create a larger memorization surface.
- Cross-family panels may outperform one strong reviewer under a matched budget, but this campaign did not test that comparison.
- Cross-model disagreement may reflect provider state, scaffolding, or prompt differences rather than reasoning diversity.
- AI predictions about human usability and enjoyment remain unvalidated without human participants.

## Evidence limits

This is an anonymized practitioner report. It omits project identity, application details, exact
metrics, population sizes, prompts, private runtime information, session records, and internal route
aliases. Exact dates and public route names are retained for evidence provenance. Search burden appears
only in broad bands, and all subjective human claims remain outside the evidence authority.
