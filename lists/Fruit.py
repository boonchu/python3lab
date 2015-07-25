#! /usr/bin/env python

# -- constructs dict from array --
# http://stackoverflow.com/questions/26112855/how-to-convert-an-array-to-a-dict-in-python?lq=1
# -- sort by value --
# http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
# -- OrderedDict class --
# https://docs.python.org/2/library/collections.html#ordereddict-examples-and-recipes
# -- print None from show() --
# http://stackoverflow.com/questions/7053652/random-none-output-from-basic-python-function
# -- show with type() --
# http://stackoverflow.com/questions/707674/how-to-compare-type-of-an-object-in-python
# -- __str__() --
# http://stackoverflow.com/questions/12448175/confused-about-str-in-python

# array of data
from collections import OrderedDict
import operator
import fileinput

class Fruit(object):
	def __init__(self, Names):
		# constructs key, value
		self.fruit_labels = { 'item{}'.format(i): x for i, x in enumerate(Names) }
	
	def __str__(self):
		return str(self.fruit_labels)

	def s_orderdict(self):
		return OrderedDict(sorted(self.fruit_labels.items(), key=lambda t: t[0], reverse=False))

	def s_operator(self):
		# key=operator.itemgetter(1) should be more scalable for efficiency than key=d.get
		return sorted(self.fruit_labels.iteritems(), key=operator.itemgetter(0), reverse=False)

def show(object):
	if object is None:
		print 'Object is none'
		return 

	if isinstance(object, OrderedDict): 
		for (k, v) in object.items(): 
			if k is not None: print k, v
	elif type(object) is list:
		for item, name in object:
			print item, name

Names = list()
for line in fileinput.input('list_of_fruits.txt'):
	line = line.rstrip()
	Names.append(line)	

fruits = Fruit(Names)
print fruits

print 'Show the fruit order with Ordered Dict'
show(fruits.s_orderdict())

print 'Show the fruit order with operator'
show(fruits.s_operator())

print fruits
