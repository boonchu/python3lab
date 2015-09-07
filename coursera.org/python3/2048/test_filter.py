#! /usr/bin/env python

def zeros(zero): return zero == 0
def no_zeros(zero): return zero != 0

print filter(zeros, [0,0,0,1])
print filter(no_zeros, [0,0,0,1])

print filter(zeros, [0,0,0])
print filter(no_zeros, [0,0,0])

more_zeros = [[x,y] for x,y in zip([0,0,0,1], [0,0,0,1])]
print '[[x,y] for x,y in zip([0,0,0,1], [0,0,0,1])]'
print more_zeros
more_zeros = reduce(lambda x,y: x+y, more_zeros)
print 'reduce(lambda x,y: x+y, more_zeros)'
print more_zeros
print 'filter(zeros, more_zeros)'
print filter(zeros, more_zeros)
print 'filter(no_zeros, more_zeros)'
print filter(no_zeros, more_zeros)
