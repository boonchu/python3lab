#! /usr/bin/env python

import random

class Cheese(object):
    def __init__(self, num_holes=0):
        "defaults to a solid cheese"
        self.number_of_holes = num_holes

    @classmethod
    def random(cls):
        return cls(random(100))

    @classmethod
    def slightly_holey(cls):
        return cls(random(33))

    @classmethod
    def very_holey(cls):
        return cls(random(66, 100))

gouda = Cheese()
emmentaler = Cheese.random()
