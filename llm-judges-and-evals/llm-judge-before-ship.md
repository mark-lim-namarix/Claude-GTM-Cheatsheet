---
name: llm-judge-before-ship
description: Scores any output (a message, a summary, a piece of code's description) against a written, weighted rubric and marks it REWRITE below the pass bar and HOLD after two failed rewrites. Proposes the rewrites; a human decides.
tools: Read
version: 0.1.0
---

# Judge before ship

## The problem
An output sounds fine, so it ships. Later you find it made a claim you cannot back or tried to do three things at once. You cannot unship it.

## When to use it
On any output that leaves your hands, right before you approve it.

## Inputs
- The output.
- Who it is for and the source behind its main claim.
- Your rubric. The default below works; edit the weights, keep them summing to 1.

## Steps
1. Score each criterion from 0 to 1 and write one sentence of evidence for each score.
2. Multiply by the weights and add them up.
3. Score 0.90 or higher: PASS, return the output with its score table.
4. Below 0.90: label REWRITE, name the lowest-scoring criterion, propose one rewrite, and score the rewrite.
5. After two proposed rewrites still below 0.90: HOLD the output for a human.

Default rubric (weights sum to 1.00):

| Criterion | Weight | 0 | 0.5 | 1 |
|---|---:|---|---|---|
| Main claim rests on a real, cited source | 0.30 | no source | source named, not checkable | source named and checkable |
| One clear purpose | 0.20 | three or more asks | two asks | one ask |
| Fits this reader's role and moment | 0.20 | wrong reader | partly fits | clearly fits |
| Plain, specific words | 0.15 | vague or jargon throughout | mixed | plain and specific |
| Every claim can be backed | 0.15 | claims with no support | some supported | all supported |

## The check that fires
Below 0.90 the output does not pass. Example (synthetic):

```
Output v1: a release note praising "our recent speed-up"; no source given; asks readers to try three new things.
Scores: source 0.2, purpose 0.3, fit 0.7, words 0.8, claims 0.5
Total: 0.06 + 0.06 + 0.14 + 0.12 + 0.075 = 0.455  -> BELOW 0.90, REWRITE 1
Output v2: 0.71 -> BELOW 0.90, REWRITE 2
Output v3: 0.86 -> still BELOW 0.90, HOLD for a human. Recommendation: do not ship until a human decides.
```

## Approval route
A passing output still goes to you. The score table sits next to it so you can see why it passed. A held output is yours to edit or drop.

## Outcome to measure
The real result you care about (replies, clicks, questions asked) for outputs that passed first try versus ones that needed rewrites. If the score does not predict the result, change the weights and measure again.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet. Draws on community work on grading AI output with written rubrics. Credit is not endorsement.
