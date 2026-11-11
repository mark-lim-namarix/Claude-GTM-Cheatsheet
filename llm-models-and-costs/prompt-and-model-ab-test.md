---
name: prompt-and-model-ab-test
description: Compares two models, prompts or agents on the same test cases and says which is better, or that the data is too thin to say. Keeps every error in the counts.
tools: Read
version: 0.1.0
---

# Model A/B scorer

## The problem
You switch to a new prompt or model because a few outputs looked better. A week later results are worse, and you cannot tell if the switch did it or you were just looking at lucky examples.

## When to use it
Before you replace a prompt, model or agent that already works, and any time someone says "the new one is better".

## Inputs
- A list of test cases, the same for both versions.
- For each case: did version A pass, did version B pass. You decide pass or fail with a rule written before you look.

## Steps
1. Before you look at results, fix the rule for pass or fail and the threshold for "clear" (default: likelihood below 0.05).
2. Count the cases where only A passed, only B passed, both passed and both failed.
3. A version that crashed or gave no answer on a case is recorded as a fail for that case. Never drop the case.
4. Use only the cases where the two disagree. Work out how likely that split is if the versions were equal: the exact two-sided binomial test with probability 0.5, which is 2 times the chance of getting the smaller count or fewer out of the disagreements (for 3 and 12 out of 15 that is 2 x 576 / 32768 = 0.035). Check the figure with a calculator before you rely on it.
5. Report: the four counts, the likelihood, and a plain verdict: B better, A better, or no clear difference, using your threshold.
6. Give the number of cases next to the verdict.

## The check that fires
Fewer than 20 cases, or any case where no pass or fail was recorded for one version (a crash counts as a recorded fail, a blank does not), means no verdict. Example (synthetic):

```
40 cases. Only A passed: 3. Only B passed: 12. Both passed: 20. Both failed: 5.
Disagreements: 15. Likelihood if equal: about 0.035.
Verdict: B better (40 cases).

Second run: 12 cases, 2 missing results for version B
Verdict: NO VERDICT, fewer than 20 cases and missing results
```

## Approval route
The agent only reports. You decide whether to switch, and you keep the old version available until the new one has run on real work.

## Outcome to measure
Of the switches you made on a clear verdict, how many still look better after a month of real use. That tells you if your test cases are good enough.

## Credits
Draws on published guidance on evaluating AI agents: Anthropic, Demystifying evals for AI agents. Credit is not endorsement.
