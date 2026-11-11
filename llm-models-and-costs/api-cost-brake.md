---
name: api-cost-brake
description: Compares your spend on paid APIs and LLM usage against caps you set, and tells you to stop at 95 percent of a cap. Reports the cost per finished item.
tools: Read
version: 0.1.0
---

# Cost brake

## The problem
A batch job or a test loop runs all night. In the morning the monthly budget is gone, and the next two weeks of work stop.

## When to use it
Before any large or repeated run, and daily over your usage numbers.

## Inputs
- Your caps (per day, per week, per month) for each paid service.
- Your current usage numbers, copied from each service's dashboard.
- The number of items finished in the same period, and last week's number.
- The start date of each cap period and today's date.
- The list of runs or jobs that use each service.

## Steps
1. For each service, divide usage by its cap.
2. Below 80 percent: report OK.
3. From 80 up to 95 percent: report WARN and the date you will hit the cap at the current pace.
4. At 95 percent or more: report STOP.
5. Work out cost per finished item and compare it with last week's. Flag any service where it is rising.

## The check that fires
At 95 percent of any cap the answer is STOP, and the agent lists which runs to pause. Example (synthetic):

```
Service A: weekly cap 100, used 96  -> STOP, pause the nightly batch until the cap resets
Service B: monthly cap 200, used 150 -> OK, 75 percent
Cost per finished item: 0.42 this week vs 0.31 last week -> rising, check retries
```

## Approval route
The agent cannot pause anything or change a cap. You pause the runs and you decide whether to raise a cap.

## Outcome to measure
Number of times a cap was hit before you noticed (target: zero), and cost per finished item over time.

## Credits
Draws on the common practice of budgeting and pacing paid API use. Credit is not endorsement.
