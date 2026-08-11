---
{
  "case": 9,
  "title": "FreeTranscribe.org GPU inference optimization",
  "started": "2026-08-06",
  "ended": "2026-08-08",
  "featured_rank": 2,
  "summary_markdown": "[FreeTranscribe.org](https://freetranscribe.org/) doubled transcription throughput while sharing one RTX 3090 between live production and autoresearch. Error counts stayed unchanged across 295 broad cases and fell from 105 to 103 on a reviewed long-form set."
}
---

# Case 09 - FreeTranscribe.org GPU inference optimization

Observation window: 2026-08-06 through 2026-08-08
Disclosure mode: named detailed, private repository
Duration: three calendar days in one concentrated campaign
Project: [FreeTranscribe.org](https://freetranscribe.org/), a production web service for private AI transcription

The implementation repository, evaluator, and primary artifacts remain private. This is an authorized
practitioner account of my work, not independently reproducible public evidence. Current-infrastructure
checks on 2026-08-10 and 2026-08-11 are comparisons, not extensions of the campaign window.

## What the campaign covered

FreeTranscribe.org served real transcription requests from the same 24 GB RTX 3090 used for research.
The resident NVIDIA Parakeet worker occupied about 3.2 GiB while idle. The research problem therefore
combined model-serving optimization with production-priority admission, cleanup, restoration,
evaluator authority, and campaign orchestration.

The ledger contains 92 transactions: 67 complete, 9 crashed, 7 invalid, and 9 timed out. Verdicts were
21 keep, 46 discard, 18 crash, and 7 invalid. Recorded research use totaled 6,996 GPU-seconds, or 1.94
GPU-hours, and retained manifests, telemetry, results, and ledgers occupied about 9 GB. Search was
intensive, GPU measurement was serialized, and human steering remained frequent.

## Infrastructure and evidence authority

On 2026-08-06, FreeTranscribe.org had a live resident model, a customer queue, a validation package,
and manual controls. It lacked a research transaction type, frozen evaluator, structured ledger,
isolated candidate workers, persistent conductor, research admission, complete artifact identity,
automated recovery, and progress monitoring.

On 2026-08-07, the project added bounded experiment contracts, isolated worktrees, structured
manifests and results, process-group timeouts, an append-only operational ledger, and a production-owned
priority queue. The live worker became the only authority allowed to admit research to the GPU.
Identity capture covered candidate, workload, model artifact, evaluator, dependencies, effective
configuration, device, timing, memory, power, and normalized output.

Discovery operations could not claim promotion. One exact Parakeet candidate received a separately
authored clean promotion route with frozen broad and representative confirmation, disagreement review,
and explicit owner authorization. A broader promotion-evaluator prototype failed two adversarial
reviews on 2026-08-08 and never became promotion authority. Later batching results also remained
discovery-only.

## What happened

### Production owned every research lease

The production queue prioritized paid customers, free customers, local-agent transcription, and then
research. Research used its own lifecycle rather than masquerading as customer work. The isolated
runner received no production database, uploads, results, payment, email, deployment credentials, or
customer media.

After atomically confirming that no customer request was waiting, the production worker unloaded the
resident model, verified released CUDA state, granted one opaque experiment to the isolated runner,
heartbeated the lease, enforced a five-minute deadline, recorded a normalized result, and exited. The
service manager then started a fresh worker that reloaded, warmed, and identity-checked the production
model.

This prevented independent CUDA processes from competing for memory and made one state machine own
admission, deadlines, cleanup, and restoration. The design was intentionally non-preemptive: a customer
arriving immediately after admission could still wait for the remaining research slice plus roughly
25 seconds of model reload, about five and a half minutes in the worst case. The pattern is therefore
appropriate only for the observed low-demand service and latency contract.

### Deployed: throughput doubled with flat broad errors and fewer long-form errors

The production gain came from faster inference inside the already resident model, not from startup or
model loading. The promoted `nvidia/parakeet-tdt-0.6b-v3` stack used local relative-position attention
with context `[256, 256]`, conditional FP16 encoder compute for inputs longer than five seconds, an
FP32 handoff into the decoder, FP16 decoder and joint compute plus parameter storage, and no unused
full-alignment retention while preserving timestamps. Deterministic initialization controlled identity
and reproducibility rather than providing the speedup.

Aggregate audio throughput rose from 175.54x to 365.55x realtime, a 2.08x increase. The direct endpoint
comparison reduced warm median inference processing time from 0.5722 to 0.2020 seconds, and the sealed
promotion independently reproduced a 65.39% reduction in that measure.

Quality was neutral to positive on the frozen evidence. Across 295 Open ASR cases, baseline and
candidate each produced 1,743 total errors, every case retained the same error count, and six
equal-error output differences were reviewed. The private long-form set improved from 105 to 103
reviewed errors. A fresh ordinary queued production transcription then completed in 0.752 seconds with
timestamps and promoted settings persisted.

These were warm resident-model measurements. They excluded the roughly 25-second reload after a
research lease, and ordinary production amortized startup by keeping Parakeet loaded. FreeTranscribe.org
did not buy the deployed speed by accepting lower measured quality on the promotion corpora.

This was the campaign's one sealed promotion. It does not promote every retained checkpoint or prove
that the same configuration generalizes to other models, hardware, or workloads.

### Discovery-only: batching offered a second throughput path

A separate batch-size-two path reduced same-duration pair completion time by 40.20%, equivalent to
67.2% more pair throughput. Mixed-duration pairs improved 44.78% at the median, equivalent to 81.1%
more pair throughput. Tested outputs retained exact normalized transcript and millisecond timestamp
parity.

Batching was not deployed. It was not proven to compose with the complete promoted stack, and live
admission, customer waiting, delivery, recovery, and the proposed promotion evaluator remained
unvalidated. It is promising evidence for a second throughput multiplier, not part of the claimed
production gain.

Other attempted speed paths did not survive. Conditional CUDA graphs failed reproduction, TF32 stayed
below the gain threshold, a newer NeMo runtime was slower, encoder compilation timed out, narrower
attention improved too little, and direct FP16 handoff regressed.

### Exact parity was too strict for a quality-changing mechanism

An early universal exact-output gate rejected the retained stack even though aggregate quality did not
regress and reviewed long-form errors improved. Precision and decoding changes can legitimately alter
equivalent wording, formatting, or boundaries.

The corrected evaluator kept deterministic replay, frozen references, aggregate and per-case limits,
and explicit review of every new disagreement. Exact parity remained mandatory for mechanisms claiming
identical behavior. For semantics-affecting changes, it became a review trigger rather than automatic
rejection.

### Parallel agents did not imply parallel GPU experiments

Codex workers produced competing recovery designs, a quantization audit, and independent evaluator
attacks while all RTX 3090 measurements remained serialized. Parallel reasoning exposed issues that a
linear pass had missed, but it did not increase GPU throughput because there was no sustained backlog
of executable measurements.

Two final evaluator reviews completed together in 636.66 seconds; their recorded task durations summed
to 1,228.30 seconds. That is not a controlled 1.93x speedup because startup, caching, task variance, and
a matched serial run were absent. Raising parallelism mainly to consume an expiring agent quota also
caused lower-priority tasks to be stopped before producing usable artifacts.

Autoresearch therefore had two schedulers: one for parallelizable reasoning and review, and another for
contested physical measurement.

### Evaluator hardening became its own search surface

Successive evaluator revisions bound more source, runtime, model, corpus, timing, and artifact
identity. Two adversarial reviews still found caller-asserted admission, overflow in derived numeric
values, weak time conservation, runtime impersonation, permissive scalar typing, incoherent structured
output, and artifact replacement races.

The broader evaluator had expanded its trusted computing base faster than local fixes could establish
authority. It was rejected. The lesson was to prefer a small runner-owned program, closed inputs,
single-open artifact verification, exact environment binding, and finite checks on both raw and derived
values. Repeated integrity failures called for simplifying the premise, not adding another check.

### A live process was not a live campaign

The research runner remained healthy after the campaign, but the managed conductor stopped and no
research transactions were queued. On 2026-08-11, the production worker and runner were still active,
the customer queue was empty, no Codex workers were running, and no research was progressing.

A healthy unattended campaign therefore needs a recent ledgered result, valid queued or running work,
or a named blocked gate. PID, service, and socket health only prove availability.

## Model and agent observations

OpenAI Codex CLI acted as the persistent judgment-layer orchestrator, isolated implementation worker,
and adversarial evaluator reviewer from 2026-08-07 through 2026-08-08. Archived records identify the
Codex product, subscription billing, and high reasoning for the final reviews, but their model field is
empty. The current 2026-08-11 configuration names GPT-5.6-sol and must not be projected backward.

Codex was effective at unfamiliar-code inspection, bounded implementation, deterministic testing,
concrete evaluator attacks, layer-specific diagnosis, and theory revision after counterexamples.
Nearby variants, infrastructure counted as progress, evaluator complexity growth, and process
liveness mistaken for campaign progress were recurring failures. There was no controlled model-family
comparison.

## Project impact and limits

Autoresearch materially changed FreeTranscribe.org's deployed Parakeet path, established safe
production-priority GPU sharing, and prevented several nonreproducible or weakly authorized results
from advancing. Its strongest value came from causal falsification, adversarial review, and explicit
evidence boundaries rather than uninterrupted autonomy.

Readers cannot inspect the private evaluator, model artifacts, customer workload, manifests, or
promotion review. The frozen results support no measured quality tradeoff on the tested promotion
corpora, not a universal accuracy improvement on all future audio.
