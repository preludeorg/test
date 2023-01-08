# Verified Security Tests

A [VST](https://docs.prelude.org/docs/tests) is a production ready TTP. Tests from this repository are automatically loaded into [Build](https://build.preludesecurity.com). You can run these tests by using [Detect](https://docs.prelude.org/docs/detect-getting-started).

## What is production ready?

Tests that are safe to execute, run reliably every time, and produce a standardized output are considered production ready.

A VST should:
- Answer a question, exiting with a standard code from the Prelude [lookup table](https://docs.prelude.org/docs/tests#results)
- Have test and clean functions, the latter reversing any effects of the former
- Compile into a standard binary
- Be lightweight, both in footprint and resources used during execution 

## An example

The [Malicious files are quarantined](https://github.com/preludeorg/test/blob/master/tests/b74ad239-2ddd-4b1e-b608-8397a43c7c54/b74ad239-2ddd-4b1e-b608-8397a43c7c54.go) test verifies if your endpoint defense is responding to a known malicious file. 

It does this by first embedding a malicious .xlsm file into the test:
```go
//go:embed malicious.xlsm
var malicious []byte
```

During the test it runs the ``Quarantined`` check, which writes the file to disk, waits 2s, and evaluates if the file was removed. If the check returns true the test exists with a 100 (good/expected) otherwise it exits with a 101 (bad/unexpected).
```go
if Endpoint.Quarantined("malicious.xlsm", malicious) {
	println("[+] Malicious file was caught!")
	os.Exit(100)
}
println("[-] Malicious file was not caught")
os.Exit(101)
```

Finally, the clean function ensures the malicious .xlsm file is removed from the disk, exiting with either a 100 (good/expected) or 103 (bad/cleanup failure) status:
```go
status := Endpoint.Remove("malicious.xlsm")
os.Exit(status)
```

## Write your own tests

The Endpoint module is a shared set of functions for security tests to use. Shared functions revolve around common needs, such as writing or reading files or downloading files from the internet.

If developing tests locally, install the Go module:
```bash
go get -u github.com/preludeorg/test/endpoint
```

Then use any of the included functions in your own tests. Note a few use cases in the example above.
