package VST

import (
	"fmt"
	"os"
)

func Stop(code int, stage string) {
	print(fmt.Sprintf("Completed %s stage: %d", stage, code))
	os.Exit(code)
}
