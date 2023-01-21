# What is the password policy?

> Modeled after Operator TTP #e82f39e2-56f8-4f19-8376-b007f9ac5f8a

If an adversary breaches a device they often won't have administrator privileges. This limits their surface area, which depending on their objectives, could prevent them from achieving their goals. In order to identify the local administrator password they can run a brute-force attack or dump the local caches. 
Either of these is likely to be caught by endpoint defense, so another option is to read the local password policy and attempt to find strings (inside files)
that match the specified pattern. For example, if a policy requires 20 character passwords with 1 uppercase letter and 1 symbol, the attacker may scan all files
hoping the user stores their passwords in a text file.

Example output: 
```
Getting global account policies
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>policyCategoryPasswordContent</key>
	<array>
		<dict>
			<key>policyContent</key>
			<string>policyAttributePassword matches '.{4,}+'</string>
			<key>policyContentDescription</key>
			<dict>
				<key>ar</key>
				<string>أدخل كلمة سر لا تقل عن أربعة أحرف أو رموز.</string>
				<key>ca</key>
				<string>Introdueix una contrasenya que tingui quatre caràcters o més.</string>
				<key>cs</key>
				<string>Zadejte heslo o minimální délce čtyři znaky.</string>
				<key>da</key>  
.....
.....
```

Looking up the password policy programmatically should be flagged as suspicious.

## How

This test attempts to read the local password policy stored on disk. If the policy is not readable by the local user, it should fail. If the policy can be read, the test then scans all files in their home directory looking for strings starting with the letter "P" and that are exactly 20 characters long (a made up policy).