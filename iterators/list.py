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

x = list(firstn(fibonacci(), 100))
ix = iter(x)
while ix:
    try:
	print ix.next()
    except StopIteration:
	print 'end of list'
	break
