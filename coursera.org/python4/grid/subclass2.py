#! /usr/bin/env python
"""
Simple example of using inheritance.
"""

class Base:
    """
    Simple base class.
    """
    def __init__(self, num):
        self._number = num

    def __str__(self):
        """
        Return human readable string.
        """
        return str(self._number)

class Sub(Base):
    """
    Simple sub class.
    """
    def __init__(self, num):
       Base.__init__(self, num)
       #super(Sub, self).__init__(num)

obj = Sub(42)
print obj
