#! /usr/bin/env python

import re
import fileinput

file_handler = fileinput.input('mbox-short.txt')
raw_domains = list()
for line in file_handler:
	search = re.findall('^From .*@([^ ]+) ', line)
	if len(search) > 0: 
		raw_domains.append(search)

# collecting raw domains
print raw_domains
	
digest_domains = list()
for d in raw_domains:
	for x in d:
		digest_domains.append(x)	

# combine results to one array
print digest_domains

# ** constructs dict from domains data **
domains_counts = dict()
# constructs a dictionary from domains data (original)
for d in digest_domains: 
	domains_counts[d] = domains_counts.get(d, 0) + 1

# counts by lambda
for k, v in sorted(domains_counts.iteritems(), key=lambda (k, v): (v, k), reverse=True):
	print k, v
