# Agent database: work with AI without being an AI expert

<p align="center">
  <img src="assets/readme-hero.gif" width="480" alt="Agent database: work with AI without being an AI expert. 36 agents in 8 topics, plus 3 rules and 2 hooks. Free, MIT license, for Claude Code. Topics: Make AI understand you (4 agents), AI judges AI (4), AI-made test sets (3), Keeping up with new models (4), Handoffs between agents (3), Rules and guardrails (5, plus 3 rules and 2 hooks), Product and engineering (6), Go-to-market (7). An orange highlight steps through each topic. Founder photo, bottom left. Copy an agent into ~/.claude/agents/">
</p>


A free database of agents for Claude Code. Each agent encodes a checklist for its field, so you can check AI work against a clear checklist without a deep understanding of how AI works. Topics so far include: how to make AI understand you, AI judging AI, AI-made test sets, keeping up with new models, handoffs between agents, rules and guardrails, product and engineering, and go-to-market. More topics follow.

## Install

Pick an agent, copy its file into `~/.claude/agents/`, then ask Claude Code to use it by name:

```
mkdir -p ~/.claude/agents && cp make-ai-understand-you/prompt-intent-brief.md ~/.claude/agents/
```

Or install a whole folder: `mkdir -p ~/.claude/agents && cp make-ai-understand-you/*.md ~/.claude/agents/` (run from the repo folder). Read an agent file before you install it, and review everything an agent produces before it goes out.

## Make AI understand you

Say what you mean once, so the AI builds the right thing the first time.

| Agent | What it does | Install |
|---|---|---|
| [prompt-intent-brief](make-ai-understand-you/prompt-intent-brief.md) | Turns a vague request into a short brief and states the intent it infers in one line, for you to correct | `cp make-ai-understand-you/prompt-intent-brief.md ~/.claude/agents/` |
| [mam](make-ai-understand-you/mam.md) | MAM (Metacognitive Alignment Matrix): checks what you and the AI each know, and only think they know, about a task, then asks the questions that situation needs before anything is built | `cp make-ai-understand-you/mam.md ~/.claude/agents/` |
| [plan-reality-audit](make-ai-understand-you/plan-reality-audit.md) | Tags every claim in a plan Known, Reasoned, Assumed or Unknown, lists the hidden work and marks it RISKY or UNREALISTIC when it is | `cp make-ai-understand-you/plan-reality-audit.md ~/.claude/agents/` |
| [decision-batcher](make-ai-understand-you/decision-batcher.md) | Drafts your real decisions as one batch, with a recommendation | `cp make-ai-understand-you/decision-batcher.md ~/.claude/agents/` |

## AI judges AI

Let an AI judge another AI's work against a rubric you wrote, so you label less by hand.

| Agent | What it does | Install |
|---|---|---|
| [llm-judge-rubric-builder](llm-judges-and-evals/llm-judge-rubric-builder.md) | Turns your goal into a weighted rubric with 0, half and 1 anchors | `cp llm-judges-and-evals/llm-judge-rubric-builder.md ~/.claude/agents/` |
| [llm-judge-before-ship](llm-judges-and-evals/llm-judge-before-ship.md) | Marks an output REWRITE below the pass bar and HOLD after two failed rewrites | `cp llm-judges-and-evals/llm-judge-before-ship.md ~/.claude/agents/` |
| [prompt-vs-judge-alignment-check](llm-judges-and-evals/prompt-vs-judge-alignment-check.md) | Finds where the writer's instructions and the judge's questions differ | `cp llm-judges-and-evals/prompt-vs-judge-alignment-check.md ~/.claude/agents/` |
| [llm-judge-agreement-check](llm-judges-and-evals/llm-judge-agreement-check.md) | Compares three judges' scores and points to the one to fix | `cp llm-judges-and-evals/llm-judge-agreement-check.md ~/.claude/agents/` |

## AI-made test sets

Test your prompts and agents without labelling everything yourself. Real items are labelled only from recorded outcomes you supply, and any label that came from the model being tested is left out. A few made-up bad cases are added and marked AUTHORED.

| Agent | What it does | Install |
|---|---|---|
| [eval-test-set-maker](eval-test-sets/eval-test-set-maker.md) | Proposes an eval test set whose labels come from recorded outcomes, and leaves out labels that came from the model under test | `cp eval-test-sets/eval-test-set-maker.md ~/.claude/agents/` |
| [eval-pass-and-fail-check](eval-test-sets/eval-pass-and-fail-check.md) | Checks a test passes good inputs and fails bad ones, to catch a test that passes by luck | `cp eval-test-sets/eval-pass-and-fail-check.md ~/.claude/agents/` |
| [api-mock-drift-check](eval-test-sets/api-mock-drift-check.md) | Compares a fake copy of an outside service with a real sample and lists what changed | `cp eval-test-sets/api-mock-drift-check.md ~/.claude/agents/` |

## Keeping up with new models

Compare models fairly and watch the bill.

| Agent | What it does | Install |
|---|---|---|
| [prompt-and-model-ab-test](llm-models-and-costs/prompt-and-model-ab-test.md) | Compares two models or prompts on the same cases, or says there is too little data | `cp llm-models-and-costs/prompt-and-model-ab-test.md ~/.claude/agents/` |
| [api-cost-brake](llm-models-and-costs/api-cost-brake.md) | Compares usage with your caps and reports STOP at 95 percent | `cp llm-models-and-costs/api-cost-brake.md ~/.claude/agents/` |
| [llm-model-pin-check](llm-models-and-costs/llm-model-pin-check.md) | Flags model names that are an alias or an unlisted name instead of an exact version, fallbacks included | `cp llm-models-and-costs/llm-model-pin-check.md ~/.claude/agents/` |
| [new-llm-model-rerun](llm-models-and-costs/new-llm-model-rerun.md) | Applies your switch rule to old and new results and says KEEP, SWITCH, INCONCLUSIVE or NOT COMPARABLE, and flags a rule written after the results | `cp llm-models-and-costs/new-llm-model-rerun.md ~/.claude/agents/` |

## Handoffs between agents

Check that what one agent was told is what the next one acts on.

| Agent | What it does | Install |
|---|---|---|
| [agent-relay-receipts](multi-agent-handoffs/agent-relay-receipts.md) | Checks an instruction reached everyone who needs it | `cp multi-agent-handoffs/agent-relay-receipts.md ~/.claude/agents/` |
| [subagent-brief-builder](multi-agent-handoffs/subagent-brief-builder.md) | Drafts a complete brief for another agent and says NOT READY when a part is missing | `cp multi-agent-handoffs/subagent-brief-builder.md ~/.claude/agents/` |
| [subagent-report-check](multi-agent-handoffs/subagent-report-check.md) | Checks a worker's report for missing parts and claims with no output behind them | `cp multi-agent-handoffs/subagent-report-check.md ~/.claude/agents/` |

## Rules and guardrails

The rules for how work is checked, accepted and released.

| Agent | What it does | Install |
|---|---|---|
| [fresh-eyes-reviewer](claude-md-rules-and-guardrails/fresh-eyes-reviewer.md) | Reviews work from the work and your criteria alone, never the author's reasoning | `cp claude-md-rules-and-guardrails/fresh-eyes-reviewer.md ~/.claude/agents/` |
| [release-gate](claude-md-rules-and-guardrails/release-gate.md) | Labels each item SENDABLE or BLOCKED before anything for an outside reader goes out | `cp claude-md-rules-and-guardrails/release-gate.md ~/.claude/agents/` |
| [bug-triage](claude-md-rules-and-guardrails/bug-triage.md) | Turns a list of problems into fix-now, your decision and your action | `cp claude-md-rules-and-guardrails/bug-triage.md ~/.claude/agents/` |
| [agent-done-claim-check](claude-md-rules-and-guardrails/agent-done-claim-check.md) | Marks each "done" claim VERIFIED, UNVERIFIED or CONTRADICTED against pasted evidence | `cp claude-md-rules-and-guardrails/agent-done-claim-check.md ~/.claude/agents/` |
| [test-fail-closed-check](claude-md-rules-and-guardrails/test-fail-closed-check.md) | Treats anything skipped or not run as a failure, never a pass | `cp claude-md-rules-and-guardrails/test-fail-closed-check.md ~/.claude/agents/` |

Copy-paste rules for your `CLAUDE.md` (not agents; paste the text in the box):

| Rule | What it does |
|---|---|
| [fix-never-report](claude-md-rules-and-guardrails/rules/fix-never-report.md) | Fix and check a problem; only real decisions and owner-only steps come back to you |
| [claim-is-not-evidence](claude-md-rules-and-guardrails/rules/claim-is-not-evidence.md) | A "done" statement needs evidence next to it, or it is marked UNVERIFIED |
| [reproduce-before-report](claude-md-rules-and-guardrails/rules/reproduce-before-report.md) | A finding is reproduced against the real code or data before it is reported |

Hook patterns (small scripts you copy and test first; see [the hooks guide](claude-md-rules-and-guardrails/hooks/README.md)):

| Hook | What it does |
|---|---|
| [stop-gate](claude-md-rules-and-guardrails/hooks/stop-gate.py) | A Stop hook that keeps Claude working while your check command fails; fails closed |
| [secret-scan-before-commit](claude-md-rules-and-guardrails/hooks/secret-scan-before-commit.sh) | A git pre-commit hook that refuses a commit adding a secret-shaped line |

## Product and engineering

Decide what to build, and keep the shared facts current.

| Agent | What it does | Install |
|---|---|---|
| [rice-score-before-build](product-and-engineering/rice-score-before-build.md) | Scores a task on need, ease and outcome and recommends parking the low scorers | `cp product-and-engineering/rice-score-before-build.md ~/.claude/agents/` |
| [gtm-context-company-brain](product-and-engineering/gtm-context-company-brain.md) | Checks the shared facts your agents rely on exist and are current before a task starts | `cp product-and-engineering/gtm-context-company-brain.md ~/.claude/agents/` |
| [spec-to-acceptance-tests](product-and-engineering/spec-to-acceptance-tests.md) | Turns a feature description into numbered acceptance tests and flags what cannot be checked | `cp product-and-engineering/spec-to-acceptance-tests.md ~/.claude/agents/` |
| [code-review-brief](product-and-engineering/code-review-brief.md) | Builds the brief for an independent code review from the change and your criteria only | `cp product-and-engineering/code-review-brief.md ~/.claude/agents/` |
| [release-readiness-check](product-and-engineering/release-readiness-check.md) | Marks a release READY only if every checklist item has proof | `cp product-and-engineering/release-readiness-check.md ~/.claude/agents/` |
| [claude-md-rules-check](product-and-engineering/claude-md-rules-check.md) | Flags conflicting, repeated, vague or stale rules in your CLAUDE.md | `cp product-and-engineering/claude-md-rules-check.md ~/.claude/agents/` |

## Go-to-market

The first topic: outbound work, replies and results.

| Agent | What it does | Install |
|---|---|---|
| [cold-email-opener-from-source](gtm-and-outbound/cold-email-opener-from-source.md) | Drafts a cold-email opener only from a real article, or holds the lead | `cp gtm-and-outbound/cold-email-opener-from-source.md ~/.claude/agents/` |
| [outbound-send-guard](gtm-and-outbound/outbound-send-guard.md) | Flags a draft with the wrong recipient, greeting or signature as BLOCKED | `cp gtm-and-outbound/outbound-send-guard.md ~/.claude/agents/` |
| [outbound-reply-desk](gtm-and-outbound/outbound-reply-desk.md) | Sorts replies, drafts answers for you to approve, flags a clear no as STOP and drafts nothing | `cp gtm-and-outbound/outbound-reply-desk.md ~/.claude/agents/` |
| [buying-signal-router](gtm-and-outbound/buying-signal-router.md) | Turns a buying signal into a message you approve or edit | `cp gtm-and-outbound/buying-signal-router.md ~/.claude/agents/` |
| [outbound-ab-test-scorecard](gtm-and-outbound/outbound-ab-test-scorecard.md) | Compares results against a control group so you learn what works | `cp gtm-and-outbound/outbound-ab-test-scorecard.md ~/.claude/agents/` |
| [fake-quote-check](gtm-and-outbound/fake-quote-check.md) | Checks every quote in a draft against the source text | `cp gtm-and-outbound/fake-quote-check.md ~/.claude/agents/` |
| [ooo-auto-reply-filter](gtm-and-outbound/ooo-auto-reply-filter.md) | Labels machine-sent messages so you can keep them out of your reply queue | `cp gtm-and-outbound/ooo-auto-reply-filter.md ~/.claude/agents/` |

## How Namarix runs Claude Code

Practice cards from how Namarix runs its own sales, lead and AI work. Each step has an output you can check. No result numbers are published for them yet.

| Card | What it covers | Install |
|---|---|---|
| [connect-gtm-tools-one-workflow](how-namarix-runs-claude-code/connect-gtm-tools-one-workflow.md) | Connect your CRM, enrichment tool and sequencer into one workflow with one owner per record and per token | `cp how-namarix-runs-claude-code/connect-gtm-tools-one-workflow.md ~/.claude/agents/` |
| [design-agent-workflow-for-gtm](how-namarix-runs-claude-code/design-agent-workflow-for-gtm.md) | Design an AI agent for a repeating GTM job with its sources, tools, review limit and spend cap set first | `cp how-namarix-runs-claude-code/design-agent-workflow-for-gtm.md ~/.claude/agents/` |
| [plan-answer-engine-citations](how-namarix-runs-claude-code/plan-answer-engine-citations.md) | Plan content so AI assistants name your client when buyers ask | `cp how-namarix-runs-claude-code/plan-answer-engine-citations.md ~/.claude/agents/` |
| [gates-hooks](how-namarix-runs-claude-code/gates-hooks.md) | Make a test gate report only verified-green or not-green | `cp how-namarix-runs-claude-code/gates-hooks.md ~/.claude/agents/` |
| [worktrees](how-namarix-runs-claude-code/worktrees.md) | Run parallel AI sessions in separate git worktrees without collisions | `cp how-namarix-runs-claude-code/worktrees.md ~/.claude/agents/` |
| [session-roles](how-namarix-runs-claude-code/session-roles.md) | Split planner and builder AI sessions so each decision has one owner | `cp how-namarix-runs-claude-code/session-roles.md ~/.claude/agents/` |
| [context-cost-rule](how-namarix-runs-claude-code/context-cost-rule.md) | Decide when to do a change yourself and when to delegate it, and how to review it | `cp how-namarix-runs-claude-code/context-cost-rule.md ~/.claude/agents/` |
| [codex-worker](how-namarix-runs-claude-code/codex-worker.md) | Run Codex as a worker under Claude Code: brief, review, retry, take over | `cp how-namarix-runs-claude-code/codex-worker.md ~/.claude/agents/` |
| [build-review-test](how-namarix-runs-claude-code/build-review-test.md) | Build, review and test in a loop until every layer is green | `cp how-namarix-runs-claude-code/build-review-test.md ~/.claude/agents/` |
| [api-cost-discipline](how-namarix-runs-claude-code/api-cost-discipline.md) | Keep paid API work inside a budget with small tests first | `cp how-namarix-runs-claude-code/api-cost-discipline.md ~/.claude/agents/` |

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

MIT. Provided as is, with no warranty or support. Check each card's `tools:` line before you install it: most agents here only read, but anything that lists more can act on your project. The hook scripts run on your machine, so read them and test them first. The examples are synthetic.

## Changelog

- 0.9.0: Folders and agents renamed to words GTM engineering teams already use (for example go-to-market is now gtm-and-outbound, send-guard is now outbound-send-guard, reply-desk is now outbound-reply-desk); the 10 how-namarix-runs-claude-code cards added; mam added. Descriptions kept, with one or two familiar words added.
- 0.7.0: Added three copy-paste rules and two hook patterns to rules-and-guardrails; spec-to-acceptance-tests, code-review-brief, release-readiness-check and claude-md-rules-check to product-and-engineering.
- 0.6.0: Added ai-made-test-sets (3), llm-model-pin-check, new-llm-model-rerun, subagent-brief-builder, subagent-report-check; outbound-send-guard and outbound-reply-desk descriptions now say "flags".
- 0.5.0: Folders renamed by the problem they solve; added make-ai-understand-you (3 new) and ai-judges-ai (3 new, plus judge-before-send renamed llm-judge-before-ship).
- 0.4.0: Six agents on rules and checks.
- 0.3.0: Three agents on keeping work in order.
- 0.2.0: Four agents on quality and spend.
- 0.1.0: First release, six outbound agents.
