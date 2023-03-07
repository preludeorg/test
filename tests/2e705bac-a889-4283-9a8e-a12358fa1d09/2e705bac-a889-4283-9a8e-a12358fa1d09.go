/*
ID: 2e705bac-a889-4283-9a8e-a12358fa1d09
NAME: Will your computer quarantine Royal Ransomware?
CREATED: 2023-02-22
*/
package main

import (
	_ "embed"

	Endpoint "github.com/preludeorg/test/endpoint"
)

//go:embed 09a79e5e20fa4f5aae610c8ce3fe954029a91972b56c6576035ff7e0ec4c1d14.elf
var malicious []byte

func test() {
	println("[+] Extracting file for quarantine test")
	println("[+] Pausing for 1 second to gauge defensive reaction")
	if Endpoint.Quarantined("09a79e5e20fa4f5aae610c8ce3fe954029a91972b56c6576035ff7e0ec4c1d14.elf", malicious) {
		println("[+] Malicious file was caught!")
		Endpoint.Stop(105)
	}
	println("[-] Malicious file was not caught")
	Endpoint.Stop(101)
}

func clean() {
	println("[+] Ensuring malicious file is no longer present")
	if Endpoint.Remove("09a79e5e20fa4f5aae610c8ce3fe954029a91972b56c6576035ff7e0ec4c1d14.elf") {
		Endpoint.Stop(100)
	}
	Endpoint.Stop(105)
}

func main() {
	defer clean()
	Endpoint.Start(test)
}
