/*
ID: d769fb8c-2cf9-4c10-b5ef-7035468b6ffd
RULE: Enforce an outbound firewall
CREATED: 2023-01-24
*/
package main

import (
	"github.com/preludeorg/test/endpoint"
)

func test() {
	code := Endpoint.DialTCP("77.88.55.80:443", "hello world")
	if code == 0 {
		Endpoint.Stop(101)
	}
	Endpoint.Stop(100)
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
