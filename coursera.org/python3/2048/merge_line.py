#! /usr/bin/env python

"""
2048 merge timings: a program
https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=87

first created a list that contained all the non-zero elements from 'line' consecutively, 
and in the order in which they originally appear, followed by trailing zeros. 
However the rest of the implementation was my own idea as I didn't really understand 
the suggestions for the rest of the program. 

I know I can try other methods, but I want to know if there are simpler solutions 
that would require less lines of code. 
"""

import time
import random


# Increase SAMPLE_SIZE if the timings are too small
SAMPLE_SIZE = 10000
LIMIT = 2**12

def merge_1(line):
    """
    Function that merges a single row or column in 2048.
    """
    return []

def merge_2(line):
    """
    Function that merges a single row or column in 2048.
    """
    return []

def merge_3(line):
    """
    Function that merges a single row or column in 2048.
    """ 
    return line
    

def val_to_lst(val, base=4):
    """Converts val to a list of digits in the chosen base"""
    lst = [] if val else [0]
    while val:
        lst += [val % base]
        val /= base
    return lst

def fct(n):
    """Mystery function"""
    return 2 ** n if n else 0

def lst_produce():
    """
    Create a random list of number that could represent
    tiles from a 2048 game (not necessarily)
    """
    return map(fct, val_to_lst(random.randrange(LIMIT)))
         
def here_we_go():
    """This is were it all begins!"""
    
    # You can add or remove functions in this dictionary 
    # if necessary. Choose a description.
    functions = {
                    merge_1 : "my first try!",
                    merge_2 : "this is v2",
                    merge_3 : "you should write something else!",
    }

    timings = {}

    list_sample = [lst_produce() for i in range(SAMPLE_SIZE)]

    for func in functions.keys():
        start = time.time()
        for lst in list_sample:
            merge_lst = func(lst)
        timings[func]=time.time() - start

    for func, tim in sorted(timings.items(), key=lambda x: x[1], reverse = True):
        print '{time:%fs} <- {%s}' % (tim, functions[func])

here_we_go()
