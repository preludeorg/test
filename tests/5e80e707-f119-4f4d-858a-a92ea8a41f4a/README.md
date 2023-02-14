# Can you stop common persistence methods?

Persistence is a common goal of many adversaries. It increases their chances of survival in an environment. This test focuses on one specific type of persistence mechanism that is commonly used by attackers, scheduled task persistence. This involves creating scheduled tasks that run a command at regular intervals, making it more difficult to detect and remove.

Endpoint protection should detect and stop the unathorized scheduled task.

## How

> Safety: the test only echo's "Hello World" in the tasks and the tasks are removed

This test creates a scheduled task using native utilities such as `schtasks.exe` and `at` that will echo `Hello World`. If allowed to complete the test will exit with code 101.