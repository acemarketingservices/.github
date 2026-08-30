---
name: verification-loop
description: "Drive an authorized multi-step implementation or operational task through quiet execution, independent verification, source-of-truth repair, downstream cleanup, and changed-strategy recovery until the requested outcome is proven or no safe action remains. Use when handling a nontrivial build, fix, setup, troubleshooting, migration-execution, or other action request that requires multiple tool calls, retries, current-branch reconciliation, conflicting repository facts, or authoritative readback, especially when the user wants Codex to keep going, finish end to end, run autonomously, avoid running commentary, recover from blockers, or interrupt only for something the user must provide."
---

# Verification Loop

Own an authorized task through execution, proof, and recovery instead of
returning the first obstacle. Finish only when the requested outcome is proven
or every remaining path requires a specific user action or new authority.

The visible experience is completion-first: work quietly, keep the execution
record internal, and surface only the result or one genuine user gate.

## Start Contract

Before acting, identify:

- **Outcome:** the real-world or repository state the user needs.
- **Done proof:** the observable readback, test, artifact, or source that proves it.
- **Scope:** affected surfaces, non-goals, and the instructions that govern them.
- **Authority:** actions already allowed and actions requiring a separate gate.
- **Closure surfaces:** downstream alerts, messages, issues, tasks, reports, and
  copied facts that the task may make stale or misleading.
- **Stop conditions:** material ambiguity, safety boundary, cost limit, or unavailable
  authority that would make further action invalid.

Keep this contract implicit for simple work. For multi-step work, put it in the
host's durable plan or task-state mechanism so interruptions do not erase it.
Inspect available context and sources before asking the user to repeat an input.

## Loop Invariant

While the outcome is not proven and a safe in-scope action remains:

1. inspect the latest authoritative state;
2. take the next checkable action;
3. verify the result independently;
4. repair with a materially different strategy when proof fails; and
5. repeat without handing routine execution back to the user.

A plan, finding, attempted action, queued job, saved setting, passing command,
or prepared handoff is an intermediate state. Do not substitute it for the
requested result.

## Workflow

1. **Observe.** Read the current state, applicable instructions, source of truth,
   existing work, and tool capability. Treat memory and prior attempts as leads,
   not current proof.
2. **Plan the next checkable step.** Prefer the smallest reversible action that
   moves the outcome forward. Track dependencies and keep only one active step.
3. **Act.** Use the narrowest supported tool and preserve unrelated state. Do not
   turn research or preparation authority into permission for a consequential
   external action.
4. **Verify independently.** Check the result against the done proof. Prefer a
   deterministic command, authoritative query, provider readback, rendered
   artifact, or end-user surface over the agent's own assessment. When semantic
   review is necessary, run a fresh criteria-only review when the host permits it.
5. **Reconcile truth and closure.** If the task exposes stale or conflicting
   repository facts, identify the controlling authority, repair bounded stale
   GitHub copies that are authorized and directly relevant, and add a drift guard
   when practical. Inspect downstream closure surfaces and remove or correct only
   those records covered by the user's authority; otherwise hold the exact gate.
6. **Refresh before the expensive finish.** Immediately before a long final test,
   merge, or release candidate, refresh the target branch and other volatile
   dependencies. Rebase or replan first when they changed, then run the final proof
   once against the current candidate.
7. **Repair on failure.** Classify the failure, form one root-cause hypothesis,
   choose a materially different safe attempt, and record what new evidence that
   attempt should produce. Follow [the recovery playbook](references/recovery-playbook.md).
8. **Replan and repeat.** Return to Observe after each attempt. Keep unaffected
   work moving while an exact approval, login, or external dependency waits.
9. **Close honestly.** Mark complete only when every in-scope acceptance condition
   has proof. Otherwise report the exact remaining gate, its owner, the smallest
   action that clears it, and everything already finished around it.

## Repository Truth Repair

Do not leave a known GitHub fact wrong merely because the immediate code now
works. When a task discovers one stale source or two conflicting sources:

1. read the repository's current instructions and `SOURCES_OF_TRUTH.md`;
2. reopen the named live authority or highest-precedence current source;
3. compare scope, timestamp, identity, and definitions before choosing a winner;
4. repair every bounded stale repository copy directly relevant to the task when
   the request authorizes repository changes;
5. add or strengthen a deterministic drift check when the mismatch can recur; and
6. verify the corrected copy against the authority after merge.

Never average conflicting facts, let the newest file win without authority, or
copy protected facts across repository boundaries. If two sources both claim to
be authoritative and the instruction hierarchy does not resolve them, the
remaining choice is a genuine user gate. External providers, payments, messages,
access, production, employment, and legal records keep their separate approval
rules; this section grants only the repository repair already within scope.

## Downstream Cleanup

A root-cause fix and cleanup are separate acceptance conditions. Inventory any
incident alert, Slack message, issue, task, report, dashboard row, or copied fact
made misleading by the repaired defect. Preserve a stable locator such as a URL,
record ID, channel plus timestamp, or issue number whenever the source supports
one. If cleanup is authorized, perform it and read the exact target back. If it is
not authorized, state the one precise cleanup action awaiting approval instead of
calling the whole surface clean.

## Communication Gate

Do not narrate the loop by default. Plans, tool names, research summaries,
attempt histories, partial discoveries, and routine errors belong in internal
task state, not user-facing commentary.

Interrupt the user only when at least one of these is true:

- the next required input, identity choice, approval, credential interaction,
  passkey, CAPTCHA, or other security step can only come from the user;
- an unresolved ambiguity materially changes the recipient, business outcome,
  authority, safety, or irreversible effect;
- every safe path reaches a controlling approval, access, policy, or provider
  gate; or
- after trying supported automation, narrower searches, and equivalent sources,
  the only remaining path would add a material scope expansion, meaningful paid
  cost, or multiple hours of manual work disproportionate to the requested
  outcome.

"I have not found it yet," a tedious path, a tool error, or a normal five-to-
sixty-minute investigation is not a user gate. Keep working. When a genuine
gate exists, ask for one exact action or decision and include only the context
needed to make it.

Follow any host requirement to provide progress updates, but compress each
required update to one short outcome-focused sentence. Say whether work is
continuing and whether the user needs to act; omit the work diary. If the user
asks for status, answer directly and then resume unless the objective changed.

## Blocker Challenge

Before asking the user for help or calling the task blocked, answer:

1. Is this a routine transient, tool-choice, evidence, or execution failure?
2. Can current state or a missing input be discovered safely?
3. Is there another supported path that preserves the same authority boundary?
4. Can the failing unit be narrowed, repaired, or verified another way?
5. Can unrelated steps continue while this one waits?

Continue when any answer yields a safe next action. Ask only for the exact
decision, approval, credential interaction, or unavailable fact that no allowed
path can supply.

## Retry Contract

- Never repeat the same failed attempt without a changed condition or new evidence.
- For ordinary failures, try up to three materially different safe strategies when
  they exist. Stop earlier when risk, cost, or an explicit gate controls the step.
- A timeout or rate limit may be retried with bounded backoff through the host's
  wait mechanism; stay communicative during longer work.
- Before retrying a non-idempotent external write, read the target back. If its
  outcome is unknown, do not risk a duplicate.
- Never weaken the acceptance criteria, suppress a failing check, substitute a
  weaker source, or declare partial coverage complete to make the loop pass.
- Preserve evidence from the last known good state while repairing a later failure.

## Boundaries

- This skill improves persistence; it does not broaden the user's request,
  repository scope, tool permissions, or approval authority.
- Do not bypass authentication, CAPTCHA, passkeys, access controls, safety gates,
  branch protections, human review, or provider restrictions.
- Payments, external messages, publishing, production changes, access changes,
  destructive actions, legal filings, employment decisions, and comparable
  commitments retain their controlling approval rules.
- New user direction may replace the active objective. Reconcile it with the
  contract rather than continuing stale work.
- Do not expose credentials or sensitive source content in plans, attempt logs,
  errors, traces, or learning artifacts.

## Completion Report

Lead with the outcome. State the proof that matters, anything still unverified
that changes the result, and the one exact user action if one remains. When the
task is complete and no action remains, say so plainly. Do not include the plan,
tool list, source tour, attempt log, or a recap of everything completed unless
the user asks for it.

Explicitly distinguish the root-cause prevention, correction of stale repository
information, and cleanup of already-created downstream records. Do not say an
old alert, message, issue, report, or copied fact was removed merely because the
underlying defect can no longer recur.

After a repeated failure or correction reveals a reusable lesson, submit it to
the current approved learning workflow as a bounded candidate. Validate it on a
representative case before changing durable guidance; one success is not a rule.

## Quality Gate

- The start contract names an outcome and a proof source before consequential work.
- Every retry changes the hypothesis, method, condition, or evidence sought.
- The strongest available independent proof supports every completion claim.
- The final candidate was refreshed against current branch and dependency state
  before the expensive proof cycle.
- Every discovered source conflict is corrected, safely routed, or held at one
  exact authority decision; no known in-scope repository fact remains silently
  wrong.
- Prevention and downstream cleanup have separate proof.
- A genuine gate pauses only the affected step, not safe unaffected work.
- User-facing updates contain no routine play-by-play and no avoidable question.
- Final status clearly separates complete, partial, waiting, and unverified state.
- Evaluate the cases in [the behavior contract](references/evaluation-cases.json).
