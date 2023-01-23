package VST

import (
	"fmt"
	"os"
)

type fn func()

func Start(test fn, clean fn) {
	args := os.Args[1:]
	if len(args) > 0 {
		println("Starting cleanup")
		clean()
	} else {
		println("Starting test")
		test()
	}
}

func Stop(code int) {
	println(fmt.Sprintf("Completed with code: %d", code))
	os.Exit(code)
}
