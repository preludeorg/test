# Can adversaries gather information about an IP address on my network?

After compromising a device adversaries often programmatically look up and check IP addresses both public and private. This information provides details about the physical location of the device, open public ports and if the IP's are pingable on the network.

Example output: 
```
[+] Starting test
[+] Getting Public IP Address & Location
Public IP: 207.212.122.224
Latitude: 33.3444
Longitude: -84.0915
[+] Searching IP on Shodan
No open ports found for the public IP on Shodan.
[+] Ping Sweep
192.168.86.28 is up and belongs to a4:cf:99:72:d7:91
10.211.55.2 is up and belongs to a6:cf:99:27:ec:64
10.37.129.2 is up and belongs to a6:cf:99:27:ec:65
[+] Completed with code: 101 
```

While looking up this information from a browser may be normal, looking it up programmatically should be flagged as suspicious.

## How

> Safety: discovered details are never sent off the device

This test uses a free service hosted at http://ip-api.com/ which displays the IP information of the caller. It will then use Shodan to query the public ip and determine if any ports are open for that host. Lastly, the addresses on the host network inferfaces are gathered and a ping sweep is performed to determine if the IP's are reachable. It exits successfully if all the lookups are allowed to complete.
