/*
FILENAME: e82ea7eb-2bd5-4762-8dae-9580124da094.go
RULE: Malicious files are quarantined
CREATED: 2023-01-18
*/
package main

import (
    _ "embed"
    "os"
    "io"
    "bytes"
    "path/filepath"
    "archive/zip"

    Endpoint "github.com/preludeorg/test/endpoint"
)

//go:embed malicious.zip
var malicious []byte

func unzip() {
    Endpoint.Write(os.TempDir()+"\\malicious.zip", malicious)
    reader, err := zip.NewReader(bytes.NewReader(malicious), int64(len(malicious)))
    if err != nil {
        panic(err)
    }

    for _, f := range reader.File {
        fpath := filepath.Join(os.TempDir(), f.Name)

        if f.FileInfo().IsDir() {
            os.MkdirAll(fpath, os.ModePerm)
            continue
        }

        if err = os.MkdirAll(filepath.Dir(fpath), os.ModePerm); err != nil {
            panic(err)
        }

        inFile, err := f.Open()
        if err != nil {
            panic(err)
        }
        defer inFile.Close()

        outFile, err := os.OpenFile(fpath, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, f.Mode())
        if err != nil {
            panic(err)
        }
        defer outFile.Close()

        _, err = io.Copy(outFile, inFile)
        if err != nil {
            panic(err)
        }
    }
}

func test() {
    println("[+] Extracting file for quarantine test")
    println("[+] Pausing for 2 seconds to gauge defensive reaction")
    if Endpoint.Quarantined(os.TempDir()+"\\malicious.xlsm", malicious) {
        println("[+] Malicious file was caught!")
        os.Exit(100)
    }
    println("[-] Malicious file was not caught")
    os.Exit(101)
}

func clean() {
    exitCode := Endpoint.Remove(os.TempDir() + "\\malicious.zip")
    exitCode = Endpoint.Remove(os.TempDir() + "\\malicious.xlsm")
    os.Exit(exitCode)
}

func main() {
    args := os.Args[1:]
    if len(args) > 0 {
        clean()
    } else {
        unzip()
        test()
    }
}