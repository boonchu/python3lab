#! /usr/bin/env python

import sqlite3

conn = sqlite3.connect("example.db")
c = conn.cursor()
c.execute('create table Persons (id int, name text, city text)')
c.execute('insert into Persons VALUES (1, "smith", "dallas")')
conn.commit()
conn.close()

conn = sqlite3.connect('example.db')
c = conn.cursor()
x = c.execute("select * from Persons")
print x.fetchall()
conn.close()
