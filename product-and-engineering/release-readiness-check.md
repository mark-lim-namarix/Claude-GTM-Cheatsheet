---
name: release-readiness-check
description: Reads your release checklist and the evidence you paste, and marks it READY only if every item has proof. A missing check, a skipped test or an unapplied data change is NOT READY.
tools: Read
version: 0.1.0
---

# Release readiness check

## The problem
A release looks ready because the tests that ran were green. A check that did not run, or a data change that was never applied, looks the same until it breaks in production.

## When to use it
Right before you ship a change that users will see.

## Inputs
- Your checklist (default: tests run, data changes applied to production, rollback step known, one real-user path tried, secrets absent from the change).
- Evidence for each item: output, a log line, a screenshot description.

## Steps
1. Go through the checklist one item at a time.
2. For each, find the matching evidence. No evidence is MISSING.
3. A test that was skipped, a data change that was not applied, or a check that ran against the wrong target is NOT PROVEN.
4. Label each item PROVEN, MISSING or NOT PROVEN with one line of reason.
5. Mark the release READY only if every item is PROVEN. Otherwise NOT READY, listing every gap.

## The check that fires
One MISSING or NOT PROVEN item means NOT READY. Green on one environment does not prove another. Example (synthetic):

```
Tests run: PROVEN (output pasted, 120 passed, 0 skipped)
Data change applied to production: MISSING, no evidence
Rollback step known: PROVEN
One real-user path tried: NOT PROVEN (tried on the test copy, not production)
Secrets absent: PROVEN
Result: NOT READY, 2 gaps: production data change, real-user path
If all 5 items were PROVEN -> READY
```

## Approval route
The agent only reports. You close the gaps and decide when to ship. The release itself is always your step.

## Outcome to measure
Releases that needed a fix within a day. The target is to see it fall as the checklist stays fail-closed.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
