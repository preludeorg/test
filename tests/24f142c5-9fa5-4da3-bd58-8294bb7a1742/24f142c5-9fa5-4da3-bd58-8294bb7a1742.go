/*
NAME: macro.go
RULE: Has a macro-enabled document been executed
CREATED: 2023-01-04
*/
package main

import (
	"golang.org/x/sys/windows/registry"
	"os"
	"regexp"
	"runtime"
)

func test() {
	if runtime.GOOS != "windows" {
		println("This is a Windows-only test")
		os.Exit(104) // The test is not relevant to the endpoint
	}

	exit := 101
	errors := 0
	applications := [3]string{"Word", "Excel", "PowerPoint"}
	office_path := "Software\\Microsoft\\Office"

	k, err := registry.OpenKey(registry.CURRENT_USER, office_path, registry.QUERY_VALUE|registry.ENUMERATE_SUB_KEYS)
	if err != nil {
		if err.Error() == "The system cannot find the file specified." {
			println("Office is not installed.")
			k.Close()
			os.Exit(exit)
		} else {
			println("Error opening registry key: HKCU\\" + office_path)
			println(err.Error())
			k.Close()
			os.Exit(1)
		}
	}
	defer k.Close()

	office_versions, _ := k.ReadSubKeyNames(-1)

	for i := 0; i < len(office_versions); i++ {
		matched, err := regexp.MatchString(`\d{1,2}\.\d`, office_versions[i])
		if err != nil {
			println("Error matching Office version string: " + office_versions[i])
			println(err.Error())
			os.Exit(1)
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
						os.Exit(1)
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
		os.Exit(1)
	}
	os.Exit(exit)
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
