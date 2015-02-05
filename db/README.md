### PostgresQL 9.x ###

##### Getting started on CentOS 7/Red Hat Enterprise 7
```
sudo yum install -y postgresql-server
sudo postgresql-setup initdb
sudo systemctl start postgresql.service
sudo systemctl enable postgresql.service
sudo systemctl status postgresql.service -l
```
