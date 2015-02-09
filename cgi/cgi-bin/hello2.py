#!/usr/bin/env python2

import markdown

print "Content-type: text/html"
print ""
print ''' 
<html>
<head>
<title>Hello Word - First CGI Program</title>
</head>
<body>
<h2>Hello Word! This is my first CGI program</h2>'''

content = """
Chapter 
=======

Section 
-------

* item 1
* item 2
"""

print markdown.markdown(content)

print '''
</body>
</html>'''
