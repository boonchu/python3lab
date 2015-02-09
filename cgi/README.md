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

###### Getting started with Markdown (similar to GIT markdown)
* idea: http://daringfireball.net/projects/markdown/basics
* claim it faster: https://github.com/trentm/python-markdown2

* test with markdown command line on **python2.x** to see how it works.
```
$ sudo yum install python-markdown -y
$ echo "* When I use **GIT README.md** for awhile and I think \
markdown on GIT is cool. :-)*" | python -m markdown
<ul>
<li>When I use <strong>GIT README.md</strong> for awhile and I think markdown on GIT
  is cool. :-)*</li>
```
* use CGI to convert markdown
* provide markdown content for rendering
```
content = """
Chapter 
=======

Section 
-------

* item 1
* item 2
"""
```
* execute from CGI
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

###### Using Markdown with tables extensions
extensions: https://pythonhosted.org/Markdown/extensions/index.html

* create temporary table template file
```
$ cat /tmp/tables | python -m markdown
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell
```
* pipes them to extensions and see output
```
$ cat /tmp/tables | python -m markdown -x markdown.extensions.tables
<table>
<thead>
<tr>
<th>First Header</th>
<th>Second Header</th>
</tr>
</thead>
<tbody>
<tr>
<td>Content Cell</td>
<td>Content Cell</td>
</tr>
<tr>
<td>Content Cell</td>
<td>Content Cell</td>
</tr>
</tbody>
</table>
```

###### Using Markdown with postgresql (similar to GIT markdown)
requirement: [my instruction how to set up postgresql](https://github.com/boonchu/python3lab/tree/master/db)

* create table in markdown format
```
content = """
List of Ticket
=============

Section
-------

Ticket No | Ticket Title
--------- | ------------
"""

for row in rows:
        content += str(row[1]) + "|" + row[2] + "\n"

print markdown.markdown(content, extensions=['markdown.extensions.tables'])
```

* Output will be like this
```
TBD (find place to host photo)
```

###### security concerns
* this simple CGI setup intend for using in development cycle only and 
not design to use for live production. Your web service application may introduce
vulnerability by XSS or SQL injections [XSS Cheatsheet](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet)
* [Sanitising HTML user input](http://stackoverflow.com/questions/16861/sanitising-user-input-using-python)
* Use web framework instead. ([django](https://www.djangoproject.com/) heavy or [flask](http://flask.pocoo.org/) light weight)
