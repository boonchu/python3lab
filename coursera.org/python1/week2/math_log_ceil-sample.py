import math

# any secret number in the range [low, high) can always be found in
# at most n guesses where n is the smallest integer such that
# 2 ** n >= high - low + 1
# use log to solve this: https://www.youtube.com/watch?v=TTCY1SvKNgw
# log(2 ** n) >= log(high - low + 1)
# n*log(2) >= log(high - low + 1)
# n >= log(high - low + 1) / log(2)
# n >= ceiling(log(high - low + 1) / log(2))
#
# Test Case
# how_much_guess_is(100, 0) = 6
# how_much_guess_is(1000, 0) = 10
#
def how_much_guess_is(high, low):
    return int(math.ceil(math.log(high-low)/math.log(2)))

print how_much_guess_is(100, 0)
print how_much_guess_is(1000, 0)
