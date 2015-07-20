#! /usr/bin/env python
# want to be able to initialize the class with, for example, a filename 
# (which contains data to initialize the list) or with an actual list.
# http://stackoverflow.com/questions/141545/overloading-init-in-python
#
class MyData:
    def __init__(self, data):
        self.myList = list()
        if isinstance(data, tuple):
            for i in data:
                self.myList.append(i)
        else:
            self.myList = data

    def GetData(self):
	if self.myList:
            print self.myList

a = [1,2]
b = (2,3)
c = MyData(a)
d = MyData(b)

print "c instance : ", c.GetData()
print "d instance : ", d.GetData()
