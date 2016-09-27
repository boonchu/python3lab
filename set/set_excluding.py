#!/usr/bin/env python

from sets import Set

tor_ranges = Set(range(0,100))
excludings = Set(range(60,80))
for item in list(tor_ranges - excludings):
    print "item {}".format(item)
