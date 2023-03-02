# Will your computer quarantine Redline Stealer Malware?

This test drops a defanged Redline Stealer Malware executable file, a Trojan that targets sensitive information such as credentials and personal information from the victim's computer. Redline Stealer Malware was first discovered by researchers from Fortinet in August 2018 and has since been used in various cyberattacks and campaigns. Recently, it has been observed in attacks by the cybercriminal group SteelClover. This test will monitor if any endpoint defense quarantines the malware.

Example Output:
```
[+] Extracting file for quarantine test
[+] Pausing for 1 second to gauge defensive reaction
[-] Malicious file was not caught
```

Defenses should quarantine files with known signatures immediately.

## How

> Safety: the Redline Stealer Malware has been defanged, so even if run, it will immediately exit.

An executable file of the Redline Stealer Malware is extracted from the test and written to a user-owned directory. The test then waits briefly before running a few checks to determine if it was responded to (not just detected) by any defensive products on the endpoint.