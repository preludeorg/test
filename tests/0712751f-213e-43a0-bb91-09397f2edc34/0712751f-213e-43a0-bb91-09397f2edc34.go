/*
ID: 0712751f-213e-43a0-bb91-09397f2edc34
NAME: Download Homebrew
CREATED: 2023-02-24 05:30:23.575000
*/
package main

import (
	"github.com/preludeorg/test/endpoint"
	"fmt"
)

var installURL = "https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh"
var uninstallURL = "https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh"

func test() {
	if Endpoint.IsAvailable("brew") {
	    println("[+] Brew is already installed")
	    Endpoint.Stop(104)
	}
    cmd = fmt.Sprintf("curl -fsSL %s | NONINTERACTIVE=1 /bin/bash", installURL)
	response, err := Endpoint.Shell([]string{"bash", "-c", cmd})
	print(response)
    if err != nil {
	    Endpoint.Stop(100)
    }
	Endpoint.Stop(101)
}

func clean() {
    if Endpoint.IsAvailable("brew") {
        Endpoint.Stop(100)
    }
    cmd = fmt.Sprintf("curl -fsSL %s | NONINTERACTIVE=1 /bin/bash", uninstallURL)
	response, err := Endpoint.Shell([]string{"bash", "-c", cmd})
    print(response)
    if err != nil {
	    Endpoint.Stop(103)
    }
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
