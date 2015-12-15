#! /usr/bin/env python

from functools import wraps

def logger(f):
    """wraps takes a function used in decorator and adds"""
    """the functionality of copying over the function name"""
    """docstring and argument lists"""
    @wraps(f)
    def with_logging(*args, **kwds):
        print f.__name__ + ' : Calling decorated function'
        return f(*args, **kwds)
    return with_logging


@logger
def example(x=0):
    """Docstring"""
    print 'Calling example function'
    return x + x * x

print example(15)
print example.__name__
print example.__doc__
