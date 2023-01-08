//go:build !windows
// +build !windows

/*
FILENAME: 53ff0bda-537e-4493-90cf-220145d9569a.go
RULE: Block obfuscated scripts from running
CREATED: 2023-01-06 10:54:04.264000
*/
package main

import (
	"encoding/base64"
	"fmt"
	"os"
	"os/exec"
)

func test() {
	encoded := base64.StdEncoding.EncodeToString([]byte("whoami"))
	task := fmt.Sprintf("base64 -D <<< %s | bash", encoded)

	cmd := exec.Command("bash", "-c", task)
	stdout, err := cmd.Output()

	if err != nil {
		println(err.Error())
		os.Exit(1)
	}
	println(stdout)
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
