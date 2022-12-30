/*
NAME: 6f16602a-2cb4-4004-b3c6-0e80fbef708c.go
QUESTION:
CREATED: 2022-12-30
*/
package main

import (
	"os"
)

func test() {
	println("[*] Running test")
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
