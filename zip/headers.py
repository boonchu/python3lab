#! /usr/bin/env python
# http://stackoverflow.com/questions/1679384/converting-python-dictionary-to-list
# 

headers = ['Capital', 'Food', 'Year']
countries = [
    ['London', 'Fish & Chips', '2012'],
    ['Beijing', 'Noodles', '2008'],
]

for olympics in countries:
    print zip(headers, olympics)
