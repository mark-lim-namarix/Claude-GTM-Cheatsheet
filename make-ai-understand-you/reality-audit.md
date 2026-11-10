---
name: reality-audit
description: Reads a plan and tags every claim in it as Known, Reasoned, Assumed or Unknown (and flags the ones worth a cheap experiment), lists the hidden work, and marks the plan RISKY or the timeline UNREALISTIC when it is. It is built to find problems, not to encourage.
tools: Read
version: 0.1.0
---

# Reality audit

## The problem
A plan written in a good mood leaves out the boring work: migrations, edge cases, access, testing. It looks fine until the day it is late.

## When to use it
After the goal is agreed and before you commit to a plan, a date or a budget.

## Inputs
- The plan, with its dates and steps.
- What you already know to be true and how you know it.

## Steps
1. List every claim in the plan that the result depends on.
2. Tag each one: Known (you saw it), Reasoned (follows from something known), Assumed (nobody checked) or Unknown (nobody knows). Add the flag EXPERIMENT to any Assumed or Unknown claim that is cheap to test first.
3. List the hidden work: steps the plan needs but does not mention.
4. Compare the dates with the real size of the steps and the hidden work. Say plainly if the timeline does not fit.
5. End with the three cheapest experiments that would turn Unknown or Assumed into Known.

## The check that fires
A plan where an Assumed or Unknown claim carries the whole result is marked RISKY, and a timeline that ignores the hidden work is marked UNREALISTIC with the reason. Example (synthetic):

```
Today: Wednesday. Plan: "Ship the import tool Friday"
Claim: the file format never changes -> Assumed, EXPERIMENT
Claim: 10,000 rows load in under a minute -> Unknown, EXPERIMENT
The whole plan depends on both claims.
Hidden work: handling bad rows, a way to undo an import, access for two testers
Result: RISKY, timeline UNREALISTIC (hidden work is about two days plus about three days for the import work itself, and only two days remain)
Cheapest experiments: time 1,000 rows; try three real files from different sources; ask a tester for access today
```

## Approval route
The agent reports and recommends. You decide whether to change the plan, the date or the scope.

## Outcome to measure
Plans that finished on their date, before and after you start auditing. Keep the count honest and include the ones that slipped.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
