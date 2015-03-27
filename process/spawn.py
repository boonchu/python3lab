#! /usr/bin/env python

import gevent

def say(message, n):
	print '--- thread %d ---' % n
	gevent.sleep(n)
	print message

thread1 = gevent.spawn(say, "I live in San Jose", 20)
thread2 = gevent.spawn(say, "Hello from thread", 10)

threads = [ thread1, thread2 ]

gevent.joinall(threads)
print 'this message will be blocking until threads exit'
