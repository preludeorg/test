import asyncio
import os,binascii
from playwright.async_api import async_playwright

async def main():
    username = os.environ.get('GITHUB_USERNAME')
    password = os.environ.get('GITHUB_PASSWORD')
    repo_name = binascii.b2a_hex(os.urandom(8)).decode()
    async with async_playwright() as p:
        browser_type = p.chromium
        browser = await browser_type.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://github.com/")

        # Login 
        await page.get_by_role("link", name="Sign in").click()
        await page.get_by_label("Username or email address").click()
        await page.get_by_label("Username or email address").fill(username)
        await page.get_by_label("Password").click()
        await page.get_by_label("Password").fill(password)
        await page.get_by_role("button", name="Sign in").click()

        # New repository
        await page.get_by_role("heading", name="Top Repositories New").get_by_role("link", name="New").click()
        await page.get_by_label("Repository name").click()
        await page.get_by_label("Repository name").fill(repo_name)
        await page.get_by_label("Add a README file").check()
        await page.get_by_role("button", name="Create repository").click()

        # Add file
        await page.get_by_role("button", name="Add file").click()
        await page.get_by_role("button", name="Create new file").click()
        await page.get_by_placeholder("Name your file…").click()
        await page.get_by_placeholder("Name your file…").fill("Hello_World.py")
        await page.locator("#code-editor pre").click()
        await page.fill("#code-editor pre", "def hello_world():\n    print('hello world')\nhello_world()")
        await page.get_by_placeholder("Create Hello_World.py").click()
        await page.get_by_placeholder("Create Hello_World.py").fill("Testing Playwright")
        await page.get_by_role("button", name="Commit new file").click()

        # Issue
        await page.get_by_role("link", name="Issues Issues").click()
        await page.get_by_role("button", name="New issue").click()
        await page.get_by_placeholder("Title").fill("Add goodbye to script")
        await page.get_by_placeholder("Leave a comment").click()
        await page.get_by_placeholder("Leave a comment").fill("This script is too basic and should allow for a user to select hello and print hello world and also the same thing for goodbye. This way the user has two options that do two different things.")
        await page.get_by_role("button", name="Submit new issue").click()

        # Settings
        await page.get_by_role("link", name="Settings Settings").click()
        await page.get_by_role("link", name="Branches").click()
        await page.get_by_role("link", name="Add branch protection rule").click()
        await page.get_by_label("Lock branch").check()
        await page.get_by_label("Branch name pattern").click()
        await page.get_by_label("Branch name pattern").fill("main")
        await page.get_by_text("Create").click()
        await page.get_by_role("link", name="Code Code").click()

        # Log out
        await page.get_by_role("button", name="View profile and more").click()
        await page.get_by_role("menuitem", name="Sign out").click()
        await browser.close()

asyncio.run(main())
