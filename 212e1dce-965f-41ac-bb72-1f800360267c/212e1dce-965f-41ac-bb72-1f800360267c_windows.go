/*
NAME: 212e1dce-965f-41ac-bb72-1f800360267c_windows.go
QUESTION: Are malicous macro enabled documents quarantined?
CREATED: 2022-12-28 10:49:57.012000
*/
package main

import (
    "fmt"
    "io"
    "net/http"
    "os"
    "time"
)

func downloadFile() {
	
	url := "https://github.com/bfuzzy1/randomz/raw/main/Notepad.dotm" // Needs to be changed

	response, err := http.Get(url)
	if err != nil {
		fmt.Printf("Error making GET request: %s\n", err)
		os.Exit(1)
	}
	defer response.Body.Close()

	file, err := os.Create("Notepad.dotm") // Needs to be changed
	if err != nil {
		fmt.Printf("Error creating file: %s\n", err)
		os.Exit(1)
	}
	defer file.Close()

	_, err = io.Copy(file, response.Body)
	if err != nil {
		fmt.Printf("Error writing to file: %s\n", err)
		os.Exit(1)
	}

	fmt.Println("Successfully downloaded file")
}

func checkFileExists() bool {
  time.Sleep(5 * time.Second)
  
  _, err := os.Stat("Notepad.dotm") // Needs to be changed
  if os.IsNotExist(err) {
    fmt.Println("Error: File does not exist")
    return false
  }
  fmt.Println("File exists")
  return true
}

func test() {
  fmt.Println("Run test")
  downloadFile()
  if checkFileExists() {
    clean()
  } else {
    os.Exit(100)
  }
}

func clean() {
  fmt.Println("Clean up")
  if checkFileExists() {
    err := os.Remove("Notepad.dotm") // Needs to be changed
    if err != nil {
      fmt.Printf("Error deleting file: %s\n", err)
      os.Exit(103)
    }
    fmt.Println("File deleted")
    os.Exit(101)
  }
}

func main() {
    args := os.Args[1:]
    if len(args) > 0 {
        clean()
    } else {
        test()
    }
}
