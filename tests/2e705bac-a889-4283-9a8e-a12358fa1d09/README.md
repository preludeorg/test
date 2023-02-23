# Will your computer quarantine Royal Ransomware?

This test uses a defanged Royal Ransomware ELF which is then dropped to disk. 
Ransomware is a form of malware that encrypts files on a device.  After encrypting files, the ransomware operator demands a ransom to decrypt the encrypted files. If the ransom is not paid, file recovery may not be possible.
For this ransomware sample to work, the ELF needs to be executed on a supported Linux x86_64 device.

Example output:
```
[+] Extracting file for quarantine test
[+] Pausing for 1 second to gauge defensive reaction
[-] Malicious file was not caught
```

Defenses should quarantine files with known signatures immediately.

## How

> Safety: the ransomware has been defanged, so even if run, it will immediately exit.

An ELF file is extracted from the test and written to a user-owned directory. The test then waits briefly before running a few checks to determine if it was responded to (not just detected) by any defensive products on the endpoint. 
