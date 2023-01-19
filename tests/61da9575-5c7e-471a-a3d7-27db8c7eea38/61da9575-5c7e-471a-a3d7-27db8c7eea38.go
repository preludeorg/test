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
	"os/exec"
	"runtime"

	Endpoint "github.com/preludeorg/test/endpoint"
)

//go:embed playwright.py
var playwright []byte

var scriptPath = os.TempDir() + "\\playwright.py"

func run(command string) (int, string, string) {
	if runtime.GOOS == "windows" {
		cmd := exec.Command("cmd.exe", "/C", command)
		stdout, err := cmd.Output()
		if err != nil {
			if exitError, ok := err.(*exec.ExitError); ok {
				return exitError.ExitCode(), string(stdout), string(exitError.Stderr)
			}
		}
		return 0, string(stdout), ""

	} else {
		cmd := exec.Command("bash", "-c", command)
		stdout, err := cmd.Output()
		if err != nil {
			if exitError, ok := err.(*exec.ExitError); ok {
				return exitError.ExitCode(), string(stdout), string(exitError.Stderr)
			}
		}
		return 0, string(stdout), ""
	}
}

func runPython(command string) (int, string, string) {
	if runtime.GOOS == "windows" {
		cmd := exec.Command("python", "-c", command)
		stdout, err := cmd.Output()
		if err != nil {
			if exitError, ok := err.(*exec.ExitError); ok {
				return exitError.ExitCode(), string(stdout), string(exitError.Stderr)
			}
		}
		return 0, string(stdout), ""
	} else {
		cmd := exec.Command("python3", "-c", command)
		stdout, err := cmd.Output()
		if err != nil {
			if exitError, ok := err.(*exec.ExitError); ok {
				return exitError.ExitCode(), string(stdout), string(exitError.Stderr)
			}
		}
		return 0, string(stdout), ""
	}
}

func installed() {
	task := fmt.Sprintf("playwright --version")
	exitCode, stdout, stderr := run(task)
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
	exitCode, _, _ := runPython("python3 " + scriptPath)
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
