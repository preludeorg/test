/*
FILENAME: 61da9575-5c7e-471a-a3d7-27db8c7eea38.go
RULE: Playwright GitHub Actions
CREATED: 2023-01-18
*/
package main

import (
	_ "embed"
	Endpoint "github.com/preludeorg/test/endpoint"
	"os"
	"os/exec"
	"runtime"
)

//go:embed playwright.py
var playwright []byte

func joinPath(path string, file string) string {
	if runtime.GOOS == "windows" {
		return path + "\\" + file
	} else {
		return path + file
	}
}

var scriptPath = joinPath(os.TempDir(), "playwright.py")

func Run(command string, args []string) (int, string, string) {
	cmd := exec.Command(command, args...)
	stdout, err := cmd.Output()
	if err != nil {
		if exitError, ok := err.(*exec.ExitError); ok {
			return exitError.ExitCode(), string(stdout), string(exitError.Stderr)
		} else {
			return 1, string(stdout), err.Error()
		}
	}
	return 0, string(stdout), ""
}

func installed() {
	exitCode, stdout, stderr := run("playwright", []string{"--version"})
	if exitCode != 0 {
		print("[+] Playwright is not installed: " + stderr)
		os.Exit(104)
	}
	println("[+] Playwright installed: " + stdout)
}

func test() {
	installed()

	os.Setenv("GITHUB_REPO_NAME", "")
	os.Setenv("GITHUB_USERNAME", "")
	os.Setenv("GITHUB_PASSWORD", "")

	Endpoint.Write(scriptPath, playwright)
	exitCode, _, _ := run("python3", []string{scriptPath})
	os.Exit(exitCode)
}

func clean() {
	exitCode := Endpoint.Remove(scriptPath)
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
