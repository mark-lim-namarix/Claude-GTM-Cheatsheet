---
name: source-backed-opener
description: Writes a one-sentence cold-email opener only from an article the prospect really published on their own domain. If no real, recent article exists, it holds the lead and writes nothing.
tools: Read, WebSearch, WebFetch
version: 0.1.0
---

# Source-backed opener

## The problem
AI can write a confident compliment about an article that does not exist. The prospect knows at once, and the email is wasted.

## When to use it
Before any cold email where the first line should prove you read something. Skip it for warm replies.

## Inputs
- Company name and website domain.
- The sections you may read: blog, newsroom, podcast, resources.

## Steps
1. Confirm the domain belongs to the company and is live (not parked, not redirected to an acquirer).
2. Find one specific article, post or episode on that domain with a URL and a publish date. A homepage tagline is not an article.
3. Check it was published in the last six months.
4. Point to the sentence in the article that supports your topic phrase.
5. Write one line: "Saw {company} publish {topic}", plus one short reason it matters to the reader. 25 words at most.

## The check that fires
Any failed step in 1 to 4 ends in `HOLD: <which step failed>` and no opener. Example of the check firing (synthetic):

```
Company: Example Studio (examplestudio.test)
Result: HOLD: step 2, no dated article found on examplestudio.test
```

An honest hold beats an invented compliment.

## Approval route
The agent returns the opener with its `SOURCE: <url> <date>` line. You read the source before the email is used or sent. It never sends anything itself.

## Outcome to measure
Positive reply rate for leads with a source-backed opener versus the same list with your old opener. Count holds as a result, not as failures.

## Credits
Draws on open GTM skill collections and the community habit of grounding outreach in real signals: ColdIQ GTM Skills, Cold Outbound Skills, Extruct GTM Skills. Credit is not endorsement.
