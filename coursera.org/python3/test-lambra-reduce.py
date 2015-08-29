#!/usr/bin/env python
# http://stackoverflow.com/questions/9712507/trying-to-use-reduce-and-lambda-with-a-list-containing-strings
from operator import mul as multiply

multiply = lambda a,b: a*b
listOfInts = map(int, ['2','3','4'])

print reduce(multiply, listOfInts) 
