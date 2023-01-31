/*
ID: d769fb8c-2cf9-4c10-b5ef-7035468b6ffd
RULE: Enforce an outbound firewall
CREATED: 2023-01-31 07:59:52.294747
*/
package main

import (
	Endpoint "github.com/preludeorg/test/endpoint"
)

var ips = []string{
	"77.88.55.80:443",
	"39.156.66.10:443",
}

func test() {
	for _, ip := range ips {
		code := Endpoint.DialTCP(ip, "hello world")
		if code == 0 {
			println("[+] Message sent successfully to", ip)
			continue
		}
		println("[-] Failed to send message to", ip)
	}
	Endpoint.Stop(101)
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}

