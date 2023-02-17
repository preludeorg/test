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
	"net/http"
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

func test() {
	println("[+] Getting Public IP Address & Location")
	query, lat, long, err := getPublicIP()
	if err != nil {
		println("Error while retrieving public IP")
	}

	println("Public IP:", query)

	fmt.Printf("Latitude: %.4f\n", lat)
	fmt.Printf("Longitude: %.4f\n", long)

	println("[+] Searching IP on Shodan")
	searchShodan(query)

	Endpoint.Stop(101)
}

func clean() {
	Endpoint.Stop(100)
}

func main() {
	Endpoint.Start(test, clean)
}
