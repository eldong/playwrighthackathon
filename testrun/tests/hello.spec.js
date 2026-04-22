import { test, expect } from '@playwright/test';

test('press me button displays exact hello text', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('button', { name: 'Press me' }).click();
  await expect(page.locator('#message')).toHaveText('Hello from JavaScript!');
});
