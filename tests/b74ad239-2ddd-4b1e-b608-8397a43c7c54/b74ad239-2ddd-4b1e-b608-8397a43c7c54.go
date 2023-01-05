/*
NAME: b74ad239-2ddd-4b1e-b608-8397a43c7c54.go
RULE: Malicious files are quarantined
CREATED: 2023-01-03
*/
package main

import (
	_ "embed"
	"github.com/preludeorg/test/endpoint"
	"os"
)

//go:embed malicious.xlsm
var malicious []byte

func test() {
	println("[+] Dropping file for quarantine test")
	if Endpoint.Quarantined("malicious.xlsm", malicious) {
		os.Exit(100)
	}
	os.Exit(101)
}

func clean() {
	status := Endpoint.Remove("malicious.xlsm")
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
