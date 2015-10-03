#! /usr/bin/env python
from ConfigParser import RawConfigParser
from subprocess import PIPE, Popen
import codecs

CONFIG_FILE='config.ini'
processes = []


def init(config):
    cf=RawConfigParser()
    cf.readfp(codecs.open(CONFIG_FILE,'r','utf-8'))
    return [ (acc.split(':')[0], acc.split(':')[1]) for acc in cf.get('config','Account').split('\n') ]


def slave_cmd():
    return ['python', 'slave.py']


def f_open(accounts):
    for user,pwd in accounts:
        cmd = slave_cmd()
        cmd += [user,pwd]
        processes.append(Popen(cmd,stdin=PIPE, stdout=PIPE, bufsize=1))
        print user,pwd, 'slave.py'


def f_send(message):
    for ps in processes:
       output = ps.stdout.readline()
       if output:
          print output + 'still alive!'
       else:
          print 'all processes are dead...'
          sys.exit(1)


if __name__ == '__main__':
    try:
        accounts = init(CONFIG_FILE)
        f_open(accounts)
        print 'after forks'
        import time
        for _ in xrange(30):
            time.sleep(2) 
            f_send("pinging from __main__")
    except Exception as e:
        print e
    finally:
        print 'end'
