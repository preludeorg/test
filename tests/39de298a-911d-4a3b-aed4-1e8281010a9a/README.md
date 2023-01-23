# Health check

The Prelude Health Check is a basic test that checks if a device is capable of running future Verified Security Tests. 

Endpoint protection should not interfere with this test.

## How

> Safety: no code exists in the test or clean functions of this test

The health check has no business logic but instead just exits with a successful code (100) if it is runnable. 