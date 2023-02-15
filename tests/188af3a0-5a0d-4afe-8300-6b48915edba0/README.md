# Can you stop common remote system utilities?

Lateral movement is a common goal of many adversaries most especially ransomware. The presence of open remote administration ports indicates a problem as it may allow unauthorized access to individual machines on the network in turn expanding the foothold and damage caused by an adversary inside the network during compromise. This test focuses on targetted port scanning of the two most common ports for ssh and RDP (22 and 3389).

Example output:
```
[+] Starting test
[+] Scanning network for open ports:
No host found with port 22 or port 3389 open
[+] Completed with code: 100
```

## How

> Safety: the test only sends a TCP packet to the hosts to check if the specific port is open and no other data is sent

This test finds the current internal IP address of the host and then conducts a port scan on the /24 subnet of that IP that scans for ports 22 (ssh) and 3389 (RDP) on the hosts within the range. If a host is found to have either of those ports open the test will exit with a 101 code. If no hosts are found with those ports open it will return a 100 code.