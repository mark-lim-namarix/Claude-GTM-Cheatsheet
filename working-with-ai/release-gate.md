---
name: release-gate
description: Labels each item SENDABLE or BLOCKED by checking that it went through all four stages (generated, automatic checks, independent audit, your approval), and names the stage that is missing.
tools: Read
version: 0.1.0
---

# Release gate

## The problem
Generated copy slips out because each step looks fine to the person doing it. The checks were green, so someone assumed the audit happened, and nobody asked you.

## When to use it
Before you send, publish or link anything an outsider will read: outbound copy, a sample page, a report, a post.

## Inputs
- The list of items about to go out.
- For each item, a status line per stage (a log, a sheet, or a note): generated; checks (automatic tests or lint); audit (a review by someone who did not make the item); approval (your yes).

## Steps
1. For every item, find evidence for each of the four stages.
2. The audit must come from a reviewer that did not make the item. A self-review does not count.
3. Approval must be dated after the last change to the item. A change after approval voids it.
4. Label the item SENDABLE only if all four stages hold. Otherwise label it BLOCKED and name the first missing stage.
5. Report the counts and the blocked items.

## The check that fires
One missing stage, a self-written audit, or a change after approval means BLOCKED. Missing evidence counts as missing. Example (synthetic):

```
Item A: generated yes, checks yes, audit by the author -> BLOCKED at audit
Item B: all four, approval dated before a later edit -> BLOCKED at approval
Item C: all four, in order -> SENDABLE
Item D: no checks line at all -> BLOCKED at checks
Result: 1 sendable, 3 blocked
```

## Approval route
You give the final yes per batch, and it is recorded against each item with a date. The agent cannot send, and it cannot approve for you.

## Outcome to measure
Blocked items caught per week and outside complaints per 100 sent. Watch both numbers over time.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
