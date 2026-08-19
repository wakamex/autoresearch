# Contributing autoresearch learnings

Scope: Guidance for extracting transferable autoresearch lessons under anonymized, named-private, or public full-detail disclosure.

This repository accepts curated methodology findings and case studies, not raw private project
records. Contributions from another project should begin as drafts under the ignored
`.local/contributions/` staging area, outside tracked repository content. A curator can then apply the
declared disclosure boundary, deduplicate findings, and prepare any tracked publication.

## Contribution workflow

1. Read the current synthesis before extracting new findings.
2. Declare anonymized, named detailed with private repository, or public full-detail disclosure mode.
3. Identify observations that add, refine, qualify, falsify, or contradict an existing principle.
4. Apply the privacy or publication boundary for the selected disclosure mode.
5. Classify the evidence and state its boundary conditions.
6. Write one draft under `.local/contributions/`. Do not edit tracked repository files directly.
7. Run the required disclosure audit over the finished draft.
8. Give the draft to the repository curator for review and integration.

Do not create one permanent synthesis document per source project. Aggregate lessons remain organized
by knowledge type; curated case studies may retain project history when their disclosure mode permits.

## Existing synthesis

Read these documents before drafting:

- [`principles.md`](principles.md)
- [`agent-search-retrospective.md`](agent-search-retrospective.md)
- Any relevant domain playbook listed in [`README.md`](README.md)

A contribution is material when it does at least one of the following:

- Adds a genuinely new workflow lesson.
- Provides independent support for an existing observation.
- Identifies a boundary condition or counterexample.
- Replaces a vague rule with a falsifiable one.
- Shows that an apparent failure was attributed to the wrong layer.
- Records a failed practice that future agents might otherwise repeat.

Repeating an existing conclusion without new evidence or qualification is not a material contribution.

## Disclosure modes

### Anonymized

Use this mode for private projects or whenever identifying the application is unnecessary. Follow the
privacy boundary below and publish only a neutral, sanitized case study.

Anonymized describes what identity is withheld, not how abstract every other detail must be. The
strict boundary in this guide is the default. A project owner may explicitly authorize a narrower,
project-specific boundary that retains selected context or methodological detail while continuing to
withhold the project identity. Record the allowed and withheld categories in the local contribution.
Do not reuse one project's authorization for another project.

### Public full-detail

Use this mode only when the project owner explicitly authorizes detailed publication. A public
repository alone does not authorize publishing private operations, unpublished results, local logs, or
deployment details that are absent from the public project.

A public full-detail contribution may include:

- Project and repository name, application domain, and canonical public URL.
- Exact autoresearch dates and project milestones.
- Public commit hashes, issue or pull-request links, and released implementation names.
- Exact model versions, providers, prompts, and harness configuration when authorized.
- Exact experiment counts, resource use, performance results, and before-and-after comparisons when
  authorized and supported by public or publishable artifacts.
- Concrete starting and ending infrastructure, including which controls were added during the work.
- Direct evidence links that let a reader inspect the public implementation or result.

Public full-detail mode still forbids:

- Credentials, tokens, authentication state, private endpoints, or account identifiers.
- Personal information, customer data, private user data, or confidential counterparties.
- Security-sensitive operational details that are not intentionally public.
- Third-party private material or unpublished conversations without permission.
- Claims that cannot be distinguished from inference or reconstructed from authorized evidence.

Record who authorized full-detail publication and the authorization date in the local contribution.
The public case study may state that publication was authorized without naming a private approver.

### Named detailed, private repository

Use this mode when the contributor is authorized to name the project and publish detailed accounts of
their work, but is not authorized to publish the underlying repository. This is appropriate when the
repository belongs to another person or organization, remains private, or contains material outside
the contributor's publication authority.

A named detailed contribution may include authorized:

- Project name, application domain, and a high-level description of the private system.
- Exact autoresearch dates, experiment design, metrics, configurations, resource burden, and results.
- Architecture, implementation mechanics, internal terminology, failure modes, and project impact,
  described in the contributor's own words.
- Exact public model versions, provider routes, prompts, harness configuration, and role observations.
- Detailed negative results, causal counterfactuals, maturity changes, and evidence limitations.

It must not include:

- Source code, private repository files, private repository URLs, or links that require unauthorized
  access.
- Large or reconstructive excerpts from private documentation, logs, prompts, schemas, or records.
- Credentials, private endpoints, authentication state, personal data, or confidential third-party
  information.
- Proprietary implementation detail whose publication would effectively reconstruct repository
  content outside the contributor's authority.
- Claims presented as publicly reproducible when readers cannot inspect the underlying evidence.

Prefer concrete, detailed paraphrase over anonymous abstraction. State prominently that the repository
and primary evidence are private and cannot be independently inspected by public readers. Record who
authorized publication of the contributor's work and the authorization date in the local draft.

## Privacy boundary

This section applies to anonymized mode. Unless the local contribution records an explicit exception,
do not include or imply:

- Project, repository, company, client, protocol, product, or internal system names.
- Filesystem paths from the source project.
- The specific application domain.
- Instruments, assets, venues, datasets, users, or counterparties.
- Proprietary architecture, feature, strategy, or implementation names.
- Internal model aliases, experiment names, or research-era names.
- Exact private milestones tied to identifying events, result counts, performance values, monetary
  values, or dataset sizes.
- Private URLs, commit hashes, filenames, schemas, logs, prompts, or quotations.
- Combinations of otherwise harmless details that could fingerprint the project.

Project-specific authorization may retain any of the following without changing the contribution to
named-private or public full-detail mode:

- The application domain while withholding the project, asset class, instruments, venues, users, and
  counterparties.
- Exact observation dates, campaign durations, and aggregate experiment, completion, resource, or
  dataset-scale figures.
- Public model routes, effort levels, aggregate ratings, token accounting, and API-equivalent costs.
- Generic operational and evaluation descriptions, including categories of public input data,
  artifact and effective-configuration hashing, shared-resource replay, and non-proprietary screening
  procedures.

These exceptions do not authorize project identity, repository details, source paths, specific assets
or markets, loaded private settings, proprietary strategy mechanics or names, exact private economic
outcomes, credentials, private endpoints, personal data, confidential third-party material, or raw
private artifacts. A permitted combination must still be generalized if it would identify the project
or disclose a withheld category.

It is acceptable to name publicly available LLMs, agent products, and runners. In anonymized mode,
describe role-specific strengths and weaknesses within the recorded disclosure boundary. Named
detailed and public full-detail modes may retain authorized task context.

General public principles about trading, software optimization, evaluation, or autonomous agents are
also acceptable. State which domain the source project applied only when the local contribution
explicitly authorizes domain disclosure.

When uncertain whether a detail is identifying, remove or generalize it.

## Evidence discipline

Classify every proposed learning as one of:

- Anonymized practitioner observation.
- Named-private practitioner observation.
- Repeated practitioner observation.
- Public-source-supported principle.
- Inference requiring further validation.

Separate the observed behavior from the proposed causal explanation. Do not turn one successful
result into a universal rule. Include relevant failures, alternative explanations, counterexamples,
and conditions under which the lesson may not transfer.

For each finding, propose the cheapest experiment that could falsify it in another setting.

## Useful contribution areas

Useful findings often concern:

- Agent and model role specialization.
- Model strengths, weaknesses, speed, cost, and failure patterns.
- Experiment design and causal attribution.
- Evaluator bugs, stale artifacts, or ineffective configuration.
- Search anchoring, correlated proposals, and repeated candidates.
- Research memory, reflections, and exclusion maps.
- Discovery versus promotion evidence.
- Orchestration, recovery, and unattended-operation failures.
- Stop conditions and premise audits.
- Information gained per unit of compute.
- Expected fixes that failed a cheap counterfactual.
- Practices that sounded useful but did not work.

## Exposure and project impact

Every draft should describe when and how much opportunity the project had to observe the autoresearch
workflow. This helps distinguish a short evaluation on basic infrastructure from a mature operating
pattern. Local ignored drafts should record the calendar window. Public synthesis may generalize that
window when an exact date would identify the project. In anonymized mode, use coarse bands for counts,
costs, and identifying milestones by default, but retain exact aggregate values when the local
contribution explicitly authorizes them. Named detailed and public full-detail modes may retain
authorized exact values.

Record:

- Contribution prepared: the date the contribution draft was written.
- Calendar window: the dates when the underlying autoresearch observations occurred, not the draft,
  review, or file-modification dates. Use exact start and end dates when known, otherwise month,
  quarter, or year.
- Observation period: several days, several weeks, several months, or longer.
- Usage pattern: one concentrated campaign, several campaigns, intermittent use, or continuous use.
- Project phase: early exploration, implementation, optimization, validation, deployment preparation,
  maintenance, or multiple phases.
- Search intensity: low, moderate, high, or very high.
- Parallelism: primarily sequential, limited parallel proposal work, or broad parallel search.
- Human involvement: mostly autonomous, periodic review, frequent steering, or tightly supervised.
- Resource intensity: use a qualitative band in anonymized mode unless exact aggregate compute or cost
  is explicitly authorized. Named detailed and public full-detail modes may retain authorized exact
  compute or cost.
- Breadth: isolated component, several components, or project-wide methodology.
- Starting infrastructure: the evaluator, ledger, worker isolation, orchestration, recovery, and
  promotion capabilities available when the observations began.
- Ending infrastructure: the same capabilities at the end of the observation window.
- Infrastructure changes: which findings were observed before or after major harness improvements.
- Decision influence: advisory, useful, important, or critical to major project decisions.
- Outcome contribution: little value, mixed value, meaningful acceleration, key discoveries, stronger
  validation, prevented failures, or essential project infrastructure.
- Counterfactual: what likely would have been slower, weaker, missed, or unchanged without autoresearch.

Separate usage intensity from usefulness. A highly intensive campaign may produce little value, while
a small targeted experiment may prevent an important mistake. Also separate raw candidate generation
from the value of evaluation design, research memory, auditing, or orchestration.

Describe infrastructure through concrete capabilities rather than a single maturity label. At minimum,
record whether each end of the observation window had:

- A frozen or worker-writable evaluator.
- A structured experiment ledger and exclusion map.
- Disposable or isolated workers.
- A persistent orchestrator or manually launched sessions.
- Explicit discovery and promotion gates.
- Effective-configuration and artifact identity checks.
- Timeout, crash, resume, cleanup, and restoration handling.
- Shared-resource admission and measurement serialization.
- Progress-freshness monitoring and named blocked states.
- Independent review or a designated judgment owner.

## Draft template

Write one file to `/code/autoresearch/.local/contributions/PROJECT_LABEL.md`. Use a short,
human-readable local label that will help the curator recognize the source project. The `.local/`
directory is excluded through `.gitignore` and must remain untracked, so its filenames are not
part of the public privacy boundary.

```text
# Autoresearch contribution draft

Privacy status:
Sanitized for anonymized mode, publication-authorized for named detailed private-repository mode, or
publication-authorized for public full-detail mode
Evidence basis:
Anonymized observations, named private project evidence unavailable to public readers, or named public
project evidence with links and revisions
Intended use: editorial input, not direct publication
Disclosure mode:
Anonymized, named detailed with private repository, or public full-detail
Publication authorization:
Required for named detailed and public full-detail modes. Record the authorizing person or source and
date locally. For anonymized mode, record any explicitly authorized exceptions to the strict privacy
boundary and the categories that remain withheld.
Contribution prepared:
YYYY-MM-DD

Project identity:
In anonymized mode, write "withheld" and state whether the domain is withheld or explicitly authorized
for publication. In public full-detail mode, provide the authorized public name, domain, repository
URL, and relevant public revision. In named detailed private-repository mode, provide the authorized
project name and domain, state that the repository is private, and do not include its URL or private
revisions.

## Exposure and project impact

Calendar window:
Give the dates when the observations occurred, not the report date. Use exact start and end dates when
known. Otherwise provide month, quarter, or year.

Observation period:
Use a coarse duration band.

Usage pattern:
Concentrated, repeated, intermittent, or continuous.

Project phases:
List broad phases. Anonymized mode must avoid identifying milestones unless the recorded boundary
authorizes them; named detailed and public full-detail modes may retain authorized specifics.

Search intensity:
Low, moderate, high, or very high.

Parallelism:
Primarily sequential, limited parallel proposal work, broad parallel search, or another concise
description. Separate reasoning parallelism from measurement parallelism where relevant.

Human involvement:
Mostly autonomous, periodic review, frequent steering, or tightly supervised.

Resource intensity:
Use a qualitative band in anonymized mode unless the recorded boundary authorizes exact aggregate
counts, compute, time, or cost. Named detailed and public full-detail modes may retain authorized exact
values.

Breadth:
Isolated component, several components, or project-wide methodology.

Starting infrastructure:
Describe the evaluator, experiment ledger, worker isolation, orchestration, recovery, promotion
gates, and monitoring present at the beginning.

Ending infrastructure:
Describe the same capabilities at the end.

Infrastructure changes:
State which observations came from the earlier setup and which followed major harness improvements.
Use the capability checklist from the contribution guide rather than relying only on a maturity label.

Decision influence:
Advisory, useful, important, or critical.

Outcome contribution:
State whether it accelerated work, produced key discoveries, strengthened validation, prevented
failures, supplied infrastructure, or had mixed or little value.

Counterfactual:
What likely would have happened without autoresearch. State uncertainty.

## Material new learnings

### Short descriptive title

Observation window:
State when this specific behavior was observed within the overall calendar window.

Infrastructure context:
State the evaluator, ledger, isolation, orchestration, promotion, recovery, and monitoring capabilities
that materially affected this observation.

Observation:
What happened. Remove identifying details in anonymized mode, but retain concrete context authorized
by its recorded project-specific boundary. Named detailed or public full-detail mode may retain other
authorized concrete context.

Interpretation:
The proposed general lesson and causal explanation.

Evidence class:
One of the evidence classes in the contribution guide.

Confidence:
Low, medium, or high.

Boundary conditions:
When the learning may not transfer.

Maturity dependence:
State whether the finding is likely about the model or research method, the infrastructure available at
the time, or an interaction between them.

Cheapest falsification:
How another project could test whether the lesson applies.

Existing synthesis relationship:
State whether this is new, strengthens an existing principle, qualifies it, or contradicts it. Name
the relevant heading in the existing learnings.

Suggested destination:
principles.md, agent-search-retrospective.md, a domain playbook, or no promotion yet.

## LLM and agent observations

For every named model or agent system used, record:

- Public model or product name.
- Calendar window in which it was observed.
- Exact model version or route when known.
- Role it performed.
- What it was consistently good at.
- What it was consistently bad at.
- Relative speed or cost. Use qualitative terms in anonymized mode unless exact aggregate values are
  explicitly authorized. Retain authorized exact values in named detailed or public full-detail mode
  when useful.
- Recurring failure patterns.
- Best role assignment.
- Evidence strength as low, medium, or high. Anonymized mode may retain explicitly authorized aggregate
  counts. Named detailed and public full-detail modes may also retain authorized exact counts.
- Possible dependence on version, provider routing, prompting, tools, or harness design.

In anonymized mode, do not reveal the private task or application domain unless the recorded boundary
explicitly authorizes that context. In named detailed mode, retain authorized task context that makes
the model observation understandable without reproducing private repository content.

## Findings that should remain unpublished

List only categories of useful material that were intentionally excluded. Do not include the excluded
content itself. For named detailed mode, distinguish repository-owned material from details the
contributor authorized for publication.

## Findings not ready for promotion

Record plausible observations that lack evidence, have unresolved confounders, or may be
project-specific.

## Proposed wording

Provide concise, publication-ready wording for the strongest findings. It must be understandable
without knowing the source project.

## Disclosure audit

For anonymized mode, compare the completed draft against the locally recorded allowed and withheld
categories. Report whether it contains project identifiers, private paths, unauthorized domain
fingerprints, unauthorized exact metrics, proprietary terminology, private URLs, raw hashes, or
identifying combinations of details. Remove or generalize anything outside the boundary before
reporting that the audit passed.

For public full-detail mode, run a publication audit instead. Confirm that every identifying detail,
metric, link, revision, and operational fact is authorized for publication. Independently check for
credentials, personal data, confidential third-party information, private endpoints, unpublished
conversations, and security-sensitive details. Remove anything outside the authorization boundary.

For named detailed private-repository mode, run a named-detailed publication audit. Confirm that the
draft retains as much authorized concrete detail as possible while reproducing no source code, private
repository files or URLs, reconstructive excerpts, credentials, personal data, or confidential
third-party material. Confirm that the report clearly states that its primary evidence is private and
not independently inspectable by public readers.
```

## Instructions for contributing agents

An agent following this guide must:

- Treat the current private workspace as evidence to summarize, not material to copy.
- Avoid copying raw records, logs, prompts, code, or long quotations into the draft. Named detailed
  mode permits detailed paraphrase, not republication of private repository content.
- Avoid running Git commands or editing tracked files in `/code/autoresearch`.
- Record the local calendar window and infrastructure maturity. Publish exact or generalized dates
  according to the declared disclosure mode and authorization boundary.
- State the disclosure mode and never infer detailed-publication authority merely from repository
  visibility or access.
- Prefer a short set of defensible findings over an exhaustive project narrative.
- State uncertainty and unresolved confounders explicitly.
- Write only the contribution draft under `/code/autoresearch/.local/contributions/`.
- End its response with the draft path and whether the applicable redaction or publication audit passed.

## Curator review

Before promotion, the curator should:

- Verify the declared disclosure mode, any anonymized-mode exceptions, and explicit authorization for
  named detailed or public full-detail publication.
- Repeat the applicable privacy or publication audit without opening unnecessary private records.
- Compare the draft against existing learnings for duplication.
- Verify that the calendar window describes the actual observations rather than file dates or the date
  the contribution was written.
- Calibrate confidence against the observation period, intensity, independence, and breadth of use.
- Check whether a model or workflow observation depends on the infrastructure available during that
  calendar window rather than on the model itself.
- Compare the contribution against newer case studies and current harness capabilities. Mark older
  findings as legacy, superseded, narrowed, or requiring retest when the infrastructure scope changed.
- Check that claimed project impact includes a plausible counterfactual and is not inferred from
  experiment volume alone.
- Check whether observations and interpretations are clearly separated.
- In anonymized mode, reject claims whose useful meaning depends on restoring withheld details, but
  retain explicitly authorized domain, aggregate, and methodological context when it improves meaning.
  In named detailed mode, include authorized details when they materially improve meaning, while
  excluding repository-owned content.
- Preserve model names only when their role-specific behavior is informative.
- Merge accepted wording into the smallest relevant existing document.
- Update review dates and source relationships where appropriate.
- Keep the local contribution draft out of Git.

## Publishing anonymized case studies

The curator may publish a contribution as a case study after integrating its durable findings. Keep
the complete contribution draft local and create a separate curated file under `case-studies/`.

A public case study should retain:

- A coarse or exact calendar window when publication is safe.
- Duration, intensity, project phases, parallelism, and human involvement.
- Starting infrastructure, ending infrastructure, and the timing of material harness changes.
- Project impact and a qualified counterfactual.
- Named public models and role-specific observations.
- Material findings, provisional hypotheses, and evidence limits.
- Any domain, aggregate metrics, dataset scale, or generic operational detail explicitly authorized by
  the recorded anonymized boundary.

It should remove editorial routing fields, repeated proposed wording, private-content inventories,
local paths, unauthorized identifying operational combinations, and unnecessary implementation
detail. Use a neutral title based on research shape by default; an explicitly authorized domain may
appear in the title.

Do not mark a case study ready for publication while its calendar window, starting infrastructure,
ending infrastructure, or material infrastructure-change timing remains unknown. A clearly labeled
draft may retain pending fields while the source project backfills them.

Local contribution drafts are inputs to editorial judgment and case-study curation. They are not
published directly.

## Publishing full-detail project reports

For an authorized public project, the curator may publish a named report instead of an anonymized case
study. Use a human-readable project title and link claims to public commits, evaluations, issues, or
other authorized evidence where practical.

The report should make the timeline and infrastructure evolution explicit, distinguish discovery from
promotion runs, preserve failed interventions and provisional hypotheses, and state how materially
autoresearch affected the project. It should also identify which observations are likely specific to
the model version, provider route, harness maturity, hardware, or workload.

When a report describes an older or materially simpler harness, label it prominently as legacy
evidence. Do not present its autonomy, throughput, or model limitations as current capability claims
without reproduction on the newer infrastructure.

Full-detail reports still require the publication audit. Public project identity does not weaken the
rules against secrets, personal data, third-party confidentiality, or unsupported claims.

## Publishing named reports backed by a private repository

For authorized work in a private repository, the curator may publish a named, detailed report without
publishing or linking the repository. The report should explain the project, experiments, exact
results, infrastructure evolution, model roles, failures, and impact as concretely as the contributor's
authority permits.

State near the beginning that the underlying repository and primary artifacts are private, so the
report is a practitioner account rather than publicly reproducible evidence. Prefer original summary,
small derived tables, and detailed paraphrase. Do not reproduce source code, private files, private
links, or enough proprietary structure to substitute for access to the repository.

Named private-repository reports require a named-detailed publication audit. Naming a project does not
weaken the rules against credentials, personal data, third-party confidentiality, unsupported causal
claims, or material outside the contributor's publication authority.
