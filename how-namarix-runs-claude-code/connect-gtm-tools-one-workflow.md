---
name: connect-gtm-tools-one-workflow
description: Connect a client's CRM, enrichment tool and sequencer into one workflow in which every record type has one owning system, one shared identifier joins the tools, each handoff has a duplicate rule, and every write is proven by reading it back.
tools: Read
version: 0.1.0
---

# Connect the GTM tool stack (CRM, sequencer, enrichment) into one workflow

## When to use it
- A client runs a CRM, an enrichment tool and a sequencer, and records drift or duplicate between them.
- You are about to give an AI coding agent access to a GTM tool.

## Steps
1. List the tools and the record types (lead, company, reply, deal). For each record type, name the one system that owns it and the people on the client side who answer for it.
   - Output: a table of record type, owning system and client owner.
2. Pick the shared identifier that joins the tools (for people the profile address or a verified email, for companies the domain) and write the field map: which field in each tool holds which value, using one spelling per field. Match on the identifier's core part (a profile's slug, not its full web address), because tools rewrite addresses.
   - Output: a field map and the identifier rule, with five example rows that use made-up values.
3. Choose how your code reaches each tool, in this order: the vendor's own command line tool; a direct API call for a one-off job; a small command line tool you write only when the job recurs (our rule of thumb: a schedule depends on it, three or more sessions use it, or five or more endpoints); an MCP server only when none of those can reach what you need. Give every credential one owner: one piece of code may refresh a token, everything else reads it.
   - Output: a table of tool, access path and reason, and a code search showing one refresh path per tool.
4. Build each handoff in the flow: new lead to enrichment, enriched lead to sequence, reply back to the CRM, and a stop of every channel when a person replies or says no. For each handoff write the duplicate rule (what is checked before a record is created). A person approves the first live run of each handoff before it is switched on. Make every write a dry run unless you pass an explicit apply flag, and after each write read the record back and compare.
   - Output: a handoff list with the duplicate rule, a dry-run diff before the write and a read-back match after it.
5. Test the known traps offline: a success code that changed nothing (read the list again after a delete), a field written under one name and read under another, and a duplicate created by running twice. Then run the whole flow once on a small test list in a test account and compare the counts in every tool.
   - Output: one failing-then-passing test per trap and matching counts across tools.
6. Send sync errors to one alert channel and send a test error to prove it arrives. Review the log each week for failed handoffs and records missing from a tool.
   - Output: a received test alert and a weekly list of failed handoffs.

## Pitfalls
- A tool token refreshed from two places gets revoked by the second one.
- A success response does not prove the change happened.
- Matching on a full web address misses records that a tool rewrote.

## Measured result
No number is published for this practice yet.

## Credits
Mark Lim, Founder at Namarix and Cheatsheet, from how Namarix connects its own sales and lead tools.
