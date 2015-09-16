#! /usr/bin/env python

l1 = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
print l1

l1 = [map(int, nested_list) for nested_list in l1]
print l1
