# Verified Security Tests

A [VST](https://docs.prelude.org/docs/tests) is a production ready TTP. Tests from this repository are automatically loaded into [Build](https://build.preludesecurity.com).

## What is production ready?

Tests that are safe to execute, run reliably every time, and produce a standardized output are considered production ready.

A VST should:
- Answer a question
- Have test and clean functions, the latter reversing any effects of the former
- Exit with a standard code from the Prelude [lookup table](https://docs.prelude.org/docs/tests#results)
- Compile into a standard binary
- Be lightweight, both in footprint and resources used during execution 

### Endpoint

The Endpoint module is a shared set of functions for security tests to use. 

If developing tests locally, install the Go module:
```bash
go get -u github.com/preludeorg/test/endpoint
```

Then use any of the included functions in your own tests.
