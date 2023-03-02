# Can you escalate to admin without a password

It's not uncommon for Linux machines to be configured for `sudo` access with no
password. While Windows environments don't have a direct equivalent of `sudo`,
they do have a `runas` command that can be passed a `/savecreds` flag which
allows subsequent runs as that user to be done without passing in another
password.

Example output:

```
Failure
[+] Starting test
[+] Passwordless escalation succeeded!
[+] Completed with code: 101
```

```
Success
[+] Starting test
[+] Passwordless escalation failed!
[+] Completed with code: 107
```

# Windows

The windows usecase is a bit contrived when running as a system user. A system
would have to have someone raise a shell in the system context, and then do a
runas with a savecreds flag. That said, there are several blogs on the internet
suggesting this as a work around for windows UAC prompts.

You can inspect the saved creds for a user by running `cmdkey /list`

The test pipes and empty string to a runas command running as the local admin
user. If creds have been saved, no prompt for a password is issued, and the
command succeeds. If the creds have not been saved, the pipe writes into the
login prompt and the prompt fails.

```
echo '' | runas /user:$env:computername\administrator /savecred whoami
```

# Darwin / Linux

MacOS and most linux distros ship with some sort of sudo access. Mac defaults to
requiring a password, where as Linux distro's vary wildly. The linux version of
this test attempts to escalate to run whoami. If prompted for a password it
receives and empty string the escalation fails.

```
echo '' | sudo -S whoami
```
