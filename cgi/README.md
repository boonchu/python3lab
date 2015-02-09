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

* change permission 0755 on cgi-bin files
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

###### Test Markdown (similar to GIT markdown)

* test with markdown command line on python2.x to see how it works
  When I use GIT for awhile and I think markdown on GIT is cool. :-)
```
$ sudo yum install python-markdown -y
$ echo "Some **Markdown** text." | python -m markdown
<p>Some <strong>Markdown</strong> text.</p>
```
* use CGI to convert markdown
```
$ curl http://server1.cracker.org:8080/cgi-bin/hello2.py

<html>
<head>
<title>Hello Word - First CGI Program</title>
</head>
<body>
<h2>Hello Word! This is my first CGI program</h2>
<h1>Chapter</h1>
<h2>Section</h2>
<ul>
<li>item 1</li>
<li>item 2</li>
</ul>

</body>
</html>
```

###### security concerns
* this simple CGI setup intend for using in development cycle only and 
not design to use for live production. Your web service application may introduce
vulnerability by XSS or SQL injections [XSS Cheatsheet](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet)
* [Sanitising HTML user input](http://stackoverflow.com/questions/16861/sanitising-user-input-using-python)
* Use web framework instead. ([django](https://www.djangoproject.com/) heavy or [flask](http://flask.pocoo.org/) light weight)
