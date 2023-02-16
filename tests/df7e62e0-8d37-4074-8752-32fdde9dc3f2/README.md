# Can you stop common remote system utilities?

The presence of remote administration tools such as netcat on a host presents an opportunity for attackers to take advantage of living-off-the-land techniques that evade defenses by blending in with the normal day-to-day usage of system utilities in the environment. This test focuses on one of those utilities called netcat. Netcat offers adversaries multiple capabilities including network connection testing in preparation for lateral movement, port scanning, and listener capabilities for reverse shells.

Example output:
```
[+] Starting test
[bash -c nc -vz google.com 80]
Netcat was able to connect
[+] Completed with code: 101
```
Any attempts to use netcat are expected to be blocked by endpoint security controls.

## How

> Safety: the netcat command scans for listening daemons, without sending any data to them

This test will check if netcat exists on the host if it does exist a netcat command is executed to test a connection to `google.com` on port 80. If the connection is successful it will exit with 101. If the utility is installed but the connection is not successful it will exit with 100.
