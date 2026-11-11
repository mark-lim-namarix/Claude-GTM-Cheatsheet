---
name: mam
description: MAM (Metacognitive Alignment Matrix). Before a task starts, checks what you know and what the AI knows about it, including what either side only thinks it knows, places the task in one of 16 situations, and asks the questions that situation needs. Reports READY TO BUILD only when every gap is closed.
tools: Read
version: 0.2.0
---

# MAM (Metacognitive Alignment Matrix)

## The problem
You explain what you want, the AI builds what you typed instead of what you meant, and next time you explain it all again. A better prompt does not fix this. The gap is in what each side knows, and in what each side only thinks it knows.

## When to use it
Before any task that takes more than an hour, or whenever you catch yourself re-explaining. Tell your AI: "Use MAM to ask me questions about this task."

## Inputs
- The task or request.
- What is already decided, so nothing is asked twice.
- Any files, notes or past decisions the AI can read about you and the task.

## Steps
1. Place you in one of 4 states, and say why, quoting your request:
   - U1 Sure and right: specific, consistent, and nothing the AI can find contradicts it.
   - U2 Rough idea: goal words, no limits, no picture of done.
   - U3 Knows they don't know: asks how things work, asserts nothing.
   - U4 Sure but wrong: states something that contradicts a fact the AI can name. Never chosen on a hunch.
2. Place the AI in one of 4 states, and show the basis:
   - A1 Knows your context accurately and in depth: it can cite the file, note or source.
   - A2 Knows only parts: it names the missing parts.
   - A3 Has no data: it says so plainly.
   - A4 Thinks it knows you but is making it up: it cannot point to a file, note or source. It must declare this itself.
3. The two states give one of 16 situations. Ask the questions that situation calls for:
   - U1 with A1: ask nothing and report READY TO BUILD.
   - U1 with A2, A3 or A4: ask you for the missing context and treat your answer as the reference.
   - U2: offer concrete options to choose from, and design nothing until the limits are set.
   - U3: explain the options first, then confirm what you chose.
   - U4: challenge the premise with the named fact, before anything is built.
   - U4 with A3 or A4: challenge only with a fact from a named outside source. If none exists, treat you as U1 and ask for your reference.
   - A4 in any row: no invented detail. Find a source or ask.
4. For each question: would a different answer change the result? If not, drop it. If a safe default exists, state the default instead of asking.
5. Rank what is left by what is at stake (money or customers first, then rework, then taste) and give a recommended answer for each. A question with no possible recommendation is listed as "Sent back, needs your input".
6. End with NOT READY (any question open or sent back) or READY TO BUILD (none left). Run it again after you answer. It reports READY TO BUILD only when nothing is open or sent back.

## The check that fires
The agent drops from its report, or marks "Sent back, needs your input", any state given without its basis, any A1 with nothing cited, any U4 with no named contradicting fact, and any question that repeats something already decided. An A4 the AI did not declare itself is marked A4 and its invented details are struck from the report. The output says NOT READY while any question is open or sent back. Example (synthetic):

```
Task: add a refund button
You: U4 (you said "refunds are instant"; the payment provider's docs say 5 to 10 days)
AI: A2 (knows the checkout code and the provider docs, has no data on your own refund policy)
Declared: "I assumed you want refunds to go back to the card. I have no note saying so."
Situation: U4 with A2
Q1 (customers, premise): refunds take 5 to 10 days at your provider. Show "processing" instead of "refunded"? Recommended: yes
Q2 (money): full or partial refunds? Recommended: full only for now
Q3 (money): refund to card or store credit? Recommended: card
Dropped: button colour (default: match the app)
Sent back, needs your input: Q4 "what about taxes?" has no recommended answer yet
Result: NOT READY, 3 questions open, 1 sent back
```

## Approval route
The agent only asks and recommends. It writes nothing. You answer once, put your answers in your own brief, and run it again to get a new result.

## Outcome to measure
How often you have to re-explain a task, and changes requested after delivery. Both should fall.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
