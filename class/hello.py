#! /usr/bin/env python

import sys
import optparse

class hello(object):
	def __init__(self):
		usage = '%prog [OPTION] <message>'
		self.op = optparse.OptionParser(usage=usage)
		self.op.add_option('-c', dest='count', type='int', default=sys.maxint, help='Total number of message to make loop')

	def header(self, opts): pass
	def footer(self, opts): pass

	def main(self, argv=None):
		if not argv:
			argv = sys.argv[1:]	
		# passing options and message
		opts, args = self.op.parse_args(argv)

		if not args:
			self.op.error('missing message here')
		elif len(args) > 1:
			self.op.error('I need only one message here')
		
		hello_message = args[0]
		self.header(opts)
		# loop message per option said
		for i in xrange(opts.count):
			print '%d --- Hello %s ---' % (i, hello_message)
		self.footer(opts)

class say(hello):
	def __init__(self):
		hello.__init__(self)

	def header(self, opts):
		print 'Header'

	def footer(self, opts):
		print 'Footer'

if __name__ == '__main__':
	p = say()
	p.main()
