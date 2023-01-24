/*
ID: 6c167bf1-e6d3-4a8a-8c50-aa2da53b7fb5
RULE: Quarantine malicious files
CREATED: 2023-01-22 11:07:25.006000
*/
package main

import (
	_ "embed"
	"os"
	"path/filepath"

	Endpoint "github.com/preludeorg/test/endpoint"
)

//go:embed SharpWMI.exe
var sharpwmi []byte
var binPath = filepath.Join(os.TempDir(), "SharpWMI.exe")

func test() {
	Endpoint.Write(binPath, sharpwmi)
	exitCode, _, _ := Endpoint.Run("cmd.exe", []string{"/C", binPath})
	if exitCode == 0 {
		Endpoint.Stop(101)
	} else {
		exitCode := Endpoint.Remove(binPath)
		Endpoint.Stop(exitCode)
	}
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
