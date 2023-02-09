package Endpoint

import (
	"fmt"
	"io/fs"
	"net"
	"os"
	"os/exec"
	"path/filepath"
	"time"
)

type fn func()

func Start(test fn, clean fn) {
	args := os.Args[1:]
	if len(args) > 0 {
		println("[+] Starting cleanup")
		RunWithTimeout(clean)
	} else {
		println("[+] Starting test")
		RunWithTimeout(test)
	}
}

func Stop(code int) {
	println(fmt.Sprintf("[+] Completed with code: %d", code))
	os.Exit(code)
}

func RunWithTimeout(function fn) {
    go function()
    select {
    case <- time.After(10 * time.Second):
        os.Exit(102)
    }
}

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
	time.Sleep(1 * time.Second)
	if Exists(path) {
		file, err := os.Open(path)
		if err != nil {
			return true
		}
		defer file.Close()
	}
	return false
}

func Remove(path string) bool {
	e := os.Remove(path)
	return e == nil
}

func NetworkTest(address string, message string) int {
	println("[+] Connection opening to", address)
	conn, err := net.DialTimeout("tcp", address, 15*time.Second)
	if err != nil {
		println("[-] Connection failure:", err.Error())
		return 1
	}

	_, err = conn.Write([]byte(message))
	if err != nil {
		println("[-] Write to server failed:", err.Error())
		return 2
	}

	conn.Close()
	println("[+] Client connection closing")
	return 0
}

func Serve(address string, protocol string) {
	println("[+] Serving: ", address)
	listen, err1 := net.Listen(protocol, address)
	if err1 != nil {
		println("Listener (serve) failed:", err1.Error())
		os.Exit(1)
	}
	defer listen.Close()

	conn, err2 := listen.Accept()
	if err2 != nil {
		println("[-] Listener (read) failed:", err2.Error())
		os.Exit(1)
	}

	buffer := make([]byte, 1024)
	_, err3 := conn.Read(buffer)
	if err3 != nil {
		println("[-] Connection (read) failed:", err3.Error())
	}

	conn.Write([]byte("hello"))
	conn.Close()
}

func Shell(args []string) string {
	cmd := exec.Command(args[0], args[1:]...)
	stdout, err := cmd.Output()
	if err != nil {
		if exitError, ok := err.(*exec.ExitError); ok {
			println(string(exitError.Stderr))
			os.Exit(exitError.ExitCode())
		} else {
			println(err.Error())
			os.Exit(1)
		}
	}
	return string(stdout)
}
