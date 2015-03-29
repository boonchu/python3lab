#! /usr/bin/env python

a = [ 4, 3490, 30, -2, 10 ]
print sorted(a)
print sorted(a, reverse=True)

strs = [ 'CCc', 'AaAA', 'd', 'bb' ]
print sorted(strs, key=len)
print sorted(strs, key=str.lower)

multi = """ This is professor from Birmingham to give
 an introduction class training to all professional
 students around the world. Students should be attending
 from schedule time that provide on the meeting invite. 
 Delay is not professionally acceptable. Please be ontime.
"""
lines = multi.split('\n')
def sorting(s):
	return s[-1]
for i in lines:
	a = i.split(' ')
	print sorted(a, key=len)
