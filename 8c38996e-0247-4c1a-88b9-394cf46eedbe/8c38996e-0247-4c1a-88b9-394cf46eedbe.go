/*
NAME: 8c38996e-0247-4c1a-88b9-394cf46eedbe.go
QUESTION: Are there macro enabled Office documents on this host?
CREATED: 2022-12-29 09:23:45.285000
*/
package main

import (
	"archive/zip"
	"fmt"
	"io/fs"
	"io/ioutil"
	"os"
	"path/filepath"
	"strings"
)

type myCloser interface {
	Close() error
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func closeFile(f myCloser) {
	err := f.Close()
	check(err)
}

func readAll(file *zip.File) []byte {
	fc, err := file.Open()
	check(err)
	defer closeFile(fc)

	content, err := ioutil.ReadAll(fc)
	check(err)

	return content
}

func find_files(root string) []string {
	extensions := [10]string{
		".docm",
		".doc",
		".dotm",
		".xlsm",
		".xltm",
		".xls",
		".pptm",
		".potm",
		".ppsm",
		".ppt",
	}
	var a []string
	filepath.WalkDir(root, func(s string, d fs.DirEntry, e error) error {
		check(e)
		for _, ext := range extensions {
			if filepath.Ext(d.Name()) == ext {
				a = append(a, s)
			}
		}
		return nil
	})
	return a
}

func handle_macro() int {
	val := 101
	if err := os.Mkdir("/tmp/macros", os.ModePerm); err != nil {
		panic(err)
	}
	home_dirname, e := os.UserHomeDir()
	check(e)
	dst_file := "/tmp/macros/macro_file"
	for _, s := range find_files(home_dirname) {
		input, err := ioutil.ReadFile(s)
		check(err)

		err = ioutil.WriteFile(dst_file, input, 0777)
		check(err)

		zf, err := zip.OpenReader(dst_file)
		if err != nil {
			continue
		}
		defer closeFile(zf)
		for _, file := range zf.File {
			if strings.Contains(string(readAll(file)), "Sub") {
				fmt.Println(s)
				val = 100
				break
			}
		}
		if strings.Contains(string(input), "Sub") {
			fmt.Println(s)
			val = 100
		}
		e := os.Remove("/tmp/macros/macro_file")
		check(e)
	}
	return val
}

func test() {
	if handle_macro() == 100 {
		os.Exit(100)
	} else {
		os.Exit(101)
	}
}

func clean() {
	fmt.Println("Clean up")
	e := os.RemoveAll("/tmp/macros")
	check(e)
	os.Exit(100)
}

func main() {
	args := os.Args[1:]
	if len(args) > 0 {
		clean()
	} else {
		test()
	}
}
