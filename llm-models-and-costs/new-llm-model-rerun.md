---
name: new-llm-model-rerun
description: Reads the results of the same test set run on your current model and on a new one, and says KEEP, SWITCH, INCONCLUSIVE or NOT COMPARABLE, using your stated rule. It also flags RULE NOT PRE-REGISTERED (an added flag, not a verdict) when the rule was written after seeing the results. It lists any cases that used to pass and now fail, and the cost per item.
tools: Read
version: 0.1.0
---

# New model rerun

## The problem
A new model arrives and people either switch because it is new or stay because it is familiar. Neither is a measurement. A new model can be better on average and still break things that worked.

## When to use it
When a new model is released, or when you consider changing the model or prompt behind a feature.

## Inputs
- The scores per test item for the current model and for the new model (each item counts as a pass or a fail by your own pass bar), on the same test set and the same prompts (paste both).
- The cost per item for each.
- Your switch rule written in advance (for example: switch only if the pass rate rises by 0.05 or more and no more than 2 items regress).

## Steps
1. Check both runs used the same items. If not, report NOT COMPARABLE.
2. Compute each pass rate and the difference.
3. List the REGRESSIONS: items that passed on the current model and fail on the new one.
4. Compare the cost per item. Cost is reported only; it does not change the verdict unless your rule says so.
5. Apply your switch rule in this order: if the absolute difference in passing items is smaller than the noise count you named (default: 2 items), report INCONCLUSIVE. Otherwise SWITCH if the rule is met, KEEP if it is not, including when the new model is clearly worse. Ask whether the rule was written before you saw the results; if not, add RULE NOT PRE-REGISTERED.

## The check that fires
A comparison on different items is NOT COMPARABLE, and a rule that was written after seeing the results is reported as RULE NOT PRE-REGISTERED. Example (synthetic):

```
Items: 40 both runs. Current 31 pass (0.775), new 34 pass (0.850), difference 0.075
REGRESSIONS: 3 items passed before, fail now (items 7, 18, 33)
Cost per item: 0.8 vs 1.4 cost units
Rule: switch if rise is 0.05 or more and 2 or fewer regress -> 3 regress -> KEEP (rule not met)
If only 1 regressed -> SWITCH
If the rise were 1 item (under the 2-item noise level) -> INCONCLUSIVE
If the new run used different items (40 vs 38) -> NOT COMPARABLE
If the rule was written after seeing the results -> RULE NOT PRE-REGISTERED, added to the KEEP or SWITCH result
Note: SWITCH means your rule was met, not that the new model is proven better. Pin the exact id of whichever model you keep
```

## Approval route
The agent applies your rule and reports. You decide, and you pin the exact model id after any change.

## Outcome to measure
Pass rate and cost per item after each model change, kept in one list over time.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
