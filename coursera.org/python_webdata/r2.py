#! /usr/bin/env python

import re

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print y

y = re.findall('[AEIOU]+', x)
print y

x = 'From: using the : character'
y = re.findall('^F.+:', x)
print y
