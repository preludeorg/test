/*
ID: 53ff0bda-537e-4493-90cf-220145d9569a
NAME: Block obfuscated behaviors
CREATED: 2023-01-06 10:54:04.264000
*/
package main

import (
	"runtime"
	"strings"

	Endpoint "github.com/preludeorg/test/endpoint"
)

var supported = map[string][]string{
	"windows": {"powershell.exe", "-e", "ZQBjAGgAbwAgAC0AbgAgAFAAcgBlAGwAdQBkAGUA"},
	"darwin":  {"bash", "-c", "base64 -d <<< ZWNobyAtbiBQcmVsdWRl | bash"},
	"linux":   {"bash", "-c", "base64 -d <<< ZWNobyAtbiBQcmVsdWRl | bash"},
}

func test() {
	command := supported[runtime.GOOS]
	result := Endpoint.Shell(command)
	if strings.Contains(result, "Prelude") {
		println(result)
		Endpoint.Stop(101)
	} else {
		Endpoint.Stop(100)
	}
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
