# Case 04 - Public headless live automation

Observation window: 2026-04-14 through 2026-04-16
Disclosure mode: public full-detail
Project: [Gradient Bang Headless](https://github.com/wakamex/gradient-bang-headless)
Evidence cutoff: [`0e5dace`](https://github.com/wakamex/gradient-bang-headless/commit/0e5dace72ac489afcdf35adc90af9949ea079ce2)

## Scope and evidence boundary

This case covers one concentrated campaign to build and operate a headless client against the live
[Gradient Bang](https://www.gradient-bang.com) production game with ordinary player authority. Some
actions passed through an LLM-mediated session, while others were direct client messages or public
control-plane requests. The campaign had to locate each semantic action, build reliable transports,
convert recurring behavior into bounded commands, and verify progress against live state.

The owner authorized public full-detail publication on 2026-08-10. Public history contains 64 commits
over three days, but that count mixes implementation, diagnosis, documentation, and live operation.
There was no structured run ledger, sealed evaluator, resettable account, complete session archive, or
cost record. Live leaderboard values are operational snapshots, not stable promotion evidence.

## Exposure and project impact

- Duration: three days in one highly concentrated build and live-operation campaign.
- Search intensity: very high implementation and diagnostic activity.
- Execution: mostly sequential, with isolated subprocess workers added for parallel exploration late in the campaign.
- Human involvement: iterative steering and final strategy judgment, without preserved turn-level attribution.
- Resource burden: moderate, using many short live transactions and transport diagnostics rather than heavy compute.
- Breadth: authentication, transport, event correlation, exact actions, routing, state validation, recovery, worker isolation, and strategy.

The campaign created a reusable live-player control surface and materially accelerated progression. It
also prevented repeated invalid actions by correcting transport, event, market, and map assumptions.
The durable contribution is the control and validation methodology, not the observed leaderboard rank.

Without source tracing and bounded live tests, the project would likely have extended brittle browser
automation, credited old task completions to new requests, issued invalid trades, and spent movement
resources on false frontiers. This is a qualified reconstruction rather than a measured counterfactual.

## Infrastructure timeline

On 2026-04-14, the project began as a small Python CLI in a shared writable worktree with pinned
upstream source. It had manually launched commands and live production outcomes, but no experiment
ledger, isolation, orchestration, recovery controller, artifact identity, or promotion gate.

The first phase added browser action sequences and DOM fallbacks. Source tracing then showed that
visible actions resolved to direct public requests, Pipecat client messages, or local UI state. On
2026-04-15, the project [refocused on semantic transports](https://github.com/wakamex/gradient-bang-headless/commit/af1b9e49af732936a6e6424e0097ed64f0673871)
and [removed the supported browser gameplay layer](https://github.com/wakamex/gradient-bang-headless/commit/92e253bcb3e40b5ef4339fd542ea985dabb6b2f4).
The browser remained only where it hosted a required transport or supplied diagnostics.

The middle phase added raw and browser-backed session transports, named messages, live state reads,
and task-aware commands. A production race showed that an old terminal event could be mistaken for the
completion of a new request. [Task-control hardening](https://github.com/wakamex/gradient-bang-headless/commit/a53b67995088983aed0491572095515fc7c39623)
bound completion to the newly observed task identity and added authoritative postcondition polling for
actions whose terminal events were delayed or missing.

On 2026-04-16, recurring gameplay moved from broad natural-language objectives toward deterministic
outer loops and exact frontend-derived contracts. A
[deterministic trade loop](https://github.com/wakamex/gradient-bang-headless/commit/4bafd1d468cbe94cef2aa13ef17b89d04a4df342)
still failed until [legality checks](https://github.com/wakamex/gradient-bang-headless/commit/a31a562e320c2fa8cfe6e4a14ff3c3f17888f620)
included market direction, stock, capacity, and credits.

Exploration then exposed a bounded-view error. A local map response could omit an already known sector,
making it look unexplored. The [validated frontier selector](https://github.com/wakamex/gradient-bang-headless/commit/532fa2a1a2aaba7a38d90875b5cbbc98be235dbf)
recentered queries before committing movement. The final phase added a
[probe fleet loop](https://github.com/wakamex/gradient-bang-headless/commit/d649d5daa4757b0bd7c7bf7387781549b0dbeda0)
with one subprocess and session per ship, followed by
[explicit frontier targets](https://github.com/wakamex/gradient-bang-headless/commit/820e0b5cac2fbbd4182bb66c81aec94bdfcb3bf1)
after generic exploration prompts failed to exploit staged frontiers reliably.

By the end of 2026-04-16, the project had a broad live-player CLI, bounded waits and retries, exact
prompt builders, task identity, postcondition checks, route and frontier validation, and isolated probe
workers. The public narrative recorded completed tutorials, trade, combat, salvage, garrison, fleet,
and exploration activity. It also recorded contemporaneous visible ranks of 29 in exploration, 27 in
trading, and 70 in wealth. These were mutable snapshots in a live multiplayer system.

Important gaps remained. The live evaluator and narrative were mutable, every run changed account
state, recovery was command-specific, and there was no complete transaction identity, persistent
orchestrator, freshness monitor, sealed promotion stage, or independent review.

## Durable findings

### Trace the semantic action before automating presentation

The campaign initially automated the rendered browser interface. One representative source trace
showed that stable semantic requests and session messages owned most gameplay actions, leading to the
deletion of the supported browser gameplay layer.

Before investing in UI automation, trace a visible action to its outbound semantic transaction and
compare postconditions. A browser may be required to host a transport without being the correct action
API. UI automation remains appropriate when presentation behavior itself is the claim.

### Bind asynchronous completion to identity and state

An acknowledgement, start event, finish-shaped event, and changed state proved to be different
authorities. An old finish event could satisfy a new watcher, some valid tasks changed state without a
timely finish, and closing a session after start could cancel work.

Capture the new operation identity, reject unrelated terminal events, remain attached for the required
lifecycle, and verify the smallest authoritative postcondition. State polling can establish completion
only when the transition is unique and the read is fresh.

### Put deterministic contracts around a stochastic executor

Broad agent objectives drifted, timed out, or stopped in partial states. Exact prompt builders and
deterministic outer loops computed quantities and paths, rejected illegal actions, issued one bounded
semantic step, and checked the resulting state.

When an agent is intentionally part of the product path, keep arithmetic, legality, identity,
sequencing, and stopping in deterministic code. This does not remove the agentic layer; it confines its
authority to the semantic work that requires it.

### Missing data in a bounded view is not a novel state

The first frontier ranker treated sectors absent from a local map window as unexplored. Recentered
queries showed that some were already known outside the response window, wasting movement on false
frontiers.

Before acting on absence from a local, paginated, cached, or windowed response, expand or recenter the
query and verify that the identity remains absent. This is especially important when testing the
boundary consumes scarce or irreversible resources.

### Parallel actions need exclusive observation lanes

Independent ships did not imply independent measurements when concurrent workers shared one event
stream. One worker could consume another operation's event. The project moved each selected ship into
its own subprocess and session.

Parallel external transactions need isolated observation lanes or correct identity-aware
demultiplexing. If correlation-safe multiplexing is unavailable, isolate by process or session. This
qualifies general advice to parallelize reasoning while serializing contested measurement.

## Model and agent observations

The public history does not retain the coding agent's exact model, provider route, prompt, or cost. It
supports sustained repository-wide implementation, source tracing, reusable command construction, and
current narrative maintenance. Workflow failures included building the wrong layer first, accepting
event-shaped evidence without identity, omitting market semantics, and extending exploration before
auditing the map representation. Human judgment and changing infrastructure prevent attribution of
those failures to a named model.

The live game agent also mediated some actions. Its exact production route was not retained and may
have changed upstream. Prompt drift and incomplete long objectives were confounded by controller and
session behavior, so they do not support a named-model claim.

## Unresolved claims

- Live leaderboard movement is not a frozen autoresearch evaluator.
- The final parallel-probe strategy was not compared with a matched sequential policy.
- The campaign does not establish autonomous reliability, throughput, or model capability.
- Public operational snapshots do not establish an optimal game strategy.

## Current status

This is short, high-intensity legacy evidence from a live, non-resettable environment. Several findings
are strong because concrete failures were reproduced and corrected at the responsible layer. A modern
retest should add an append-only transaction ledger, complete code and configuration identity, explicit
evidence labels, recovery tests, progress freshness, and independent promotion authority where a
stable promotion claim is possible.
