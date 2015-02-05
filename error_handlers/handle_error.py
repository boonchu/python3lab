#!/usr/bin/env python3

x = input("Enter number at this prompt: (you can try alphanumeric) ")

try:
	int(x)
	print("value is an integer")
except ValueError:
	print("valiue is not an integer")
