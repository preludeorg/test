/*
ID: 87f45943-055d-4bb1-9ef5-a1497f277935
RULE: Quarantine malicious files
CREATED: 2023-01-22 10:43:39.988000
*/
package main

import (
	_ "embed"
	"os"
	"path/filepath"

	Endpoint "github.com/preludeorg/test/endpoint"
)

//go:embed Seatbelt.exe
var seatbelt []byte
var binPath = filepath.Join(os.TempDir(), "Seatbelt.exe")

func test() {
	Endpoint.Write(binPath, seatbelt)
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
