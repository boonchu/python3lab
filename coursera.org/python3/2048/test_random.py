#! /usr/bin/env python
#
# https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=133
#
# https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=148
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

def multiple_trials(trials):
    trial_count = 0
    two_count = 0
    while True:
      sample = two_or_four()
      two_count += sample.count(2)
      trial_count += 1
      if trial_count == trials:
        print "Percentage of 2s with ",trials, "trials: ", two_count/(trial_count*10.)
        break

multiple_trials(1)
multiple_trials(1)
multiple_trials(1)
multiple_trials(1)
print
multiple_trials(10000)
multiple_trials(10000)
multiple_trials(10000)
multiple_trials(10000)
