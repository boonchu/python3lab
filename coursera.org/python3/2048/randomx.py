#! /usr/bin/env python
#
# https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=133
#
# The tile should be 2 90% of the time and 4 10% of the time.

import random

def two_or_four():
    """
    The tile should be 2 90% of the time and
    4 10% of the time.
    """
    two_and_fours = (2, 2, 2, 2, 2, 2, 2, 2, 2, 4)
    for _ in range(10):
        return [ random.choice(two_and_fours) for _ in range(10) ]

print two_or_four()
