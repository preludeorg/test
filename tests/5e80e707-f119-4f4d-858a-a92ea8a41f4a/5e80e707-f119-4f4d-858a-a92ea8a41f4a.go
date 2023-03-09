/*
ID: 5e80e707-f119-4f4d-858a-a92ea8a41f4a
NAME: Can scheduled task persistence be established on my host?
CREATED: 2023-02-14
*/
package main

import (
	"bytes"
	"runtime"

	Endpoint "github.com/preludeorg/test/endpoint"
)

var supported = map[string][]string{
	"windows": {"powershell.exe", "-c", "schtasks.exe /Create /TN detect-task /SC DAILY /ST 00:00 /TR cmd.exe"},
	"darwin":  {"bash", "-c", "(crontab -l && echo \"* * * * *  echo detect-task\") | crontab -"},
	"linux":   {"bash", "-c", "(crontab -l && echo \"* * * * *  echo detect-task\") | crontab -"},
}

var remove = map[string][]string{
	"windows": {"powershell.exe", "-c", "schtasks.exe /Delete /TN detect-task /F"},
	"darwin":  {"bash", "-c", "crontab -l | grep -v 'detect-task' | crontab -"},
	"linux":   {"bash", "-c", "crontab -l | grep -v 'detect-task' | crontab -"},
}

var list = map[string][]string{
	"windows": {"powershell.exe", "-c", "schtasks.exe /query /TN detect-task"},
	"darwin":  {"bash", "-c", "crontab -l"},
	"linux":   {"bash", "-c", "crontab -l"},
}

func isTaskScheduled(output string) bool {
	command := list[runtime.GOOS]
	output, err := Endpoint.Shell(command)
	if err != nil {
		return false
	}
	if runtime.GOOS == "windows" {
		return bytes.Contains([]byte(output), []byte("detect-task"))
	} else {
		return bytes.Contains([]byte(output), []byte("echo detect-task"))
	}
}

func test() {
	command := supported[runtime.GOOS]
	output, _ := Endpoint.Shell(command)
	if isTaskScheduled(output) {
		println("[-] Scheduled task was allowed")
		Endpoint.Stop(101)
	} else {
		println("[+] Scheduled task was not allowed!")
		Endpoint.Stop(100)
	}
}

func clean() {
	command := remove[runtime.GOOS]
	Endpoint.Shell(command)
}

func main() {
	Endpoint.Start(test, clean)
}
