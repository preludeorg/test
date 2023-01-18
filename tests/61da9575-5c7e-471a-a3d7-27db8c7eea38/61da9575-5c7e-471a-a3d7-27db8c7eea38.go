/*
FILENAME: 61da9575-5c7e-471a-a3d7-27db8c7eea38.go
RULE: Playwright GitHub Actions
CREATED: 2023-01-18
*/
package main

import (
	_ "embed"
	"fmt"
	"os"

	Endpoint "github.com/preludeorg/test/endpoint"
)

//go:embed playwright.py
var playwright []byte

func installed() {
		task := fmt.Sprintf("playwright --version")
		stdout := Endpoint.Run(task)
		println(stdout)
	}

func test() {
 	os.Setenv("GITHUB_REPO_NAME", "")
 	os.Setenv("GITHUB_USERNAME", "")
 	os.Setenv("GITHUB_PASSWORD", "")

 	Endpoint.Write(os.TempDir()+"\\playwright.py", playwright)

 	scriptPath := os.TempDir()+"\\playwright.py"
 	Endpoint.Run("python3 " + scriptPath)
 	os.Exit(100)
 }

 func clean() {
 	exitCode := Endpoint.Remove(os.TempDir() + "\\playwright.py")
 	os.Exit(exitCode)
 }

func main() {
	args := os.Args[1:]
	if len(args) > 0 {
		clean()
	} else {
		installed()
		test()
	}
}