/*
NAME: fdf82548-69a9-4e7e-b8e9-11f127c309dd.go
QUESTION: Can we use playwright to test a webapp?
CREATED: 2023-01-05 11:23:52.646000
*/
package main

import (
	"fmt"
	"log"
	"os"

	"github.com/playwright-community/playwright-go"
)

func assertErrorToNilf(message string, err error) {
	if err != nil {
		log.Fatalf(message, err)
	}
}

func initialize(url string) (*playwright.Playwright, playwright.Browser, playwright.Page) {
	pw, err := playwright.Run()
	assertErrorToNilf("could not launch playwright: %w", err)

	// Create browser
	browser, err := pw.Chromium.Launch(playwright.BrowserTypeLaunchOptions{
		Headless: playwright.Bool(false),
	})
	assertErrorToNilf("could not launch Chromium: %w", err)

	// Create a context
	context, err := browser.NewContext()
	assertErrorToNilf("could not create context: %w", err)

	// Create a page to navigate around with.
	page, err := context.NewPage()
	assertErrorToNilf("could not create page: %w", err)
	_, err = page.Goto(url)
	assertErrorToNilf("could not goto: %w", err)

	return pw, browser, page
}

func test() {
	url := "http://127.0.0.1:8080/login.php"
	pw, browser, page := initialize(url)
	// Enter Username
	assertErrorToNilf("could not click: %v", page.Click("input#inputUsername.form-control"))
	assertErrorToNilf("could not type: %v", page.Type("input#inputUsername.form-control", "prelude"))

	// Enter Password
	assertErrorToNilf("could not click: %v", page.Click("input#inputPassword.form-control"))
	assertErrorToNilf("could not type: %v", page.Type("input#inputPassword.form-control", "password"))

	// Login
	assertErrorToNilf("Could not press: %v", page.Press("input#inputPassword.form-control", "Enter"))

	// Exit
	assertErrorToNilf("could not close browser: %w", browser.Close())
	assertErrorToNilf("could not stop Playwright: %w", pw.Stop())
	os.Exit(100)
}

func clean() {
	fmt.Println("Clean up")
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
