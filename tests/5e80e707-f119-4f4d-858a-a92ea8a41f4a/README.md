# Can persistence be established on my host?

Many adversaries seek to establish persistence within a system as a means of increasing their chances of survival and success. In order to achieve this, they often rely on a variety of persistence mechanisms that allow their malicious activities to continue undetected. One particularly common method of persistence is known as scheduled task persistence, in which attackers create scheduled tasks that run a command at regular intervals. This technique can make it much more challenging for defenders to detect and remove the attacker's presence, which underscores the importance of understanding and defending against this type of threat.

Example output:
```
[+] Starting test
[-] Scheduled task was not caught
[+] Completed with code: 101
```

Endpoint protection should detect and stop the unathorized scheduled task.

## How

> Safety: the test does not execute any malicious code and removes the tasks as part of cleanup

This test creates a scheduled task using native utilities such as `schtasks.exe` and `cron`. For Linux, the task will just echo a string to emulate command execution. On Windows, the `cmd.exe` executable is added as part of the task to emulate a single binary being added to a task, which is common among many adversary groups and their malware for command and control. Once added to the host the `isTaskScheduled` function will check if the task exists and will exit with code 101. Indicating security controls failed to prevent unauthorized persistence.
