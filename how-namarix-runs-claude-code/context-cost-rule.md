---
name: context-cost-rule
description: Use when deciding whether an AI coding task belongs in the main session or with a subagent, and when you need a verified change before committing.
tools: Read
version: 0.1.0
---

# delegating work to AI subagents

## When to use it
- A change may be small enough to perform inline, but its context, iteration needs or production impact are uncertain.
- Work involves exploration, repeated test and fix cycles, multiple files or a large build.
- Delegated work needs independent review and verification before it is committed.

## Steps
1. Classify the change against all four inline conditions: the main session can state the complete final content without opening an unread file, the change is at most 3 files and 40 changed lines, no test and fix iteration is expected, and it is not production runtime code.
   - Why: This replaces a blanket delegation rule with a context and risk threshold. Small, already-known changes do not need to create more context, while production runtime work remains delegated because its blast radius is higher.
   - Check: Record whether every condition is true. If any condition is false or becomes false during the work, route the change to a subagent.
2. Keep the change in the main session only when every inline condition is yes. Otherwise delegate it, including exploration, iterative work, multi-file work, bulk drafting, and runtime changes.
   - Why: The rule is a threshold rather than a blanket ban: inline work is limited to changes whose content is already known, while broader or iterative work is routed away from the main session.
   - Check: Confirm the chosen route matches every condition and exception, especially the runtime-code exception.
3. For mechanical delegated work, set an explicit lower-cost model and low or medium effort instead of allowing the delegation to inherit the top tier. For judgment review, use a fresh reviewer at the work's tier and not below the producer's tier.
   - Why: Tier discipline preserves the saving from delegation, while reviewer independence provides the value of judgment review.
   - Check: Inspect the delegation request and reviewer request to confirm that the mechanical tier is explicit and that the reviewer receives only the diff and acceptance criteria.
4. After delegated work, have the orchestrator run the deterministic checks and reread the changed files on disk.
   - Why: The files and mechanical gates are evidence; the producing session's reasoning and a delegated verifier's claim are not sufficient evidence.
   - Check: Confirm that the checks pass, the on-disk content matches the intended change, and the reviewer was fresh and independent.
5. Send judgment review to a fresh reviewer that receives only the diff and acceptance criteria. Keep mechanical checking at a lower tier, keep judgment review at the session tier and never below the producer, then decide from the gates and files rather than the reviewer's verdict alone.
   - Why: Independence is the value of review, while a review finding directs attention but is not evidence by itself. Mechanical checks and judgment review therefore require different treatment.
   - Check: Confirm that the reviewer had no producing conversation or reasoning, and resolve findings by inspecting the files and deterministic checks rather than adding work solely to satisfy a finding.

## Outcome
Work is routed by context, iteration risk and production blast radius: eligible small changes stay inline, while other work is delegated, mechanically checked and independently reviewed before a person approves what lands.

## Example (made up)
Team Alpha has a small documentation edit whose final text is already known, touches only a few files, needs no test and fix cycle, and is not production runtime code. It keeps that edit inline. A separate request involves exploration, repeated fixes and multiple slices, so Team Alpha delegates each slice, assigns mechanical checks to a lower tier, has the orchestrator verify the files before committing, and sends only the diff and criteria to a fresh judgment reviewer. A person approves what lands, and only work supported by the checks and file review is put forward.

## Pitfalls
- Delegating every small edit can consume more tokens, output, and elapsed time than doing the edit inline.
- Leaving a mechanical delegation without an explicit lower-cost tier can cause it to inherit the top tier and lose the intended saving.
- Treating a reviewer verdict as evidence, reviewing with the producing context, or verifying after the commit weakens independent review and evidence-based verification.
- Accepting a producer's summary or a reviewer's verdict without checking the files and deterministic gates treats a claim as evidence.

## Measured result
No number is published for this practice yet.

## Credits
Mark Lim, Founder at Namarix and Cheatsheet, from how Namarix runs its own AI work.
