#! /usr/bin/env python
from ConfigParser import RawConfigParser
import codecs
import subprocess

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
        processes.append(subprocess.Popen(cmd,stdin=subprocess.PIPE))
        print user,pwd, 'slave.py'


def f_send(message):
    pIdx=0
    for ps in processes:
        if ps.poll():
            ps.communicate()
            processes.remove(ps)
            print pIdx,'process quits by accident'
            if ps:
                ps.stdin.write(message)
            else:
                print 'all processes are dead...'
                sys.exit(1)


def f_close():
    for p in processes:
        print 'inform process to quit'
        if p.poll():
            p.stdin.write('quit')
        else:
            print 'process was die'


if __name__ == '__main__':
    try:
        accounts = init(CONFIG_FILE)
        f_open(accounts)
        print 'after forks'

        import time
        for _ in xrange(5):
            time.sleep(1)
            f_send("ping from __main__")

    except Exception as e:
        print e
    finally:
        f_close()
        print 'end'
