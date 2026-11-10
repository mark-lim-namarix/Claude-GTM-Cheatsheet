---
name: send-guard
description: Checks an outbound draft against its target record before it goes out. Flags it as BLOCKED if the recipient, greeting or signature does not match the person and the channel.
tools: Read
version: 0.1.0
---

# Send guard

## The problem
The email goes to the right company with the wrong name in the greeting, or the LinkedIn message ends with the email signature. The prospect sees a mass mailing and the team looks careless. It happens most when drafts are made in bulk.

## When to use it
As the last step before any outbound draft is approved, on every channel.

## Inputs
- The draft (greeting, body, signature).
- The target record: recipient name, company, channel.
- The names of the other recipients in the same batch.
- Your signature rules per channel.

## Steps
1. Compare the greeting with the recipient's name on the record.
2. Check that no other person's name from the same batch appears in the draft.
3. Check the signature matches the channel (a LinkedIn message carries no email footer).
4. Check the company name in the body matches the record.
5. Return PASS, or BLOCKED with the exact line that failed.

## The check that fires
Any mismatch is flagged BLOCKED, and the draft should not go out. Example (synthetic):

```
Record: [Recipient A], Sample Co, LinkedIn
Draft: "Hi [Recipient B], saw Sample Co ... Best, [Sender] | Head of Growth | sender@example.test"
Result: BLOCKED, greeting [Recipient B] does not match [Recipient A]; email footer on a LinkedIn message
Another draft, greeting [Recipient A], correct footer for LinkedIn -> PASS (still waits for your approval)
```

## Approval route
It never edits or sends. A blocked draft goes back to the writer with the failed line; a PASS still waits for your approval.

## Outcome to measure
Number of blocked drafts per 100, and the share of replies that mention a wrong name or a mass-mail feeling. Both should fall to near zero.

## Credits
Draws on cold outreach quality checks shared in open collections: Cold Outbound Skills, ColdIQ GTM Skills. Credit is not endorsement.
