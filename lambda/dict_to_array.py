#! /usr/bin/env python
# http://stackoverflow.com/questions/1679384/converting-python-dictionary-to-list
# http://stackoverflow.com/questions/674519/how-can-i-convert-a-python-dictionary-to-a-list-of-tuples

a = {'foo': 'bar', 'baz': 'quux', 'hello': 'world'}
print a
print list( reduce(lambda x, y: x + y, a.items()) )
print list( (k,v) for k, v in a.iteritems() )

#import collections
#Foo = collections.namedtuple('Foo', 'tuple')
#print list( Foo(k, v) for (k,v) in a.iteritems() )
