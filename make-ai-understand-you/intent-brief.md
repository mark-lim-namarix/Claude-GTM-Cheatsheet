---
name: intent-brief
description: Turns a vague request into a short brief (goal, why, limits, what done looks like, what never to do) and states the intent it infers in one line, then asks only for what is missing.
tools: Read
version: 0.1.0
---

# Intent brief

## The problem
AI does exactly what you typed, not what you meant. A vague request gets a confident, wrong result, and you find out after the work is done.

## When to use it
Before you hand any non-trivial task to an AI, including a coding agent.

## Inputs
- Your request in your own words, however rough.
- Anything the AI cannot see: who it is for, what already exists, what you tried.

## Steps
1. State the intent you infer in one line: the goal behind the request, not the request itself. Ask the user to correct it.
2. Fill five fields from what you gave: goal, why it matters, limits (time, tools, things not to touch), what done looks like (a check you can run), what must never happen.
3. Mark each field FILLED, GUESSED or MISSING. A GUESSED field shows the guess.
4. List the MISSING fields as questions, most important first, at most five.
5. Output the brief ready to paste as the first message of the task.

## The check that fires
A brief is NOT READY if any field is MISSING. A missing "what done looks like" is named first, because nobody can tell when the work is finished. Example (synthetic):

```
Request: "make the signup faster"
Intent: users should finish signup without giving up
Goal: FILLED  Why: GUESSED (fewer drop-offs)  Limits: MISSING  Done: MISSING  Never: MISSING
Result: NOT READY (any MISSING field) -> 3 questions, one per missing field, "done" first:
  Done: what does faster mean (seconds or steps) and how will we measure it?
  Limits: how long do we have and which tools may we use?
  Never: what must not change?
```

## Approval route
The agent only drafts the brief and the questions as text for you. You answer, and you decide when it is ready to send.

## Outcome to measure
Tasks that need a redo because the AI misunderstood. Count them per week before and after you start using briefs.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
