/*
ID: 07d31938-92fa-40aa-b8af-77a54055f481
NAME: Will your computer quarantine Redline Stealer?
CREATED: 2023-02-28
*/
package main

import (
	_ "embed"

	Endpoint "github.com/preludeorg/test/endpoint"
)

//go:embed redline.exe
var malicious []byte

func test() {
	println("[+] Extracting file for quarantine test")
	println("[+] Pausing for 1 second to gauge defensive reaction")
	if Endpoint.Quarantined("redline.exe", malicious) {
		println("[+] Malicious file was caught!")
		Endpoint.Stop(105)
	}
	println("[-] Malicious file was not caught")
	Endpoint.Stop(101)
}

func clean() {
	println("[+] Ensuring malicious file is no longer present")
	if Endpoint.Remove("redline.exe") {
		Endpoint.Stop(100)
	}
	Endpoint.Stop(105)
}

func main() {
	Endpoint.Start(test, clean)
}
