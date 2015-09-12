#!/usr/bin/env python
# http://stackoverflow.com/questions/9712507/trying-to-use-reduce-and-lambda-with-a-list-containing-strings
from operator import mul as multiply

multiply = lambda a,b: a*b
listOfInts = map(int, ['2','3','4'])

print reduce(multiply, listOfInts) 


# http://stackoverflow.com/questions/2295290/what-do-lambda-function-closures-capture-in-python?rq=1
#def createAdder(x):
#    return lambda y: y + x

#adders = [createAdder(i) for i in range(4)]
#print adders[1](3), adders[1](4)

# https://docs.python.org/3/reference/datamodel.html
class Adders(object):
    def __getitem__(self, key):
        return lambda a: a + key

adders = Adders()
print adders[1](3), adders[1](4)

# why lambda so useful?
# http://stackoverflow.com/questions/890128/why-python-lambdas-are-useful?rq=1

mod3 = lambda x: x % 3 == 0
result = filter(mod3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print result
