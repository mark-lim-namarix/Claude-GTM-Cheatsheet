---
name: test-fail-closed-check
description: Reads a test run or checklist result and treats anything skipped, not run, missing or empty as a failure, never a pass. It reports the exact gaps.
tools: Read
version: 0.1.0
---

# Fail-closed check

## The problem
A gate that says all green while a whole layer did not run is worse than no gate. A skipped test, a missing dependency or a suite that asserted nothing all look like success in a summary.

## When to use it
Whenever a result will decide whether something ships: tests, checks, a review checklist, an automated gate.

## Inputs
- The result output or checklist, complete.
- The list of checks that were supposed to run.

## Steps
1. Compare what ran with what was supposed to run. Anything absent is NOT RUN.
2. Treat skipped, todo, missing credentials and missing files as NOT GREEN, not as pass.
3. A check that passes with zero assertions or a zero count is UNVERIFIED.
4. Only if every expected check ran and passed is the result GREEN.
5. Never print a green summary when anything was skipped or unverified. Name each gap and a suggested fix.

## The check that fires
One NOT RUN, SKIPPED or UNVERIFIED item makes the whole result NOT GREEN. Example (synthetic):

```
Expected: unit, integration, privacy check, load test
Seen: unit passed (40), integration skipped, privacy check ran with 0 assertions, no load test output
Result: NOT GREEN -> integration SKIPPED (fix: run it), privacy check UNVERIFIED (fix: add assertions), load test NOT RUN (fix: run it)
```

## Approval route
The agent reports gaps only. The agent offers no override. Fixing the environment and re-running is up to you.

## Outcome to measure
Releases that shipped with an unrun check. The target is zero.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
