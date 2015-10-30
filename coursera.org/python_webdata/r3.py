import re

x = 'From stephen.marquard@uct.ac.za Sat Jab 5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print y
y = re.findall('^From (\S+\@\S+)', x)
print y
