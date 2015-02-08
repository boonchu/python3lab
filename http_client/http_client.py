#!/usr/bin/env python2

import urllib2

github_url = 'https://api.github.com/user'

req = urllib2.Request(github_url)

password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password( None, github_url, 'user', 'password' )

auth_manager = urllib2.HTTPBasicAuthHandler( password_manager )

opener = urllib2.build_opener( auth_manager )

urllib2.install_opener( opener )

handler = urllib2.urlopen( req )

print handler.read()
