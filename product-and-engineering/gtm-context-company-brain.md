---
name: gtm-context-company-brain
description: Checks that the shared facts your agents rely on (your ICP, who you sell to, what you offer, your proof, your voice) exist and are current before a task starts, and reports what is missing or old.
tools: Read
version: 0.1.0
---

# Company brain

## The problem
Every new chat starts from zero, so the answers come out generic. Or each person keeps different facts in their head and the agents contradict each other.

## When to use it
At the start of any task that writes for or about your company, and once a month as a freshness check.

## Inputs
- A folder of short files, one per topic. The default eight: buyers and ideal customers, offer, positioning, proof and case studies, voice and tone, common objections, competitors, rules (what never to say or do).
- The file names and the date each was last changed. Either put a "Last updated: YYYY-MM-DD" line at the top of every file, or paste in the list with dates.
- The task you are about to run.

## Steps
1. List which of the eight files exist and read the "Last updated" date of each.
2. Decide which files this task needs (an outbound email needs buyers, offer, proof, voice, rules).
3. Report each needed file as READY, MISSING or OLD (not changed in 90 days).
4. Say what answer quality to expect from what is missing. A MISSING file means the task should not start; an OLD file is a warning and you decide whether to go on.

## The check that fires
A needed file that is missing means STOP; an old file means WARN. Example (synthetic):

```
Task: write a cold email for the new offer
Needs: buyers, offer, proof, voice, rules
buyers: READY (12 days)   offer: OLD (140 days)   proof: MISSING   voice: READY   rules: READY
Result: STOP, proof is missing and offer is old; the email would be generic or invent proof
```

## Approval route
The agent only reports. You write or update the files; it never edits them. You decide whether to start the task anyway.

## Outcome to measure
Share of tasks that start with every needed file READY, and how often a draft needs a fact corrected afterwards (should fall).

## Credits
Draws on the shared-context habit in open Claude Code setups, such as keeping project context files: Anthropic Skills. Credit is not endorsement.
