---
name: defect-triage
description: Sorts a list of findings into three piles (fix now, needs your decision, needs your own action) plus UNVERIFIED and REJECTED. It never reports a bare defect without a next step.
tools: Read
version: 0.1.0
---

# Defect triage

## The problem
A report that says there is a problem and stops hands the work back to you. You asked for a result, not a list of what is broken.

## When to use it
After an audit, a failed check, or an agent's report listing problems.

## Inputs
- The list of findings.
- What you are able to do yourself, and what only you can decide (prices, legal calls, anything outward-facing).

## Steps
1. For each finding, ask: can it be fixed without a decision from you? If yes, put it in FIX NOW (proposed) and write the proposed fix in one line.
2. If it needs a real choice only you can make, put it in YOUR DECISION with the options and a recommendation.
3. If it needs a step only you can take, put it in YOUR ACTION and state the exact step.
4. Nothing may stay as a bare problem. A finding that has a check to run but cannot be reproduced yet is marked UNVERIFIED with what to check. A finding with no content and no next step is REJECTED and sent back to its author.
5. Order FIX NOW first, since those need nothing from you.

## The check that fires
A finding without a next step is rejected back to the author. A finding that cannot be reproduced is labelled UNVERIFIED, never stated as fact. Example (synthetic):

```
Finding 1: typo in the footer -> FIX NOW (proposed): correct to "Berlin"
Finding 2: should the offer name change? -> YOUR DECISION: keep (recommended) or rename
Finding 3: contract wording unclear -> YOUR ACTION: send it to your lawyer
Finding 4: "emails are slow" -> UNVERIFIED: time ten sends first
Finding 5: "something is wrong" -> REJECTED: no next step, sent back to the author
```

## Approval route
The agent sorts and proposes. The fixes are applied by whoever owns the work, and you answer only the decision pile.

## Outcome to measure
Share of findings in YOUR DECISION or YOUR ACTION. Watch this share; a shrinking share suggests more is fixed before it reaches you.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
