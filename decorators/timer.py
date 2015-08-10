#! /usr/bin/env python

import time
def timer(wrapped):
    def inner(*args, **kwargs):
        print 'start timer...'
        t = time.time()
        ret = wrapped(*args, **kwargs)
        print 'end timer ', time.time() -t
        return ret
    return inner

@timer
# http://stackoverflow.com/questions/28284996/python-pi-calculation
def pi():
    from decimal import Decimal, getcontext
    getcontext().prec=1000
    print sum(1/Decimal(16)**k * (Decimal(4)/(8*k+1) - Decimal(2)/(8*k+4) - Decimal(1)/(8*k+5) - Decimal(1)/(8*k+6)) for k in range(100))

pi = timer(pi())
