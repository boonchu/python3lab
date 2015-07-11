#! /usr/bin/env python

plural_rules = [
    lambda n: '#0 all',
    lambda n: 'singular' if n == 1 else '#1 plural',
    lambda n: 'singular' if 0 <= n <= 1 else '#2 plural',
]

print plural_rules[0](4)
print plural_rules[1](4)
print plural_rules[2](1) 
