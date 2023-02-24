/*
ID: 0cf97096-b3b2-4dda-b6ef-ab92b0eadaba
NAME: Are your SSH Private Key permissions restricted?
CREATED: 2023-02-24 09:33:03.227000
*/
package main

import (
	"fmt"
	"os"

	"github.com/preludeorg/test/endpoint"
)

func test() {
	dirname, err := os.UserHomeDir()
	if err != nil {
		println("[-] Unable get home directory")
		Endpoint.Stop(104)
		return
	}
	println("[+] Found home directory")

	s, err := os.Stat(fmt.Sprintf("%s/.ssh/id_rsa", dirname))
	if err != nil {
		println("[-] SSH Private Key not found")
		Endpoint.Stop(104)
		return
	}

	println("[+] Found SSH Private Key")

	if s.Mode().Perm() == 0o600 || s.Mode().Perm() == 0o400 {
		println("[+] SSH Private Key permissions are restricted")
		Endpoint.Stop(100)
		return
	}

	println("[-] SSH Private Key permissions are too open")
	Endpoint.Stop(101)
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
