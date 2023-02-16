/*
ID: dd270c6f-a41c-4115-b54d-ff940abd9c27
NAME: What is my IP address?
CREATED: 2023-01-21
*/
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net"
	"net/http"
	"os/exec"
	"strings"

	Endpoint "github.com/preludeorg/test/endpoint"
)

func getPublicIP() (query string, lat float64, long float64, err error) {
	response, err := http.Get("http://ip-api.com/json")
	if err != nil {
		return "", 0, 0, err
	}
	defer response.Body.Close()

	var data struct {
		Lat   float64 `json:"lat"`
		Lon   float64 `json:"lon"`
		Query string  `json:"query"`
	}

	err = json.NewDecoder(response.Body).Decode(&data)
	if err != nil {
		return "", 0, 0, err
	}

	return data.Query, data.Lat, data.Lon, nil
}

func searchShodan(ip string) {
	url := "https://www.shodan.io/search?query=" + ip
	response, err := http.Get(url)
	if err != nil {
		println("Error while searching IP on Shodan:", err)
		return
	}
	defer response.Body.Close()

	body, err := ioutil.ReadAll(response.Body)
	if err != nil {
		println("Error while reading response body:", err)
		return
	}

	if strings.Contains(string(body), "Ports open: ") {
		startIndex := strings.Index(string(body), "Ports open: ") + len("Ports open: ")
		endIndex := strings.Index(string(body)[startIndex:], "\" />")

		openPorts := string(body)[startIndex : startIndex+endIndex]
		println("Open ports found on the public IP:", openPorts)
	} else {
		println("No open ports found for the public IP on Shodan.")
	}
}

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
	println("[+] Getting Public IP Address & Location")
	query, lat, long, err := getPublicIP()
	if err != nil {
		println("Error while retrieving public IP")
		return
	}

	println("Public IP:", query)

	fmt.Printf("Latitude: %.4f\n", lat)
	fmt.Printf("Longitude: %.4f\n", long)

	println("[+] Searching IP on Shodan")
	searchShodan(query)

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
