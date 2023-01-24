# Verified Security Tests

A [VST](https://docs.preludesecurity.com/docs/tests) is a production ready TTP. Tests from this repository are automatically loaded into [Build](https://platform.preludesecurity.com). You can run these tests on endpoints by using [Detect](https://docs.preludesecurity.com/docs/detect-getting-started).

## What is production ready?

Tests that are safe to execute, run reliably every time, and produce a standardized output are considered production ready.

A VST should:
- Answer a question, exiting with a standard code from the Prelude [lookup table](https://docs.preludesecurity.com/docs/tests#results)
- Have test and clean functions, the latter reversing any effects of the former
- Compile into a standard binary specific to an OS/architecture

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
	Endpoint.Stop(100)
}
println("[-] Malicious file was not caught")
Endpoint.Stop(101)
```

Finally, the clean function ensures the malicious .xlsm file is removed from the disk, exiting with either a 100 (good/expected) or 105 (file was already removed) status:
```go
if Endpoint.Remove("malicious.xlsm") {
    Endpoint.Stop(100)
}
Endpoint.Stop(105)
```

## Quick start

Run any test in this project by first installing the Endpoint module:
```bash
go get -u github.com/preludeorg/test/endpoint
```

Then compile any test:
```
go build -o test <UUID>.go
```

And run the test with ``./test`` and clean up function with ``./test cleanup``. Evaluate the exit code of each to check passed/failed state.
