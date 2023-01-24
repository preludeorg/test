/*
ID: b74ad239-2ddd-4b1e-b608-8397a43c7c54
RULE: Quarantine malicious files
CREATED: 2023-01-03
*/
package main

import (
	_ "embed"
	"github.com/preludeorg/test/endpoint"
)

//go:embed malicious.xlsm
var malicious []byte

func test() {
	println("[+] Extracting file for quarantine test")
	println("[+] Pausing for 2 seconds to gauge defensive reaction")
	if Endpoint.Quarantined("malicious.xlsm", malicious) {
		println("[+] Malicious file was caught!")
		Endpoint.Stop(100)
	}
	println("[-] Malicious file was not caught")
	Endpoint.Stop(101)
}

func clean() {
	println("[+] Ensuring malicious file is no longer present")
	if Endpoint.Remove("malicious.xlsm") {
		Endpoint.Stop(100)
	}
	Endpoint.Stop(105)
}

func main() {
	Endpoint.Start(test, clean)
}
