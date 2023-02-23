# Will my host detect an attempted ping sweep?

This VST tests whether a host can detect an attempted ping sweep, which is a common technique used by attackers to discover live hosts on a network. The code utilizes the "ping" command to send a single ICMP packet to each IP address within a specified network range, and checks if any of the hosts respond. If a response is received, it indicates that the host is up and an attacker may want to attempt to pivot to that machine. 

```
[+] Starting test
[+] Ping Sweep
192.168.0.1 is up
[+] Completed with code: 101
exit status 101
```

## How 

> Saftey: No packets beyond an ICMP packet are sent to the hosts.

This code defines a ping sweep function that performs a scan of the local network to identify online hosts by sending ICMP echo request packets. If any hosts are found, the function stops the program execution via the Endpoint module's Stop function. 