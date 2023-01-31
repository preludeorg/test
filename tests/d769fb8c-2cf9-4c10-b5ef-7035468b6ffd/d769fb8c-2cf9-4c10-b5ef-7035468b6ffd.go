/*
ID: d769fb8c-2cf9-4c10-b5ef-7035468b6ffd
NAME: Enforce an outbound firewall
CREATED: 2023-01-31 07:59:52.294747
*/
package main

import (
	Endpoint "github.com/preludeorg/test/endpoint"
)

var ips = []string{
	"77.88.55.80:443", // https://yandex.com
	"104.193.88.77:443", // https://www.baidu.cn
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
	Endpoint.Stop(106)
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}

