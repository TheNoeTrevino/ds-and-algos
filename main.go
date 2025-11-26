package main

import "fmt"

func PrintHello(foo string) {
	fmt.Print(foo)
}

func main() {
	foo := "foo"
	PrintHello(foo)
}
