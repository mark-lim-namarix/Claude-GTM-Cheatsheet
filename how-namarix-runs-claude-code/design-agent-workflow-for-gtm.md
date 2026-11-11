---
name: design-agent-workflow-for-gtm
description: Design an AI agent workflow for a repeating GTM job such as sorting replies to outbound email or drafting a first message per prospect, with its context sources, tools, review limit and spend cap set before it runs.
tools: Read
version: 0.1.0
---

# Design the agent setup behind a GTM workflow

## When to use it
- You want an AI agent to handle a repeating GTM job, for example sorting and answering replies to outbound messages, or drafting a first message for each prospect on a list.
- The job touches real prospects, so a wrong output costs trust.

## Steps
1. Write the job in one line. List what a person must see to approve one result (the message, the record it came from, the label given), the review limit (who approves, how many per day) and the spend cap per batch. Write the acceptance checks as yes or no questions.
   - Output: a one-line job statement, a checklist, the review limit and the cap.
2. Choose what the agent may read and call: the reply thread, the CRM record, the fact sheet of approved claims, and nothing else. List the tools it may call and mark every tool that writes as approval-only. Split the job: everything with a fixed answer set (labels, channels, stop rules) is plain code; the model is used only for open text it must read or write. The model labels; it never rewrites the prospect's words, and code acts on the label.
   - Output: a list of allowed sources, allowed tools and a two-column list of code steps and model steps.
3. Draw the flow in order: fetch new items, label, draft, put into an approval queue, send after approval and a short delay. Save a pending record for each item before any message leaves, so a crash cannot send twice or lose one.
   - Output: a flow with a stored state for every item.
4. Set permissions and review points: the agent drafts and queues, a person approves each send, a clear "no" from a prospect stops every channel for that person, and automatic replies (out of office, bounces) stay out of the person's queue.
   - Output: a permission list and the stop rule written down.
5. Build a test set of 15 to 20 real or realistic inputs (out of office, wrong person, clear no, a question, a positive answer) and check both directions: the right label passes and a deliberately wrong one fails.
   - Output: a test set with the expected label for each input and a result table.
6. Measure after a week: share of drafts approved unchanged, share held, and actual cost per finished item against the cap. Stop at the cap, and keep the review limit until the numbers hold.
   - Output: a weekly table with the three numbers.

## Pitfalls
- Letting the model rewrite the prospect's text hides what was actually said.
- A pending record written after the send leaves a gap in which one message can go twice.
- A cap that is only measured after a week is too late to stop a bad batch.

## Measured result
No number is published for this practice yet.

## Credits
Mark Lim, Founder at Namarix and Cheatsheet, from how Namarix handles replies to its own outbound campaigns.
