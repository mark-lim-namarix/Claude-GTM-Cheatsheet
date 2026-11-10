# Outbound team: a free agent database for GTM agencies and B2B teams

A department-structured agent database for Claude Code. Release 1 is one full department, the **Outbound team**: six agents you install one at a time. Every agent carries a check that fires, an approval step before anything leaves your hands, and an outcome you measure. Review everything before it goes out.

## The Outbound team

| Agent | What it does | Install |
|---|---|---|
| [Source-backed opener](outbound-team/source-backed-opener.md) | Writes a cold-email opener only from an article the prospect really published, or holds the lead | `mkdir -p ~/.claude/agents && cp outbound-team/source-backed-opener.md ~/.claude/agents/` |
| [Judge-before-send](outbound-team/judge-before-send.md) | Scores a draft against your written, weighted rubric and blocks it below 0.90 | `mkdir -p ~/.claude/agents && cp outbound-team/judge-before-send.md ~/.claude/agents/` |
| [Send guard](outbound-team/send-guard.md) | Stops a draft with the wrong recipient, greeting or signature | `mkdir -p ~/.claude/agents && cp outbound-team/send-guard.md ~/.claude/agents/` |
| [Reply desk](outbound-team/reply-desk.md) | Sorts replies, drafts answers for you to approve, and stops on a clear no | `mkdir -p ~/.claude/agents && cp outbound-team/reply-desk.md ~/.claude/agents/` |
| [Closed-loop scorecard](outbound-team/closed-loop-scorecard.md) | Compares results against a control group so you learn what works | `mkdir -p ~/.claude/agents && cp outbound-team/closed-loop-scorecard.md ~/.claude/agents/` |
| [Signal-to-approval router](outbound-team/signal-to-approval-router.md) | Turns a buying signal into a message you approve or edit | `mkdir -p ~/.claude/agents && cp outbound-team/signal-to-approval-router.md ~/.claude/agents/` |

One line per agent: copy the file into `~/.claude/agents/` (create the folder if needed), then ask Claude Code to use it by name. Install one, or all six: `mkdir -p ~/.claude/agents && cp outbound-team/*.md ~/.claude/agents/`.

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

## License and limits

MIT. Provided as is, with no warranty or support. Agents can read the web and run commands in your project, so read an agent file before you install it. The examples are synthetic.

## Changelog

- 0.1.0: Outbound team, six agents.
