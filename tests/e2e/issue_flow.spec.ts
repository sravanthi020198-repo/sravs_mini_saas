import { test, expect } from '@playwright/test'

test('Issue creation and display', async ({ page }) => {
  await page.goto('http://localhost:5173/login');
  await page.fill('input[type="email"]', 'user@example.com');
  await page.fill('input[type="password"]', 'password123');
  await page.click('button:has-text("Login")');

  await page.goto('http://localhost:5173/issues');
  await page.fill('input[name="title"]', 'E2E Issue');
  await page.fill('textarea[name="description"]', 'Created from Playwright');
  await page.click('button:has-text("Submit")');

  await expect(page.locator('li')).toContainText('E2E Issue');
});
