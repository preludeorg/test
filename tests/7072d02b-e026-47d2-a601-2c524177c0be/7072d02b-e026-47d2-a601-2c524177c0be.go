/*
FILENAME: 7072d02b-e026-47d2-a601-2c524177c0be.go
RULE: Create GitHub test action
CREATED: 2023-01-17
*/
package main

import (
	_ "embed"
	"os"

	"github.com/preludeorg/test/endpoint"
)

//go:embed playwright.exe
var playwrightBinary []byte

func test() {
	os.Setenv("GITHUB_REPO_NAME", "")
	os.Setenv("GITHUB_USERNAME", "")
	os.Setenv("GITHUB_PASSWORD", "")
	endpoint.Write(os.TempDir()+"\\playwright.exe", playwrightBinary)
	exitCode, exitMsg := endpoint.RunNoExit(os.TempDir() + "\\playwright.exe")
	println(exitMsg)
	endpoint.Exit(exitCode)
}

func clean() {
	exitCode := endpoint.Remove(os.TempDir() + "\\playwright.exe")
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
