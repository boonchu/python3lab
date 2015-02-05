#! /usr/bin/env python

import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

Handler = SimpleHTTPRequestHandler
Server = BaseHTTPServer.HTTPServer

server_address = ( '127.0.0.1', 8000 )

Handler.protocol_version = 'HTTP/1.0'
httpd = Server( server_address, Handler )

httpd.serve_forever()
