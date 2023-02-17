/*
ID: d1f90df0-de33-431f-b9f5-f73569d18b7b
NAME: Will my host detect an attempted ping sweep?
CREATED: 2023-02-17 10:45:43.815000
*/
package main

import (
	"net"
	"os/exec"

	Endpoint "github.com/preludeorg/test/endpoint"
)

func pingSweep() {
	interfaces, err := net.Interfaces()
	if err != nil {
		println(err)
		return
	}

	for _, i := range interfaces {
		if i.Flags&net.FlagUp == 0 {
			continue
		}
		if i.Flags&net.FlagLoopback != 0 {
			continue
		}
		addrs, err := i.Addrs()
		if err != nil {
			println(err)
			return
		}
		for _, addr := range addrs {
			var ip net.IP
			switch v := addr.(type) {
			case *net.IPNet:
				ip = v.IP
			case *net.IPAddr:
				ip = v.IP
			}
			if ip == nil || ip.IsLoopback() {
				continue
			}
			if ip.To4() != nil {
				ipStr := ip.String()
				cmd := exec.Command("ping", "-c", "1", "-t", "1", ipStr)
				if err := cmd.Run(); err != nil {
					println(ipStr, "is down")
				} else {
					println(ipStr, "is up and belongs to", i.HardwareAddr.String())
				}
			}
		}
	}
}

func test() {
	println("[+] Ping Sweep")
	pingSweep()

	Endpoint.Stop(101)
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
