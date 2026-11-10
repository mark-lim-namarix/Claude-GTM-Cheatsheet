# Outbound team: a free agent database for GTM agencies and B2B teams

A department-structured agent database for Claude Code. The first department is the **Outbound team** (six agents you install one at a time); **Quality and measurement** (four), **Operating system** (three) and **Working with AI** (six) follow. Every agent carries a check that fires, an approval step before anything leaves your hands, and an outcome you measure. Review everything before it goes out.

## The Outbound team

| Agent | What it does | Install |
|---|---|---|
| [Source-backed opener](outbound-team/source-backed-opener.md) | Writes a cold-email opener only from an article the prospect really published, or holds the lead | `mkdir -p ~/.claude/agents && cp outbound-team/source-backed-opener.md ~/.claude/agents/` |
| [Judge-before-send](outbound-team/judge-before-send.md) | Scores a draft against your written, weighted rubric and blocks it below 0.90 | `mkdir -p ~/.claude/agents && cp outbound-team/judge-before-send.md ~/.claude/agents/` |
| [Send guard](outbound-team/send-guard.md) | Stops a draft with the wrong recipient, greeting or signature | `mkdir -p ~/.claude/agents && cp outbound-team/send-guard.md ~/.claude/agents/` |
| [Reply desk](outbound-team/reply-desk.md) | Sorts replies, drafts answers for you to approve, and stops on a clear no | `mkdir -p ~/.claude/agents && cp outbound-team/reply-desk.md ~/.claude/agents/` |
| [Closed-loop scorecard](outbound-team/closed-loop-scorecard.md) | Compares results against a control group so you learn what works | `mkdir -p ~/.claude/agents && cp outbound-team/closed-loop-scorecard.md ~/.claude/agents/` |
| [Signal-to-approval router](outbound-team/signal-to-approval-router.md) | Turns a buying signal into a message you approve or edit | `mkdir -p ~/.claude/agents && cp outbound-team/signal-to-approval-router.md ~/.claude/agents/` |

One line per agent (run from the repo folder): copy the file into `~/.claude/agents/` (create the folder if needed), then ask Claude Code to use it by name. Install one, or all six: `mkdir -p ~/.claude/agents && cp outbound-team/*.md ~/.claude/agents/`.

## Quality and measurement

Four agents that check your work and your spend. Install one at a time.

| Agent | What it does | Install |
|---|---|---|
| [Model A/B scorer](quality-and-measurement/model-ab-scorer.md) | Compares two models or prompts on the same cases and says which is better, or that there is too little data | `mkdir -p ~/.claude/agents && cp quality-and-measurement/model-ab-scorer.md ~/.claude/agents/` |
| [Cost brake](quality-and-measurement/cost-brake.md) | Compares usage with your caps and says STOP at 95 percent | `mkdir -p ~/.claude/agents && cp quality-and-measurement/cost-brake.md ~/.claude/agents/` |
| [Relay receipts](quality-and-measurement/relay-receipts.md) | Checks an instruction reached everyone who needs it | `mkdir -p ~/.claude/agents && cp quality-and-measurement/relay-receipts.md ~/.claude/agents/` |
| [Fake-quote check](quality-and-measurement/fake-quote-check.md) | Checks every quote in a draft against the source text | `mkdir -p ~/.claude/agents && cp quality-and-measurement/fake-quote-check.md ~/.claude/agents/` |

## Operating system

Three agents that keep the work itself in order. Install one at a time.

| Agent | What it does | Install |
|---|---|---|
| [Company brain](operating-system/company-brain.md) | Checks the shared facts your agents rely on exist and are current before a task starts | `mkdir -p ~/.claude/agents && cp operating-system/company-brain.md ~/.claude/agents/` |
| [Score before build](operating-system/score-before-build.md) | Scores a proposed task on need, ease and outcome and recommends parking the low scorers | `mkdir -p ~/.claude/agents && cp operating-system/score-before-build.md ~/.claude/agents/` |
| [Auto-reply filter](operating-system/auto-reply-filter.md) | Labels machine-sent messages so you can keep them out of your reply queue, never real questions | `mkdir -p ~/.claude/agents && cp operating-system/auto-reply-filter.md ~/.claude/agents/` |

## Working with AI: rules and guardrails

Six agents that carry the rules we use to work with AI every day: who checks the work, what counts as done, and when a human decides. Install one at a time.

| Agent | What it does | Install |
|---|---|---|
| [Fresh-eyes reviewer](working-with-ai/fresh-eyes-reviewer.md) | Reviews work from the work and your criteria alone, never the author's reasoning | `mkdir -p ~/.claude/agents && cp working-with-ai/fresh-eyes-reviewer.md ~/.claude/agents/` |
| [Release gate](working-with-ai/release-gate.md) | Labels each item SENDABLE or BLOCKED before anything for an outside reader goes out | `mkdir -p ~/.claude/agents && cp working-with-ai/release-gate.md ~/.claude/agents/` |
| [Defect triage](working-with-ai/defect-triage.md) | Turns a list of problems into fix-now, your decision and your action | `mkdir -p ~/.claude/agents && cp working-with-ai/defect-triage.md ~/.claude/agents/` |
| [Done-claim check](working-with-ai/done-claim-check.md) | Marks each "done" claim VERIFIED or UNVERIFIED against pasted evidence | `mkdir -p ~/.claude/agents && cp working-with-ai/done-claim-check.md ~/.claude/agents/` |
| [Fail-closed check](working-with-ai/fail-closed-check.md) | Treats anything skipped or not run as a failure, never a pass | `mkdir -p ~/.claude/agents && cp working-with-ai/fail-closed-check.md ~/.claude/agents/` |
| [Decision batcher](working-with-ai/decision-batcher.md) | Writes your real decisions as one batch, with a recommendation | `mkdir -p ~/.claude/agents && cp working-with-ai/decision-batcher.md ~/.claude/agents/` |

## What most free packs miss

Prompts and role descriptions are easy to find. These agents add three things:

1. **A check that fires.** Each agent says exactly what makes it refuse, hold or flag, and ships an example where it does.
2. **An approval route.** Nothing is sent for you. You approve, edit or reject.
3. **A feedback loop.** Each agent names the one outcome to measure, so you can compare against a control and keep what works.

## How an agent card reads

Every card has the same shape: the problem, when to use it, inputs, steps, the check that fires, the approval route, the outcome to measure, and credits.

## Credits

Built on ideas and open work from the community, with thanks. Credit is not endorsement.

- [Marketing Skills](https://github.com/coreyhaines31/marketingskills)
- [Cold Outbound Skills](https://github.com/growthenginenowoslawski/coldoutboundskills)
- [ColdIQ GTM Skills](https://github.com/sachacoldiq/ColdIQ-s-GTM-Skills)
- [Extruct GTM Skills](https://github.com/extruct-ai/gtm-skills)
- [Anthropic Skills](https://github.com/anthropics/skills)
- [RICE prioritization (Intercom)](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers)
- [Demystifying evals for AI agents (Anthropic)](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)

## License and limits

MIT. Provided as is, with no warranty or support. Check each card's `tools:` line before you install it: some agents here only read, but anything that lists more can act on your project. The examples are synthetic.

## Changelog

- 0.4.0: Working with AI, six agents.
- 0.3.0: Operating system, three agents.
- 0.2.0: Quality and measurement, four agents.
- 0.1.0: Outbound team, six agents.
