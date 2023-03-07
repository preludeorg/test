# Are your SSH Private Key permissions restricted?

It is common occurance where SSH private keys are not restricted to the correct permissions. SSH credentials permission should be instead restricted to `600` (readable and writable only by the owner) or `400` (readable only by the owner). This test checks that your private key is not more permissive than that.

Example output:
```
[+] Found home directory
[+] Found SSH Private Key
[-] SSH Private Key permissions are too open
```

Endpoint SSH Private Key permissions should be restricted

## How

> Safety: the test does not read or modify the ssh private key file content. It only checks the file permissions.

The test finds the user's home directory and then looks for a private key file in the `~/.ssh` directory. If a private key file is found, the test checks the file permissions.
