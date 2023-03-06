# Can a regular user run administrator-level commands?

Non-root users being able to run unauthorized commands as root can pose a significant security risk, potentially leading to compromise of the entire system. Two notable CVEs based on this issue are CVE-2019-14287 and CVE-2016-0099. CVE-2019-14287 (applicable to Linux and Darwin systems) is caused by a flaw in the sudo command that allows a non-root user to bypass restrictions and run commands as root by specifying the user ID -1. CVE-2016-0099 (applicable to Windows systems) exploits a vulnerability in the Windows Secondary Logon Service that allows a non-administrative user to run arbitrary code with SYSTEM privileges. 

This VST tests whether a host is vulnerable to these CVEs.
Example output:

```
[+] Starting Test
[+] Testing CVE-2019-14287 on Linux/Darwin OR CVE-2016-0099 on Windows.
[-] Test failed (unauthorized access to root was gained)
```
Properly updated systems should not allow a non-root user to run unauthorized commands as root.

## How

> Safety: As a proof-of-concept, this VST utilizes the identified vulnerabilities and only executes the "whoami" command

This test involves running the "whoami" command as a non-root user, which outputs the user ID of the user who runs it and can be used to determine if the machine is vulnerable to the mapped CVEs. This test is safe because running this command makes no lasting change (it only outputs a text value), and no other commands are run.
