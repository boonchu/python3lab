#! /usr/bin/env python

def fact( n ):
    return n * fact( n - 1 ) if n > 1 else 1

print [ ( n, fact(n) ) for n in range( 8 ) ]
