# GPU-optimization autoresearch

Status: active
Reviewed: 2026-08-10
Scope: Evaluation contracts, research loops, safeguards, and operating rules for dependable GPU-backed optimization.
Case-study basis: Cases 01, 02, 04, and 06 under `case-studies/`, covering performance measurement,
GPU-backed training and runtime work, accelerated execution, and production-constrained accelerator use.
External-review basis: `external-review/README.md`.
Synthesis dependency: `principles.md` and `agent-search-retrospective.md`.
Applied evidence windows: adjacent GPU-backed and accelerator work from 2026-04-15 through 2026-05-08,
2026-07-08 through 2026-07-27, and 2026-08-06 through 2026-08-08. No dedicated campaign with custom
GPU kernel code as the primary edit surface is documented.

Build the pipeline around these principles. Keep it lean; the objective is dependable GPU-backed
optimization, not an elaborate agent framework. Kernel work is one possible edit surface, not the
only one.

## Architecture

- Use a thin, long-running orchestrator that launches one fresh isolated worker per experiment.
- Give each worker one concrete hypothesis, the current baseline, the allowed edit surface, and the immutable evaluation protocol.
- Use separate worktrees or disposable copies. Workers must never share mutable source state.
- Permit modification of only the component or kernel under study. The evaluator, correctness oracle, benchmark cases, timing code, and promotion rules must be read-only to workers.
- Run one hypothesis per experiment and preserve the exact diff.

## Evaluation contract

### Correctness gate

- Compare against a trusted reference across all registered dtypes, shapes, layouts, alignments, boundary sizes, and relevant numerical edge cases.
- Define tolerances before starting. Candidates cannot weaken tolerances, drop cases, specialize by detecting benchmark inputs, skip computation, reuse stale output, or change semantics.
- Use exact parity when the candidate claims to preserve numerical or output semantics. When the declared mechanism intentionally changes precision, decoding, boundaries, formatting, or another semantic layer, treat parity differences as review triggers under a frozen operation-specific quality contract rather than automatic failures.
- Include awkward and adversarial shapes, not only tile-friendly dimensions.
- Reject crashes, races, nondeterminism, illegal memory accesses, and architecture-specific failures.

### Performance measurement

- Before measuring timing dispersion, prove that repeated baseline runs execute the same workload using a compact operation signature, output digest, and relevant stochastic-state checks.
- Use GPU events with explicit synchronization, warm-up iterations, and enough timed repetitions.
- Randomize or alternate baseline/candidate order to reduce thermal, clock, and cache drift.
- Report medians and dispersion, not the single fastest run.
- Confirm improvements in a fresh process and preferably after rerunning the baseline.
- Select on the aggregate target workload while enforcing per-case regression limits. Do not allow one spectacular shape to conceal material regressions elsewhere.
- Test multiple seeds where candidates contain stochastic behavior.
- Test every production GPU architecture in scope. A gain on one device is not automatically a general win.
- Exclude compilation/autotuning time unless it is part of the production objective.
- Treat profiler counters as diagnostic evidence, not the promotion metric.
- Use microbenchmarks and profiler buckets for mechanism discovery, then require transfer to the representative end-to-end workload unless the local primitive is itself the declared production objective.
- If an optimization changes model or component quality, select it through the deployed outer loop at the real resource budget and in the representative data regime. Throughput is a direct selector only after the declared quality contract establishes behavior preservation.
- When both a compiled artifact and its runtime path changed, rerun the unchanged artifact on the new runtime before attributing the result. If needed, complete the crossed comparison, and record content digests for both artifacts, both executables, and the loaded configuration.

### Evaluation stages

1. Smoke: compile, correctness, sanitizer/race checks, a few benchmark cases.
2. Scout: short benchmark across the complete shape-class matrix.
3. Confirm: more repetitions, fresh process, baseline rerun, full correctness suite, and all target GPUs.
4. Promote only if the confirmed gain exceeds a predeclared noise margin and no protected case regresses beyond its limit.

## Research loop

For every experiment:

1. Read the append-only ledger and exclusion map so known dead ends are not repeated.
2. State the mechanism before editing: e.g. occupancy, memory coalescing, reduced synchronization, instruction count, register pressure, shared-memory traffic, launch overhead, or fusion.
3. Make one attributable change.
4. Run the locked evaluator.
5. Keep or discard mechanically according to the registered gates.
6. Record the hypothesis, diff/commit, hardware, compiler flags, correctness result, full timing distribution, profiler explanation, verdict, and runtime.
7. Commit the result - even negative results should update the ledger so they compound into knowledge.

## Search policy

- Permit at most one bounded parameter sweep per hypothesis, with a small preregistered grid.
- Select the parameter on scout cases, then evaluate that one choice on untouched confirmation cases.
- Do not repeatedly narrow grids around noise.
- Prefer structural hypotheses over tile-size churn.
- After roughly five incremental cycles, or whenever progress plateaus, run a fresh-start cycle: ask a worker to ignore the current implementation and derive a materially different approach from the operation's constraints.
- Periodically ask a different model to propose hypotheses; cross-model diversity was more useful to us than having one model endlessly refine its own local optimum.

## State and artifacts

Maintain:

- An append-only experiment ledger in JSONL/TSV.
- A concise Markdown learnings file containing breakthroughs, dead families, architecture-specific findings, and unresolved questions.
- Exact source commit, toolchain versions, GPU model/driver, benchmark manifest hash, evaluator hash, and command line for every run.
- Raw timing and correctness artifacts outside Git, with hashes or a durable artifact location.
- The promoted implementation and every promotion decision in Git.

## Operational rules

- Bound every experiment by wall time.
- Detect and clean up orphaned compiler/benchmark processes.
- Limit parallel experiments so workers do not contend for the same GPU or distort measurements.
- Never benchmark two candidates concurrently on one GPU.
- If a production service shares the GPU, submit research through the production scheduler as a bounded lowest-priority transaction. The scheduler must enforce deadlines, clean up descendants, and restore the known resident state before admitting normal work.
- Restore the baseline after every failed or interrupted experiment.
- Resume from the ledger, not from a growing chat transcript.

## Stop conditions

Stop an optimization family when repeated independent variants fail, gains are below the measured noise floor, or improvements only transfer to benchmark-specific cases. Declare the pipeline complete when the remaining ideas have low expected value - not merely when the agent runs out of ideas.

## First deliverable

Before launching a long campaign, demonstrate three end-to-end experiments:

- one deliberately incorrect candidate that the correctness gate rejects;
- one performance-neutral change classified inside the noise band;
- one known optimization that is correctly measured and promoted.

Do not start an overnight run until all three behave as expected.

## Additional safeguards learned the hard way

- Prove that the intended candidate was actually evaluated. Have every evaluator result echo the source commit, candidate diff hash,
  compiled artifact or implementation hash, benchmark manifest hash, and effective configuration. Build in a fresh process or content-addressed
  cache namespace. Treat an unknown option, ignored environment variable, stale binary, or configuration mismatch as a hard failure.
- Keep the evaluator claim surface small. Admission and program identity should be runner-owned rather than caller-asserted; schemas
  should be closed; numeric checks should cover derived values and reject non-finite results; artifact identity should be established
  from one opened object rather than separate read and hash paths.
- Test the orchestration machinery, not only the optimized component. Before a campaign, deliberately exercise timeout, crash, malformed output,
  interrupted build, stale-cache, and resume paths. Verify that each produces the expected ledger entry and restores a usable baseline.
- Deduplicate both source and behavior. Reject byte-identical patches immediately, and compare each candidate's per-case timing vector,
  generated-code hash, and mechanism family against prior work. Repeated discovery is evidence only when runs began from meaningfully
  independent context and produced materially different implementations.
- Keep discovery and confirmation separate. Workers may see scout workloads, but preserve an untouched confirmation set or workload
  slice for promotion. Do not feed detailed confirmation failures back into repeated tuning against that same set.
- Assign one explicit judgment owner. Workers propose and measure; the lead curates the brief, closes exhausted families, designs exact
  follow-up experiments, and audits surprising wins. Do not let automatic LLM synthesis overwrite a stronger hand-written brief.
- Use fresh sessions for workers and persist only structured state: hypothesis, mechanism, patch, score, and takeaway. Share accumulated
  takeaways for exploitation cycles, but occasionally run a blinded fresh-start worker that cannot anchor on the current champion.
- Distinguish cheap and expensive claims. Compilation and scout timing can be decided mechanically in-loop; portability across GPU
  generations, production workload representativeness, and release readiness require a predeclared confirmation battery and explicit
  judgment-layer sign-off.
- Optimize information gained per GPU-hour, not experiment count. A deterministic sweep or targeted falsification test is often more
  valuable than another open-ended agent cycle, especially after several agents converge on the same local optimum.
