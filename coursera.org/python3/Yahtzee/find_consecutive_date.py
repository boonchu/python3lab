#! /usr/bin/env python

from datetime import date, timedelta

def checked(d1, d2):
    """
    We assume the date list is sorted.
    If d2 & d1 are different by 1, everything up to d2 is consecutive, so d2
    can advance to the next reduction.
    If d2 & d1 are not different by 1, returning d1 - 1 for the next reduction
    will guarantee the result produced by reduce() to be something other than
    the last date in the sorted date list.

    Definition 1: 1/1/14, 1/2/14, 1/2/14, 1/3/14 is consider consecutive
    Definition 2: 1/1/14, 1/2/14, 1/2/14, 1/3/14 is consider not consecutive

    """
    #if (d2 - d1).days == 1 or (d2 - d1).days == 0:  # for Definition 1
    if (d2 - d1).days == 1:                          # for Definition 2
        return d2
    else:
        return d1 + timedelta(days=-1)

# datelist = [date(2014, 1, 1), date(2014, 1, 3),
#             date(2013, 12, 31), date(2013, 12, 30)]

# datelist = [date(2014, 2, 19), date(2014, 2, 19), date(2014, 2, 20),
#             date(2014, 2, 21), date(2014, 2, 22)]

datelist = [date(2014, 2, 19), date(2014, 2, 21),
            date(2014, 2, 22), date(2014, 2, 20)]

datelist.sort()

if datelist[-1] == reduce(checked, datelist):
    print "dates are consecutive"
else:
    print "dates are not consecutive"
