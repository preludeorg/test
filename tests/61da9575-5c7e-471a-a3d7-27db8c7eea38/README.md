# SaaS test: GitHub

> SaaS tests have preconditions which must be set before execution. These tests do not test endpoint defenses but instead trigger events you should observe in your backend SIEM or event dashboards.

Playwright is an open-source library for automating web browsers. It allows developers to write scripts in multiple languages, including Python, that can interact with web pages in a similar way as a human. On the security side, Playwright can be used to run a series of actions inside a Software as a Service (SaaS) provider to test if any defenses notice odd or suspicious behaviors. 

GitHub is a popular SaaS tool for software engineers to store and collaborate on code. If tampered with - code repositories being deleted, an insider threat cloning all company code, access keys being created on the side - GitHub can cause an organization headaches.

Example output:
```
[+] Playwright installed: Version 1.29.1
```

This test should run normally but you should validate your detection rules observed the performed actions.

## How

> Safety: only white-glove, non-destructive actions are run inside GitHub

This test first checks if Playwright is installed, and if it is, drops a Playwright script called test.py to disk and executes it. A Chromium browser will then launch and the script continues with no user interaction. It will attempt to log in using the ``GITHUB_USERNAME`` and ``GITHUB_PASSWORD`` environment variables, which must be set before execution. Once logged in, a new repository is created and is immediately populated with a source code file. Next, the test creates a new issue with the title "Add goodbye to script". Finally, the test navigates to the repo settings and adds a new branch protection rule to lock the ``main`` branch.
