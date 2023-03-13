# Will your computer quarantine Colour-Blind malware?

This test drops a defanged Colour-Blind malware python file, a Remote Access Trojan (RAT) that targets sensitive information such as credentials and personal information from the victim's computer. Colour-Blind malware was first discovered by researchers from Kroll in March 2023 and has been seen in the Python Package Index (PyPI) being used to deliver Colour-Blind malware via malicious Python packages. This test will monitor if any endpoint defense quarantines the malware.

Example Output:
```
[+] Extracting file for quarantine test
[+] Pausing for 1 second to gauge defensive reaction
[-] Malicious file was not caught
```

Defenses should quarantine files with known signatures immediately.

## How

> Safety: the Colour-Blind malware has been defanged, so even if run, it will immediately exit.

A python file of the Colour-Blind malware is extracted from the test and written to a user-owned directory. The test then waits briefly before running a few checks to determine if it was responded to (not just detected) by any defensive products on the endpoint.