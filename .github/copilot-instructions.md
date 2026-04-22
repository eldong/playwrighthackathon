# GitHub Copilot Instructions

## Project Context

This is a Playwright hackathon facilitation kit for a GitHub Copilot + Playwright workshop. Participants build a document-validation web app across three phases and write end-to-end tests using Playwright, guided by Copilot.

## General Principles

- Prefer accessible Playwright locators: `getByRole`, `getByLabel`, `getByText` over CSS selectors or XPath
- Write tests that are readable, stable, and assert meaningful outcomes — not just "page contains text"
- Keep fixture data in a `test-data/` folder; use clearly named files for valid and invalid inputs
- Structure tests under `tests/` with subfolders: `tests/happy-path/`, `tests/negative-path/`, `tests/deeper/`
- Each test should cover one clear scenario — avoid combining multiple assertions from different flows

## Code Style

- Use `async/await` throughout Playwright tests (no callback patterns)
- Prefer `expect(locator).toBeVisible()` and `expect(locator).toHaveText()` over generic page assertions
- Add a short comment above each test describing what it proves, not how it works
- Keep test files focused: one feature or user flow per file

## Copilot Workflow

- Use **Plan agent** first to outline work before generating code
- Use **Agent Mode** for multi-step implementation tasks
- When stuck on a selector or assertion, ask Copilot to explain alternatives rather than just generate a fix
- Save generated prompts to `phase{N}-prompts.md` so the team can review and reuse them

## What to Avoid

- Do not add `page.waitForTimeout()` as a fix for flaky tests — diagnose the root cause instead
- Do not use `page.$()` or `page.$$()` — use the Locator API
- Do not hard-code base URLs in test files — use `playwright.config.ts` `baseURL`
- Do not scope new features if testing coverage is incomplete
