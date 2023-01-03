package Endpoint

import (
	"io/fs"
	"os"
	"path/filepath"
	"time"
)

func Find(ext string) []string {
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

func Write(path string, contents []byte) {
	err := os.WriteFile(path, contents, 0644)
	if err != nil {
		println("[-] Failed to write " + path)
	}
	println("File written: " + path)
}

func Exists(path string) bool {
	if _, err := os.Stat(path); err == nil {
		println("File exists: " + path)
		return true
	} else {
		println("File does not exist: " + path)
		return false
	}
}

func Quarantined(path string, contents []byte) bool {
	Write(path, contents)
	time.Sleep(2 * time.Second)
	if Exists(path) {
		return false
	} else {
		return true
	}
}

func Remove(path string) int {
	e := os.Remove(path)
	if e != nil {
		println("[-] Failed to remove " + path)
		return 103
	}
	return 100
}
