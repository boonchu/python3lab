#! /usr/bin/env python


# turn [[1, 2, 3], [4, 5], [6, 7, 8]] into [1, 2, 3, 4, 5, 6, 7, 8]

print reduce(list.__add__, [[1, 2, 3], [4, 5], [6, 7, 8]], [])
print sum([[1, 2, 3], [4, 5], [6, 7, 8]], [])


# from Yahtzee get_all_hand()

hand = (1, 2, 2)
# [[], [1], [2], [1, 2], [2], [1, 2], [2, 2], [1, 2, 2]]
_p = reduce(lambda r, d: r + [l + [d] for l in r], hand, [[]])
# [(), (1,), (2,), (1, 2), (2,), (1, 2), (2, 2), (1, 2, 2)]
_m = map(tuple, _p)
# ([(), (1,), (2,), (1, 2), (2,), (1, 2), (2, 2), (1, 2, 2)])
print set(_m)
# set([(1, 2), (1,), (1, 2, 2), (2,), (), (2, 2)])

# hand size 3 => possibility => 2 ^ 3
#_list = list()
#for i in xrange(1 << len(hand)):
#    _list.append(tuple(d for p, d in enumerate(hand) if i >> p & 1))
# [(), (1,), (2,), (1, 2), (2,), (1, 2), (2, 2), (1, 2, 2)]
#print _list
# set([(1, 2), (1,), (1, 2, 2), (2,), (), (2, 2)])
#print set(_list)
#print set(tuple(d for p, d in enumerate(hand) if i >> p & 1) for i in xrange(1 << len(hand)))

# Function composition: If you already have a list of functions that
# you'd like to apply in 

color = lambda x: x.replace('brown', 'blue')
speed = lambda x: x.replace('quick', 'slow')
work = lambda x: x.replace('lazy', 'industrious')
fs = [str.lower, color, speed, work, str.title]

call = lambda s, func: func(s)
s = "The Quick Brown Fox Jumps Over the Lazy Dog"
print reduce(call, fs, s)


# to get the list with the maximum nth element, would return [5, 2, 5, 7] as it is the list
# with max 3rd element
print reduce(lambda x,y: x if x[2] > y[2] else y,[ [1,2,3,4], [5,2,5,7], [1,6,0,2]])


# to find the MIN/MAX values in each month across the different years.
# For example, for January it would be 10. And for February it would be 15.

from collections import Counter

stat2011 = Counter({"January": 12, "February": 20, "March": 50, "April": 70, "May": 15,
           "June": 35, "July": 30, "August": 15, "September": 20, "October": 60,
           "November": 13, "December": 50})

stat2012 = Counter({"January": 36, "February": 15, "March": 50, "April": 10, "May": 90,
           "June": 25, "July": 35, "August": 15, "September": 20, "October": 30,
           "November": 10, "December": 25})

stat2013 = Counter({"January": 10, "February": 60, "March": 90, "April": 10, "May": 80,
           "June": 50, "July": 30, "August": 15, "September": 20, "October": 75,
           "November": 60, "December": 15})

stat_list = [stat2011, stat2012, stat2013]

print reduce(lambda x, y: x & y, stat_list)     # MIN
print reduce(lambda x, y: x | y, stat_list)     # MAX
