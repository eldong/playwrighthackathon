---
name: playwright-hackathon
description: Guide Codex to help hackathon teams learn Playwright from near-zero while building a simple app with Copilot. Use when creating, refining, or debugging Playwright end-to-end tests for a hackathon or workshop, especially for happy-path tests, negative-path validation tests, deeper scenarios, selector improvements, flaky test diagnosis, trace or screenshot debugging, and stack-agnostic Playwright coaching across JavaScript, Python, Java, or .NET projects.
---

# Playwright Hackathon

Keep the app simple and make testing depth the main investment after the core flow works.

## Work In This Order

1. Confirm the app has a minimal end-to-end flow before expanding scope.
2. Set up Playwright and get one happy-path test running.
3. Add one negative-path validation test.
4. Add one deeper scenario only after the first two tests are stable.
5. Improve selectors and assertions before adding more coverage.
6. Use trace or screenshot output to debug failures instead of guessing.

If the team is behind, reduce app complexity before reducing Playwright learning.

## Default Outcomes

Aim for these three test scenarios:

- Happy path: valid input produces a clear success result.
- Negative path: invalid or missing input produces a clear validation error.
- Deeper scenario: file upload, alternate document type, backend failure handling, retry handling, or mocked API behavior.

Treat those as the standard bar for the session, not stretch goals.

## Selector Rules

Prefer stable, accessible locators in this order:

1. `getByRole`
2. `getByLabel`
3. `getByText` for visible status or validation messages
4. `getByPlaceholder` only when the UI does not expose better semantics

Avoid long CSS selectors, DOM-depth selectors, and arbitrary waits unless there is no practical alternative.

When selectors are brittle, suggest small app changes that improve accessibility and testability, such as:

- Add proper labels to inputs
- Use semantic buttons and headings
- Give banners or result areas clear visible text
- Expose stable text for pass/fail states

## Assertion Rules

Write assertions that prove behavior, not just page existence.

Prefer:

- Specific success text or status banner
- Specific validation messages
- Visibility of the expected result container
- Request outcome reflected in the UI

Avoid vague checks like "page contains some text" when a more precise assertion is possible.

## Debugging Rules

When a test fails:

1. Read the exact Playwright failure.
2. Decide whether the problem is selector, timing, app state, or assertion quality.
3. Inspect trace, screenshot, or error output before rewriting large parts of the test.
4. Fix one issue at a time and rerun.

Do not recommend blind `waitForTimeout` calls as the default fix.

Prefer:

- Waiting for visible UI states
- Waiting for a response or known result element
- Improving locators
- Tightening or clarifying assertions

## Copilot Prompt Patterns

Use prompts like these and adapt them to the stack and use case:

### Create the first test

`Write a Playwright test for a valid invoice submission. Use accessible selectors, submit the form, and assert that a success result appears.`

### Add a negative-path test

`Write a Playwright test for a failed validation where the amount is missing. Assert that the correct validation message appears and the submission is treated as invalid.`

### Improve selectors

`Review this Playwright spec and replace brittle selectors with stable accessible locators such as getByRole and getByLabel. Explain each change briefly.`

### Debug a failure

`This Playwright test is failing. Here is the error and trace summary. Tell me whether the main issue is selector choice, timing, or app behavior, and suggest the smallest reliable fix.`

### Strengthen assertions

`Improve this Playwright test so the assertions clearly verify the user-visible success or validation outcome instead of generic text checks.`

## Stack Notes

Keep the guidance stack-agnostic unless the project clearly commits to one stack.

- JavaScript/TypeScript: usually the most direct Playwright path; colocated test files and npm scripts are common.
- Python: Playwright still drives the browser similarly; be explicit about how to run the app and the test runner separately.
- Java: help with Playwright setup, package structure, and reliable test commands, but keep examples focused on behavior rather than framework ceremony.
- .NET: keep attention on run commands, local URLs, and stable selectors; avoid overcomplicating test setup.

If stack-specific details matter, ask Copilot to tailor commands and file locations to the repo's actual structure.

## Coaching Guidance

Nudge teams toward these habits:

- Build the smallest app that can be tested meaningfully.
- Run tests early, not only after the app feels finished.
- Treat the first failure as part of the lesson.
- Prefer one stable test over several flaky ones.
- Use Copilot to explain failures, not only generate code.

If the team is ahead, deepen coverage.
If the team is behind, protect the happy path first.
