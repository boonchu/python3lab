#! /usr/bin/env python2

import psycopg2

conn = psycopg2.connect("dbname=postgres user=bigchoo")

query = conn.cursor()

query.execute("DROP TABLE IF EXISTS mydb.ticket;");
query.execute("CREATE TABLE mydb.ticket (id serial PRIMARY KEY, num integer, data varchar);")
query.execute("INSERT INTO mydb.ticket (num, data) VALUES (100, 'abcdef');")
query.execute("SELECT * FROM mydb.ticket;")

query.fetchone()

conn.commit()

query.close()
conn.close()
