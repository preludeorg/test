//go:build windows || !darwin || !linux
// +build windows !darwin !linux

/*
NAME: 24f142c5-9fa5-4da3-bd58-8294bb7a1742.go
RULE: Has a macro-enabled document been executed
CREATED: 2023-01-04
*/

package main

import (
	"golang.org/x/sys/windows/registry"
	"os"
	"regexp"
	"runtime"

	"github.com/preludeorg/test/endpoint"
)

func test() {
	exit := 101
	errors := 0
	applications := [3]string{"Word", "Excel", "PowerPoint"}
	office_path := "Software\\Microsoft\\Office"

	k, err := registry.OpenKey(registry.CURRENT_USER, office_path, registry.QUERY_VALUE|registry.ENUMERATE_SUB_KEYS)
	if err != nil {
		if err.Error() == "The system cannot find the file specified." {
			println("Office is not installed.")
			k.Close()
			Endpoint.Stop(104)
		} else {
			println("Error opening registry key: HKCU\\" + office_path)
			println(err.Error())
			k.Close()
			Endpoint.Stop(1)
		}
	}
	defer k.Close()

	office_versions, _ := k.ReadSubKeyNames(-1)

	for i := 0; i < len(office_versions); i++ {
		matched, err := regexp.MatchString(`\d{1,2}\.\d`, office_versions[i])
		if err != nil {
			println("Error matching Office version string: " + office_versions[i])
			println(err.Error())
			Endpoint.Stop(1)
		}

		if matched {
			println("[*] Checking Office version: " + office_versions[i])
			for _, app := range applications {
				println("[*] Checking " + app + " macro-enabled documents...")
				path := "Software\\Microsoft\\Office\\16.0\\" + app + "\\Security\\Trusted Documents\\TrustRecords"
				k, err := registry.OpenKey(registry.CURRENT_USER, path, registry.QUERY_VALUE)
				if err != nil {
					if err.Error() == "The system cannot find the file specified." {
						continue
					} else {
						println("Error opening registry key: HKCU\\" + path)
						println(err.Error())
						k.Close()
						Endpoint.Stop(1)
					}
				}
				defer k.Close()

				v, _ := k.ReadValueNames(-1)

				for i := 0; i < len(v); i++ {
					s, _, err := k.GetBinaryValue(v[i])
					if err != nil {
						println("Error reading registry key binary value: " + v[i])
						println(err.Error())
						errors = 1
					}
					if s[len(s)-4] == 0xff && s[len(s)-3] == 0xff && s[len(s)-2] == 0xff && s[len(s)-1] == 0x7f {
						println("Found executed macro-enabled document: " + v[i])
						exit = 100
					}
				}
			}
		}
	}
	if errors > 0 && exit == 101 {
		Endpoint.Stop(1)
	}
	Endpoint.Stop(exit)
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
