#! /usr/bin/env python

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)

count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    words[1] = words[1].rstrip()
    print words[1]
    count += 1
    
print "There were " + str(count) + " lines in the file with From as the first word"

