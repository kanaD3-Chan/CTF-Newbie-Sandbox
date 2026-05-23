package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func check(s string) bool {
	enc := []byte{
		0x8d, 0x87, 0x8a, 0x8c, 0x90, 0x8c, 0xdb, 0xb4,
		0x99, 0xd8, 0x9d, 0xd8, 0x99, 0x98, 0xd8, 0xb4,
		0x8f, 0x9c, 0xdf, 0x99, 0x8d, 0x96,
	}
	if len(s) != 22 {
		return false
	}
	for i := 0; i < 22; i++ {
		if s[i]^0xeb != enc[i] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Print("Enter the flag: ")
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	input = strings.TrimSpace(input)
	if check(input) {
		fmt.Println("Correct!")
	} else {
		fmt.Println("Wrong!")
	}
}
