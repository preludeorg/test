/*
ID: 5e80e707-f119-4f4d-858a-a92ea8a41f4a
NAME: Can persistence be established on my host?
CREATED: 2023-02-14
*/
package main

import (
	"runtime"

	Endpoint "github.com/preludeorg/test/endpoint"
)

var supported = map[string][]string{
	"windows": {"powershell.exe", "-c", "schtasks.exe", "/Create", "/TN", "detect-task", "/SC", "DAILY", "/ST", "00:00", "/TR", "cmd.exe", "/C", "echo Hello World"},
	"darwin":  {"bash", "-c", "echo Hello World | at now + 1 minute", "detect-task"},
	"linux":   {"bash", "-c", "echo Hello World | at now + 1 minute", "detect-task"},
}

var cleanup = map[string][]string{
	"windows": {"powershell.exe", "-c", "schtasks.exe", "/Delete", "/TN", "detect-task", "/F"},
	"darwin":  {"bash", "-c", "at -l | awk '/detect-task/ {print $1}' | xargs -I{} at -r {}"},
	"linux":   {"bash", "-c", "at -l | awk '/detect-task/ {print $1}' | xargs -I{} at -r {}"},
}

func test() {
	command := supported[runtime.GOOS]
	Endpoint.Shell(command)
	Endpoint.Stop(101)
}

func clean() {
	command := cleanup[runtime.GOOS]
	Endpoint.Shell(command)
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
