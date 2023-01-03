# Verified Security Tests

A [VST](https://docs.prelude.org/docs/tests) is a production ready TTP. 

This repository contains open-source code variants (implementations) of VSTs published by the Prelude security team.

A VST should:
- Answer a question
- Have test and clean functions, the latter reversing any effects of the former
- Exit with a standard code from the Prelude [lookup table](https://docs.prelude.org/docs/tests#results)
- Compile into a standard binary
- Be lightweight, both in footprint and resources used during execution

Variants from this repository are automatically loaded into [Build](https://build.preludesecurity.com).

### Endpoint

The Endpoint module is a shared set of functions for security tests to use. 

Install this module with:
```bash
go get -u github.com/preludeorg/test/endpoint
```