import { test, expect } from '@playwright/test';

test('contact us link navigates to contact page', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('link', { name: 'Contact Us' }).click();
  await expect(page).toHaveURL(/\/contact\.html$/);
  await expect(page.getByRole('heading', { name: 'Contact Us' })).toBeVisible();
});

test('contact form requires all fields before submitting', async ({ page }) => {
  await page.goto('/contact.html');
  const confirmation = page.locator('#confirmation');

  // Submit with all fields empty
  await page.getByRole('button', { name: 'Submit' }).click();
  await expect(confirmation).toBeEmpty();

  // Fill only name, submit
  await page.getByLabel('Name').fill('Alice');
  await page.getByRole('button', { name: 'Submit' }).click();
  await expect(confirmation).toBeEmpty();

  // Fill name and email, leave message empty
  await page.getByLabel('Email').fill('alice@example.com');
  await page.getByRole('button', { name: 'Submit' }).click();
  await expect(confirmation).toBeEmpty();

  // Fill all fields, submit should succeed
  await page.getByLabel('Message').fill('Hello there');
  await page.getByRole('button', { name: 'Submit' }).click();
  await expect(confirmation).toHaveText('Thank you for your message!');
});
