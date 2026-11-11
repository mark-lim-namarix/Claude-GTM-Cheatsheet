---
name: plan-answer-engine-citations
description: Build a content plan that gets a client named in the answers AI assistants give to buyer questions, from the questions buyers ask to a dated plan per question and a weekly re-check.
tools: Read
version: 0.1.0
---

# Plan content for AI answer engine citations

## When to use it
- A client wants to be named when buyers ask ChatGPT, Claude or Perplexity about their category.

## Steps
1. Write 20 questions a buyer would ask when looking for what the client sells. Ask each one in three assistants and record which sites are named in each answer.
   - Output: a sheet with question, assistant and the sites named.
2. Mark every question where the client is named, and list the sites that are named instead.
   - Output: a gap list showing the competing sites per question.
3. Rank the unanswered questions by how close they are to a purchase, and keep the top five.
   - Output: five ranked questions with the buying reason.
4. For each of the five questions, write the plan row: the asset to make or the place to get mentioned (reviews, community threads, partner pages, registries where the assistants already look), the evidence it carries (a number, a named customer, a dated claim), the owner and the date. Put mentions on other sites first: in our experience, not measured, they mattered more than changes to the client's own pages.
   - Output: a content plan with five rows of asset or place, evidence, owner and date.
5. Publish the client's own pages with the full answer as readable text in the page itself, a named author, dated claims and links to the sources (a page that gives crawlers only a short stub is not read). Do not rely on schema markup or an llms.txt file as the main lever; we saw no clear gain from them (also not measured).
   - Output: published pages with the full text visible without scripts.
6. Re-ask the same 20 questions every week in the same three assistants and record the citations gained or lost. From the first day, also record visits that arrive from assistant referrals; tie them to revenue once the client has some.
   - Output: a weekly sheet with citations gained or lost and referral visits.

## Pitfalls
- Changing many pages at once hides which change moved a citation.
- A short stub page gives crawlers almost nothing to quote.

## Measured result
No number is published for this practice yet.

## Credits
Mark Lim, Founder at Namarix and Cheatsheet, from Namarix's own work on being cited by AI assistants.
