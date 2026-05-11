# 2-Hour Consolidated Hackathon Plan (Proctor Guide)

## Mission

Keep teams moving to a demoable outcome in 120 minutes. Protect test time, prevent over-scope, and unblock quickly.

Primary success target:
- Every team leaves with a working app flow plus 2 passing Playwright tests (happy + negative).

---

## Session Timeline and Checkpoints

| Time | Expected State | Red Flag | Proctor Action |
|---|---|---|---|
| 0:10 | Use case selected, plan prompts generated | Still debating stacks/features | Force one scenario and one endpoint |
| 0:45 | Frontend and API connected | UI only, no API response visible | Simplify to plain form + single POST |
| 1:00 | Validation + fixtures ready | No reusable test data | Create 1 valid + 2 invalid fixtures immediately |
| 1:30 | Happy-path Playwright test passing | Playwright not running yet | Pair-drive setup and run one starter spec |
| 1:50 | Negative-path test passing | Only happy path or flaky tests | Narrow to one failure case and stabilize locators |
| 2:00 | Demo rehearsed, clean run | Still coding new features | Stop coding and force final run + talk track |

---

## Operating Rules for the 2-Hour Format

1. Protect the timeline aggressively.
2. Intervene after 8-10 minutes of repeated blockage.
3. Prefer simplification over re-architecture.
4. No net-new scope after 1:50.

---

## Fast Intervention Playbook

## A) Team is stuck in setup (first 30 minutes)

Symptoms:
- Environment issues, package install loops, no app scaffold yet

Actions:
- Move them to the simplest path in their current stack
- Skip non-essential tooling and styling
- Get one route and one form working first

Prompt to give:
"Generate the minimal frontend + POST /validate endpoint for this stack with no extras."

---

## B) Team over-scopes features (any time)

Symptoms:
- Wants database/auth/multi-page UX before first passing test

Actions:
- Enforce scope lock: one use case, one form, one endpoint, 2-3 rules
- Park ideas in a "stretch" list, do not build now

Prompt to give:
"Refactor this plan to a 2-hour MVP with only core validation and testability."

---

## C) Team cannot get Playwright stable (1:00-1:50)

Symptoms:
- Failing selectors, unclear assertions, timing confusion

Actions:
- Switch to accessible locators only (`getByRole`, `getByLabel`, `getByText`)
- Reduce to one deterministic happy path, then one deterministic negative case
- Validate expected text from fixtures before writing assertions

Prompt to give:
"Rewrite this test using accessible locators and exact assertions for success/error states."

---

## D) Team behind at 1:30

Required triage plan:
1. Get one happy-path test passing first.
2. Add one quick negative case (missing required field).
3. Skip deeper scenarios and polish.

---

## E) Team behind at 1:50

Hard stop actions:
1. Freeze feature work.
2. Keep only passing path + one failing validation path.
3. Prepare 3-minute demo from what works now.

---

## What to Ask During Check-ins

Use these quick checks:
- "Can you show one valid submission working now?"
- "Which fixture powers your negative-path test?"
- "Are both tests deterministic if run twice?"
- "What exact 3-step demo will you show at the end?"

If answers are unclear, reset them to the minimal path.

---

## Demo Enforcement (Last 10 Minutes)

At 1:50, tell every team:
1. Stop coding.
2. Restart app once.
3. Run tests once.
4. Rehearse story: app flow -> happy test -> negative test -> Copilot moment.

---

## Success Criteria for This Short Format

Minimum successful outcome:
- App flow works end-to-end
- 2 validation rules implemented
- 2 Playwright tests passing (happy + negative)
- Team can deliver a clear 3-5 minute demo

Strong outcome:
- Tests use accessible locators and clear assertions
- Team can explain one failure they debugged with Copilot
