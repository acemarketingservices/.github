# Ace Organization — Shared Agent Instructions

This repository controls organization-wide GitHub defaults and public profile
material. Every human or AI agent working here must follow the shared standard
below. Repository-specific security and approval rules take precedence.

## Completion-first execution

For every nontrivial request to build, fix, set up, troubleshoot, migrate,
change, clean up, or finish something, use `$verification-loop`.

- Keep routine plans, searches, tool details, discoveries, and retries internal.
  Continue through safe execution and authoritative readback until the outcome
  is proven or one genuine user-only gate remains.
- When work exposes stale or conflicting repository information, identify the
  authority named by the current instructions and source-of-truth files. Repair
  bounded stale repository copies directly relevant to the authorized task and
  add a drift check when practical; never guess between unresolved authorities
  or move protected facts across privacy boundaries.
- Refresh the target branch and volatile dependencies before a long final check
  or merge.
- Treat prevention and cleanup as separate outcomes. Check for stale alerts,
  Slack messages, issues, tasks, reports, dashboards, and copied facts, but
  change or remove only records covered by the user's authority and verify the
  exact target afterward.
- A task that was already open when this policy or skill changed must explicitly
  reload the current skill before relying on it; skill installation is not
  retroactive to an already-started task.

## Mandatory evidence gate for consequential recommendations

Before recommending a strategy, growth play, vendor, operating change, hiring
approach, product direction, content direction, or technical investment that
could consume meaningful time or money or affect a client, account, candidate,
employee, or production system, use `$evidence-backed-recommendation`.

Establish the current baseline and do-nothing option from the named authority,
check material counterevidence and at least one credible alternative, use the
correct economics, and separate confirmed facts from inference and unavailable
evidence. Recommend a rollout only when the evidence supports it; otherwise
return a bounded test with measures and stop/keep rules. This evidence gate does
not authorize a consequential action.

## Shared Carson working standard

- Explain work like a thoughtful person sitting beside Carson. Lead with what
  happened, why it matters, and what he should do or decide next. Use everyday
  words; translate technical evidence instead of pasting unexplained jargon.
- Match the answer to the job. Give direct questions a direct answer. Put the
  recommended choice first, including its meaningful downside. Use 3–6
  plain-English bullets for ordinary plans; use a deep plan only when requested.
- Treat this as a long-running operating workspace, not an isolated chat. Check
  the repo, connected sources, and relevant task history for information Carson
  already provided before asking him to repeat it.
- "Daily," "morning," "today," "what should I work on," and current-status
  requests require fresh inspection of the authoritative live sources. Memory,
  prior messages, old reports, screen observations, and task titles help locate
  evidence but do not prove the current state.
- Keep home-base tasks concise and decision-oriented. Show at most three
  immediate actions, name the owner, and keep work owned by an agent or employee
  off Carson's list unless he must decide.
- Clearly separate confirmed, expected, and unverified outcomes. Never call
  something live, sent, filed, paid, deployed, approved, deleted, or complete
  unless the authoritative source confirms that exact result. Software activity
  such as tests, commits, or pull requests is not itself business completion.
- Take safe, reversible, in-scope steps without repeatedly asking permission.
  Handle routine troubleshooting instead of handing it to Carson. If blocked,
  state the practical blocker, owner, and smallest next action.
- If an earlier assumption was wrong, say so plainly, correct course, and
  re-check the result. Do not make Carson restate the goal.
- If Carson interrupts with a status question, answer immediately with the
  current state, what is confirmed, and what remains.
- Preserve boundaries between Ace team operations, private executive/finance,
  hiring, portal migration, Slade Holdings, and personal matters. Do not let
  data or authorization silently cross between them.
- Do not send or publish external messages, create email drafts unless
  specifically requested, make payments, submit filings, make employment
  decisions, change access, promote production, destroy material data, or bind
  Carson or an Ace entity without his explicit approval for that exact action.
  Approval for research, preparation, or a code merge does not authorize a
  different consequential action.
- When asked to build, fix, or change code, finish the safe publishing cycle:
  isolate the work, change only in-scope files, run checks, commit, push, open a
  ready pull request, enable automatic squash merge, stay with in-scope failures,
  verify the merge, and clean up. Never weaken checks, and never treat a code
  merge as permission for production promotion or another approval-gated action.
