/*
FILENAME: 86b7b817-1264-4b3b-a23e-434f351c8c9c.go
RULE: Change GitHub User Password
CREATED: 2023-01-17
*/
package main

import (
	"embed"
	"os"

	"github.com/preludeorg/test/endpoint"
)

//go:embed playwright_password_change.exe
var playwrightBinary []byte

func test() {
	os.Setenv("GITHUB_USERNAME", "")
	os.Setenv("GITHUB_PASSWORD", "")
	endpoint.Write(os.TempDir()+"\\playwright_password_change.exe", playwrightBinary)
	exitCode, exitMsg := endpoint.RunNoExit(os.TempDir() + "\\playwright_password_change.exe")
	println(exitMsg)
	endpoint.Exit(exitCode)
}

func clean() {
	exitCode := endpoint.Remove(os.TempDir() + "\\playwright_password_change.exe")
	os.Exit(exitCode)
}

func main() {
	args := os.Args[1:]
	if len(args) > 0 {
		clean()
	} else {
		test()
	}
}
