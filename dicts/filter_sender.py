#! /usr/bin/env python

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)

count = 0
senders = dict()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    sender = words[1].rstrip()
    senders[sender] = senders.get(sender, 0) + 1
    
#print senders
max_count  = None
max_sender = None

for sender, count in senders.items():
	if max_count is None or count > max_count:
		max_count = count
		max_sender = sender

print max_sender, max_count

