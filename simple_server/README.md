### Python2:: SimpleHTTPServer
### Python3:: http.server

How to run from python2:
```
$ chmod +x ./server2.py
$ ./server2.py
```

How to run from python3:
* use this instruction to generate self-signed certificate
  * http://www.akadia.com/services/ssh_test_certificate.html
* make directory "ssl"  and install ssl certificates
* see sample how to get the certificate done from my end
```
$ mkdir ssl
$ openssl genrsa -des3 -out server.key 1024
$ openssl req -new -key server.key -out server.csr
$ openssl rsa -in server.key -out server_revised.key
$ openssl x509 -req -days 15 -in server.csr -signkey server_revised.key -out server.crt
$ mv server.key server_old.key
$ mv server_revised.key server.key
$ cat server.crt server.key > server3.pem
$ chmod 0400 *
```
* start server3 web server
```
$ chmod +x ./server3.py
$ ./server3.py
```
* check your SSL output with curl tool
```
$ curl -v -f -k 'https://localhost:8000'                                                                                      [13/313]
* About to connect() to localhost port 8000 (#0)
*   Trying ::1...
* Connection refused
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 8000 (#0)
* Initializing NSS with certpath: sql:/etc/pki/nssdb
* skipping SSL peer certificate verification
* SSL connection using TLS_RSA_WITH_AES_128_CBC_SHA
* Server certificate:
*       subject: E=bigchoo@gmail.com,CN=localhost,OU=Engineering,O=Web Server Team INC,L=Sunnyvale,ST=CA,C=US
*       start date: Feb 05 17:08:21 2015 GMT
*       expire date: Feb 20 17:08:21 2015 GMT
*       common name: localhost
*       issuer: E=bigchoo@gmail.com,CN=localhost,OU=Engineering,O=Web Server Team INC,L=Sunnyvale,ST=CA,C=US
> GET / HTTP/1.1
> User-Agent: curl/7.29.0
> Host: localhost:8000
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Server: SimpleHTTP/0.6 Python/3.3.2
< Date: Thu, 05 Feb 2015 17:21:53 GMT
< Content-type: text/html
< Content-Length: 82
< Last-Modified: Thu, 05 Feb 2015 14:59:13 GMT
<
<html>
<h1>hello boonchu</h1>
<p>
        this is a test web <b>server</b>
</p>
</html>
```
The instance default listens to port 8000
