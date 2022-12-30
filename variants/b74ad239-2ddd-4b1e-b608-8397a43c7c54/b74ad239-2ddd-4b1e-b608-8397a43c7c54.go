/*
NAME: b74ad239-2ddd-4b1e-b608-8397a43c7c54.go
QUESTION: Does the endpoint respond to a benign file?
CREATED: 2022-12-30
*/
package main

import (
	_ "embed"
	"github.com/preludeorg/test/endpoint"
	"os"
)

//go:embed nonsense.txt
var special string

func test() {
	println("[*] Running test")
	if Endpoint.Respond("nonsense.txt", special) {
		os.Exit(105)
	}
	os.Exit(100)
}

func clean() {
	println("[*] Running clean")
	code := Endpoint.Remove("nonsense.txt")
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
