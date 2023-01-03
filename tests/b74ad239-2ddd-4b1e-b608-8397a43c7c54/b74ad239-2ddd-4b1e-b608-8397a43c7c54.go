/*
NAME: b74ad239-2ddd-4b1e-b608-8397a43c7c54.go
RULE: Quarantine a benign file
CREATED: 2023-01-03
*/
package main

import (
	_ "embed"
	"github.com/preludeorg/test/endpoint"
	"os"
)

//go:embed malicious.xlsx
var special []byte

func test() {
	println("[*] Running test")
	if Endpoint.Quarantined("nonsense.xlsx", special) {
		os.Exit(105)
	}
	os.Exit(100)
}

func clean() {
	println("[*] Running clean")
	code := Endpoint.Remove("nonsense.xlsx")
	os.Exit(code)
}

func main() {
	args := os.Args[1:]
	if len(args) > 0 {
		clean()
	} else {
		test()
	}
}
