/*
NAME: 39de298a-911d-4a3b-aed4-1e8281010a9a.go
RULE: Health check
CREATED: 2023-01-03
*/
package main

import "os"

func test() {
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
