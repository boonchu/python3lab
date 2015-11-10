from socket import *

_s = socket(AF_INET, SOCK_STREAM)
_s.connect( ('www.py4inf.com', 80) )

_s.send('GET http://www.py4inf.com/code.romeo.txt HTTP/1.0\n\n')

while True:
    data = _s.recv(512)
    if ( len(data) < 1 ) : 
        break
    print data
_s.close()
