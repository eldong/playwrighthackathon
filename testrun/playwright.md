# Playwright Setup & Usage

## Prerequisites

- [Node.js](https://nodejs.org/) (v18+)
- The app files in this folder (`index.html`, `server.js`, `package.json`)

## 1. Install Playwright

From the `testrun` folder:

```bash
npm init playwright@latest
```

When prompted:
- Choose **JavaScript** (or TypeScript if preferred)
- Accept the default `tests` folder
- Say **yes** to installing browser binaries

This adds `@playwright/test` to `package.json` and creates `playwright.config.js`.

## 2. Configure Base URL

In `playwright.config.js`, set the base URL so tests know where the app is running:

```js
use: {
  baseURL: 'http://localhost:3000',
}
```

Optionally add a `webServer` block so Playwright starts the server automatically:

```js
webServer: {
  command: 'npm start',
  port: 3000,
  reuseExistingServer: true,
}
```

## 3. Add Test Script

In `package.json`, add a `test` script:

```json
"scripts": {
  "start": "node server.js",
  "test": "npx playwright test"
}
```

## 4. Write Tests

Create a test file at `tests/hello.spec.js`:

```js
const { test, expect } = require('@playwright/test');

test('button displays hello text', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('button', { name: 'Press me' }).click();
  await expect(page.getByText('Hello from JavaScript!')).toBeVisible();
});

test('clear button removes text', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('button', { name: 'Press me' }).click();
  await page.getByRole('button', { name: 'Clear' }).click();
  await expect(page.getByText('Hello from JavaScript!')).not.toBeVisible();
});
```

## 5. Run Tests

Start the server (skip if you configured `webServer` above):

```bash
npm start
```

In a separate terminal, run the tests:

```bash
npm test
```

### Useful Run Options

| Command | Description |
|---|---|
| `npx playwright test` | Run all tests headless |
| `npx playwright test --ui` | Open interactive test runner |
| `npx playwright test --headed` | Run tests in a visible browser |
| `npx playwright show-report` | View the HTML test report |
| `npx playwright test --trace on` | Capture traces for debugging |

## 6. Selector Best Practices

Use stable, accessible locators (in order of preference):

1. `getByRole('button', { name: '...' })`
2. `getByLabel('...')`
3. `getByText('...')`
4. `getByPlaceholder('...')`

Avoid brittle CSS or DOM-depth selectors.

## 7. Debugging Failures

1. Read the exact error message from Playwright output.
2. Check whether the issue is a selector, timing, or app state problem.
3. Use `--trace on` or `--headed` to inspect what the browser sees.
4. Fix one issue at a time and rerun.

Avoid using `waitForTimeout` — prefer waiting for visible UI states instead.
