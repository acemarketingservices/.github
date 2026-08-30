# Recovery and Verification Playbook

Use this reference when the first execution path does not prove the requested
outcome. The objective is progress with bounded risk, not endless retries.

## Attempt Record

For every repair attempt retain, in the host's plan or task state:

- failing step and last known good state;
- observed error or missing proof;
- root-cause hypothesis;
- next action and why it differs from the prior attempt;
- expected evidence;
- actual evidence and resulting state.

Keep records short, redact sensitive values, and update the existing task state
instead of creating a shadow tracker.

The attempt record is internal continuity state. Do not copy it into routine
commentary or the final answer unless the user explicitly asks for the history.

Normalize each observation to `status`, `summary`, `evidence`, and
`next_safe_action` even when the underlying tool returns unstructured output.
That makes a restart or handoff useful without replaying the entire transcript.

## State Model

Use explicit state for each step:

```text
READY -> EXECUTING -> VERIFYING -> COMPLETE
             ^            |
             |            v
             +-------- REPAIRING

WAITING_USER or WAITING_EXTERNAL pauses only the affected branch.
FAILED means the bounded loop ended without proof; it is not a synonym for blocked.
```

A step enters `COMPLETE` only with its done proof. When a paused branch resumes,
refresh its current state before using an old plan or repeating an action.

## User Interruption Threshold

Exhaust supported automation, narrower searches, current context, and equivalent
authoritative paths before escalating. Interrupt only for a user-only input or
interaction, a material decision, a controlling approval or safety boundary, or
a remaining path whose new paid cost, scope, or multiple hours of manual work is
disproportionate to the outcome. A difficult ordinary investigation is not a
blocker.

When escalation is necessary, ask for one exact action. Do not attach the
attempt record, a source inventory, or a progress recap unless it is necessary
for that decision.

## Failure Classes

| Class | Signals | Next safe action | Stop condition |
|---|---|---|---|
| Transient | timeout, rate limit, temporary network/provider error | bounded backoff, refresh current state, retry once with the same idempotency key | provider remains unavailable or retry budget is spent |
| Execution defect | deterministic test, build, validation, or runtime failure | narrow to the smallest failing unit, form a cause hypothesis, patch, rerun focused proof, then the broader check | repair would leave scope or violate a constraint |
| Wrong tool or path | unsupported operation, missing tool, mismatched interface | inspect current capability, select another supported official path, translate the input shape | no authorized supported path exists |
| Evidence gap | action may have worked but completion proof is missing | query the authoritative target or end-user surface; preserve unknown until readback | source is unavailable and no equal authority exists |
| Missing input | value or choice appears absent | search current context, repository, and authorized source; infer only low-risk reversible details | the missing choice materially changes outcome, risk, recipient, or authority |
| Authentication or permission | expired session, OAuth, passkey, CAPTCHA, denied scope | use documented existing-session or sign-in path; prepare everything around the gate | a user-only security interaction or access grant is required |
| Approval gate | next action sends, pays, publishes, deploys, deletes, changes access, or otherwise commits | prepare exact action and proof plan; continue unaffected work | user or controlling authority has not approved the exact action |
| Conflicting requirements | two instructions or sources cannot both control | apply instruction hierarchy and current source of truth; surface the smallest unresolved choice | choice would materially change the requested result |
| Source-of-truth drift | a repository fact disagrees with its named authority or two copies conflict | identify the controlling authority, repair bounded stale GitHub copies in scope, and add a recurrence check | authority remains genuinely ambiguous or repair would cross privacy or approval boundaries |
| Stale final candidate | target branch or volatile dependency changed before final proof | refresh, integrate current state, rerun focused checks, then run the final proof once | integration changes the authorized outcome or creates an unresolved conflict |
| Downstream residue | the defect is fixed but an old alert, message, issue, report, or copied fact remains misleading | resolve the stable locator, apply authorized cleanup, and read the exact target back | cleanup lacks exact authority or the target cannot be identified safely |
| Capability gap | available host cannot perform the necessary operation | search installed capabilities and official alternatives; adapt only reviewed behavior | no safe supported capability is available |

## Strategy Ladder

Move down this ladder only as needed:

1. Correct the input, command, or selected tool.
2. Refresh current state and retry a confirmed idempotent operation.
3. Narrow to the failing unit and test the root-cause hypothesis.
4. Use a different supported tool or authoritative read path.
5. Reconcile the current source of truth and repair stale bounded copies.
6. Refresh the final candidate against current branch and dependency state.
7. Replan the dependency order or isolate the blocked branch.
8. Request one exact user action or approval.

Do not rotate between equivalent commands merely to increase an attempt count.

## Evidence Strength

Use the strongest proof available for the outcome:

1. Authoritative external or end-user readback.
2. Deterministic acceptance test against the real output.
3. Reproducible build, validation, query, or rendered-artifact inspection.
4. Independent criteria-only review of the artifact or diff.
5. Agent reasoning or a success-shaped tool response.

Levels four and five cannot replace a stronger required source. A queued action,
configuration, HTTP success, commit, merge, or message draft proves only that
stage unless it is itself the requested outcome.

## Verification Separation

When proof requires judgment rather than a deterministic check:

- give the verifier the acceptance criteria and resulting artifact;
- omit implementation advocacy and the implementer's conclusion;
- ask for pass, fail, or unavailable with evidence for every criterion;
- return failures to repair without weakening the criteria.

Use a context-isolated verifier only when the host and repository permit it.
Otherwise perform a fresh verification pass that reopens the raw artifact and
criteria instead of relying on the execution narrative.

## Design Basis

This package adapts complementary MIT-licensed patterns reviewed on 2026-08-27:

- `broomva/harness-engineering` at `12d68503307a2843f29d7043adfdbc3045378723`:
  explicit setpoints, sensors, controllers, feedback, stability, and observable
  run state.
- `affaan-m/ECC` at `5eddf1a3ffd311423be2d4ba7d26f7209c91b033`:
  typed action/observation contracts, bounded retries, root-cause recovery, and
  completion-rate metrics.
- `JuliusBrussee/skills` at `8470b263d82579bd5b563b1e4e494472d3f0457f`:
  acceptance criteria, visible task state, audit artifacts, and separated review.
- `zhaono1/agent-playbook` at `be7a9d7d17593abd8cf029d51c87dbd5b445351e`:
  bounded learning candidates that require representative validation before
  durable behavior changes.

The source packages are not installed. This skill keeps their strongest generic
control ideas while adding operational failure classification, changed-strategy
repair, non-idempotent write protection, and continue-around-the-gate behavior.
