/*
ID: 53ff0bda-537e-4493-90cf-220145d9569a
NAME: Block obfuscated behaviors
CREATED: 2023-01-06 10:54:04.264000
*/
package main

import (
	"github.com/preludeorg/test/endpoint"
	"runtime"
)

var supported = map[string][]string{
	"windows": {"powershell.exe", "-e", "dwBoAG8AYQBtAGkA"},
	"darwin":  {"bash", "-c", "base64 -d <<< d2hvYW1p | bash"},
	"linux":   {"bash", "-c", "base64 -d <<< d2hvYW1p | bash"},
}

func test() {
	command := supported[runtime.GOOS]
	result := Endpoint.Shell(command)
	println(result)
	Endpoint.Stop(101)
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
