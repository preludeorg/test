/*
FILENAME: 6c167bf1-e6d3-4a8a-8c50-aa2da53b7fb5.go
RULE: Ghostpack binaries should not run
CREATED: 2023-01-22 11:07:25.006000
*/
package main

import (
	_ "embed"
	"os"
	"os/exec"
	"runtime"

	Endpoint "github.com/preludeorg/test/endpoint"
)

//go:embed Sharpwmi.exe
var seatbelt []byte

func joinPath(path string, file string) string {
	if runtime.GOOS == "windows" {
		return path + "\\" + file
	} else {
		return path + file
	}
}

var binPath = joinPath(os.TempDir(), "Seatbelt.exe")

func run(command string, args []string) (int, string, string) {
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

func test() {
	Endpoint.Write(binPath, seatbelt)
	exitCode, _, _ := run("cmd.exe", []string{"/C", binPath})
	if exitCode == 0 {
		os.Exit(101)
	} else {
		os.Exit(100)
	}
}

func clean() {
	exitCode := Endpoint.Remove(binPath)
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
