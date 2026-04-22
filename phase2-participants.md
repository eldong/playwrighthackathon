# Build Phase 2 — Playwright Foundations (1.5 hours)

## Goal

By the end of this phase, you should have **Playwright installed and working** with a stable happy-path test, and ideally one negative-path test started (or completed) so Phase 3 can focus on deeper scenarios.

---

## Step 1: Validate Your Test Fixtures (5-10 min)

Before writing Playwright tests, confirm your fixture data from Phase 1 is ready.

**Quick checks:**
- You have at least one valid input and two invalid inputs
- Field names match your frontend/API exactly
- Expected results are clear (success vs specific validation error)
- Optional file-upload sample exists if you plan that scenario later

If fixtures are missing, create them now in a `test-data/` folder.

---

## Step 2: Plan and Generate Your Prompts (10 min)

Follow the **Copilot Workflow Guide** (`copilot-workflow-guide.md`) again:

1. Use **Plan agent** to plan your Phase 2 Playwright work — describe what you built in Phase 1 and what user flow you want to test
2. Switch to **Agent Mode** and break the plan into step-by-step prompts
3. Have Copilot save the prompts to a `phase2-prompts.md` file in your project

**Example Plan agent prompt:**
> "I have a working [use case] app with a [stack] frontend and API. The form submits data, the API validates it, and results display on screen. Create a plan for me to set up Playwright, create a first happy-path end-to-end test, and debug the likely issues."

---

## Step 3: Install and Configure Playwright (20-25 min)

Set up Playwright in your project and make sure you can run the test runner.

**What to do:**
- Install Playwright using the standard setup for your stack
- Add the generated config and example spec files
- Make sure your app can run locally while Playwright tests run against it
- Run the starter test once so you understand the workflow

> **Copilot tip:** *"Set up Playwright for this project, add the recommended config, and explain how to run the tests against my local app."*

---

## Step 4: Create Your First Happy-Path Test (25-30 min)

Write one end-to-end Playwright test that proves your app works for a valid submission.

**What to test:**
- Load the page
- Fill in the form with valid data
- Submit the form
- Verify the success result appears on screen

Focus on reliable selectors. Prefer accessible locators like `getByRole`, `getByLabel`, and visible text over fragile CSS selectors.

> **Copilot tip:** *"Write a Playwright test for a valid [document type] submission. Use accessible selectors and assert that the success result appears."*

---

## Step 5: Run, Debug, and Refine the Test (20-25 min)

Your first Playwright test probably won't pass on the first try. That's normal.

**What to do:**
- Run the test and read the failure output carefully
- Fix selectors, timing, or assertion issues
- Ask Copilot to explain why the test failed and suggest a better locator or assertion
- Re-run until the happy-path test passes consistently

> **Copilot tip:** *"This Playwright test is timing out when it clicks submit. Here is the error. Help me diagnose whether the issue is the selector, timing, or app behavior."*

---

## Step 6: Start Your Negative-Path Test Now (15-20 min)

Don't wait until Phase 3 if you have time. Add one negative-path test now while your selectors and fixture data are fresh.

**Pick one quick failure case:**
- Missing required field
- Invalid numeric value
- Invalid date/value format

**What to assert:**
- Validation error is visible
- Submission is treated as invalid
- Success state does not appear

> **Copilot tip:** *"Write a Playwright test for an invalid submission where [field] is missing. Assert the exact validation message and verify the success banner is not shown."*

---

## Step 7: Harden and Prepare for Phase 3 (10-15 min)

Pick the next two scenarios you want to automate in Phase 3:
- One **negative-path** test, such as missing required fields or invalid values
- One **deeper** scenario, such as file upload, alternate document type, backend failure handling, or mocked responses

Then do these quick setup tasks so Phase 3 starts fast:
- Save your current tests in a clean structure (`tests/happy-path/`, `tests/negative-path/`, etc.)
- Confirm fixtures are reusable and named clearly
- Capture one passing run (`npx playwright test --headed` optional) and verify report output
- Note known flaky selectors or timing pain points to fix first in Phase 3

> **Copilot tip:** *"Suggest two high-value Playwright scenarios for this app beyond the happy path, and help me choose one negative-path test and one deeper scenario."*

---

## Checkpoint

By now you should have:
- [ ] Playwright installed and runnable
- [ ] One happy-path Playwright test passing
- [ ] One negative-path test started (preferably passing)
- [ ] A basic understanding of selectors, assertions, and test failures
- [ ] A plan for one negative-path test and one deeper scenario in Phase 3

**If you're ahead of schedule:** Start a deeper scenario spike (for example: mocked API failure, file-upload path, or alternate document type).

**If you're behind:** Focus on one happy-path test passing and a clearly defined negative-path test plan. Don't chase deeper scenarios until that foundation is working.
