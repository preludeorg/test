/*
ID: 53ff0bda-537e-4493-90cf-220145d9569a
RULE: Block obfuscated behaviors
CREATED: 2023-01-06 10:54:04.264000
*/
package main

import (
	"runtime"
	"strings"

	Endpoint "github.com/preludeorg/test/endpoint"
)

func test() {
	if runtime.GOOS == "windows" {
		encoded := "ZQBjAGgAbwAgAC0AbgAgAFAAcgBlAGwAdQBkAGUA"
		exitCode, stdout, stderr := Endpoint.Run("powershell.exe", []string{"-e", encoded})
		if strings.Contains(stdout, "Prelude") {
			Endpoint.Stop(101)
		}
		if exitCode != 0 {
			println(stderr)
			Endpoint.Stop(1)
		}
		println(stdout)
	} else {
		encoded := "ZWNobyAtbiBQcmVsdWRl"
		cmd := "base64 -d <<< " + encoded + " | bash"
		exitCode, stdout, stderr := Endpoint.Run("bash", []string{"-c", cmd})
		if strings.Contains(stdout, "Prelude") {
			Endpoint.Stop(101)
		}
		if exitCode != 0 {
			println(stderr)
			Endpoint.Stop(1)
		}
		println(stdout)
	}
	Endpoint.Stop(100)
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
