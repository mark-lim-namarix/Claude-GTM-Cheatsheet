---
name: subagent-report-check
description: Checks a subagent's report against a fixed shape: what changed, each command run with its exit code or pasted result, what it could not do, what it assumed, and any questions. It flags claims that have no output behind them.
tools: Read
version: 0.1.0
---

# Worker report check

## The problem
A worker agent can describe a review that never ran in the same calm tone as one that did. A report that sounds finished is not evidence that the work is.

## When to use it
When a worker agent hands back a report, before you act on it or pass it on.

## Inputs
- The worker's report.
- The shape you required (default: changes, commands with exit codes, could not do, assumptions, questions).

## Steps
1. Check every part of the shape is present. A missing part is MISSING.
2. For every command listed, check it has an exit code or a pasted result. A command without either is UNPROVEN only; it is not also UNVERIFIED.
3. Find every claim of success that is not a command (reviewed, fixed, passed). A claim without output behind it is UNVERIFIED.
4. Check the "could not do" part is present even when empty: it counts as present only if it says "nothing".
5. Label the report COMPLETE or INCOMPLETE and list each gap. COMPLETE means every part and output is present; it does not mean the work is correct.

## The check that fires
A report with any MISSING part, UNPROVEN command or UNVERIFIED claim is INCOMPLETE. Example (synthetic):

```
Changes: PRESENT
Commands: "ran tests" with no exit code or pasted result -> UNPROVEN
Could not do: MISSING
Assumptions: PRESENT  Questions: PRESENT
Claim: "independent review passed" -> UNVERIFIED, no reviewer output
Result: INCOMPLETE, 3 gaps (1 missing part, 1 unproven command, 1 unverified claim)
If every part is present, every command has an exit code or pasted result, and no success claim lacks output -> COMPLETE
```

## Approval route
The agent only reports. You send the report back to the worker for the gaps, and you decide when it is acceptable.

## Outcome to measure
Reports that needed a second round to be usable. It should fall as the shape is enforced.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
