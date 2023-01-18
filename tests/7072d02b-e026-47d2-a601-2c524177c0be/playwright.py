import playwright.sync_api as sync_api
import time
import os
import sys


def login(page):
    print("Logging in")
    url = "https://github.com/login"
    page.bring_to_front()
    page.goto(url)

    # Wait for the login form to be present
    page.wait_for_selector('#login_field')

    username = os.environ.get('GITHUB_USERNAME')
    password = os.environ.get('GITHUB_PASSWORD')

    # Fill out the login form with your username and password
    page.fill('#login_field', username)
    page.fill('#password', password)

    # Click the "Sign in" button
    page.click('[type="submit"]')


def setup_github_test_action(page, repo_name):
    repo_name = os.environ.get('GITHUB_REPO_NAME')
    username = os.environ.get('GITHUB_USERNAME')
    # Go to a repo
    url = f"https://github.com/{username}/{repo_name}"
    page.goto(url)
    # Click on the "Actions" tab
    page.click('#actions-tab')
    time.sleep(5)

    # Click on the "Set up a workflow yourself" url
    page.click('a[data-hydro-click*="actions.onboarding_setup_workflow_click"]')
    time.sleep(5)

    # Define the test GitHub action code
    action_code = """
    name: Test
    on: [push]
    jobs:
    test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Test
    run: echo 'Hello, world!'
    """

    page.wait_for_selector('#code-editor')
    page.fill('#code-editor', action_code)

    time.sleep(5)
    page.click('summary[class*="btn-primary"]')

    time.sleep(5)
    page.wait_for_selector('#submit-file')

    # Click the submit button
    page.click('#submit-file')


def select_browser(playwright):
    browsers = ["chrome", "msedge"]
    for b in browsers:
        try:
            browser = playwright.chromium.launch(channel=b)
            return browser
        except:
            continue
    print("A supported browser is not available.")
    sys.exit(1)


def main():
    print("Initializing playwright")
    with sync_api.sync_playwright() as playwright:
        browser = select_browser(playwright)
        page = browser.new_page()
        login(page)
        # Check if login was successful
        if page.url == 'https://github.com/':
            print('Login successful!')
            # Github test action
            setup_github_test_action(page)
            sys.exit(100)
        else:
            # Login was not successful
            print('Login failed!')
            sys.exit(101)


if __name__ == "__main__":
    print("Starting engine")
    main()
