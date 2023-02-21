# Are exploit attempts prevented?

Exploit attempts represent a significant security threat by allowing attackers to gain unauthorized access, perform malicious actions, and potentially lead to data theft or downtime. Blocking exploit attempts is critical to maintaining system security and preventing negative consequences, as well as protecting against privilege escalation vulnerabilities, which enable attackers to bypass security controls and gain higher levels of access than authorized. 

Example output:
```
[+] Starting Test
[-] Test was not prevented
```
Defenses should prevent exploit attempts from running.

## How

> Safety: This VST exploits the vulnerabilities and only runs the command `whoami` as a proof-of-concept.

This VST exploits two different vulnerabilities, depending on the operating system, by targeting CVE-2019-14287 for Linux or Darwin, or CVE-2016-0099 for Windows, allowing a user with limited privileges to escalate their privileges and run `whoami` as a proof-of-concept. Blocking these exploits is necessary to ensure the security and integrity of a system, preventing potential attacks and their negative consequences.
