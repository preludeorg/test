# Is Netcat installed and operational?

The presence of remote administration tools, such as Netcat, on a host provides attackers with a unique opportunity to exploit "living-off-the-land" techniques. These techniques are difficult to detect as they blend in with the normal day-to-day usage of system utilities. Netcat, known as the swiss-army knife for hackers, is a versatile utility that enables adversaries to carry out various operations, such as lateral movement and port scanning. In essence, attackers can leverage Netcat to evade defenses and compromise the targeted system.

Example output:
```
[+] Starting test
[-] Netcat was able to connect 
[+] Completed with code: 101
```

Netcat should not exist on an endpoint. If it is, any attempt to use it should be blocked by endpoint security controls.

## How

> Safety: the test sends a ping request to google.com using Netcat; no data is otherwise sent off the machine.

This test first checks if Netcat is installed and available on the PATH of the host. If not, the test exits with a "not relevant" code (104) - which is what you should expect to see. If Netcat is available, the test uses it to send a ping request to google.com at port 80. If the request succeeds, the test exits with an "unprotected" code (101). If the request fails, a "protected" (100) code is returned. 
