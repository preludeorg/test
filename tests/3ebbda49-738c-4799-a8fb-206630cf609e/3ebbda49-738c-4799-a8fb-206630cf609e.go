/*
ID: 3ebbda49-738c-4799-a8fb-206630cf609e
NAME: Will a long running VST be stopped properly?
CREATED: 2023-03-13 16:27:09.604918
*/
package main

import (
	Endpoint "github.com/preludeorg/test/endpoint"
)

func test() {
	println("[+] Sleeping for 15 seconds")
	Endpoint.Shell([]string{"sleep", "15"})
	println("[-] VST did not stop properly, returned exit code 101")
	Endpoint.Stop(101)
}

func main() {
	Endpoint.Start(test)
}
