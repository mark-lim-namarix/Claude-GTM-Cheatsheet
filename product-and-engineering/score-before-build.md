---
name: score-before-build
description: Scores a proposed task on need, ease and expected outcome before anyone starts it, and recommends parking the low scorers with a question instead of building them.
tools: Read
version: 0.1.0
---

# Score before build

## The problem
Every idea sounds worth doing, so the team starts all of them. The ones that never mattered eat the week, and the ones that did matter wait.

## When to use it
The moment someone proposes a new task, tool or experiment, before work starts.

## Inputs
- The proposal in one or two sentences.
- Who benefits and what result you expect (a number or a named outcome).
- A rough size of the work (hours or days).
- The current open queue, if you keep one (optional).

## Steps
1. Check the proposal names an outcome. If not, stop here.
2. Score three things from 0 to 100, with one sentence of evidence each: need (do people want it, and do they lack it today), ease (how simple to finish), outcome (how much result or revenue it can bring).
3. Combine them: 40 percent outcome, 35 percent need, 25 percent ease.
4. 60 or above: recommend build. Below 60: recommend parking it and ask "now or later?".
5. If you gave the queue, say where the item would rank in it.

## The check that fires
No named outcome means no score, and below 60 means a recommendation to park. Example (synthetic):

```
Proposal: "add a dashboard of all agent logs"
Outcome: none named -> NOT SCORED, name the result you expect first

Proposal: "stop sending follow-ups after a no", outcome: fewer complaints
need 70, ease 80, outcome 60 -> 0.35x70 + 0.25x80 + 0.40x60 = 68.5 -> BUILD
```

## Approval route
The agent recommends; you decide. A parked item is not deleted, it waits in the queue.

## Outcome to measure
Share of started tasks that finish and are still in use after a month. It should rise as low scorers stay parked.

## Credits
Draws on prioritization methods used in product teams: Intercom, RICE prioritization. Credit is not endorsement.
