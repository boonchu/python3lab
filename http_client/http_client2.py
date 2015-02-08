#! /usr/bin/env python2

import requests
url = 'https://api.github.com/user'
auth = ('user', 'password')

r = requests.get(url, auth=auth)
print r.content
