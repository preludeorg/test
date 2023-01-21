/*
ID: 021a1dbf-e080-495c-937e-7fa79d39bf30
RULE: Adversary emulation
CREATED: 2023-01-21
*/
package main

import (
	"github.com/preludeorg/test/endpoint"
	"os"
	"runtime"
)

func command1() string {
	if runtime.GOOS == "windows" {
		return ""
	} else if runtime.GOOS == "darwin" {
		return "pwpolicy getaccountpolicies"
	} else {
		return "(([xml](Get-GPOReport -Name 'Default Domain Policy' -ReportType Xml)).GPO.Computer.ExtensionData.Extension.Account)| Select-Object Name, SettingNumber"
	}
}

func command2() string {
	if runtime.GOOS == "windows" {
		return ""
	} else {
		return "awk '$1 ~ /^P.{20}$/ {print}' ~"
	}
}

func test() {
	response1 := Endpoint.Run(command1())
	print(response1)
	if len(response1) > 0 {
		response2 := Endpoint.Run(command2())
		print(response2)
	}
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
