/*
FILENAME: 53ff0bda-537e-4493-90cf-220145d9569a.go
RULE: Block obfuscated scripts from running
CREATED: 2023-01-06 10:54:04.264000
*/
package main

import (
	"fmt"
	"github.com/preludeorg/test/endpoint"
	"os"
	"runtime"
)

func test() {
	if runtime.GOOS == "windows" {
		encoded := "dwBoAG8AYQBtAGkA"
		task := fmt.Sprintf("powershell.exe -e %s", encoded)
		stdout := Endpoint.Run(task)
		println(stdout)
		os.Exit(100)
	} else {
		encoded := "d2hvYW1p"
		task := fmt.Sprintf("base64 -d <<< %s | bash", encoded)
		stdout := Endpoint.Run(task)
		println(stdout)
		os.Exit(100)
	}
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
