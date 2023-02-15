/*
ID: 188af3a0-5a0d-4afe-8300-6b48915edba0
NAME: What hosts can I RDP or SSH into in my environment?
*/
package main

import (
	"fmt"
	"net"
	"sync"
	"time"

	Endpoint "github.com/preludeorg/test/endpoint"
)

func portScan() bool {
	addrs, err := net.InterfaceAddrs()
	if err != nil {
		panic(err)
	}

	var localIP net.IP
	for _, addr := range addrs {
		ipnet, ok := addr.(*net.IPNet)
		if ok && !ipnet.IP.IsLoopback() && ipnet.IP.To4() != nil {
			localIP = ipnet.IP
			break
		}
	}

	println("[+] Scanning network for open ports:")

	var wg sync.WaitGroup

	targetSubnet := localIP.Mask(net.CIDRMask(24, 32))
	openPorts := make(map[string]bool)
	var count int

	for i := 1; i <= 254; i++ {
		targetIP := net.IPv4(targetSubnet[0], targetSubnet[1], targetSubnet[2], byte(i))
		ports := []int{22, 3389}

		for _, port := range ports {
			wg.Add(1)
			go func(targetIP net.IP, port int) {
				defer wg.Done()
				target := fmt.Sprintf("%s:%d", targetIP.String(), port)
				conn, err := net.DialTimeout("tcp", target, 1*time.Second)
				if err == nil {
					conn.Close()
					openPorts[fmt.Sprintf("Port %d is open on %s", port, targetIP.String())] = true
					count++
				}
			}(targetIP, port)
		}
	}

	wg.Wait()

	if count == 0 {
		println("No hosts found with port 22 or port 3389 open")
		return false
	} else {
		for result := range openPorts {
			println(result)
		}
		return true
	}
}

func test() {
	openPorts := portScan()
	if openPorts {
		Endpoint.Stop(101)
	} else {
		Endpoint.Stop(100)
	}
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
