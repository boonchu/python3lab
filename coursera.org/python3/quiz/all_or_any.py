#! /usr/bin/env python

items = [(1, 2, 3, 4, 5, 6, 8), (1, 2, 6, 7, 8, 10), (1, 3, 5), (4, 6, 8), (1, 2, 3)]

def _in_seq(item):
    _flags_it = list()
    for element in item:
        _flags_it.append(all(earlier + 1 == later for earlier, later in zip(item, item[1:])))
    return _flags_it

for item in items:
    print "item %s is all %s or any %s" % (item, str(any(_in_seq(item))), str(all(_in_seq(item))))
