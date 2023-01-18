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

def edit_repository(page):
    page.get_by_role("button", name="View profile and more").click()
    page.get_by_role("menuitem", name="Your repositories").click()
    page.wait_for_load_state("networkidle") 
    page.get_by_role("link", name="Test-repo").click()
    page.get_by_role("button", name="Add file").click()
    page.get_by_role("button", name="Create new file").click()
    page.get_by_placeholder("Name your file…").click()
    page.get_by_placeholder("Name your file…").fill("Hello_World.py")
    page.locator("#code-editor pre").click()
    page.fill("#code-editor pre", "def hello_world():\n    print('hello world')\nhello_world()")
    page.get_by_placeholder("Create Hello_World.py").click()
    page.get_by_placeholder("Create Hello_World.py").fill("Testing Playwright")
    page.get_by_role("button", name="Commit new file").click()

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
            print('Login successful!')
            # Github test actions
            changepassword(page)
            time.sleep(10)
            edit_repository(page)
            time.sleep(10)
            sys.exit(100)
        else:
        # Login was not successful
        print('Login failed!')
        sys.exit(101)

if __name__ == "__main__":
    print("Starting engine")
    main()
