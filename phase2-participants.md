# Build Phase 2 — Playwright Foundations (1.5 hours)

## Goal

By the end of this phase, you should have **Playwright installed and working** with at least one meaningful end-to-end test covering your app's happy path.

---

## Step 1: Plan and Generate Your Prompts (10 min)

Follow the **Copilot Workflow Guide** (`copilot-workflow-guide.md`) again:

1. Use **Plan agent** to plan your Phase 2 Playwright work — describe what you built in Phase 1 and what user flow you want to test
2. Switch to **Agent Mode** and break the plan into step-by-step prompts
3. Have Copilot save the prompts to a `phase2-prompts.md` file in your project

**Example Plan agent prompt:**
> "I have a working [use case] app with a [stack] frontend and API. The form submits data, the API validates it, and results display on screen. Help me set up Playwright, create a first happy-path end-to-end test, and debug the likely issues."

---

## Step 2: Install and Configure Playwright (20-25 min)

Set up Playwright in your project and make sure you can run the test runner.

**What to do:**
- Install Playwright using the standard setup for your stack
- Add the generated config and example spec files
- Make sure your app can run locally while Playwright tests run against it
- Run the starter test once so you understand the workflow

> **Copilot tip:** *"Set up Playwright for this project, add the recommended config, and explain how to run the tests against my local app."*

---

## Step 3: Create Your First Happy-Path Test (25-30 min)

Write one end-to-end Playwright test that proves your app works for a valid submission.

**What to test:**
- Load the page
- Fill in the form with valid data
- Submit the form
- Verify the success result appears on screen

Focus on reliable selectors. Prefer accessible locators like `getByRole`, `getByLabel`, and visible text over fragile CSS selectors.

> **Copilot tip:** *"Write a Playwright test for a valid [document type] submission. Use accessible selectors and assert that the success result appears."*

---

## Step 4: Run, Debug, and Refine the Test (20-25 min)

Your first Playwright test probably won't pass on the first try. That's normal.

**What to do:**
- Run the test and read the failure output carefully
- Fix selectors, timing, or assertion issues
- Ask Copilot to explain why the test failed and suggest a better locator or assertion
- Re-run until the happy-path test passes consistently

> **Copilot tip:** *"This Playwright test is timing out when it clicks submit. Here is the error. Help me diagnose whether the issue is the selector, timing, or app behavior."*

---

## Step 5: Prepare for Deeper Coverage in Phase 3 (10-15 min)

Pick the next two scenarios you want to automate in Phase 3:
- One **negative-path** test, such as missing required fields or invalid values
- One **deeper** scenario, such as file upload, alternate document type, backend failure handling, or mocked responses

> **Copilot tip:** *"Suggest two high-value Playwright scenarios for this app beyond the happy path, and help me choose one negative-path test and one deeper scenario."*

---

## Checkpoint

By now you should have:
- [ ] Playwright installed and runnable
- [ ] One happy-path Playwright test passing
- [ ] A basic understanding of selectors, assertions, and test failures
- [ ] A plan for one negative-path test and one deeper scenario in Phase 3

**If you're ahead of schedule:** Start your negative-path Playwright test now.

**If you're behind:** Focus on getting one happy-path test passing. Don't chase extra scenarios until that foundation is working.
