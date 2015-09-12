#! /usr/bin/env python
#
# Error owl test unit test failure in move __str__ return different
# https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=125#comment-541
#
oldlist = [ [0, 1, 2, 3], [9, 8, 7, 6] ]

newlist = list(oldlist)

# These should be the same
print "oldlist:", oldlist
print "newlist:", newlist
print

oldlist[0][0] = -999

# We think these should be different, but they
# are not:
print "oldlist:", oldlist
print "newlist:", newlist
print

oldlist[0] = [3000, 3001, 3002, 3003]

# Now see the difference:
print "oldlist:", oldlist
print "newlist:", newlist
print


oldlist[0] = [100, 101, 102, 103]

# What we want for out game is something like this:
oldlist = [ [0, 1, 2, 3], [9, 8, 7, 6] ]
newlist = [list(sublist) for sublist in oldlist]

oldlist[0][2] = -999

# Ah hah!
print "oldlist:", oldlist
print "newlist:", newlist
print
