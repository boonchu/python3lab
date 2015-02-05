#! /usr/bin/env python3

import http.server
import ssl

httpd = http.server.HTTPServer(('localhost', 8000), http.server.SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket(httpd.socket, certfile='ssl/server3.pem', server_side=True)

httpd.serve_forever()
