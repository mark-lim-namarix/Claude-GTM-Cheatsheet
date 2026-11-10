---
name: judge-before-send
description: Scores a draft message against a written, weighted rubric and blocks it unless it clears the pass bar. Rewrites at most twice, then holds the draft for a human.
tools: Read
version: 0.1.0
---

# Judge before send

## The problem
A draft sounds fine, so it gets sent. Later you find it made a claim you cannot back or asked for three things at once. You cannot unsend it.

## When to use it
On every outbound draft, right before you approve it. Skip it for replies inside an existing conversation.

## Inputs
- The draft.
- Who it is for (role, company) and the source behind the first line.
- Your rubric. The default below works; edit the weights, keep them summing to 1.

## Steps
1. Score each criterion from 0 to 1 and write one sentence of evidence for each score.
2. Multiply by the weights and add them up.
3. Score 0.90 or higher: pass, return the draft with its score table.
4. Below 0.90: name the lowest-scoring criterion, rewrite once, and score again.
5. After two rewrites still below 0.90: stop and hold the draft for a human.

Default rubric (weights sum to 1.00):

| Criterion | Weight |
|---|---:|
| First line rests on a real, cited source | 0.30 |
| One clear ask | 0.20 |
| Fits this reader's role and moment | 0.20 |
| Plain, specific words | 0.15 |
| Every claim can be backed | 0.15 |

## The check that fires
Below 0.90 the draft does not pass. Example (synthetic):

```
Draft v1: opener praises "your recent keynote"; no source given; asks for a call, a demo and an intro.
Scores: source 0.2, ask 0.3, fit 0.7, words 0.8, claims 0.5
Total: 0.06 + 0.06 + 0.14 + 0.12 + 0.075 = 0.455  -> BELOW 0.90, rewrite 1
Draft v3 after two rewrites: 0.86 -> HOLD for a human. Not sent.
```

## Approval route
A passing draft still goes to you. The score table sits next to it so you can see why it passed. A held draft is yours to edit or drop.

## Outcome to measure
Positive replies per 100 sends for drafts that passed on the first try versus drafts that needed rewrites. If the score does not predict replies, change the weights and measure again.

## Credits
Draws on community work on grading AI output with written rubrics, and on open outreach skill collections: Marketing Skills, Cold Outbound Skills. Credit is not endorsement.
