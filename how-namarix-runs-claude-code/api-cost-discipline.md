---
name: api-cost-discipline
description: Use when a coding agent will build or test against paid APIs, to produce a call plan, small-test result, approved bulk run, and per-item cost report.
tools: Read
version: 0.1.0
---

# AI API cost discipline

## When to use it
- Before building or testing any feature that calls a paid API
- When a design may use multiple calls for questions or items that could be batched
- Before scaling a live test beyond the small test set
- Before running a paid lead-list search or other bulk external-API job

## Steps
1. Design the request to consolidate work that one API call can answer, and state expected calls per item and per run before building.
   - Why: A design that uses multiple calls where one batched call works is a defect and increases spend.
   - Check: Review the plan for batching, shared context, structured results, and the expected call counts before implementation.
2. Name the cheapest decisive test, prove plumbing with offline tests or stubs, and use a paid run only for behavior that code cannot measure.
   - Why: Planning first prevents spending on tests that do not answer a necessary question.
   - Check: The plan identifies the decisive paid measurement and shows that cheaper offline checks happen first.
3. Run a small live test first, grow only after it is clean, and reuse cached paid results for unchanged inputs.
   - Why: Small staged tests limit unnecessary spend, and caching avoids paying again for unchanged work.
   - Check: Confirm the small test is clean before expanding, and confirm reruns skip unchanged inputs.
4. Report calls and cost per item for every run, compare cost per item with the previous run, and take an available option that keeps quality while reducing spend.
   - Why: Cost discipline requires visibility into per-item changes and favors lower spend at equal quality.
   - Check: The run report includes calls and cost per item, flags an increase, and records any equal-quality reduction applied.
5. Before changing or scaling an external API integration, verify the current plan, limits, account tier, and multi-account terms, then size bounded concurrency and pacing from the verified information.
   - Why: Assumed tiers or noncompliant account pooling can waste capacity or violate provider terms; pacing must be fast without breaching limits.
   - Check: The plan records verified limits and tier, confirms the applicable terms, identifies the bottleneck, and specifies safe concurrency and pacing.
6. For bulk work, wait for explicit approval of that specific run after the small-test result and cost estimate; for lead lists, show the complete filter, expected lead count, and cost before any paid search or enrichment.
   - Why: General permission to continue does not authorize a bulk paid run, and lead-list spend requires the exact filter to be approved first.
   - Check: The approval explicitly covers the planned bulk run, or the lead-list filter is shown and the owner selects the run option before spending.
7. Run approved batches at bounded concurrency, honor retry delays and back off on repeated rate-limit responses, while keeping internal systems within safe load.
   - Why: Serial batches waste time, while excessive concurrency can breach provider or internal-system limits.
   - Check: The run uses the selected bounded concurrency, responds to rate-limit signals by slowing down, and shows no unsafe internal load.

## Outcome
Paid API work uses consolidated calls, small staged tests, cached results, verified pacing, and explicit bulk approval, while each run reports calls and cost per item.

## Example (made up)
Made-up example: Team Alpha needs to classify 20 records through a paid API. It plans one structured batched request per item, checks the plumbing offline, and starts with 4 live items. After the small run is clean, it reuses cached results for unchanged records and expands to 20. A bulk run is held until the owner sees the result and cost estimate. The report shows calls and cost per item, with no unnecessary rerun.

## Pitfalls
- Using separate calls when one batched call works increases avoidable API spend.
- Treating a general instruction to continue as approval for a full paid run can start bulk work without the required final pass.
- Assuming a plan tier or using stale limit information can produce incorrect pacing and waste available capacity.
- Pooling accounts without checking the provider's terms can violate those terms; the compliant path differs by provider.
- Running a batch serially, or pacing it without verified limits, creates avoidable delay or rate-limit failures.

## Measured result
No number is published for this practice yet.

## Credits
Mark Lim, Founder at Namarix and Cheatsheet, from how Namarix runs its own AI work.
