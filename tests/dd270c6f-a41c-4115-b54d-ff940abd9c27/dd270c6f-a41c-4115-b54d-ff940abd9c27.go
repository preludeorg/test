/*
ID: dd270c6f-a41c-4115-b54d-ff940abd9c27
RULE: Protect user privacy
CREATED: 2023-01-21
*/
package main

import (
	Endpoint "github.com/preludeorg/test/endpoint"
	"runtime"
)

func command() (string, []string) {
	var command string
	var args []string
	if runtime.GOOS == "windows" {
		command = "powershell.exe"
		args = []string{"Invoke-RestMethod -UseBasicParsing -Uri ('http://ipinfo.io/'+ (Invoke-WebRequest -UseBasicParsing -uri 'http://ifconfig.me/ip').Content)"}
	} else {
		command = "bash"
		args = []string{"-c", "wget -qO- http://ifconfig.me/ip | wget -qO- http://ipinfo.io/$1"}
	}
	return command, args
}

func test() {
	command, args := command()
	exitCode, stdout, stderr := Endpoint.Run(command, args)
	if exitCode != 0 {
		println(stderr)
		Endpoint.Stop(exitCode)
	}
	println(stdout)
	Endpoint.Stop(exitCode)
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
