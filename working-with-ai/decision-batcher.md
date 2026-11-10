---
name: decision-batcher
description: Collects every open question from a piece of work, drops the ones that have a safe default or are really defects, and asks the rest in one batch with a recommended option each.
tools: Read
version: 0.1.0
---

# Decision batcher

## The problem
Questions scattered through a task make you the switchboard. You answer one, wait, answer another, and the work stalls between them.

## When to use it
At the end of a piece of work, when several questions have built up.

## Inputs
- The raw list of open questions from the work.
- What has already been decided, so nothing is asked twice.

## Steps
1. Remove any question already answered earlier.
2. Move any defect disguised as a question to a fix list. A defect is fixed by its owner, not asked about.
3. For each remaining question, check for a safe default. If there is one, list the default you propose to apply and note it.
4. Keep only real decisions: price, legal, outward-facing action, an ambiguous requirement with no safe default.
5. Write one batch. Each question gets two or three options, the trade-off of each, and a recommended first option.

## The check that fires
A question that has a safe default, repeats an earlier answer or is really a defect is removed. A question with no recommended option is sent back to be completed. Example (synthetic):

```
Raw: 9 questions
Already answered: 2 -> removed
Defects in disguise: 3 -> moved to a fix list, not asked
Safe default: 2 -> proposed default listed, not asked
No recommendation: 1 -> sent back, not asked
Asked: 1 real decision
  Q: Keep the offer name? A) Keep (recommended): no rework, no confusion. B) Rename: fresher, costs a week of changes.
```

## Approval route
You answer the batch once. You or the work's owner apply your answers; the agent only writes the batch and never decides the real questions for you.

## Outcome to measure
Questions per finished task and the share you accept as recommended. Fewer questions and a stable accept rate may suggest the defaults are good.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
