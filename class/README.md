###### Object Oriented in Python

* Say Hi 
```
- want to something like this: class say(hello):
- can be able to inherit from another class
- say class should has methods with unrelating to hello class

bigchoo@server1 ~/lab/python3lab/class (master)*$ ./hello.py -c 2 "world"
Header
0 --- Hello world ---
1 --- Hello world ---
Footer
```
* what is different between instant and class attribute
```
-
- http://stackoverflow.com/questions/23302018/usefulness-of-def-init-self
-
>>> class A(object):
...    def __init__(self):
...       self.list = []
...
>>> class B(object):
...    list = []
...
>>> x = B()
>>> y = B()
>>> x.list.append(1)
>>> y.list.append(2)
>>> x.list
[1, 2]
>>> y.list
[1, 2]
>>> x.list is y.list
True
>>> x = A()
>>> y = A()
>>> x.list.append('a')
>>> y.list.append('b')
>>> x.list
['a']
>>> y.list
['b']
>>> x.list is y.list
False
>>> class A(object):
...    def __init__(self):
...       self.list = []
...
>>> class B(object):
...    list = []
...
>>> x = B()
>>> y = B()
>>> x.list.append(1)
>>> y.list.append(2)
>>> x.list
[1, 2]
>>> y.list
[1, 2]
>>> x.list is y.list
True
>>> x = A()
>>> y = A()
>>> x.list.append('a')
>>> y.list.append('b')
>>> x.list
['a']
>>> y.list
['b']
>>> x.list is y.list
False>>> class A(object):
...    def __init__(self):
...       self.list = []
...
>>> class B(object):
...    list = []
...
>>> x = B()
>>> y = B()
>>> x.list.append(1)
>>> y.list.append(2)
>>> x.list
[1, 2]
>>> y.list
[1, 2]
>>> x.list is y.list
True
>>> x = A()
>>> y = A()
>>> x.list.append('a')
>>> y.list.append('b')
>>> x.list
['a']
>>> y.list
['b']
>>> x.list is y.list
False>>> class A(object):
...    def __init__(self):
...       self.list = []
...
>>> class B(object):
...    list = []
...
>>> x = B()
>>> y = B()
>>> x.list.append(1)
>>> y.list.append(2)
>>> x.list
[1, 2]
>>> y.list
[1, 2]
>>> x.list is y.list
True
>>> x = A()
>>> y = A()
>>> x.list.append('a')
>>> y.list.append('b')
>>> x.list
['a']
>>> y.list
['b']
>>> x.list is y.list
False
```
