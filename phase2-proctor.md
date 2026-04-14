# Build Phase 2 — Proctor Guide

## Your Role

During Phase 2, participants should already have a working app. Your job shifts from app setup to **helping them establish Playwright foundations** and keeping them from getting lost in tooling or flaky tests.

---

## Timeline Check-ins

| Time Into Phase | Where They Should Be | Red Flag |
|-----------------|----------------------|----------|
| 10 min | Have a Phase 2 plan and prompts saved | Still fixing major Phase 1 bugs |
| 30 min | Installing or configuring Playwright | Still debating whether to test at all |
| 50 min | Writing the first happy-path spec | Still stuck in setup or no spec file yet |
| 1 hour | Running and debugging the test | Test has never been run |
| 1.5 hours | One happy-path test passes consistently | No passing Playwright test |

---

## Common Issues

### Still Fixing Phase 1

If someone's Phase 1 isn't working yet:
- Help them get the minimum: form → API → response displayed
- Suggest simplifying: drop the frontend framework and use plain HTML + fetch
- Don't let them restart from scratch — fix what they have

### Playwright Setup Friction

Watch for people getting stuck on setup details:
- Browser install issues
- Not knowing which command runs the tests
- App and test runner not pointed at the same local URL
- Confusion about where specs should live

**Nudge:** "Don't optimize the config. Get Playwright running, generate one spec, and prove the happy path works."

### Brittle Selectors

The biggest time sink in this phase is fighting selectors that break immediately.

**Nudge:** "Use `getByRole`, `getByLabel`, and visible text first. Avoid deep CSS selectors unless there's no better option."

### Copilot Generating Inconsistent Tests

If Copilot is generating code that doesn't match their existing patterns:
- Use `#file` references to give Copilot context on existing code
- Remind them to review and adjust generated code, not just accept everything
- Ask them to paste the exact failure into chat instead of asking broad questions like "fix my test"

---

## When to Intervene

**Do intervene if:**
- Someone is stuck on a Phase 1 issue — help them fix it fast so they can move to Phase 2
- Someone has spent 15+ minutes without getting Playwright installed or a spec created
- Someone's selectors are obviously brittle and they keep retrying the same pattern
- Someone's app is broken and they don't realize it

**Don't intervene if:**
- They're learning through one or two test failures
- They're trying different assertion styles
- They're moving a little slowly but have a spec running

---

## Nudges

If someone doesn't know what to automate first:
> "Start with the most demoable success path: valid input goes in, a clear success result comes out."

If someone is fighting selectors:
> "Can Playwright find this by label, button text, or role instead of a long CSS selector?"

If someone is moving fast:
> "Great progress — start your negative-path test now so Phase 3 can be about deeper coverage and debugging."

---

## Phase 2 Success Criteria

At the end of Phase 2, each participant should have:
1. Playwright installed and runnable
2. One happy-path Playwright test passing
3. A basic understanding of how to debug selector, timing, or assertion failures

**It's OK if:** The test is simple, there is only one passing scenario, or the assertions are basic.

**It's not OK if:** They finish the phase without a passing Playwright test.
