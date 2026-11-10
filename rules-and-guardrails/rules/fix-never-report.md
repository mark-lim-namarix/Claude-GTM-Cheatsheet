# Rule: fix it, never just report it

Paste this into your `CLAUDE.md` (project or `~/.claude/CLAUDE.md`).

```
When you find something wrong, fix it, check the fix, and hand back a result that is verified.
Do not stop at "there is an error". A bare problem report leaves me nothing to act on.

Only three things come back to me:
1. A real decision only I can make (price, legal, a business choice, a requirement with no safe default). Ask it once, with your recommended option first.
2. A step only I can take (a production release, a payment, an outside account). Say it is ready and give the exact step.
3. Anything destructive or hard to undo (deleting files, rewriting history, changing live data). Ask first, every time.

If a fix is blocked after honest tries, say what is blocked and why, and finish everything that can be finished first.
```

Why it exists: an audit finds many problems, and the reflex is to ask you how far to fix them. The answer is usually "all the way", so asking only adds a round trip.

How to check it works: after any audit, count the findings you were told about versus the findings that were already fixed. Told-about should only be decisions and steps only you can take.
