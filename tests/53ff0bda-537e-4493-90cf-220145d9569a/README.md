# Can a base64 encoded script be run?

EDR products monitor every command run on an endpoint. As known bad commands are attempted, if the strings are signatured, the EDR should block it. To combat this, an adversary will often encode their command and decode and execute it in memory in one swing. This tradecraft can slip past the defense because the "real" command string is not seen until just before execution. Base64, the most common encoding technique, is a group of binary-to-text encoding schemes that represent binary data in sequences of 24 bits that can be represented by four 6-bit Base64 digits.

Example output: 
```
[+] Starting test
Prelude
[+] Completed with code: 101
```

Any script that attempts to execute an encoded string should be blocked.

## How

> Safety: the encoded string is a non-intrusive command

This test decodes the string "echo -n Prelude" in memory and executes it in a single action. If the string is found and the test is allowed to finish, it is considered a failure (of the defense), otherwise if it is blocked, it is considered a success.
