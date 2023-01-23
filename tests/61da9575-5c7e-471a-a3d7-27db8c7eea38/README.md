# Can you use Playwright to execute actions in GitHub?

Playwright is an open-source, cross-platform library for automating web browsers. It allows developers to write scripts in multiple languages including Python that can interact with web pages in a way similar to how a user would. Playwright can be used for tasks such as web scraping, browser testing, and automating web-based tasks or attacks.

This Playwright-specific test will first check if Playwright is installed if it is then it will execute a series of actions within GitHub such as creating and modifying a repository, submitting an issue, and changing Branch settings to lock the `main` branch if Playwright is installed on the host.

Example output:
```
[+] Playwright installed: Version 1.29.1
```

```
[+] Playwright is not installed: exec: "playwright": executable file not found in %PATH%
```

## How

> Safety: the test does not drop a malicious file and the actions taken within GitHub have been selected with safety in mind.

This test first checks if Playwright is installed and if it is it will drop a Playwright python script called test.py to disk and then executes it. A Chromium browser will then launch and the GitHub actions are executed automatically with no user interaction. After our Playwright script is executed it will attempt to log-in using the `GITHUB_USERNAME` and `GITHUB_PASSWORD` environment variables which must be set correctly before execution. Once log in is successful a new randomly generated repository is created. From the newly created repo a new file called `Hello_World.py` is created which contains code to print `hello world`. Next on the list of actions is issue submission this test will create and submit a new issue to the repository titled `Add goodbye to script` with a comment suggestion. For the last GitHub action, the script will navigate to Branches in GitHub settings and then attempt to add a new branch protection rule which locks the `main` branch.
