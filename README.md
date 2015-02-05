### Python3 Lab
Python3 Lab in one hour

if you setup linux desktop to play with python3, you might need to use centos 6.x. 

CentOS 7 may not have python3 be available at SCL repository since it discussed
and annouced in this thread.
http://lists.centos.org/pipermail/centos-devel/2014-August/011772.html

You also can try software collection tool for any missing software packages from SCL.

1. Search for package name "python33".  
  * https://www.softwarecollections.org/en/docs/
2. Here is the result.  
  * https://www.softwarecollections.org/en/scls/rhscl/python33/
3. Sample output from me how to install it.
```
sudo yum install -y scl-utils
sudo yum install -y https://www.softwarecollections.org/en/scls/rhscl/python33/epel-7-x86_64/download/rhscl-python33-epel-7-x86_64.noarch.rpm
repoquery -qf */python33
sudo yum install -y python33
```
4. Enable python33 at your user home environment
```
$ scl enable python33 bash
$ python
Python 3.3.2 (default, Aug 14 2014, 14:25:52)
[GCC 4.8.2 20140120 (Red Hat 4.8.2-16)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

If you concern about porting your code from 2.x to 3.x, check out this site.
[porting!](http://docs.pythonsprints.com/python3_porting/py-porting.html)
