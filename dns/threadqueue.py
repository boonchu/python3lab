import sys
import Queue
import threading
import dns.resolver

class ThreadDnsLookup(threading.Thread):
    ''' Thread-aware DNS lookup '''

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            fqdn = self.queue.get()

            resolver = dns.resolver.Resolver()
            try:
                answers = resolver.query(qname=fqdn)
                rrset = [rr.address for rr in answers.rrset]
                for rr in rrset
                    print rr
                # do whatever other sequence dependent stuff here,
                # or save returns to global objects. You shouldn't
                # return from a threaded function because you have no
                # control over when it finishes.
            except dns.resolver.NXDOMAIN:
                print 'NXDOMAIN'
            except dns.resolver.Timeout:
                print 'Timeout'
            except dns.resolver.NoAnswer:
                print 'No Answer'

            # indicate that the lookup is complete
            self.queue.task_done()

if __name__ == '__main__':
    threadCount = 6
    fqdn_list = open(sys.argv[1],'rb')

    queue = Queue.Queue()
    for i in range(threadCount):
        t = ThreadDnsLookup(queue, rcodes, rrsets)
        t.setDaemon(True)
        t.start()

    # add each fqdn to check to the queue for work
    for fqdn in fqdn_list:
        queue.put(fqdn)

    # wait for all threads to finish
    queue.join()


