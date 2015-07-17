#! /usr/bin/env python 

items = list()
a, b = (0, 1)
n=0
while n <= 40:
	items.append(b)
	a, b = b, a+b
	n += 1

print max(items)
