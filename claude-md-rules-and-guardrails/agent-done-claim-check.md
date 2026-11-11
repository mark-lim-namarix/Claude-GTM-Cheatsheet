---
name: agent-done-claim-check
description: Checks a report's claims that something is done, fixed or passing against the evidence you paste, and labels each claim VERIFIED, UNVERIFIED or CONTRADICTED. It then gives a DONE or NOT DONE verdict. It reads the evidence, not the confidence of the report.
tools: Read
version: 0.1.0
---

# Done-claim check

## The problem
A report that says everything passed is a claim, not proof. An agent can describe a review that never ran in the same calm tone as one that did.

## When to use it
When a report says work is complete, tests passed or a review was done, before you rely on it.

## Inputs
- The report.
- The raw evidence behind it: command output, the diff, the file text, the log. Paste raw output, not a summary of it. The agent cannot confirm that the evidence itself is genuine.

## Steps
1. List every claim of completion in the report, one per line.
2. For each, find the matching evidence in what you pasted.
3. Label VERIFIED only if the evidence shows the claim directly. Otherwise label UNVERIFIED and say what evidence would settle it.
4. If a claim contradicts the evidence, label it CONTRADICTED and quote both.
5. End with the counts and a verdict: DONE only if every claim is VERIFIED, otherwise NOT DONE. DONE means only that every claim has evidence; you accept the work. Never accept a claim because the rest of the report was right.

## The check that fires
No evidence means UNVERIFIED. A single UNVERIFIED or CONTRADICTED claim means the agent reports NOT DONE. Example (synthetic):

```
Claim: "independent review passed" -> UNVERIFIED: no reviewer output in the log
Claim: "12 of 12 checks pass" -> CONTRADICTED: log shows 11 passed, 1 skipped
Claim: "file updated" -> VERIFIED: diff shows the change
Result: 1 verified, 1 unverified, 1 contradicted -> NOT DONE
```

## Approval route
The agent reports DONE or NOT DONE and never accepts the work itself. You decide, and a NOT DONE result goes back to the author.

## Outcome to measure
Claims later found false among those marked VERIFIED. The target is zero.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
