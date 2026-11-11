---
name: agent-relay-receipts
description: Checks that an instruction given to one agent or person actually reached everyone who needs it, by drafting the receipt request for each and comparing the receipts you paste back. Flags the ones that stayed silent.
tools: Read
version: 0.1.0
---

# Relay receipts

## The problem
You tell the lead agent a new rule. It never reaches the two agents doing the work, and they keep doing it the old way. You find out when the wrong thing ships.

## When to use it
Any time one instruction must be passed on to more than one agent or teammate.

## Inputs
- The instruction, word for word.
- The list of agents or people who must receive it.
- A deadline for the receipts.
- The receipts, pasted in as they arrive.

## Steps
1. Give the instruction a short id.
2. Draft the receipt request for each recipient: the id, the instruction in their own words, and where they will apply it. You send it; the agent cannot message anyone.
3. Paste the receipts you get back. The agent compares each one with the original. A receipt that changes the meaning is not accepted.
4. After the deadline, list who sent a good receipt, who sent a wrong one, and who sent none.

## The check that fires
A missing or wrong receipt after the deadline is flagged as NOT RECEIVED. Example (synthetic):

```
Instruction R-14: "Do not send follow-ups to anyone who replied no."
Agent 1: receipt matches
Agent 2: receipt says "pause follow-ups for a week" -> WRONG MEANING
Agent 3: no receipt by the deadline -> NOT RECEIVED
```

## Approval route
The agent reports who is covered and who is not. You decide who to chase or re-send to.

## Outcome to measure
Share of instructions fully received by the deadline, and the number of times work was done against an old instruction.

## Credits
Draws on read-back and acknowledgement habits used in team handoffs. Credit is not endorsement.
