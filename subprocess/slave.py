#! /usr/bin/env python
import os
import sys
import time

def p_print(*args):
    print(os.getpid())
    
    for _ in xrange(30):
        time.sleep(1)
        print "slave job " + str(args) + " running"

if __name__ == '__main__':
    user, pwd = sys.argv[1], sys.argv[2]
    p_print('hello', user, pwd)
