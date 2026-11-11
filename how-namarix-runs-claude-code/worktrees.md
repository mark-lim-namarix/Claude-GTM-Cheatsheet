---
name: worktrees
description: Use when an AI coding task has independent parts and needs a faster, safer delivery approach using parallel sessions, isolated Git worktrees, and explicit sequencing checks.
tools: Read
version: 0.1.0
---

# parallel AI sessions with git worktrees

## When to use it
- A non-trivial task separates into independent research, audit, migration, or file-level work.
- Several AI coding sessions need to work at the same time.
- A task includes tightly coupled build steps that must remain ordered.
- A session is about to edit or push shared repository work.

## Steps
1. Classify the work as divisible, tightly coupled, or trivial before starting.
   - Why: Parallel work is most useful for genuinely independent parts; coupled or trivial work can gain coordination and merge overhead instead.
   - Check: List the proposed parts and confirm that each parallel part can proceed without another part's output or decision.
2. Choose the largest practical number of parallel workers for the independent parts and start those workers concurrently.
   - Why: Independent work should begin in parallel rather than being performed one part at a time, while the amount of concurrency must fit repository stability and correctness.
   - Check: Confirm that every worker has one defined, independent slice and that no worker is idle while another independent slice is available.
3. Give every concurrent worker its own Git worktree and branch, and keep the shared checkout read-only.
   - Why: Separate worktrees prevent sessions from switching each other's branches or damaging in-progress work in a shared directory.
   - Check: Before any write, verify that the worker's session is inside the worktree holding its assigned branch and that no two workers share a working directory.
4. Create worktrees in a controlled sequence and clean up abandoned worker branches afterward.
   - Why: Creating many worktrees at exactly the same moment can race Git metadata and leave orphaned branches.
   - Check: Confirm that worktree creation was staggered and that no abandoned worker branches remain after setup.
5. Derive branch and session status from the repository's current worktree, branch, lock, and session records before the first edit and before a push to the main branch.
   - Why: Memory and conversation history can be stale; observable repository state shows which work is authoritative and whether a change is already represented elsewhere.
   - Check: Record the authoritative branch and worktree for the task, confirm the target file is from the intended current line of work, and recheck before pushing. A person approves any push to the main branch.
6. Keep tightly coupled continuous builds as ordered slices handled by one delegated worker at a time, and land or deliberately delete each task branch when finished.
   - Why: Coupled files can collide when changed in parallel, and branches that outlive their tasks can strand the only copy of a decision.
   - Check: Confirm that each coupled slice follows its predecessor and that every completed branch is either landed or deliberately deleted.
7. Coordinate shared resources separately from filesystem isolation.
   - Why: Worktrees isolate files but do not isolate shared databases, production branches, deployments, or other shared resources.
   - Check: Before a worker changes a shared resource, confirm that the required coordination lock or protocol is active.

## Outcome
Independent work can proceed concurrently with each worker isolated in its own worktree and branch, while coupled work remains ordered and session, branch, and worktree state is checked before edits and pushes.

## Example (made up)
Example Co has an audit, a migration review, and a tightly coupled build change. Team Alpha assigns the audit and review to two separate worktrees and branches, starts them together, and keeps the build change ordered through one worker. It checks repository state before edits and before the final push, then lands or deletes each branch. The result is parallel independent work without shared-checkout collisions.

## Pitfalls
- Letting two sessions write in one checkout can silently switch branches and damage another session's in-progress work.
- Starting many worktree creations at the same instant can cause Git metadata races and leave orphaned branches.
- Parallelizing tightly coupled files or build slices can create collisions and merge overhead instead of speed.
- Trusting memory, conversation history, or a stale branch can make a session edit the wrong line of work or leave completed work stranded.
- Treating a worktree as protection for shared databases, production branches, or deployments can allow conflicting shared-resource changes.

## Measured result
No number is published for this practice yet.

## Credits
Mark Lim, Founder at Namarix and Cheatsheet, from how Namarix runs its own AI work.
