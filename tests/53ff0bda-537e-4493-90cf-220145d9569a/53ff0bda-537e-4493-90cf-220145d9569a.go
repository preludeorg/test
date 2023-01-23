/*
ID: 53ff0bda-537e-4493-90cf-220145d9569a
RULE: Block obfuscated scripts from running
CREATED: 2023-01-06 10:54:04.264000
*/
package main

import (
	"fmt"
	"github.com/preludeorg/test/endpoint"
	"github.com/preludeorg/test/vst"
	"runtime"
)

func test() {
	if runtime.GOOS == "windows" {
		encoded := "dwBoAG8AYQBtAGkA"
		task := fmt.Sprintf("powershell.exe -e %s", encoded)
		stdout := Endpoint.Run(task)
		println(stdout)
	} else {
		encoded := "d2hvYW1p"
		task := fmt.Sprintf("base64 -d <<< %s | bash", encoded)
		stdout := Endpoint.Run(task)
		println(stdout)
	}
	VST.Stop(101)
}

func clean() {
	VST.Stop(100)
}

func main() {
	VST.Start(test, clean)
}
