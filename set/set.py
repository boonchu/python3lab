#! /usr/bin/env python

a = set([1, 2, 3, 4])
b = set([3, 4, 5, 6])
union = a|b 
print union
diff = a - b
print diff
intersect = a & b
print intersect
