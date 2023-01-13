package Endpoint

import (
	"io/fs"
	"net"
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

func Read(path string) []byte {
	bit, err := os.ReadFile(path)
	if err != nil {
		println(err)
	}
	return bit
}

func Write(path string, contents []byte) {
	err := os.WriteFile(path, contents, 0644)
	if err != nil {
		println("[-] Failed to write " + path)
	}
}

func Exists(path string) bool {
	if _, err := os.Stat(path); err == nil {
		return true
	} else {
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
		return 103
	}
	return 100
}

func DialTCP(address string, message string) string {
	tcpAddr, err := net.ResolveTCPAddr("tcp", address)
	if err != nil {
		println("Failed to resolve:", err.Error())
		os.Exit(1)
	}

	conn, err := net.DialTCP("tcp", nil, tcpAddr)
	if err != nil {
		println("Connection failure:", err.Error())
		os.Exit(1)
	}

	_, err = conn.Write([]byte(message))
	if err != nil {
		println("Write to server failed:", err.Error())
		os.Exit(1)
	}

	reply := make([]byte, 1024)

	_, err = conn.Read(reply)
	if err != nil {
		println("Write to server failed:", err.Error())
		os.Exit(1)
	}

	conn.Close()
	return string(reply)
}
