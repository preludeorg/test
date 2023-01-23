/*
ID: b74ad239-2ddd-4b1e-b608-8397a43c7c54
RULE: Malicious files are quarantined
CREATED: 2023-01-03
*/
package main

import (
	_ "embed"
	"github.com/preludeorg/test/endpoint"
	"github.com/preludeorg/test/vst"
)

//go:embed malicious.xlsm
var malicious []byte

func test() {
	println("[+] Extracting file for quarantine test")
	println("[+] Pausing for 2 seconds to gauge defensive reaction")
	if Endpoint.Quarantined("malicious.xlsm", malicious) {
		println("[+] Malicious file was caught!")
		VST.Stop(100)
	}
	println("[-] Malicious file was not caught")
	VST.Stop(101)
}

func clean() {
	println("[+] Ensuring malicious file is no longer present")
	status := Endpoint.Remove("malicious.xlsm")
	VST.Stop(status)
}

func main() {
	VST.Start(test, clean)
}
