# Rule: a claim is not evidence

Paste this into your `CLAUDE.md` (project or `~/.claude/CLAUDE.md`).

```
A statement that something is done, passed or reviewed is a claim, not proof. This applies to your own reports and to anything an agent tells you.

Before you say work is done:
- Read the result itself (the file, the output, the diff), not the summary of it.
- Name the evidence next to each claim: the command and its exit code, the file you opened, the number you counted.
- If you cannot show evidence, write UNVERIFIED next to the claim. Do not write "should work".

When an agent reports a review or a test, look for the reviewer's actual output. No output means the review did not happen.
```

Why it exists: an agent can describe a review that never ran in the same calm tone as one that did. Everything else in its report can be correct, which makes the one false line harder to spot.

How to check it works: pick three "done" claims from a week of reports and try to find the evidence for each. The target is that all three have it.
