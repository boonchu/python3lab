#! /usr/bin/env python

import unittest

class HelloWorld(object):
    """ A Hello World Class """
    def __init__(self, style=None, receiver=None):
        self._style = {
            1: 'Good morning',
            2: 'Good afternoon',
            3: 'Good evening',
        }.get(style, 'Hello')
        self._statement = ''.join([self._style, receiver or 'World', '!'])


    def statement(self):
        """ return value of Hello World class """
        return self._statement


class TestHelloWorld(unittest.TestCase):
    """ Test Case for Hello World """
    def test__init__(self):
        """ Testing __init__ """
        test_hello = HelloWorld()
        self.assertTrue(isinstance(test_hello, HelloWorld))


    def test_statement(self):
        """ Testing statement method """
        test_receiver = 'Boonchu'
        test_hello = HelloWorld()
        self.assertTrue('Hello World', test_hello.statement())


if __name__ == "__main__":
    """ Execute test case """
    unittest.main()
