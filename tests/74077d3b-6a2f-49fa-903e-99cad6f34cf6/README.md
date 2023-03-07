# Will your computer quarantine oRat Malware?

This test drops a defanged oRat malware executable file, a remote access trojan that targets Windows, Linux, and macOS platforms. It has been recently attributed to Earth Berberoka, also known as GamblingPuppet, a new APT group targeting gambling websites. It is believed that they are behind the creation of this malware. This test will monitor if any endpoint defense quarantines the malware.

Example Output:

```
[+] Extracting file for quarantine test
[+] Pausing for 1 second to gauge defensive reaction
[-] Malicious file was not caught
```

Defenses should quarantine files with known signatures immediately.

## How

> Safety: the oRat malware has been defanged, so even if run, it will immediately exit.

An executable file of the oRat malware is extracted from the test and written to a user-owned directory. The test then waits briefly before running a few checks to determine if it was responded to (not just detected) by any defensive products on the endpoint.