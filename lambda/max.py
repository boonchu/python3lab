#! /usr/bin/env python

list = [47,11,42,102,13]
f = lambda a,b: a if (a > b) else b
print reduce(f, list)
