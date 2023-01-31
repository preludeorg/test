/*
ID: dd270c6f-a41c-4115-b54d-ff940abd9c27
RULE: Protect user privacy
CREATED: 2023-01-21
*/
package main

import (
	"github.com/preludeorg/test/endpoint"
	"runtime"
)

var supported = map[string][]string{
	"windows": {"powershell.exe", "-c", "Invoke-RestMethod -UseBasicParsing -Uri ('http://ipinfo.io/'+ (Invoke-WebRequest -UseBasicParsing -uri 'http://ifconfig.me/ip').Content)"},
	"darwin":  {"bash", "-c", "wget -qO- http://ifconfig.me/ip | wget -qO- http://ipinfo.io/$1"},
	"linux":   {"bash", "-c", "wget -qO- http://ifconfig.me/ip | wget -qO- http://ipinfo.io/$1"},
}

func test() {
	command := supported[runtime.GOOS]
	response := Endpoint.Shell(command)
	print(response)
	Endpoint.Stop(101)
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
