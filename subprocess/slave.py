#! /usr/bin/env python
import os
import sys
import time

def p_print(*args):
    print(os.getpid())
    print "slave print ", args
    time.sleep(30)
    print "slave job end"

if __name__ == '__main__':
    user, pwd = sys.argv[1], sys.argv[2]
    p_print('hello', user, pwd)
