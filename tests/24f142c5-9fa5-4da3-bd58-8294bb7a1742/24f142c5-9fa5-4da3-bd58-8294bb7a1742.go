/*
NAME: macro.go
RULE: Has a macro-enabled document been executed
CREATED: 2023-01-04
*/
package main

import (
	"os"

	"golang.org/x/sys/windows/registry"
)

func test() {
	exit := 101
	applications := [3]string{"Word", "Excel", "PowerPoint"}

	for _, app := range applications {
		println("[*] Checking " + app + " macro-enabled documents...")
		path := "Software\\Microsoft\\Office\\16.0\\" + app + "\\Security\\Trusted Documents\\TrustRecords"
		k, err := registry.OpenKey(registry.CURRENT_USER, path, registry.QUERY_VALUE)
		if err != nil {
			println(err.Error())
		}
		defer k.Close()

		v, err := k.ReadValueNames(-1)
		if err != nil {
			println(err.Error())
		}

		for i := 0; i < len(v); i++ {
			s, _, err := k.GetBinaryValue(v[i])
			if err != nil {
				println(err.Error())
			}
			if s[len(s)-4] == 0xff && s[len(s)-3] == 0xff && s[len(s)-2] == 0xff && s[len(s)-1] == 0x7f {
				println("Found executed macro-enabled document: " + v[i])
				exit = 100
			}
		}
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
