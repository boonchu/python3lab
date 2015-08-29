#!/usr/bin/env python

multiply = lambda a,b: a*b
listOfInts = map(int, ['2','3','4'])

print reduce(multiply, listOfInts) 
