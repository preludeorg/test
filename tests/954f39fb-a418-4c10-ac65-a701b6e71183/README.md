# Can an unsigned app serve a port on localhost?

When an endpoint serves a port, it is signaling its readiness to start accepting traffic. This traffic could come from another process on the device or from a different computer across a network. Served ports should be known and monitored. A common tactic by adversaries is to serve a port and start directing command-and-control activities through it. It is normal for an application to serve ports on localhost - especially if a server - but the defense can ensure that only signed applications are allowed to do it.

Example output: 
```
[+] Serving:  localhost:8888
[+] Server reply:  hello
```

Unsigned applications should not be allowed to serve ports.

## How

> Safety: No actions beyond attempting to serve a port are done 

This test attempts to serve localhost:8888 and send it the string "hello" to determine if it is serving correctly. If successful, the test will print out "hello", if not, an error will print to console.