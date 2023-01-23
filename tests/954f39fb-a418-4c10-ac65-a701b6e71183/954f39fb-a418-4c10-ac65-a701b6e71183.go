/*
ID: 954f39fb-a418-4c10-ac65-a701b6e71183
RULE: The device should not serve a network-connectable port
CREATED: 2023-01-03
*/
package main

import (
	"github.com/preludeorg/test/endpoint"
	"github.com/preludeorg/test/vst"
	"time"
)

func test() {
	go Endpoint.Serve("localhost:8888", "tcp")
	time.Sleep(1 * time.Second)

	code := Endpoint.DialTCP("localhost:8888", "hello")
	if code == 0 {
		VST.Stop(101)
	}
	VST.Stop(100)
}

func clean() {
	VST.Stop(100)
}

func main() {
	VST.Start(test, clean)
}
