#! /usr/bin/env python

# print all elements in array after splitting from string with delimiter
colors = 'red;green;blue'
x = colors.split(';')
print x[0:len(x)]

# point to new reference
b = x
if 'green' in b:
	print 'I found green'

# use range()
r = range(2)
print r
for i in range(2):
	print i

# manage the list
b.append('black')
b.insert(2, 'yellow')
b.extend([ 'lightblue', 'darkgreen' ])
print b
if 'lightblue' in b:
	index = b.index('lightblue')
	print 'lightblue %d' % index
	b.pop(index)
print b

# nuke the list	
b = []
b.append('orange')
print b
