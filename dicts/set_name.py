#!/usr/bin/env python

fl = { 'Mary':'Li', 'James':"O'Day", 'Thomas':'Miller', 'William':'Garcia', 'Elizabeth':'Davis' }

#for k in sorted(fl, key=fl.get):
#    print '{0} {1}'.format(k, fl[k])

list_of_tuples = zip(fl.values(), fl.keys())
list_of_tuples.sort(key=lambda x: (x[0], x[1]))
for k in list_of_tuples:
    print '{} {}'.format(k[1], k[0])
