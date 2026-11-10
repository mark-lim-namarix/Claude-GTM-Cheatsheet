---
name: worker-brief-builder
description: Drafts a brief for another AI agent covering eight parts and marks any gap: your intent in your own words, what each term means and does not mean, the rules to follow, where the data is, what was already found, good and bad examples, how done is checked, and what is out of scope.
tools: Read
version: 0.1.0
---

# Worker brief builder

## The problem
A worker agent that gets a short instruction guesses the rest. It does a different job, asks you things you already answered, or finishes something you never wanted.

## When to use it
Every time you hand work to another agent, including a coding agent running in the background.

## Inputs
- Your request in your own words.
- Any rules, definitions, files or earlier findings that apply.
- A real example of a good result and a bad one, if you have them.
- How done will be checked, and what is out of scope.
- What was already found or tried, or a statement from you that nothing was found yet.

## Steps
1. Put your intent first, quoted exactly as you said it.
2. Define each key term, including what it does not mean. Use only definitions the user gave; if none, mark Definitions MISSING.
3. Quote the rules that apply, word for word, not summarised.
4. List where the data and files are.
5. List what was already found or tried. "Nothing found yet" is PRESENT if you stated it.
6. Add the good and bad example you were given. If none, mark Examples MISSING; do not invent one.
7. State how done is checked (a test or a result you can look at) and what is out of scope, using only what you were given. If not given, mark it MISSING; do not invent it.
8. Mark each of the eight parts PRESENT or MISSING. Any MISSING part makes the brief NOT READY.

## The check that fires
A brief with any MISSING part is NOT READY: do not hand it on until the missing parts are filled. A summarised rule where a quoted one is available counts as MISSING. Example (synthetic):

```
Intent: PRESENT (quoted)
Definitions: PRESENT ("active user" = logged in within 30 days, not signed up)
Rules: MISSING (a summarised rule where a quoted one exists counts as MISSING)
Data: PRESENT  Findings: PRESENT  Examples: MISSING  Done check: PRESENT  Out of scope: PRESENT
Result: NOT READY, 2 parts missing: rules, examples
If all eight parts are PRESENT -> READY to hand over
```

## Approval route
The agent only drafts the brief as text. You complete the missing parts and decide when to hand it over.

## Outcome to measure
Questions a worker asks that were already answered, and redo rounds per task.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
