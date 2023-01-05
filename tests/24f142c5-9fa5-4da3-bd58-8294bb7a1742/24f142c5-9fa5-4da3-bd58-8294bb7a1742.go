/*
NAME: 24f142c5-9fa5-4da3-bd58-8294bb7a1742.go
RULE: A macro-enabled document was executed
CREATED: 2023-01-04
*/
package main

import (
	"fmt"
	"os"

	"golang.org/x/sys/windows/registry"
)

func test() {
	exit := 101
	applications := [3]string{"Word", "Excel", "PowerPoint"}

	for _, app := range applications {
		fmt.Printf("[*] Checking %s macro-enabled documents...\n", app)
		path := fmt.Sprintf("Software\\Microsoft\\Office\\16.0\\%s\\Security\\Trusted Documents\\TrustRecords", app)
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
				fmt.Printf("Found executed macro-enabled document: %s\n", v[i])
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
