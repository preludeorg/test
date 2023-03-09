/*
ID: 39de298a-911d-4a3b-aed4-1e8281010a9a
NAME: Health check
CREATED: 2023-01-03
*/
package main

import (
	Endpoint "github.com/preludeorg/test/endpoint"
)

func test() {
	Endpoint.Stop(100)
}

func clean() {
}

func main() {
	Endpoint.Start(test, clean)
}
