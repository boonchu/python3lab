#! /usr/bin/env python

'''
https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=87


There's a much faster way of doing it (using list comprehensions), but it's still 
worth knowing this function exists.

The filter built-in function can be used to do that. Here is how filter works: 
    filter(function, iterable)

From the Python 2 documentation : It returns a list of the elements of iterable 
(a list is an iterable) for which function returns True.
'''

def odd(number):
    ''' Returns True iff number is odd '''
    return number % 2 == 1    

lst = [1, 2, 3, 4, 5, 7, 8, 11]
print lst

''' traditional style with filter '''
print filter(odd, lst)     # prints [1, 3, 5, 7, 11]

'''
use list comprehensions to do the same thing.
One says they are True-like values. For example, a non-zero integer is a True-like 
value and zero is a False-like value.

if val:
    print val

bool that gives the corresponding boolean value associated to any object.

bool(42) -> True
bool(0) -> False
bool([]) -> False

'''
print [value for value in lst if odd(value)]
''' compact all code above '''
print [value for value in lst if value % 2 == 1]
