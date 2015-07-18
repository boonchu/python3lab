#! /usr/bin/env python

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)

hours = dict()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    words[5] = words[5].rstrip()
    hour = words[5].split(':')[0]
    #print hour
    hours[hour] = hours.get(hour, 0) + 1

# version 1
#for k, v in sorted(hours.items()):
#    print k, v

# version 2
#keys = hours.keys()
#keys.sort()
#for k in keys:
#    print k, hours[k]

# version 3
# insertion sort list
# https://www.youtube.com/watch?v=lEA31vHiry4
#list = hours.keys()
#for index in range(1, len(list)):
#	value = list[index]
#	i = index - 1
#	while i >= 0 :
#		if value < list[i]:
#			list[i+1] = list[i]
#			list[i] = value
#			i = i - 1
#		else:
#			break	

# version 4
# simpler insertion sort list
# https://www.youtube.com/watch?v=6pyeMmJTefg
list = hours.keys()
for index in range(1, len(list)):
        value = list[index]
        i = index - 1
        while i >= 0 and (value < list[i]):
           list[i+1] = list[i]
           list[i] = value
           i = i - 1

for key in list:
    print key, hours[key]
