#! /usr/bin/env python

d = { 'a':10, 'b':1, 'c':22 }
print d

# simple code for sort in reverse order
# 
#tmp = list()
#for k, v in d.items():
#	tmp.append( (v, k) )
#print tmp
#tmp.sort(reverse=True)
#print tmp
# 
# advanced version of sort in reverse order
# 
print sorted( [ (v, k) for k, v in d.items() ], reverse=True )

