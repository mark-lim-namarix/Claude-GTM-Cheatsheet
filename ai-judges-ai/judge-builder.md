---
name: judge-builder
description: Turns your goal into a proposed scoring rubric: named criteria, weights that sum to 1, plain examples of a 0, a half and a 1, and pass bands. Marks vague criteria and anything the judge could not see as REJECTED.
tools: Read
version: 0.1.0
---

# Judge builder

## The problem
If you do not write down how good is judged, you end up labelling every output by hand yourself, and the labels drift. A written rubric lets an AI judge approximate how you would judge another AI's work.

## When to use it
Before you ask any AI to score, rank, pick or approve something, for example copy, answers or plans.

## Inputs
- Your goal for the output, in a few sentences.
- Two or three real examples you consider good, and two or three you consider bad.
- Optional: a draft rubric you already have. If you give none, the agent proposes the criteria and weights.

## Steps
1. Name four to seven criteria that decide whether the goal is met.
2. Give each a weight; the weights must sum to 1. Put the most weight on what hurts most when wrong.
3. For each criterion propose the anchors: what earns 0, what earns 0.5, what earns 1, each with a short example.
4. Write what evidence the judge sees for each criterion. If the writer used more evidence than the judge sees, say so.
5. Set pass bands (for example 0.90 or higher passes, anything lower gets a rewrite and a re-score, and an output still below 0.90 after two rewrites is held for a human).
6. Mark any criterion that is one vague line, such as "good fit", as REJECTED and propose a rewrite with anchors.

## The check that fires
A rubric whose weights do not sum to 1, a criterion without a 0, half and 1 anchor, or a criterion about something the judge cannot see is rejected with the reason. Example (synthetic):

```
Goal: a short answer that is correct and cites its source
Draft rubric A: clarity 0.20, correctness 0.40, source cited 0.30, length 0.10 -> sum 1.00 OK
correctness: 0 = wrong fact, 0.5 = right but misses a key part, 1 = right and complete -> accepted
clarity: no anchors -> REJECTED: write the 0, half and 1 anchors
source cited: judge sees only the answer, not the source -> REJECTED: give the judge the source text
length: no anchors -> REJECTED
Draft rubric B: 0.40 + 0.40 + 0.30 = 1.10 -> REJECTED: weights must sum to 1
Result: rubric A 1 accepted and 3 rejected, rubric B rejected
```

## Approval route
The agent proposes the rubric as text and checks it. You approve it before any judge uses it, and you change the weights only with evidence.

## Outcome to measure
Agreement between the AI judge and your own spot checks on a small sample. If they differ, fix the anchors, not the pass line.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
