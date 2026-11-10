---
name: auto-reply-filter
description: Labels machine-sent messages (no-reply senders, calendar notices, bounces, out-of-office) so they can be kept out of your reply queue and only messages from real people reach you. Never labels a message AUTOMATIC when it contains a question for a person.
tools: Read
version: 0.1.0
---

# Auto-reply filter

## The problem
Your reply queue fills with calendar notices, bounce messages and "I am out of office". The real answers get buried, or the system answers a robot.

## When to use it
On every incoming message, before it reaches your reply queue or any agent that drafts answers.

## Inputs
- The incoming message: sender address, subject, the first lines, and any header that marks it as automatic.

## Steps
1. Check the sender for a fixed list of machine patterns: no-reply, noreply, donotreply, notifications, mailer-daemon, postmaster. A match is only a signal.
2. Check for headers that mark an automatic message: Auto-Submitted with any value other than "no", X-Autoreply, or Precedence set to auto_reply. A match is only a signal.
3. Read the message. If it asks a question or makes a request, label it QUEUE (a person may be behind it), whatever the signals say.
4. Otherwise, if a signal matched, label it AUTOMATIC with the reason.
5. An out-of-office from a real person is labelled OUT OF OFFICE, with the return date if given. It stays visible in a separate group and is not mixed into the reply queue.
6. Anything else is labelled QUEUE.

## The check that fires
A machine pattern labels the message AUTOMATIC so you can keep it out of the queue; a question from a person is never labelled AUTOMATIC. Example (synthetic):

```
From: noreply@example.test, "Your meeting was accepted" -> AUTOMATIC (sender pattern noreply)
From: [Recipient A], "I am away until the 20th" -> OUT OF OFFICE, return 20th, follow up after
From: notifications@example.test, body contains "Can you send pricing?" -> QUEUE, a question is present, a person may be behind it
```

## Approval route
The agent only reads and labels; it cannot move or delete anything. You (or your mail rules) act on the labels, and you review the AUTOMATIC list now and then to catch a wrong label.

## Outcome to measure
Share of queue messages that are from real people (should rise), and the number of real replies wrongly labelled AUTOMATIC (target: zero).

## Credits
Draws on standard email conventions for automatic messages and on open outreach collections: Cold Outbound Skills. Credit is not endorsement.
