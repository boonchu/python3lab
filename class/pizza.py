#! /usr/bin/env python
# 
# https://newcircle.com/bookshelf/python_fundamentals_tutorial/oop
# http://intermediatepythonista.com/metaclasses-abc-class-decorators
# https://docs.python.org/2/library/abc.html

from types import *
from abc import ABCMeta, abstractmethod


class Pizza(object):
    ''' Pizza Order '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_radius(self):
        return 14

    @abstractmethod
    def get_topping(self):
        return 'Four Cheeses'


class California_Pizza(Pizza):
    ''' California Pizza '''
    def __init__(self, item_name):
        self.item_name = item_name

    def get_radius(self):
        return super(California_Pizza, self).get_radius()

    def get_topping(self):
        __obj = super(California_Pizza, self).get_topping()
        return "%s - %s" % (__obj, " Plus BBQ ")


if __name__ == "__main__":
    ''' Testing '''
    pizza = California_Pizza('Chicken')
    assert type(pizza.get_topping()) is StringType, "is not a String Type!"
    assert type(pizza.get_radius()) is IntType, "is not a Integer Type!"
    assert (pizza.get_radius() <= 14), 'pizza size is larger than 14'
    assert California_Pizza('Chicken').item_name == 'Chicken', "is not a equal class parameter!"
