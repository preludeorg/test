package Basic

import (
	"io/fs"
	"io/util"
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

func Write(path string, contents string) {
	b := []byte(contents)
	err := ioutil.WriteFile(path, b, 0644)
	if err != nil {
		println("[-] Failed to write " + path)
	}
}

func Exists(path string) bool {
	if _, err := os.Stat("sample.txt"); err == nil {
		return true
	} else {
		return false
	}
}

func Respond(path string, contents string) bool {
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
