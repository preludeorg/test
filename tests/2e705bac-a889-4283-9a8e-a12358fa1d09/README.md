# Will your computer quarantine Royal Ransomware?

This test drops a defanged Royal Ransomware ELF file, from a recent campaign [targeting Linux ESXI Servers](https://www.bleepingcomputer.com/news/security/linux-version-of-royal-ransomware-targets-vmware-esxi-servers/), then monitors if any endpoint defense quarantines it. Royal Ransomware was first spotted in the wild in January 2022 and is attributed to a group of threat actors who previously worked with the Conti operation. After encrypting their targets' enterprise network systems, the group often demands ransom payments ranging from $250,000 to tens of millions. Ransomware is a form of malware that encrypts files on a device. After executing the encryption phase, the ransomware operator demands money in exchange for the decryption key. If the ransom is not paid, file recovery may not be possible.

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
