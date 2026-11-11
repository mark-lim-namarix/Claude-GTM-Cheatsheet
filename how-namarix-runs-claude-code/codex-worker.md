---
name: codex-worker
description: Use when an AI coding agent needs to create or edit repository files and you want Codex to perform generation while Claude Code retains review, orchestration and landing responsibility.
tools: Read
version: 0.1.0
---

# running Codex as a worker under Claude Code

## When to use it
- A prompt will write or edit code, documentation, configuration or backlog content in a repository Codex can reach.
- Codex availability needs to be checked before dispatching work.
- A Codex-generated change needs review, retry handling and safe landing.
- A Codex task has failed repeatedly and needs a clear takeover point.

## Steps
1. Classify the request before dispatching it. Route file-writing work that Codex can reach to the worker path, while keeping questions, business-routing decisions and the governance files that constrain the worker with Claude.
   - Why: The worker is for file generation and editing, not peer judgment or governance of its own operating rules.
   - Check: Confirm the request produces a repository diff and is not a question, routing decision or change to the worker's governing files.
2. Check Codex availability before every eligible dispatch, without using a size exception. If it is available, send the work to Codex. If it is unavailable, use Claude's normal build path; if both sides lack headroom, surface the blocked state for a decision instead of silently proceeding.
   - Why: The routing rule uses both capacity windows and prevents work from waiting on an unavailable worker.
   - Check: Record a route decision of Codex, Claude fallback or blocked, with the availability result supporting that decision.
3. Prepare a context-complete brief with a goal, acceptance criteria, settled decisions, out-of-scope items, owner intent, definitions, relevant source content, data details, prior learning, traps and representative good and bad examples.
   - Why: Codex only knows what the brief carries, and incomplete context can make the worker misunderstand the intended criteria or decisions.
   - Check: Have another operator confirm that a stranger could perform the task from the brief alone and that every settled decision appears in the reviewer-visible sections.
4. Split a clearly oversized change into smaller slices, then dispatch each slice through one background call that stays attached until the task ends, so the session is told when it finishes. Do not invoke the worker directly, add a separate waiter, or background the dispatch twice.
   - Why: The wrapper's blocking behavior makes completion observable to the session; extra backgrounding or a separate watcher can lose the wake and leave the task unnoticed.
   - Check: Confirm the dispatch is one background call, remains attached to the task until completion, and produces a completion notification or an explicit failure.
5. Handle the result fail-closed. Read the review first on failure, continue the same worker task for a fix round, treat notes as completed unless they matter enough to fix, and stop after three failed rounds by taking over in Claude's worktree.
   - Why: The worker has a bounded retry path, and a fixed takeover point prevents endless retries while preserving review findings.
   - Check: Count every failed round without resetting the count through renaming or re-slicing, verify the review and gate status, and confirm that a third failure causes Claude to complete the remaining work directly.
6. Land only after the final review and required gates pass. If Claude changes the result after a worker round, run the equivalent final review and scans before proposing the change for integration.
   - Why: The worker's report is not evidence of review, and hand-edited or combined results still need the same final checks.
   - Check: Verify a passing final review at the proposed tip and clean required scans before proposing the pull request, and a person approves it before it merges.

## Outcome
Codex handles eligible file-writing work when available, while Claude retains judgment, review and landing. Unavailable Codex work falls back to Claude, work is reported as blocked for a decision only when neither has capacity, and repeated failures trigger direct completion by Claude.

## Example (made up)
Made-up example: Team Alpha needs a small configuration change and a documentation edit. The operator confirms both are file-writing tasks, checks availability, and routes them to Codex. The brief includes the goal, acceptance criteria, settled decisions, context and examples. Codex fails the first review, fixes the same task in a continuation round, then passes. Claude reviews the final tip and proposes it, and a person approves the merge. If the third round failed, Claude would take over instead.

## Pitfalls
- Dispatching the worker without a wake, or adding extra backgrounding or a separate waiter, can leave a finished or failed task unnoticed.
- Sending an incomplete brief can cause the worker or reviewer to miss settled decisions, definitions and acceptance context.
- Re-dispatching a completed pass only to address notes can turn a successful review into a failure.
- Continuing after the third failed round, or resetting the count by renaming or re-slicing, defeats the takeover rule.
- Treating the worker's own report as proof of independent review can allow an unreviewed change to appear complete.

## Measured result
No number is published for this practice yet.

## Credits
Mark Lim, Founder at Namarix and Cheatsheet, from how Namarix runs its own AI work.
