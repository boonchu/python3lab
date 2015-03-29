#! /usr/bin/env python

pi=3.14
# floating point to string
text = 'The value of pi is ' + str(pi)
print text

# raw string data
raw = r'this\t\n is my hello'
# string slice
print raw[1:5]

# multi line
multi = """  [this is line 1]
  [this is line 2]
  [this is line 3]  """
# detect line and replace
if multi.startswith('  [this'):
	x = multi.replace('this', 'this number')
	print x.upper()

# split from delimiter
delimiter = r'this is alex; tim; john, wilma; fred'
sp = delimiter.split(';')
print sp

# support printf like
text = '%d this little pins come out or I\'ll %s and %s and %s' % ( 3, 'huff', 'puff', 'blow down')
print text
