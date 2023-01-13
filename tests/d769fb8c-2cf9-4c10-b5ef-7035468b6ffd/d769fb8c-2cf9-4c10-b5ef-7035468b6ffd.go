/*
FILENAME: d769fb8c-2cf9-4c10-b5ef-7035468b6ffd.go
RULE: Block outbound network requests to specific countries
CREATED: 2023-01-13 07:01:44.793000
*/
package main

import (
	"github.com/preludeorg/test/endpoint"
	"os"
)

func test() {
	resp := Endpoint.DialTCP("77.88.55.80:443", "hello world")
	println("Server responded:", resp)
	os.Exit(100)
}

func clean() {
	os.Exit(100)
}

func main() {
	args := os.Args[1:]
	if len(args) > 0 {
		clean()
	} else {
		test()
	}
}
