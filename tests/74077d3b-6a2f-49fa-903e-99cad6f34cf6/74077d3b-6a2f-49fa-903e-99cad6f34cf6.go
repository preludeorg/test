/*
ID: 74077d3b-6a2f-49fa-903e-99cad6f34cf6
NAME: Will your computer quarantine oRAT malware?
CREATED: 2023-02-28
*/
package main

import (
	_ "embed"

	Endpoint "github.com/preludeorg/test/endpoint"
)

//go:embed oRAT
var malicious []byte

func test() {
	println("[+] Extracting file for quarantine test")
	println("[+] Pausing for 1 second to gauge defensive reaction")
	if Endpoint.Quarantined("oRAT", malicious) {
		println("[+] Malicious file was caught!")
		Endpoint.Stop(105)
	}
	println("[-] Malicious file was not caught")
	Endpoint.Stop(101)
}

func clean() {
	println("[+] Ensuring malicious file is no longer present")
	if Endpoint.Remove("oRAT") {
		Endpoint.Stop(100)
	}
	Endpoint.Stop(105)
}

func main() {
	Endpoint.Start(test, clean)
}
