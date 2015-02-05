### PostgresQL 9.x ###

##### Getting started on CentOS 7/Red Hat Enterprise 7
* install postgresql server and enable service on unit file at boot time.
```
$ sudo yum install -y postgresql-server
$ sudo postgresql-setup initdb
$ sudo systemctl start postgresql.service
$ sudo systemctl enable postgresql.service
```
* check running process 
```
$ sudo systemctl status postgresql.service -l

$ pstree -p postgres
postgres(2163)─┬─postgres(2164)
               ├─postgres(2166)
               ├─postgres(2167)
               ├─postgres(2168)
               ├─postgres(2169)
               └─postgres(2170)
```
* access postgres through psql
```
$ sudo -u postgres -s
$ psql
postgres=# CREATE SCHEMA mydb;
postgres=# CREATE USER bigchoo PASSWORD 'mydb123';
postgres=# GRANT ALL ON SCHEMA mydb to bigchoo;
postgres=# GRANT ALL ON ALL TABLES IN SCHEMA mydb to bigchoo;
postgres=# \q
```
* install python db driver adapter
  * version 2.5 to 2.7 use python 2.x
  * version 3.1 to 3.4 use python 3.x
```
sudo yum install python-psycopg2
```
* run create_table.py to populate mydb.ticket table in postgres database.
  In our case, I use python 2.x since my adapter version is between 2.5 - 2.7.
```
$ chmod +x ./create_table.py
$ ./create_table.py
$ psql -d postgres
psql (9.2.7)
Type "help" for help.

postgres=> SELECT * from mydb.ticket;
 id | num |  data
----+-----+--------
  1 | 100 | abcdef
(1 row)

postgres=> \q
```

