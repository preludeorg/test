# Are there hosts visible on my network?

This VST tests whether any hosts are visible on the network using ARP requests. ARP requests are used to obtain the MAC address of a device on the network. The code starts by determining the network range using the provided interface and proceeds to open a live pcap session to capture ARP reply packets.

If an ARP reply packet is received, the code stops the execution via the Endpoint module's Stop function and outputs the corresponding MAC address and IP address.

Example Output:

```
[+] Starting test
Using network range 192.168.1.0/24 for interface eth0
IP 192.168.1.1 is at 01:23:45:67:89:ab
[+] Completed with code: 101
exit status 101
```

## How

This code uses the `pcap` library to capture ARP reply packets and extract the corresponding IP and MAC addresses. Once a response is received, it immediately halts the program execution via the Endpoint module's Stop function and outputs the MAC and IP addresses.

Please note that this code uses only ARP requests and does not send any other packets to the network beyond the initial ARP requests.