/*
ID: 53ff0bda-537e-4493-90cf-220145d9569a
RULE: Block obfuscated behaviors
CREATED: 2023-01-06 10:54:04.264000
*/
package main

import (
	"github.com/preludeorg/test/endpoint"
	"runtime"
)

func test() {
	if runtime.GOOS == "windows" {
		encoded := "dwBoAG8AYQBtAGkA"
		exitCode, stdout, stderr := Endpoint.Run("powershell.exe", []string{"-e", encoded})
		if exitCode != 0 {
			println(stderr)
			Endpoint.Stop(1)
		}
		println(stdout)
	} else {
		encoded := "d2hvYW1p"
		cmd := "base64 -d <<< " + encoded + " | bash"
		exitCode, stdout, stderr := Endpoint.Run("bash", []string{"-c", cmd})
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
