# Is Netcat installed and operational?

The presence of remote administration tools, such as netcat, on a host, provides attackers with a unique opportunity to exploit "living-off-the-land" techniques. These techniques are difficult to detect as they blend in with the normal day-to-day usage of system utilities in the environment. Netcat, in particular, is a versatile utility that enables adversaries to carry out various operations, including network connection testing for lateral movement, port scanning, and listener capabilities for reverse shells. In essence, attackers can leverage netcat to evade defenses and compromise the targeted system.

Example output:
```
[+] Starting test
[-] Netcat was able to connect 
[+] Completed with code: 101
```
Any attempts to use netcat are expected to be blocked by endpoint security controls.

## How

> Safety: the test does not use any malicious commands during execution

This test aims to determine the presence of netcat on the host by executing a netcat command to test a connection to google.com on port 80. The result of the test depends on the outcome of the connection test. If the connection is successful, the test will exit with a status code of 101. Conversely, if netcat is installed on the host but the connection test is unsuccessful, the test will exit with a status code of 100. In summary, this test is designed to assess the availability and functionality of netcat, a remote administration tool that offers various capabilities to attackers.
