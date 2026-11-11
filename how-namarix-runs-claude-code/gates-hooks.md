---
name: gates-hooks
description: Use when an AI coding change must be checked before integration, and deliver a gate that reports only verified-green or not-green with clear failure reasons.
tools: Read
version: 0.1.0
---

# AI coding agent gates and hooks

## When to use it
- When adding or changing a test gate, script, or CI job.
- When a test layer may be skipped, unavailable, or only partially executed.
- When registering new test suites or changing the set of gated files.
- When local hooks and server-side checks need clear responsibilities.

## Steps
1. List the required checks for the change and confirm that each test or suite is registered with the gate.
   - Why: A check that is absent from the gate cannot protect the change, even if its test exists.
   - Check: Review the gate's registration list and confirm there are no missing files, stale entries, duplicates, or empty suites.
2. Make every required gate fail closed (when a check cannot run, it counts as not passed): allow only verified-green or not-green, and treat skips, missing dependencies, missing credentials, and absent files as failures.
   - Why: A gate that cannot run must not make an unverified change appear ready.
   - Check: Use a deliberately unavailable prerequisite or skipped layer and confirm the gate reports not-green and exits non-zero.
3. Require each child suite to demonstrate that it executed, not merely that its process returned success.
   - Why: A successful process can still have asserted nothing or have failed to run a declared portion of the suite.
   - Check: Confirm the result includes a non-zero passing count, no failing count, and no shortfall against the suite's declared total.
4. Place essential enforcement at a server-side or other mandatory layer, and use local hooks for guidance and early blocking rather than as the sole guarantee.
   - Why: Local hooks can be missed or fail open, while mandatory integration checks provide the stronger protection.
   - Check: Inspect the design and identify which rules remain enforced when an agent skips or cannot run local hooks.
5. Report the final status without calling the run green when anything was skipped or unverified.
   - Why: A summary that hides an unexecuted layer recreates the distinction between apparent success and verified work.
   - Check: Search the final report for skipped or unverified work and confirm the summary remains not-green whenever either is present.

## Outcome
Every gate produces either verified-green or not-green. Skipped, missing, unregistered, or unverified work cannot be reported as green.

## Example (made up)
Made-up example: Team Alpha adds an AI coding agent test suite. It defines verified-green and not-green, then checks that the suite ran, has passing assertions, has no failures, and reaches its declared total. Registration checks reject an unlisted test file. When one dependency is unavailable, the gate reports not-green with the repair needed, so Team Alpha does not treat the change as verified.

## Pitfalls
- Treating a skip, missing prerequisite, or absent file as a pass makes an unverified change look ready.
- Relying on a zero exit code alone can pass a suite that asserted nothing or failed to execute a declared portion.
- Adding a skip or allow-unverified escape hatch silences the failure instead of fixing the environment.
- Using local hooks as the only guarantee leaves enforcement vulnerable when a hook is forgotten or fails open.

## Measured result
No number is published for this practice yet.

## Credits
Mark Lim, Founder at Namarix and Cheatsheet, from how Namarix runs its own AI work.
