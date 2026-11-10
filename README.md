# Agent database: work with AI without being an AI expert

A free database of agents for Claude Code. Each agent encodes a checklist for its field, so you can check AI work against a clear checklist without a deep understanding of how AI works. Topics so far include: how to make AI understand you, AI judging AI, AI-made test sets, keeping up with new models, handoffs between agents, rules and guardrails, product and engineering, and go-to-market. More topics follow.

## Install

Pick an agent, copy its file into `~/.claude/agents/`, then ask Claude Code to use it by name:

```
mkdir -p ~/.claude/agents && cp make-ai-understand-you/intent-brief.md ~/.claude/agents/
```

Or install a whole folder: `mkdir -p ~/.claude/agents && cp make-ai-understand-you/*.md ~/.claude/agents/` (run from the repo folder). Read an agent file before you install it, and review everything an agent produces before it goes out.

## Make AI understand you

Say what you mean once, so the AI builds the right thing the first time.

| Agent | What it does | Install |
|---|---|---|
| [intent-brief](make-ai-understand-you/intent-brief.md) | Turns a vague request into a short brief and states the intent it infers in one line, for you to correct | `cp make-ai-understand-you/intent-brief.md ~/.claude/agents/` |
| [question-first](make-ai-understand-you/question-first.md) | Lists the questions that would change the work before it starts, with a recommended answer each, and says NOT READY or READY TO BUILD | `cp make-ai-understand-you/question-first.md ~/.claude/agents/` |
| [reality-audit](make-ai-understand-you/reality-audit.md) | Tags every claim in a plan Known, Reasoned, Assumed or Unknown, lists the hidden work and marks it RISKY or UNREALISTIC when it is | `cp make-ai-understand-you/reality-audit.md ~/.claude/agents/` |
| [decision-batcher](make-ai-understand-you/decision-batcher.md) | Drafts your real decisions as one batch, with a recommendation | `cp make-ai-understand-you/decision-batcher.md ~/.claude/agents/` |

## AI judges AI

Let an AI judge another AI's work against a rubric you wrote, so you label less by hand.

| Agent | What it does | Install |
|---|---|---|
| [judge-builder](ai-judges-ai/judge-builder.md) | Turns your goal into a weighted rubric with 0, half and 1 anchors | `cp ai-judges-ai/judge-builder.md ~/.claude/agents/` |
| [judge-before-ship](ai-judges-ai/judge-before-ship.md) | Marks an output REWRITE below the pass bar and HOLD after two failed rewrites | `cp ai-judges-ai/judge-before-ship.md ~/.claude/agents/` |
| [writer-judge-alignment-check](ai-judges-ai/writer-judge-alignment-check.md) | Finds where the writer's instructions and the judge's questions differ | `cp ai-judges-ai/writer-judge-alignment-check.md ~/.claude/agents/` |
| [three-judge-check](ai-judges-ai/three-judge-check.md) | Compares three judges' scores and points to the one to fix | `cp ai-judges-ai/three-judge-check.md ~/.claude/agents/` |

## AI-made test sets

Test your prompts and agents without labelling everything yourself. Real items are labelled only from recorded outcomes you supply, and any label that came from the model being tested is left out. A few made-up bad cases are added and marked AUTHORED.

| Agent | What it does | Install |
|---|---|---|
| [test-set-maker](ai-made-test-sets/test-set-maker.md) | Proposes a test set whose labels come from recorded outcomes, and leaves out labels that came from the model under test | `cp ai-made-test-sets/test-set-maker.md ~/.claude/agents/` |
| [both-directions-check](ai-made-test-sets/both-directions-check.md) | Checks a test passes good inputs and fails bad ones, to catch a test that passes by luck | `cp ai-made-test-sets/both-directions-check.md ~/.claude/agents/` |
| [mock-drift-check](ai-made-test-sets/mock-drift-check.md) | Compares a fake copy of an outside service with a real sample and lists what changed | `cp ai-made-test-sets/mock-drift-check.md ~/.claude/agents/` |

## Keeping up with new models

Compare models fairly and watch the bill.

| Agent | What it does | Install |
|---|---|---|
| [model-ab-scorer](keeping-up-with-models/model-ab-scorer.md) | Compares two models or prompts on the same cases, or says there is too little data | `cp keeping-up-with-models/model-ab-scorer.md ~/.claude/agents/` |
| [cost-brake](keeping-up-with-models/cost-brake.md) | Compares usage with your caps and reports STOP at 95 percent | `cp keeping-up-with-models/cost-brake.md ~/.claude/agents/` |
| [model-pin-check](keeping-up-with-models/model-pin-check.md) | Flags model names that are an alias or an unlisted name instead of an exact version, fallbacks included | `cp keeping-up-with-models/model-pin-check.md ~/.claude/agents/` |
| [new-model-rerun](keeping-up-with-models/new-model-rerun.md) | Applies your switch rule to old and new results and says KEEP, SWITCH, INCONCLUSIVE or NOT COMPARABLE, and flags a rule written after the results | `cp keeping-up-with-models/new-model-rerun.md ~/.claude/agents/` |

## Handoffs between agents

Check that what one agent was told is what the next one acts on.

| Agent | What it does | Install |
|---|---|---|
| [relay-receipts](handoffs-between-agents/relay-receipts.md) | Checks an instruction reached everyone who needs it | `cp handoffs-between-agents/relay-receipts.md ~/.claude/agents/` |
| [worker-brief-builder](handoffs-between-agents/worker-brief-builder.md) | Drafts a complete brief for another agent and says NOT READY when a part is missing | `cp handoffs-between-agents/worker-brief-builder.md ~/.claude/agents/` |
| [worker-report-check](handoffs-between-agents/worker-report-check.md) | Checks a worker's report for missing parts and claims with no output behind them | `cp handoffs-between-agents/worker-report-check.md ~/.claude/agents/` |

## Rules and guardrails

The rules for how work is checked, accepted and released.

| Agent | What it does | Install |
|---|---|---|
| [fresh-eyes-reviewer](rules-and-guardrails/fresh-eyes-reviewer.md) | Reviews work from the work and your criteria alone, never the author's reasoning | `cp rules-and-guardrails/fresh-eyes-reviewer.md ~/.claude/agents/` |
| [release-gate](rules-and-guardrails/release-gate.md) | Labels each item SENDABLE or BLOCKED before anything for an outside reader goes out | `cp rules-and-guardrails/release-gate.md ~/.claude/agents/` |
| [defect-triage](rules-and-guardrails/defect-triage.md) | Turns a list of problems into fix-now, your decision and your action | `cp rules-and-guardrails/defect-triage.md ~/.claude/agents/` |
| [done-claim-check](rules-and-guardrails/done-claim-check.md) | Marks each "done" claim VERIFIED, UNVERIFIED or CONTRADICTED against pasted evidence | `cp rules-and-guardrails/done-claim-check.md ~/.claude/agents/` |
| [fail-closed-check](rules-and-guardrails/fail-closed-check.md) | Treats anything skipped or not run as a failure, never a pass | `cp rules-and-guardrails/fail-closed-check.md ~/.claude/agents/` |

## Product and engineering

Decide what to build, and keep the shared facts current.

| Agent | What it does | Install |
|---|---|---|
| [score-before-build](product-and-engineering/score-before-build.md) | Scores a task on need, ease and outcome and recommends parking the low scorers | `cp product-and-engineering/score-before-build.md ~/.claude/agents/` |
| [company-brain](product-and-engineering/company-brain.md) | Checks the shared facts your agents rely on exist and are current before a task starts | `cp product-and-engineering/company-brain.md ~/.claude/agents/` |

## Go-to-market

The first topic: outbound work, replies and results.

| Agent | What it does | Install |
|---|---|---|
| [source-backed-opener](go-to-market/source-backed-opener.md) | Drafts a cold-email opener only from a real article, or holds the lead | `cp go-to-market/source-backed-opener.md ~/.claude/agents/` |
| [send-guard](go-to-market/send-guard.md) | Flags a draft with the wrong recipient, greeting or signature as BLOCKED | `cp go-to-market/send-guard.md ~/.claude/agents/` |
| [reply-desk](go-to-market/reply-desk.md) | Sorts replies, drafts answers for you to approve, flags a clear no as STOP and drafts nothing | `cp go-to-market/reply-desk.md ~/.claude/agents/` |
| [signal-to-approval-router](go-to-market/signal-to-approval-router.md) | Turns a buying signal into a message you approve or edit | `cp go-to-market/signal-to-approval-router.md ~/.claude/agents/` |
| [closed-loop-scorecard](go-to-market/closed-loop-scorecard.md) | Compares results against a control group so you learn what works | `cp go-to-market/closed-loop-scorecard.md ~/.claude/agents/` |
| [fake-quote-check](go-to-market/fake-quote-check.md) | Checks every quote in a draft against the source text | `cp go-to-market/fake-quote-check.md ~/.claude/agents/` |
| [auto-reply-filter](go-to-market/auto-reply-filter.md) | Labels machine-sent messages so you can keep them out of your reply queue | `cp go-to-market/auto-reply-filter.md ~/.claude/agents/` |

## What these agents add

Each agent adds three things beyond a plain prompt:

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

MIT. Provided as is, with no warranty or support. Check each card's `tools:` line before you install it: most agents here only read, but anything that lists more can act on your project. The examples are synthetic.

## Changelog

- 0.6.0: Added ai-made-test-sets (3), model-pin-check, new-model-rerun, worker-brief-builder, worker-report-check; send-guard and reply-desk descriptions now say "flags".
- 0.5.0: Folders renamed by the problem they solve; added make-ai-understand-you (3 new) and ai-judges-ai (3 new, plus judge-before-send renamed judge-before-ship).
- 0.4.0: Six agents on rules and checks.
- 0.3.0: Three agents on keeping work in order.
- 0.2.0: Four agents on quality and spend.
- 0.1.0: First release, six outbound agents.
