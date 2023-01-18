import playwright.sync_api as sync_api
import time
import os,binascii
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
    page.fill('#login_field', 'username')
    page.fill('#password', 'password')

    # Click the "Sign in" button
    page.click('[type="submit"]')

def changepassword(page):
    print("Changing password of current user")
    oldpassword = os.environ.get('GITHUB_PASSWORD')
    newpassword = "t3sting1234554321@"

    page.get_by_role("menuitem", name="Settings").click()
    page.get_by_role("link", name="Password and authentication").click()
    page.get_by_label("Old password").click()
    page.get_by_label("Old password").fill(oldpassword)
    page.locator("#user_new_password").click()
    page.locator("#user_new_password").fill(newpassword)
    page.get_by_label("Confirm new password").click()
    page.get_by_label("Confirm new password").fill(newpassword)
    page.get_by_role("button", name="Update password").click()

def select_browser(playwright):
    browsers = ["chrome", "msedge", "firefox"]
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
            # Password change
            changepassword(page)
            time.sleep(5)
            # Check if the password change was successful
            if page.url == 'https://github.com/settings/security':
                print('Password changed successfully!')
                sys.exit(100)
            else:
                print('Password change failed!')
                sys.exit(101)
        else:
            # Login was not successful
            print('Login failed!')
            sys.exit(101)

if __name__ == "__main__":
    print("Starting engine")
    main()