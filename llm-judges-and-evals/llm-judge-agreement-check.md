---
name: llm-judge-agreement-check
description: Compares the scores that three independent LLM judges gave the same items, finds where they disagree, and points to the likely reason, so you fix the unclear criterion or the odd judge's wording, not the pass line.
tools: Read
version: 0.1.0
---

# Three-judge check

## The problem
A cheap judge can sound confident and be wrong. If you only ever ask one, you do not learn it until it blocks good work or lets bad work through.

## When to use it
Before you rely on a judge, and whenever a judge fails items you think are good.

## Inputs
- About a dozen real items, mixed good, middling and bad.
- The same criteria and instructions, given to three different judges. Say which one is the cheap judge and which two are the stronger ones.
- A gap size that counts as a difference (default: 0.2 or more on a 0 to 1 score).
- The current pass line, so the agent can refuse any change to it.
- The score each judge gave each item (paste the table).

## Steps
1. For each criterion, compare the three scores per item.
2. Where two judges agree and one differs, mark the odd one out and look for the cause: unclear wording, missing context, a criterion every item scores the same on, or scores bunched in a small range so real differences are hidden.
3. Where the two stronger judges disagree with each other, the criterion itself is unclear. Say so and rewrite the criterion first.
4. Recommend changes only to the wording or structure of the criteria and the judge instructions. Do not change the pass line, the items or the weights.
5. Suggest a re-run on the same items after the change.

## The check that fires
A recommendation to move the pass line or the weights is rejected: the check only allows wording and structure changes. Example (synthetic):

```
Judges: A and B strong, C cheap. Gap that counts: 0.2 or more.
Item 4, "tone": A 0.9, B 0.85, C 0.4 -> C is the odd one out
Cause guess: judge C was not told the audience is technical -> add the audience to its instructions
Item 7, "accuracy": A 0.9, B 0.3, C 0.6 -> the two strong judges differ by 0.6: criterion unclear, rewrite it first
If someone proposes lowering the pass line from 0.9 to 0.6 -> REJECTED, wording or structure only
If someone proposes raising the accuracy weight from 0.3 to 0.5 -> REJECTED, wording or structure only
Recommendation: rewrite the accuracy criterion first; change judge C wording; pass line untouched; re-run the same 12 items
```

## Approval route
The agent compares and recommends. You decide which judge to change and when to re-run.

## Outcome to measure
How often the cheap judge matches the other two on a fresh set. Aim for it to track them closely before you let it run alone.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
