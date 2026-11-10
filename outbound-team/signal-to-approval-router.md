---
name: signal-to-approval-router
description: Turns a buying signal about a target account into a proposed message with its source, and routes it to you to approve, edit or reject. Drops signals without a dated source.
tools: Read, WebSearch, WebFetch
version: 0.1.0
---

# Signal-to-approval router

## The problem
A signal tool shows an account is hiring or just raised money. Nobody acts on it in time, or the message sent is a generic template. The window to reach them while it mattered is gone.

## When to use it
Every time your signal source flags a target account (funding, hiring, a new launch, a leadership change).

## Inputs
- The signal, with its source link and date.
- The target account and the right contact on your list.
- Your offer in one sentence.
- A list of people you contacted in the last 30 days.

## Steps
1. Check the signal has a source link and a date within the last 30 days.
2. Check you have not contacted this person in the last 30 days.
3. Draft one short message that mentions the signal and one clear ask.
4. Show you the draft, the signal and its source in the chat for your decision.
5. Wait for your answer: approve, edit or reject. If you use Slack or a tracker, you copy the draft there; the agent does not post anywhere.

## The check that fires
A signal with no source or an old date is dropped, and a person contacted within 30 days is skipped. Example (synthetic):

```
Signal: "Sample Co is raising" (no link, no date)
Result: DROP, no source; no message drafted
Signal: new VP hired at Sample Co, 40 days ago
Result: DROP, older than 30 days
```

## Approval route
Nothing goes out without your approve. If you edit, the agent shows the revised message for your approve. Reject drops the signal.

## Outcome to measure
Time from signal to approved message, and positive replies per 100 approved messages versus your untargeted outreach.

## Credits
Draws on signal-based outreach ideas shared in open collections: ColdIQ GTM Skills, Extruct GTM Skills. Credit is not endorsement.
