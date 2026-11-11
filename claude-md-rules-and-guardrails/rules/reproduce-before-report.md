# Rule: reproduce before you report

Paste this into your `CLAUDE.md` (project or `~/.claude/CLAUDE.md`).

```
A finding from an agent, an audit or a tool is not repeated to me as a fact until you have reproduced it against the real code or the real data.

- Open the real file, run the real query, load the real page.
- If it reproduces, report it with the evidence.
- If you cannot reproduce it in this turn, call it UNVERIFIED and say what check would settle it.
- Never put an unreproduced finding into a question for me.
```

Why it exists (synthetic example): an audit reports "20 pages have no images". The images exist under a different field name, so the finding was wrong in kind. A wrong finding in a decision makes you the quality check.

How to check it works: take the last five findings you were handed and see how many were reproduced before you saw them.
