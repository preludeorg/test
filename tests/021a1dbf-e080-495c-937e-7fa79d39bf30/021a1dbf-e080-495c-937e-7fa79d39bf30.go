/*
ID: 021a1dbf-e080-495c-937e-7fa79d39bf30
NAME: Block attempts to dumpster dive
CREATED: 2023-01-21
*/
package main

import (
	"runtime"

	Endpoint "github.com/preludeorg/test/endpoint"
)

var policy = map[string][]string{
	"windows": {"powershell.exe", "-c", "net accounts"},
	"darwin":  {"bash", "-c", "pwpolicy getaccountpolicies"},
	"linux":   {"bash", "-c", "cat /etc/pam.d/common-password"},
}

var search = map[string][]string{
	"windows": {"powershell.exe", "-c", "Get-ChildItem %userprofile% -File -Recurse | Select-String -List -Pattern '^P.{20}$' | Select-Object -ExpandProperty Path"},
	"darwin":  {"bash", "-c", "find ~ -maxdepth 1 -type f -exec grep -E ^P.{20} {} \\;"},
	"linux":   {"bash", "-c", "find ~ -maxdepth 1 -type f -exec grep -E ^P.{20} {} \\;"},
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
