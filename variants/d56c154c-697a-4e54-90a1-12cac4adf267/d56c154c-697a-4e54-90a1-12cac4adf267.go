/*
NAME: d56c154c-697a-4e54-90a1-12cac4adf267.c
QUESTION: Is there evidence of LockBit ransomware?
CREATED: 2022-12-30
*/
package main

import (
	"github.com/preludeorg/test/basic"
	"os"
)

func test() {
	println("[*] Running test")
	evidence := basic.Find(".lockbit")
	if evidence != nil {
		println("[!] Discovered evidence of LockBit ransomware")
		os.Exit(101)
	}
	os.Exit(100)
}

func clean() {
	println("[*] Running clean")
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
