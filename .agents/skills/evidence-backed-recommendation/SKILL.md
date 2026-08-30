---
name: evidence-backed-recommendation
description: "Require a current baseline, relevant internal and external evidence, counterevidence, economics, and a bounded test before making a consequential Ace recommendation. Use when someone asks for strategy, growth, monetization, product, hiring, operations, finance, content, social, vendor, or technical recommendations that could consume meaningful time or money or affect a client, account, employee, or production system. This read-only workflow preserves every existing approval gate and verifies the decision against the current named authority."
---

# Evidence-backed recommendation

Allow a consequential Ace recommendation only after it is compared with the
current baseline, tested against counterevidence, and tied to the business
result that matters. When the proof is incomplete, return a bounded experiment
instead of presenting a hypothesis as the answer.

## Load

Read the target repository's `AGENTS.md`, `BOUNDARY.md` and
`SOURCES_OF_TRUTH.md` when present. Load the authority for the exact decision
and the relevant current Ace baseline before using public examples.

## Evidence classes

Keep these classes separate:

1. **Current internal authority:** live Ace revenue, cost, client, account,
   capacity, retention, quality or operating evidence from the named source.
2. **Primary external evidence:** current first-party documentation, audited
   results, research, laws, platform rules or directly measured case data.
3. **Observed public behavior:** a competitor, creator or company visibly uses
   a tactic, without proof of its economics or causal effect.
4. **Anecdote or assumption:** self-reported examples, agency marketing,
   unsourced benchmarks or a plausible theory.

Observed behavior and anecdotes are discovery leads. One competitor, public
profile, article, case study or anecdote never proves that Ace should adopt the
same method.

## Workflow

1. Define the exact decision, owner, stakes and success measure. Use the real
   business outcome: contribution profit, retained revenue, conversion,
   quality, time saved, risk reduced or another decision-relevant measure—not
   views, followers, activity or gross revenue by default.
2. Establish the current baseline and the do-nothing option from the named
   authority. Record the time window, coverage, freshness and definitions. If
   a critical source is unavailable, name it instead of silently substituting
   weaker evidence.
3. Inspect all material evidence already available to Ace before relying on a
   public example. Include costs, labor, capacity, retention, refunds, churn,
   attribution and downstream effects when they could change the answer.
4. Look deliberately for disconfirming evidence. Test at least one credible
   competing explanation and compare at least one viable alternative with the
   current baseline.
5. Run the causal check. A person using a tactic does not prove the tactic made
   money. A metric changing after an action does not prove attribution. State
   what is confirmed, inferred, anecdotal and unavailable.
6. Compare economics at the correct grain. Use incremental contribution profit
   or the closest verified measure after platform fees, labor, commissions,
   refunds, cannibalization and opportunity cost when money is the goal.
7. Choose exactly one evidence mode:
   - **Recommend:** the evidence is strong enough to prefer one option over the
     current baseline. State the expected benefit, strongest supporting proof,
     meaningful downside and remaining uncertainty.
   - **Test only:** the idea is plausible but causal, economic or Ace-specific
     proof is incomplete. Define a control or baseline, bounded audience or
     scope, duration, measures, owner, stop rule and keep rule.
   - **No recommendation:** a critical source, safe comparison or bounded test
     is unavailable. State the smallest evidence needed next.
8. Lead with the decision in plain language. Include only the evidence needed
   to understand it, plus the important unassessed data. Never hide conflicting
   evidence to make the answer cleaner.

## Boundaries

- **Approval boundary:** this workflow prepares a decision only; every existing
  approval requirement still controls the resulting action.
- **Authoritative verification:** verify the baseline and material outcome
  measures against the current named authority before calling the evidence
  complete.
- This is a read-only decision workflow. It does not authorize a purchase,
  payment, hire, candidate action, production change, publish, message, access
  change, deletion, contract or other consequential write.
- Do not move private finance, candidate, credential, legal, creator or client
  evidence into a broader repository or output. Aggregate or redact it when the
  audience does not need the underlying rows.
- Do not invent a benchmark, conversion rate, cost, forecast or causal claim.
  If the relevant data cannot be verified, use `test only` or
  `no recommendation`.
- A recommendation made earlier in the conversation is not evidence. Reopen
  the decision when new facts contradict it and say plainly that the answer
  changed.

## Quality Gate

- The current baseline and do-nothing option were assessed.
- Internal authoritative evidence was checked before external examples when it
  was available and permitted.
- At least one counterexample, competing explanation or meaningful alternative
  was evaluated.
- Observed use was not presented as proof of performance or causation.
- Economics use the correct net or contribution measure, or the missing inputs
  are explicit.
- The output is visibly one of `recommend`, `test only` or `no recommendation`.
- A test-only answer defines its control, scope, duration, measures and
  stop/keep rules.
- Important unavailable or unassessed data is named.
- Evaluate the cases in [the behavior contract](references/evaluation-cases.json).
