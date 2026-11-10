---
name: code-review-brief
description: Builds the brief for an independent code review: only the change and your criteria, never the reasoning of whoever made it. Marks the brief NOT READY if it has no criteria, and strips any sentence that defends the change, marking it LEAK REMOVED.
tools: Read
version: 0.1.0
---

# Code review brief

## The problem
A reviewer who reads the author's explanation first tends to agree with it. The most useful review sees only what a stranger would see.

## When to use it
Before you ask an agent or a person to review a change.

## Inputs
- The change itself (the diff or the changed files).
- Your criteria: what must be true and what must never happen.
- The author's description of the change (so the agent can strip it out).

## Steps
1. Take the diff and remove any explanation of why the change was made.
2. List the criteria as numbered questions, for example "does it handle an empty list", "does it expose any secret".
3. State the output you want: PASS or FAIL per criterion with the quoted line, and a final verdict.
4. State that the reviewer reports only and does not fix.
5. Check the brief for leaks: any sentence that argues the change is correct. Remove it and mark it LEAK REMOVED.
6. Label the brief READY, or NOT READY if there are no criteria.

## The check that fires
A brief with no criteria is NOT READY. A sentence in it that defends the change is marked LEAK REMOVED before the brief is READY. Example (synthetic):

```
Change: 40-line diff adding a retry loop
Author note: "This is safe because retries are capped" -> LEAK REMOVED
Criteria: 1 retries are capped, 2 no secret is logged, 3 failure after the cap is reported
Output asked: PASS or FAIL per criterion with the quoted line, then a verdict; report only
Result: READY
Another brief: Criteria: none given -> NOT READY, no criteria
```

## Approval route
The agent only drafts the brief as text. You send it to a fresh reviewer, and you read the verdict.

## Outcome to measure
Defects found after merge in changes that were reviewed with a clean brief. Compare with changes reviewed with the author's notes.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
