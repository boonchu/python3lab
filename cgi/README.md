##### CGI modules

###### Python2.x

* run CGI module
```
$ python2.7 -m CGIHTTPServer 8080
Serving HTTP on 0.0.0.0 port 8080 ...
```

###### Python3.x

* run CGI module
```
$ scl enable python33 bash
$ python3 -m http.server --cgi 8080
Serving HTTP on 0.0.0.0 port 8080 ...
```

* check out this git with cgi-bin and run curl 
```
$ curl http://server1.cracker.org:8080/cgi-bin/hello
<html>
<head>
<title>Hello Word - First CGI Program</title>
</head>
<body>
<h2>Hello Word! This is my first CGI program</h2>
</body>
</html>
```

###### security concerns
* this simple CGI setup intend for using in development cycle only and 
not design to use for live production. Your web service application may introduce
vulnerability by XSS or SQL injections [XSS Cheatsheet](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet)
* [Sanitising HTML user input](http://stackoverflow.com/questions/16861/sanitising-user-input-using-python)
* Use web framework instead.
