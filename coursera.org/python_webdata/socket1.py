from socket import *

_s = socket(AF_INET, SOCK_STREAM)
_s.connect( ('www.py4inf.com', 80) )
