/*
ID: 021a1dbf-e080-495c-937e-7fa79d39bf30
RULE: Adversary emulation
CREATED: 2023-01-21
*/
package main

import (
	"github.com/preludeorg/test/endpoint"
	"github.com/preludeorg/test/vst"
	"runtime"
)

func command1() string {
	if runtime.GOOS == "windows" {
		return "(([xml](Get-GPOReport -Name 'Default Domain Policy' -ReportType Xml)).GPO.Computer.ExtensionData.Extension.Account)| Select-Object Name, SettingNumber"
	} else if runtime.GOOS == "darwin" {
		return "pwpolicy getaccountpolicies"
	} else {
		return "cat /etc/pam.d/common-password"
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
	VST.Stop(101)
}

func clean() {
	VST.Stop(100)
}

func main() {
	VST.Start(test, clean)
}
