/*
NAME: 082e2303-cc14-4854-b72f-b77ea1e1acd8.c
QUESTION: Is there evidence of an Operator C2 agent?
CREATED: 2022-12-30
*/
package main

import (
	"io/fs"
	"os"
	"path/filepath"
)

func find(ext string) []string {
	dirname, _ := os.UserHomeDir()
	var a []string
	filepath.WalkDir(dirname, func(s string, d fs.DirEntry, e error) error {
		if e == nil {
			if filepath.Ext(d.Name()) == ext {
				println("[+] Found:", s)
				a = append(a, s)
			}
		}
		return nil
	})
	return a
}

func test() {
	println("[*] Running test")
	evidence := find("pneuma")
	if evidence != nil {
		println("[!] Discovered evidence of LockBit ransomware")
		os.Exit(101)
	}
	os.Exit(100)
}

func clean() {
	println("[*] Running clean")
	os.Exit(100)
}

func main() {
	args := os.Args[1:]
	if len(args) > 0 {
		clean()
	} else {
		test()
	}
}
