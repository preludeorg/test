/*
NAME: c521b330-70eb-4c4d-b748-a8869a7bac4c.go
RULE: Malicious files are quarantined
CREATED: 2023-01-03
*/
package main

import (
	_ "embed"
	"os"

	Endpoint "github.com/preludeorg/test/endpoint"
)

//go:embed malicious.go
var malicious []byte

func test() {
	println("[+] Dropping file for quarantine test")
	if Endpoint.Quarantined("malicious", malicious) {
		os.Exit(105)
	}
	os.Exit(100)
}

func clean() {
	status := Endpoint.Remove("malicious")
	os.Exit(status)
}

func main() {
	args := os.Args[1:]
	if len(args) > 0 {
		clean()
	} else {
		test()
	}
}
