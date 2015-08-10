#! /usr/bin/env python
# 
# inner is the closure()
def make_printer(word):
    def inner():
        print(word)
    return inner

p = make_printer('such wow!')
p()
