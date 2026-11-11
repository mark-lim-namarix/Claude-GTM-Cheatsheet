---
name: eval-test-set-maker
description: Reads your real records and outcomes and proposes an eval test set whose labels come from recorded outcomes, and leaves out any label that came from the model being tested. Adds a few made-up bad cases that clearly break your goal.
tools: Read
version: 0.1.0
---

# Test set maker

## The problem
Hand-labelling a test set is slow, so people let a model label it. Then the model is graded against its own opinion, and a high score only proves it agrees with itself.

## When to use it
Before you test a prompt, a judge or an agent, when you have no labelled examples yet.

## Inputs
- A sample of real records that include an outcome (replied or not, accepted or rejected, fixed or reopened).
- Any labels that already exist on those records, and what produced each one (a person, a measured outcome, or a model).
- Your goal for the output, in a sentence.
- How many items you want (a target; the report says whether the real count meets it).

## Steps
1. For each record, take the label from the outcome that really happened. If a record has no outcome, leave it out.
2. Leave out any item whose label came from the model under test, and mark it REMOVED.
3. Count the outcomes among the real items (not the AUTHORED ones). If one outcome is more than two thirds of them, mark the set LOPSIDED; do not invent or drop real items to hide it.
4. Add three to five made-up bad cases that clearly break the goal, and mark them AUTHORED. They are the only items without a real outcome.
5. Write one line per item saying where its label came from.
6. Report the counts per label, how many items were AUTHORED, and whether the real count meets your target.

## The check that fires
A label with no real outcome behind it (except AUTHORED items), or a label that came from the model under test, is removed. A set where one outcome is more than two thirds is marked LOPSIDED. Example (synthetic):

```
Records: 30. Outcomes known: 25 (5 left out, no outcome)
Item 9: label "replied" came from the model under test -> REMOVED, not a real outcome (24 left)
Labels: replied 3, not replied 21 -> 21 of 24 is 88 percent one outcome -> LOPSIDED, collect more replies
AUTHORED bad cases: 4 (each breaks the goal on purpose, no real outcome)
Target 40, real items 24 -> target not met
Result: 24 real items plus 4 AUTHORED, LOPSIDED
```

## Approval route
The agent proposes the set as text. You check a few labels against the records, and you decide when the set is good enough to test with.

## Outcome to measure
The share of items whose label you would still agree with after a spot check of ten. It should stay high, otherwise the outcomes are a poor guide.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
