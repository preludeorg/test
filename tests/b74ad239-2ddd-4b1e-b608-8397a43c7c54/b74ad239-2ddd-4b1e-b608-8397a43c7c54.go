/*
ID: b74ad239-2ddd-4b1e-b608-8397a43c7c54
NAME: Will your computer quarantine a malicious Office document?
CREATED: 2023-01-03
*/
package main

import (
	_ "embed"

	Endpoint "github.com/preludeorg/test/endpoint"
)

//go:embed malicious.xlsm
var malicious []byte

func test() {
	println("[+] Extracting file for quarantine test")
	println("[+] Pausing for 1 second to gauge defensive reaction")
	if Endpoint.Quarantined("malicious.xlsm", malicious) {
		println("[+] Malicious file was caught!")
		Endpoint.Stop(105)
	}
	println("[-] Malicious file was not caught")
	Endpoint.Stop(101)
}

func main() {
	Endpoint.Start(test)
}
