#! /usr/bin/env python

# returns with square value from list
a = [1,2,3,4]
square = map(lambda x: x**2, a)
print square

# set mult3 to [0, 3, 6, 9] for original list that contains value with multiple by 3.
b = range(10)
mult3 = filter(lambda x: x % 3 == 0, b)
print mult3
