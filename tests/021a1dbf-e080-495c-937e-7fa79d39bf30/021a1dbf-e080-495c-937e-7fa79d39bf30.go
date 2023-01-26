/*
ID: 021a1dbf-e080-495c-937e-7fa79d39bf30
RULE: Block attempts to dumpster dive
CREATED: 2023-01-21
*/
package main

import (
	Endpoint "github.com/preludeorg/test/endpoint"
	"runtime"
)

func executor() string {
	if runtime.GOOS == "windows" {
		return "powershell.exe"
	} else {
		return "bash"
	}
}

func command1() []string {
	if runtime.GOOS == "windows" {
		return []string{"(([xml](Get-GPOReport -Name 'Default Domain Policy' -ReportType Xml)).GPO.Computer.ExtensionData.Extension.Account)| Select-Object Name, SettingNumber"}
	} else if runtime.GOOS == "darwin" {
		return []string{"-c", "pwpolicy getaccountpolicies"}
	} else {
		return []string{"-c", "cat /etc/pam.d/common-password"}
	}
}

func command2(stdout string) []string {
	if runtime.GOOS == "windows" {
		return []string{"Get-ChildItem C:/ -File -Recurse | Select-String -List -Pattern '^P.{20}$' | Select-Object -ExpandProperty Path"}
	} else {
		return []string{"-c", "cat << EOF | awk '$1 ~ /^P.{20}$/ {print}'\n" + stdout + "\nEOF"}
	}
}

func test() {
	exitCode, stdout, stderr := Endpoint.Run(executor(), command1())
	if exitCode != 0 {
		println(stderr)
		Endpoint.Stop(exitCode)
	}
	println(stdout)

	exitCode2, stdout2, stderr2 := Endpoint.Run(executor(), command2(stdout))
	if exitCode2 != 0 {
		println(stderr2)
		Endpoint.Stop(exitCode)
	}
	println(stdout2)
	Endpoint.Stop(100)
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
