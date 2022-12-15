# Verified Security Tests

A [VST](https://docs.prelude.org/docs/tests) is a production ready TTP. 

Tests should:
- Have test and cleanup functions, the latter reversing any effects of the former
- Exit with a standard code from the Prelude [lookup table](https://docs.prelude.org/docs/tests#results)
- Be easily testable 
- Remain lightweight, both in footprint and resources used during execution

VSTs from this repository are automatically loaded into [Build](https://build.preludesecurity.com).
