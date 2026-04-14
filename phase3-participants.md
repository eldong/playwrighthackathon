# Build Phase 3 — Playwright Deepening (1.5 hours)

## Goal

You have a working app and at least one passing Playwright test. Phase 3 is about **deepening your Playwright coverage** so you leave with a stronger testing workflow, not just a single happy-path check.

---

## Step 1: Plan and Generate Your Prompts (10 min)

Same workflow as before — follow the **Copilot Workflow Guide** (`copilot-workflow-guide.md`):

1. Use **Plan agent** to describe which additional Playwright scenarios you want to automate
2. **Agent Mode** to break it into prompts
3. Have Copilot save them to `phase3-prompts.md`

---

## Step 2: Add a Negative-Path Test (25-30 min)

Write a Playwright test for a failed validation scenario.

**Examples:**
- Submit with a required field missing
- Enter an invalid amount or date
- Trigger a business-rule failure for your document type

**What to verify:**
- The form submits or blocks as expected
- The user sees a clear error state
- The right validation message appears on screen

> **Copilot tip:** *"Write a Playwright test for an invalid [document type] submission where [field] is missing. Assert that the validation error appears and the submission is treated as invalid."*

---

## Step 3: Add One Deeper Scenario (25-30 min)

Choose one richer workflow that makes your test suite more realistic.

**Good options:**
- File upload flow
- Alternate document type with different rules
- Backend failure or retry handling
- Mocked API response for a specific edge case

Pick **one** and finish it well.

> **Copilot tip:** *"Suggest one deeper Playwright scenario for this app that is realistic but still achievable in this session, then generate the test and any small app changes needed to support it."*

---

## Step 4: Improve Selectors and Assertions (15-20 min)

Review your tests and make them more stable and readable.

**What to improve:**
- Replace brittle selectors with `getByRole`, `getByLabel`, or clearer text-based locators
- Make assertions more specific
- Remove unnecessary waits or fragile timing assumptions

> **Copilot tip:** *"Review this Playwright spec and replace brittle selectors with more stable accessible locators. Explain why each change improves reliability."*

---

## Step 5: Debug a Failure with Trace or Screenshot Output (15-20 min)

Use Playwright's debugging tools as part of the learning experience.

**What to do:**
- Intentionally run a failing test or inspect a real failure
- Open the trace or screenshot output
- Ask Copilot to help you interpret what happened
- Fix the issue and re-run

> **Copilot tip:** *"This Playwright test failed. Based on the error and trace, help me understand what happened and how to make the test more reliable."*

---

## Optional Stretch Goals

If you finish early, choose one:

- Add unit tests for your validation logic
- Support multiple document types in the app
- Accept PDF uploads
- Build a dashboard or persistence layer
- Create Copilot customization files such as `.github/copilot-instructions.md`, `SKILL.md`, or `.agent.md`

---

## Checkpoint

By the end of Phase 3:
- [ ] You have a happy-path Playwright test
- [ ] You have a negative-path Playwright test
- [ ] You have one deeper Playwright scenario or debugging exercise completed
- [ ] You're ready to demo

**Start preparing your demo.** Think about:
- What's the best way to show your app in 5 minutes?
- What was the most impressive Copilot + Playwright moment?
- What did you learn about working with Copilot?
