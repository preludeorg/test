## Will a long running VST be stopped properly?

This test checks if a long-running Verified Security Test (VST) is stopped properly. A long-running VST that fails to stop properly can cause issues such as resource exhaustion or unexpected results. This test will monitor if the VST is stopped correctly.

Example Output:
```
[+] Starting test
[+] Sleeping for 15 seconds
[-] VST did not stop properly, returned exit code 101
```

VST's should stop after 10 seconds.

> Safety: This test sleeps for a maximum duration of 15 seconds to simulate a long running VST.

## How

The test waits for 15 seconds before exiting. If the exit code is 101, the VST has stopped properly within 10 seconds, and the test will pass. If the exit code is 102, the VST has not stopped properly, and the test will fail.
