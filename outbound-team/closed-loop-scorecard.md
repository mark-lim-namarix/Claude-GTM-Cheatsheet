---
name: closed-loop-scorecard
description: Compares outbound results for a change against a control group that did not get it, and says which change helped, or that there is not enough data to say.
tools: Read
version: 0.1.0
---

# Closed-loop scorecard

## The problem
You change the opener and replies go up, so you keep it. But maybe the best leads just happened to get the new one. You keep a change that did nothing, or drop one that worked.

## When to use it
Whenever you test a new opener, offer, channel or list, and again once a week for the running results.

## Inputs
- The list of contacts, which version each one got, and the outcome (reply, positive reply, meeting).
- The outcome you decided to measure before the test started.

## Steps
1. Before sending, you set aside a small group (for example 10 percent) that keeps the old version. This group is the control: it shows what would have happened anyway.
2. You assign contacts to the groups at random, not by quality. The agent checks your assignment for obvious bias (for example, all top leads in one group).
3. After the test window, you give the agent the results. It counts the outcome in each group.
4. Report both rates, the difference, and the group sizes.
5. Say help, no clear difference, or not enough data. Keep every failed or empty case in the counts.

## The check that fires
No control group or too few contacts means no verdict. Example (synthetic):

```
Test: new opener, 40 contacts, no control group
Result: NO VERDICT, no control group; 40 contacts is below 30 per group
Next step: rerun with a 10 percent control and at least 30 in each group
```

## Approval route
The agent only reports. You decide whether to keep, drop or retest the change.

## Outcome to measure
The share of changes you kept that still help on a second test. That is the number that shows the loop works.

## Credits
Draws on the practice of measuring against a control group, and on open outreach skill collections: Cold Outbound Skills, Marketing Skills. Credit is not endorsement.
