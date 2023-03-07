/*
ID: d769fb8c-2cf9-4c10-b5ef-7035468b6ffd
NAME: Attempt to write data to a foreign country
CREATED: 2023-01-31 07:59:52.294747
*/
package main

import (
	Endpoint "github.com/preludeorg/test/endpoint"
)

var ips = []string{
	"77.88.55.80:443",   // https://yandex.com
	"104.193.88.77:443", // https://www.baidu.cn
}

func test() {
	exit := 106
	for _, ip := range ips {
		code := Endpoint.NetworkTest(ip, "hello world")
		if code == 0 {
			println("[+] Message sent successfully to ", ip)
			exit = 101
		} else {
			println("[-] Failed to send message to ", ip)
		}
	}
	Endpoint.Stop(exit)
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	defer clean()
	Endpoint.Start(test)
}
