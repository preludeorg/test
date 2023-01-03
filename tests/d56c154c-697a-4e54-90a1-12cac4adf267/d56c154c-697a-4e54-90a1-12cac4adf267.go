/*
NAME: d56c154c-697a-4e54-90a1-12cac4adf267.go
OBSERVATION: LockBit ransomware infection
CREATED: 2023-01-03
*/
package main

import (
	"github.com/preludeorg/test/endpoint"
	"os"
)

func test() {
	evidence := Endpoint.Find(".lockbit")
	if evidence != nil {
		println("[!] Discovered evidence of LockBit ransomware")
		os.Exit(101)
	}
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
