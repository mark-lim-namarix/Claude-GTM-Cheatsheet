---
name: fake-quote-check
description: Checks every quotation in a draft against the source text you provide, word for word, and flags any quote it cannot find.
tools: Read
version: 0.1.0
---

# Fake-quote check

## The problem
AI can put a sentence in quotation marks and credit it to a real person who never said it. If you publish it, the person and their audience see it, and your name is on it.

## When to use it
Before you publish or send any content that quotes a person, a podcast or an article.

## Inputs
- The draft.
- The source texts for every person or document quoted (transcripts, articles).

## Steps
1. List every passage in quotation marks, with who it is credited to.
2. Find the credited person's source text. If you did not provide one, mark the quote UNVERIFIED.
3. Search that source for the exact words. Differences in spacing and punctuation alone are ignored; any change in words is NOT FOUND.
4. Mark each quote FOUND, NOT FOUND or UNVERIFIED, with the place it was found.

## The check that fires
Any quote that is NOT FOUND or UNVERIFIED reports the draft as blocked until you fix or remove it. Example (synthetic):

```
Quote 1, credited to Person A: "Outbound only works with clean data" -> FOUND, transcript line 212
Quote 2, credited to Person A: "Nobody reads cold email anymore" -> NOT FOUND in the transcript
Quote 3, credited to Person B: no source provided -> UNVERIFIED
Result: BLOCK reported, 2 quotes need a fix; hold the draft
```

Coverage limit: it only checks against the sources you give it. A quote from a source you did not supply is never confirmed.

## Approval route
The agent never edits the draft. You remove the quote, find the real words, or supply the missing source.

## Outcome to measure
Number of quotes blocked before publishing, and the number of corrections you have to make after publishing (target: zero).

## Credits
Draws on source-checking habits from editorial work and from content tools that quote real transcripts. Credit is not endorsement.
