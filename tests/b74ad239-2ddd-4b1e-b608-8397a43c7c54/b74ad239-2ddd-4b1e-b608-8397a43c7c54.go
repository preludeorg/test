/*
ID: b74ad239-2ddd-4b1e-b608-8397a43c7c54
RULE: Malicious files are quarantined
CREATED: 2023-01-03
*/
package main

import (
	_ "embed"
	"github.com/preludeorg/test/endpoint"
	"os"
)

//go:embed malicious.xlsm
var malicious []byte

func test() {
	println("[+] Extracting file for quarantine test")
	println("[+] Pausing for 2 seconds to gauge defensive reaction")
	if Endpoint.Quarantined("malicious.xlsm", malicious) {
		println("[+] Malicious file was caught!")
		os.Exit(100)
	}
	println("[-] Malicious file was not caught")
	os.Exit(101)
}

func clean() {
	println("[+] Ensuring malicious file is no longer present")
	status := Endpoint.Remove("malicious.xlsm")
	os.Exit(status)
}

func main() {
	args := os.Args[1:]
	if len(args) > 0 {
		clean()
	} else {
		test()
	}
}
