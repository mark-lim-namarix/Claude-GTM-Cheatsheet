---
name: claude-md-rules-check
description: Reads your CLAUDE.md or rules files and flags rules that conflict, repeat, cannot be checked, or point to things that no longer exist. It reports only and changes nothing.
tools: Read
version: 0.1.0
---

# Rules file check

## The problem
Rules files grow by adding. After a few months they contradict each other, repeat each other, and mention folders and tools that are gone, and the AI may follow either one.

## When to use it
Once a month, and whenever the AI starts ignoring a rule you wrote.

## Inputs
- Your rules file or files (paste them).
- Optional: a list of the folders and tools that exist today.

## Steps
1. Split the rules into single statements and number them.
2. Find pairs that conflict (one says always, another says never). Label CONFLICT with both numbers.
3. Find statements that repeat another. Label DUPLICATE.
4. Find statements that cannot be checked ("be careful"). Label VAGUE and suggest an observable version.
5. If you gave the list of what exists, find rules naming something not on it. Label STALE.
6. Give a rule only its first applicable label, in this order: CONFLICT, DUPLICATE, STALE, VAGUE. Report the counts and the shortest fix for each. The user edits the file.

## The check that fires
A file with any CONFLICT is not clean: the AI may obey one rule and break the other. Example (synthetic):

```
Rule 4: "Always commit after each change"  Rule 9: "Never commit without asking" -> CONFLICT (4, 9): fix: keep one, say which
Rule 12 repeats Rule 3 -> DUPLICATE: fix: delete Rule 12
Rule 7: "Be careful with the database" -> VAGUE: suggest "never run a schema change without my yes"
Rule 15 names a folder not in your list -> STALE: fix: delete the rule or update the folder name
Result: 1 conflict, 1 duplicate, 1 vague, 1 stale
```

## Approval route
The agent only reports. You edit the rules file and decide which of two conflicting rules wins.

## Outcome to measure
Times the AI broke a written rule. Count them for a month before and after a clean-up.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
