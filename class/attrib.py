#!/usr/bin/env python

class C(object):
    """docstring:
    http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    """


    def __init__(self, disc):
        """object disc """
        self.disk = disc

    def get_disk(self):
        """ get disk """
        if not hasattr(self, 'disk'):
            return None
        else:
            return self.disk

    def get_jukebox(self):
        """get jukebox if available. otherwise, defines as default.
        """ 
        jukebox = getattr(self, 'jukebox', {})
        if jukebox:
            return self.jukebox
        else:
            self.jukebox = {}
            return self.jukebox

    def set_jukebox(self, **kwargs):
        """set jukebox if declares value
        """
        jukebox = self.get_jukebox()
        values = kwargs.get('jukebox')
        if values:
            self.jukebox = values


if __name__ == '__main__':
    """testing class instance
    checking instance
    http://effbot.org/pyfaq/how-do-i-check-if-an-object-is-an-instance-of-a-given-class-or-of-a-subclass-of-it.htm
    using asserting effectively
    https://wiki.python.org/moin/UsingAssertionsEffectively
    """
    assert isinstance(C('three'), C), 'test prep: class should be class'

    """
    checking get_disk()
    """
    c = C('five')
    assert isinstance(c, C), 'test prep: c should be class C'
    try:
        print 'test #0: PASSED'
        assert c.get_disk() == 'five'
    except AssertionError:
        print 'test #0: error in jukebox value???'
        print "C class has {}".format(c.get_disk())
        pass

    """
    validate when hits to default value
    https://pymotw.com/2/exceptions/
    """
    try:
        print 'test #1: PASSED'
        assert c.get_jukebox() == {}
    except AssertionError:
        print 'test #1: error in jukebox value???'
        print "C class has {}".format(c.get_jukebox())
        pass
    """
    set jukebox
    """
    c.set_jukebox(jukebox={'disc1':'a', 'disc2':'b'})
    try:
        print 'test #2: PASSED'
        assert c.get_jukebox() == {'disc1':'a', 'disc2':'b'}
    except AssertionError:
        print 'test #2: error in jukebox value???'
        print "C class has {}".format(c.get_jukebox())
        pass

    try:
        print c.disc
    except AttributeError:
        pass

