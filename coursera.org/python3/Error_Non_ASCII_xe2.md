>>> with open('quiz7-1.py') as fp:
...    for i, line in enumerate(fp):
...        if "\xe2" in line:
...           print i, repr(line)
...
5 'lies in the range 1\xe2\x89\xa4|a|<2 and has 53 significant bits. Floating point numbers are \n'
