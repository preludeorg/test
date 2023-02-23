/*
ID: d1f90df0-de33-431f-b9f5-f73569d18b7b
NAME: Will my host detect an attempted ping sweep?
CREATED: 2023-02-17 10:45:43.815000
*/
package main

import (
	"encoding/binary"
	"net"
	"os/exec"
	"sync"

	Endpoint "github.com/preludeorg/test/endpoint"
)

func Hosts(netw string) []string {
	_, ipv4Net, err := net.ParseCIDR(netw)
	if err != nil {
		println(err)
	}
	mask := binary.BigEndian.Uint32(ipv4Net.Mask)
	start := binary.BigEndian.Uint32(ipv4Net.IP)
	finish := (start & mask) | (mask ^ 0xffffffff)
	var hosts []string
	for i := start + 1; i <= finish-1; i++ {
		ip := make(net.IP, 4)
		binary.BigEndian.PutUint32(ip, i)
		hosts = append(hosts, ip.String())
	}
	return hosts
}

func pingSweep() {
	b := false
	interfaces, err := net.Interfaces()
	if err != nil {
		println(err)
		return
	}

	var wg sync.WaitGroup
	var mutex sync.Mutex

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
			var ipRange *net.IPNet
			var ipAddr *net.IPAddr
			switch v := addr.(type) {
			case *net.IPNet:
				if v.IP.To4() != nil {
					ipRange = v
				}
			case *net.IPAddr:
				if v.IP.To4() != nil {
					ipAddr = v
				}
			}
			if ipRange != nil || ipAddr != nil {
				hosts := Hosts(ipRange.String())
				for _, host := range hosts {
					wg.Add(1)
					go func(host string) {
						defer wg.Done()
						cmd := exec.Command("ping", "-c", "1", "-t", "1", host)
						if err := cmd.Run(); err == nil {
							mutex.Lock()
							println(host + " is up")
							mutex.Unlock()
							b = true
						}
					}(host)
				}
			}
		}
	}
	wg.Wait()
	if b {
		Endpoint.Stop(101)
	}
}

func test() {
	println("[+] Ping Sweep")
	pingSweep()

	Endpoint.Stop(106)
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
