#! /usr/bin/env python 

line = "Mississippi borders Tennessee."
counts = dict()
for letter in line:
    if letter in counts:
        counts[letter] += 1
    else:
        counts[letter] = 1

for k,v in counts.items():
    print '{0}:{1}'.format(k, '#' * int(v))
