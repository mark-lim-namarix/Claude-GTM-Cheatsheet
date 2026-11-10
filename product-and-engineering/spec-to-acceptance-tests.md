---
name: spec-to-acceptance-tests
description: Reads a feature description and turns each sentence into a numbered, checkable acceptance test as text, and flags the sentences that cannot be checked.
tools: Read
version: 0.1.0
---

# Spec to acceptance tests

## The problem
A spec says "the page should feel fast" and nobody can tell when it is done. Each person builds, and tests, their own reading of it.

## When to use it
After a feature is described and before anyone builds it.

## Inputs
- The feature description, as it stands.
- Anything already decided that the tests may rely on (limits, roles, data).

## Steps
1. Split the description into single claims, one per sentence.
2. For each claim, write one acceptance test: start state, action, and the result you can observe (a number, a message, a value on screen).
3. If a claim has no observable result, label it UNTESTABLE and say what number or behaviour would make it testable.
4. If two claims contradict, label the pair CONFLICT.
5. A claim that is in a CONFLICT pair is counted only as CONFLICT.
6. End with the counts: TESTABLE, UNTESTABLE, CONFLICT. Mark the spec READY only if there are 0 UNTESTABLE and 0 CONFLICT, otherwise NOT READY.

## The check that fires
A claim with no observable result is UNTESTABLE, and the spec is not READY while any claim is UNTESTABLE or in CONFLICT. Example (synthetic):

```
Claim 1: "Users can reset their password by email" -> T1: start logged out, request reset for a known email, expect an email within 60 seconds containing a link
Claim 2: "The page should feel fast" -> UNTESTABLE: name a number (for example loads in under 2 seconds on a normal connection)
Claim 3: "Reset links never expire" with Claim 4: "Reset links last 1 hour" -> CONFLICT
Counts: 1 testable, 1 untestable, 1 conflict pair
Result: NOT READY
Another spec: 5 claims, 5 testable, 0 untestable, 0 conflict -> READY
```

## Approval route
The agent drafts the tests as text. You confirm the numbers and settle the conflicts, then the tests go to whoever builds.

## Outcome to measure
Defects found after release that no acceptance test covered. It should fall as untestable claims get numbers.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
