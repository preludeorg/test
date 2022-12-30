/*
NAME: b74ad239-2ddd-4b1e-b608-8397a43c7c54.go
QUESTION: Is there evidence of outdated applications?
CREATED: 2022-12-30
*/
package main

import (
	"os"
	"os/exec"
)

func installed(program string) bool {
	cmd := exec.Command("ls")
	stdout, err := cmd.Output()

	if err != nil {
		fmt.Println(err.Error())
		return
	}

	return a
}

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
