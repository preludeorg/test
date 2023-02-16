/*
ID: df7e62e0-8d37-4074-8752-32fdde9dc3f2
NAME: Is Netcat installed and operational?
CREATED: 2023-02-16
*/
package main

import (
	"fmt"
	"runtime"

	Endpoint "github.com/preludeorg/test/endpoint"
)

func isNetcatInstalled() bool {
	ncCmd := "nc"
	if runtime.GOOS == "windows" {
		ncCmd = "nc.exe"
	}

	return Endpoint.Installed(ncCmd)
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
		output, err := Endpoint.Shell(command)
		if err != nil {
			println("Unable to use netcat")
			Endpoint.Stop(100)
		} else {
			println("Netcat was able to connect", output)
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
