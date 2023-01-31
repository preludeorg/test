/*
ID: 954f39fb-a418-4c10-ac65-a701b6e71183
NAME: Block server capabilities
CREATED: 2023-01-03
*/
package main

import (
	"github.com/preludeorg/test/endpoint"
	"time"
)

func test() {
	go Endpoint.Serve("localhost:8888", "tcp")
	time.Sleep(1 * time.Second)

	code := Endpoint.DialTCP("localhost:8888", "hello")
	if code == 0 {
		Endpoint.Stop(101)
	}
	Endpoint.Stop(100)
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
