with open('quiz10-1.py') as fp:
    for i, line in enumerate(fp):
       if "\xe2" in line:
          print i, repr(line)
       if "\xcf" in line:
          print i, repr(line)
       if "\xc3" in line:
          print i, repr(line)
