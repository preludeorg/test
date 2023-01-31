/*
ID: 021a1dbf-e080-495c-937e-7fa79d39bf30
NAME: Block attempts to dumpster dive
CREATED: 2023-01-21
*/
package main

import (
	"github.com/preludeorg/test/endpoint"
	"runtime"
)

var policy = map[string][]string{
	"windows": {"powershell.exe", "-c", "(([xml](Get-GPOReport -Name 'Default Domain Policy' -ReportType Xml)).GPO.Computer.ExtensionData.Extension.Account)| Select-Object Name, SettingNumber"},
	"darwin":  {"bash", "-c", "pwpolicy getaccountpolicies"},
	"linux":   {"bash", "-c", "cat /etc/pam.d/common-password"},
}

var search = map[string][]string{
	"windows": {"powershell.exe", "-c", "Get-ChildItem C:/ -File -Recurse | Select-String -List -Pattern '^P.{20}$' | Select-Object -ExpandProperty Path"},
	"darwin":  {"bash", "-c", "awk '$1 ~ /^P.{20}$/ {print}' ~"},
	"linux":   {"bash", "-c", "awk '$1 ~ /^P.{20}$/ {print}' ~"},
}

func test() {
	passwordPolicy := Endpoint.Shell(policy[runtime.GOOS])
	print(passwordPolicy)
	if len(passwordPolicy) > 0 {
		passwords := Endpoint.Shell(search[runtime.GOOS])
		print(passwords)
	}
	Endpoint.Stop(101)
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
