---
name: eval-pass-and-fail-check
description: Checks that a test or checker passes good inputs of several kinds and also fails deliberately bad ones, because a test that only ever passes proves nothing.
tools: Read
version: 0.1.0
---

# Both-directions check

## The problem
A test can pass by luck. It matched on a lucky word, or it never looked at the thing it claims to check. It stays green while the thing it guards is broken.

## When to use it
When you write or change a test, a checker or a judge, and before you trust it.

## Inputs
- The test or checker (what it looks at and the pass rule).
- At least three good inputs written in different styles.
- At least two deliberately bad inputs that should fail.
- The result each input produced (paste it).

## Steps
1. Count the inputs. With fewer than three good or two bad inputs, label NOT ENOUGH CASES and go no further.
2. Read what the test claims to check.
3. List the good inputs and the result of each. Every good input must pass.
4. List the bad inputs and the result of each. Every bad input must fail.
5. Label the test BOTH DIRECTIONS only if both hold. If it passes a bad input, label it TOO LOOSE. If it fails a good input, label it TOO STRICT. If both happen, label it TOO STRICT and TOO LOOSE.
6. Say which input exposed the problem and what it suggests about the rule.

## The check that fires
A test with fewer than three good or two bad inputs cannot be labelled BOTH DIRECTIONS; it is labelled NOT ENOUGH CASES. Example (synthetic):

```
Test: "the answer is in Korean" (counts marker words)
Good 1: formal Korean paragraph -> failed (score 1 of 2) -> TOO STRICT
Good 2: casual Korean -> failed
Good 3: Korean with English product names -> passed
Bad 1: English answer quoting one Korean phrase -> passed -> TOO LOOSE
Bad 2: plain English answer -> failed (correct)
Result: TOO STRICT and TOO LOOSE. This suggests the rule matches whole words while the language glues endings to the stem. Fix the rule, do not lower the threshold.
A different test: 3 of 3 good inputs pass, 2 of 2 bad inputs fail -> BOTH DIRECTIONS (it held on these inputs only)
Another test with only two good inputs and one bad input -> NOT ENOUGH CASES
```

## Approval route
The agent reports. You fix the test, never the threshold to make it green, and then you run it again on the same inputs.

## Outcome to measure
Tests later found passing while the thing they guard was broken. The target is zero.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
