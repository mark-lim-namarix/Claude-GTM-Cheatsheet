---
name: prompt-vs-judge-alignment-check
description: Compares the instructions given to a writing AI with the questions given to the LLM judge, and reports any place where they use different wording, factors, weights or evidence.
tools: Read
version: 0.1.0
---

# Writer and judge alignment check

## The problem
When the writer and the judge are briefed separately, the writer optimises one thing and the judge scores another. The writer scores itself 0.95 and the judge gives 0.72, and nobody knows why.

## When to use it
Whenever one AI writes something and another AI judges it, and each time you change either side.

## Inputs
- The writer's prompt.
- The judge's questions and scoring instructions.
- The evidence each side sees (paste the inputs).

## Steps
1. List every criterion in the judge's questions.
2. For each, check the writer prompt contains the same definition word for word. Different wording is a mismatch.
3. Check the writer's self-score has a field for every judged criterion.
4. Check the weights and the scoring method (the 0, half and 1 anchors) are the same on both sides.
5. Compare the evidence: the judge must see as much source material as the writer used.
6. Report every mismatch with the quoted text from both sides.

## The check that fires
One criterion missing on one side, a different weight, or less evidence for the judge means MISALIGNED, listed item by item. Example (synthetic):

```
Judge criteria: accuracy, tone, source cited
Writer prompt: accuracy, tone (no source cited) -> MISMATCH: "source cited" missing in the writer
Tone: judge defines it as "friendly", writer as "neutral" -> MISMATCH: wording differs
Writer self-score fields: accuracy, tone -> MISMATCH: no field for "source cited"
Judge sees a 600-character summary; writer used the full 4,000-character text -> MISMATCH: less evidence
Accuracy weight: judge 0.5, writer 0.6 -> MISMATCH
Tone weight: judge 0.2, writer 0.4 -> MISMATCH
Result: MISALIGNED, 6 items
```

## Approval route
The agent only reports. You or the owner of the prompts fix both sides in the same change.

## Outcome to measure
The gap between the writer's self-score and the judge's score. A shrinking gap suggests the two agree more on the target; confirm with spot checks.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
