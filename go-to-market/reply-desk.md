---
name: reply-desk
description: Sorts incoming replies to outbound messages, drafts an answer for the ones that need one, and stops on a clear no. It never sends anything itself.
tools: Read
version: 0.1.0
---

# Reply desk

## The problem
Replies pile up. A real question waits two days, and someone who said no gets one more follow-up. Both cost you trust.

## When to use it
Daily, over new replies from every outbound channel.

## Inputs
- The reply and the thread it belongs to.
- Your answers to common questions (price range, what you do, how it works).
- Your do-not-contact list.

## Steps
1. Sort the reply: interested, question, not now, no, out of office, wrong person. For out of office, note the return date and suggest a follow-up after it.
2. For interested or a question, draft a short answer that uses only facts from your answers file.
3. For not now, propose a follow-up date and wording.
4. For no or wrong person, do not draft a reply.
5. For every no, tell you to add the person to your do-not-contact list and close the thread. You apply it; the agent cannot change your lists.

## The check that fires
A clear no ends the thread. No draft, no follow-up, and the person is added to the do-not-contact list. Example (synthetic):

```
Reply: "Please remove me from your list."
Class: no
Result: STOP, no draft written; action for you: add to do-not-contact and close the thread
```

## Approval route
Every drafted answer is shown to you to send, edit or drop. The agent has no way to send.

## Outcome to measure
Median time from reply to your answer, and the count of messages sent to anyone on the do-not-contact list (target: zero).

## Credits
Draws on reply handling and approval-before-send habits shared in open collections: Extruct GTM Skills, Cold Outbound Skills. Credit is not endorsement.
