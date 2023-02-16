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
	"windows": {"powershell.exe", "-c", "schtasks.exe /Create /TN detect-task /SC DAILY /ST 00:00 /TR cmd.exe /C echo Hello World"},
	"darwin":  {"bash", "-c", "(crontab -l && echo \"* * * * *  echo detect-task\") | crontab -"},
	"linux":   {"bash", "-c", "(crontab -l && echo \"* * * * *  echo detect-task\") | crontab -"},
}

var cleanup = map[string][]string{
	"windows": {"powershell.exe", "-c", "schtasks.exe /Delete /TN detect-task /F"},
	"darwin":  {"bash", "-c", "crontab -l | grep -v 'detect-task' | crontab -"},
	"linux":   {"bash", "-c", "crontab -l | grep -v 'detect-task' | crontab -"},
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
