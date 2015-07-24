#! /usr/bin/env python 

def fibonacci():
    """Ein Fibonacci-Zahlen-Generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def firstn(g, n):
	for i in range(n):
		yield g.next()

print list(firstn(fibonacci(), 1000))
