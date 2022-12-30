/*
NAME: 39de298a-911d-4a3b-aed4-1e8281010a9a.c
QUESTION: Health check
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
