#! /usr/bin/env python

"""
Simple class inheritance
"""

class Base:
    """
    Base class
    """
    def hello(self):
        """
        hello method
        """
        print "hello"

    def message(self, msg):
        """
        message method
        """
        print msg

class Sub(Base):
    """
    sub class
    """
    def message(self, msg):
        """
        message override method
        """
        print "sub:", msg

obj = Sub()
obj.hello()
obj.message("what's going to happen?")

baseobj = Base()
baseobj.hello()
baseobj.message("another message")
