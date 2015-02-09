#! /usr/bin/env python2

import psycopg2
import markdown
import markdown.extensions.tables

print "Content-type: text/html"
print ""
print '''
<html>
<head>
<title>Show Ticket App</title>
</head>
<body>'''

conn = psycopg2.connect("dbname=postgres user=bigchoo")
query = conn.cursor()
query.execute("SELECT * FROM mydb.ticket;")
rows = query.fetchall()
conn.commit()
query.close()
conn.close()

content = """
List of Ticket 
=============

Section 
-------

Ticket No | Ticket Title
--------- | ------------
"""

for row in rows:
	content += str(row[1]) + "|" + row[2] + "\n"

print markdown.markdown(content, extensions=['markdown.extensions.tables'])

print '''
</body>
</html>'''
