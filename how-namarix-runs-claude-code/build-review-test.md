---
name: build-review-test
description: Use when an AI coding agent builds or changes non-trivial code and must deliver reviewed, tested, and verified work rather than an unresolved defect report.
tools: Read
version: 0.1.0
---

# AI build, review and test loop

## When to use it
- When building or modifying a non-trivial feature, script, or refactor.
- When a change needs unit, integration, end-to-end, or runtime validation.
- When review or QA reports a defect that must be resolved before handoff.
- When a test layer may have been skipped, missing, or unverified.

## Steps
1. Define the change and add or extend tests in the existing framework at every applicable level, in the same change.
   - Why: Every build must have tests, and the test depth must match the behavior and blast radius being changed.
   - Check: Confirm that each changed behavior has a corresponding test at the applicable unit, integration or end-to-end level.
2. Send only the change and review criteria to fresh, independent review and QA agents. Have them report findings and test results without changing the code.
   - Why: Independence preserves the value of review, while keeping fixes with the parent agent prevents a report from being mistaken for completed work.
   - Check: Confirm that the reviewers received the change and criteria rather than the producing conversation, and that their outputs contain findings or results rather than untracked fixes.
3. Run every applicable test layer, including live-preview checks for runtime changes, and treat anything that did not execute as not-green.
   - Why: A successful exit signal does not prove that a suite ran, and an unverified layer can allow an untested change to proceed.
   - Check: For each applicable layer, record execution evidence, passing and failing results, and any skipped, missing or unverified status. The run is not green if any such status exists.
4. Read the review and QA results, fix all findings and failures, then repeat review, QA and applicable tests until the gates are green.
   - Why: The loop is closed only by fixing defects and checking the fixes; stopping at the first failure or returning a defect report leaves the work unfinished.
   - Check: After each fix, verify that fresh review and QA were run again and that every applicable test layer is green.
5. Hand the change to a person to approve and ship only when review, QA and all applicable gates are green. If the work remains blocked after honest iteration, escalate the specific blocker with the buildable remainder completed and green.
   - Why: A red or known-defective result is not a valid handoff, while a specific blocker gives the decision-maker something actionable.
   - Check: Confirm both review and QA are passing, no applicable layer is skipped or unverified, and any escalation names the remaining blocker rather than merely stating that something is broken.

## Outcome
The change is handed off only after independent review, applicable tests and required runtime checks are green. A skipped or unverified layer is not treated as a pass, and a blocked result is escalated with its specific blocker.

## Example (made up)
Team Alpha changes a feature with both pure logic and runtime behavior. It adds matching unit and runtime assertions, runs fresh review and QA, and finds one defect. The parent session fixes it, reruns both reports and every applicable test layer, and checks that no layer was skipped. Because all checks are verified green, Team Alpha hands the change to a person to approve rather than forwarding the defect report.

## Pitfalls
- Treating a skipped, missing, unregistered or empty test layer as passing because another command returned success.
- Calling a change green when a test was skipped, did not run, asserted nothing, lacked a dependency or credential, or was not registered in a gate.
- Passing a red result or a defect report to the next person instead of fixing it and rerunning the applicable gates.
- Reporting a general all-clear when a layer did not execute or when a runtime change was not checked on a live preview.

## Measured result
No number is published for this practice yet.

## Credits
Mark Lim, Founder at Namarix and Cheatsheet, from how Namarix runs its own AI work.
