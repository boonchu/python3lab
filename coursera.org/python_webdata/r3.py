import re

# fine-tuning string extraction
x = 'From stephen.marquard@uct.ac.za Sat Jab 5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print '1 \S+@\S+ ', y
y = re.findall('^From (\S+\@\S+)', x)
print '2 ^From (\S+\@\S+) ', y
y = re.findall('F.+:', x)
print '3 F.+: ', y
y = re.findall('\S+?@\S+', x)
print '4 \S+?@\S+ ', y

# low level fine-tuning string extraction
atpos = x.find('@')
print atpos
sppos = x.find(' ', atpos)
print sppos
host = x[atpos+1 : sppos]
print host

# double split pattern
words = x.split()
email = words[1]
pieces = email.split('@')
print pieces[1]

# Regex version of string extraction
# @ - start with @
# [^ ] - single non-chacter
# * - zero or more
y = re.findall('@([^ ]*)', x)
print y

# final version
y = re.findall('^From .*@([^ ]*)', x)
print y
