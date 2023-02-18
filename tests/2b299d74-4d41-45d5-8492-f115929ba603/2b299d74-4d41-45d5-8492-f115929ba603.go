/*
ID: 2b299d74-4d41-45d5-8492-f115929ba603
NAME: Passwordless priv escalation
CREATED: 2023-02-17
*/
package main

import (
	"runtime"
	"os/exec"

	Endpoint "github.com/preludeorg/test/endpoint"
)

var nocreds = map[string][]string{
	"windows": {"powershell", "-c", "echo '' | runas /user:$env:computername\\administrator /savecred whoami"},
	"darwin":  {"bash", "-c", "echo '' | sudo -S whoami"},
	"linux":   {"bash", "-c", "echo '' | sudo -S whoami"},
}

func test() {
	cmd := exec.Command(nocreds[runtime.GOOS][0], nocreds[runtime.GOOS][1:]...)
  _, err := cmd.Output()

	if err != nil {    
		println("[+] Passwordless escalation failed!")
		Endpoint.Stop(105)
	}

	println("[+] Passwordless escalation succeeded!")
	Endpoint.Stop(101)
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
