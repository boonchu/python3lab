#! /usr/bin/env python

def shout(wrapped):
    def inner(*args, **kwargs):
        print('BEFORE!')
        ret = wrapped(*args,**kwargs)
        print('AFTER!')
        return ret
    inner.__name__ = wrapped.__name__
    return inner

@shout
def myfunc():
    print('such wow!')

myfunc = shout(myfunc)
