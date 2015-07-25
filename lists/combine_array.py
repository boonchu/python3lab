#! /usr/bin/env python
# https://www.python.org/dev/peps/pep-0202/
# List Comprehensions - PEP 202

x = range(10)
print x
y = [ 2*a for a in x if a % 2 == 1 ]
print y

nums = [1, 2, 3, 4]
fruit = ["Apples", "Peaches", "Pears", "Bananas"]
print [(i,f) for i in nums for f in fruit]

import re
print [(i,f) for i in nums for f in fruit if re.findall('P.*', f)]
