/*
ID: df7e62e0-8d37-4074-8752-32fdde9dc3f2
NAME: Will my host block system utilities?
CREATED: 2023-02-16
*/
package main

import (
	"fmt"
	"os/exec"
	"runtime"
	"strings"

	Endpoint "github.com/preludeorg/test/endpoint"
)

func isNetcatInstalled() bool {
	ncCmd := "nc"
	if runtime.GOOS == "windows" {
		ncCmd = "nc.exe"
	}

	_, err := exec.LookPath(ncCmd)
	if err != nil {
		return false
	}
	return true
}

var supported = map[string][]string{
	"windows": {"cmd.exe", "/c", "nc.exe -z google.com 80"},
	"darwin":  {"bash", "-c", "nc -vz google.com 80"},
	"linux":   {"bash", "-c", "nc -vz google.com 80"},
}

func test() {
	if !isNetcatInstalled() {
		println("Netcat is not installed")
		Endpoint.Stop(104)
	} else {
		command := supported[runtime.GOOS]
		fmt.Println(command)
		result := Endpoint.Shell(command)
		if strings.Contains(result, "Ncat: Connection refused") {
			println("Unable to use netcat")
			Endpoint.Stop(100)
		} else {
			println("Netcat was able to connect")
			Endpoint.Stop(101)
		}
	}
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
