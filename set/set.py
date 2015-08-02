#! /usr/bin/env python

a = set([1, 2, 2, 4, 6, 8])
print ' a from [1, 2, 2, 4, 6, 8] is set of ', a
a.remove(6)
print ' a after remove 6 is ', a

a = set([1, 2, 3, 4])
b = set([3, 4, 5, 6])
print ' a is ', a
print ' b is ', b
union = a|b 
print ' a union b == ', union
diff = a - b
print ' a diff b == ', diff
intersect = a & b
print ' a intersect b == ', intersect

s = set([1, 2, 3, 4])
t = s
print ' s is ', s
print ' t is ', t
s.intersection_update([3,4,5,6])
print ' s is after intersect with [3,4,5,6] ', s
print ' how about t? ', t


s = set([1, 2, 3])
t = set([2, 3, 4])
r = s
s.intersection_update(t)
q = s.union(r)
print q


