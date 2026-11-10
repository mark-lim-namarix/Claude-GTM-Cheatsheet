---
name: question-first
description: Before a build starts, lists the questions whose answers would change the work, ranked by what is at stake, and drops the ones that have a safe default. Reports READY TO BUILD when every gap is closed.
tools: Read
version: 0.1.0
---

# Question first

## The problem
The expensive mistake is building the wrong thing well. The cheapest moment to catch it is before the first line is written.

## When to use it
After the intent is clear and before work starts on anything that takes more than an hour.

## Inputs
- The brief or request.
- What is already decided, so nothing is asked twice.
- What the work touches (people, money, data, other systems).

## Steps
1. Read the request and list every point where two reasonable people would build different things.
2. For each point, ask: would a different answer change the result? If not, drop it.
3. If a safe default exists, write the default instead of the question.
4. Rank what is left by what is at stake: money or customers first, then rework, then taste.
5. Output the questions with a recommended answer each, and a one-line list of the defaults applied. A question you cannot recommend an answer for is listed as "Sent back, needs your input".
6. End with NOT READY (any question open or sent back) or READY TO BUILD (none left).

## The check that fires
A question with no recommended answer, or one that repeats something already decided, is removed or sent back. The output says NOT READY while any question is open or sent back, and READY TO BUILD only when none remains. Example (synthetic):

```
Request: add a refund button
Already decided: refunds go through the payment provider
Q1 (money): full or partial refunds? Recommended: full only for now
Q2 (customers): email the customer? Recommended: yes
Dropped: Q3 "which payment provider?" repeats an item already decided; button colour (default: match the app); wording (default: "Refund")
Sent back: Q4 "what about taxes?" has no recommended answer yet
Result: NOT READY, 2 questions open, 1 sent back. READY TO BUILD appears once all are answered and none is sent back
```

## Approval route
The agent only asks and recommends. You answer once, and the answers go into the brief.

## Outcome to measure
Changes requested after delivery, per finished task. It should fall as the questions get better.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
