#! /usr/bin/env python

import re
import fileinput

file_handler = fileinput.input('mbox-short.txt')
raw_emails = list()
for line in file_handler:
	search = re.findall('[A-Z,a-z,0-9,\.]+@[A-Z,a-z,0-9,\.]+', line)
	if len(search) > 0: 
		raw_emails.append(search)

# collecting raw emails
#print emails
	
digest_emails = list()
for email in raw_emails:
	for x in email:
		digest_emails.append(x)	

# combine results to one array
#print digest_emails

# ** constructs dict from email data **
email_counts = dict()
# constructs a dictionary from email data (original)
for email in digest_emails: 
	email_counts[email] = email_counts.get(email, 0) + 1

# constructs a dictionary from email data (dictionary comprehension)
# http://stackoverflow.com/questions/14507591/python-dictionary-comprehension
#email_counts = { email: email_counts.get(email, 0) + 1 for email in digest_emails }
#email_counts = dict( (email, email_counts.get(email, 0) + 1) for email in digest_emails )
#print email_counts

# ** sort by values **
# http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
# 
# counts email addresses (original)
#for email in sorted(email_counts, key=email_counts.get, reverse=True):
#	print email, email_counts[email]

# counts by lambda
for k, v in sorted(email_counts.iteritems(), key=lambda (k, v): (v, k), reverse=True):
	if v > 10: print k, v

# counts by collections (OrderedDict)
#from collections import OrderedDict
#for email in OrderedDict(sorted(email_counts.items(), key=lambda x: x[1], reverse=True)):
#	if email_counts[email] > 10: print email, email_counts[email]

# counts by collections (Counter)
#from collections import Counter
#counter = Counter(email_counts)
#for k, v in counter.most_common():
#	if v > 10: print k, v
