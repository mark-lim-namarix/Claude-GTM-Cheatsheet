---
name: session-roles
description: Use when multiple AI coding sessions share work and need clear ownership, decision routing, peer coordination, and reliable completion reporting.
tools: Read
version: 0.1.0
---

# planner and builder AI sessions

## When to use it
- When a planner needs to coordinate multiple building sessions.
- When two sessions may overlap or affect each other's work.
- When a building session needs an owner decision about its own work.
- When a session finishes and needs to report whether it can be deleted.

## Steps
1. At startup and before the first edit, identify live peers and their work. If work overlaps or duplicates another session, message the peer and agree who owns which part before continuing. For a conflict or shared-state error, talk to the session that owns the work and settle it together instead of editing its work.
   - Why: Knowing peers early prevents duplicate work and lets overlapping sessions coordinate before either changes the shared work.
   - Check: Confirm that the peer roster was reviewed and that any overlap has a recorded agreement about ownership before the first edit.
2. At the moment all work is finished, verify the work, complete required handoffs, and report completion without waiting to be asked. State that deletion is available only when verification and delivery are complete, no background activity or pending owner decision remains, and all relevant peers or planners have received the result.
   - Why: A completion report is reliable only when unfinished checks, decisions, background activity, and handoffs are excluded.
   - Check: Confirm the work is verified and delivered, no process or watcher remains for that work, no decision is pending, and every relevant planner or peer has received the result before reporting deletion readiness.

## Outcome
Planning remains focused on orchestration, work decisions stay with the owning builder, peer conflicts are resolved together, and a finished session reports deletion readiness only after its work and handoffs are complete.

## Example (made up)
Team Alpha has one planner and two builders. Both builders identify each other before editing and discover overlapping work. They message each other, agree that one owns the shared change, and continue separately. A design decision is sent to the owning builder, which asks the owner directly; the planner handles only routing. When that builder verifies and commits its work, has no background activity or pending decision, and informs the planner, its final report says it can be deleted.

## Pitfalls
- Do not turn a builder's work decision into a routing question or move it into the planner's session. That bypasses the intended decision owner.
- Do not resolve overlap, merge conflicts, or shared-state failures by editing or abandoning another session's work unilaterally. Consult the owning session and escalate only when collaboration cannot settle the issue or a business decision is required.
- Do not claim completion while a check, background process, owner decision, handoff, or promised follow-up remains open.
- Do not continue overlapping work without first agreeing with the peer who owns the related work.

## Measured result
No number is published for this practice yet.

## Credits
Mark Lim, Founder at Namarix and Cheatsheet, from how Namarix runs its own AI work.
