/*
ID: dd270c6f-a41c-4115-b54d-ff940abd9c27
RULE: Adversary emulation
CREATED: 2023-01-21
*/
package main

import (
	"github.com/preludeorg/test/endpoint"
	"os"
	"runtime"
)

func command() string {
	if runtime.GOOS == "windows" {
		return "Invoke-RestMethod -UseBasicParsing -Uri ('http://ipinfo.io/'+ (Invoke-WebRequest -UseBasicParsing -uri 'http://ifconfig.me/ip').Content)"
	} else {
		return "wget -qO- http://ifconfig.me/ip | wget -qO- http://ipinfo.io/$1"
	}
}

func test() {
	response := Endpoint.Run(command())
	print(response)
	os.Exit(100)
}

func clean() {
	os.Exit(100)
}

func main() {
	args := os.Args[1:]
	if len(args) > 0 {
		clean()
	} else {
		test()
	}
}
