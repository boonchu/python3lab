#! /usr/bin/env python

class Person1(object): #always inherit from object.  It's just a good idea...
    @staticmethod
    def call_person():
        print "hello person"

class Person2(object):
    @classmethod
    def call_person(cls):
        print "hello person",cls

#Calling static methods works on classes as well as instances of that class
Person1.call_person()  #calling on class
p1 = Person1()
p1.call_person()       #calling on instance of class

p2 = Person2().call_person() #using classmethod on instance
Person2.call_person()       #using classmethod on class
