#! /usr/bin/env python

"""

Example comparisons of growth rates
The three plots created by this program illustrate the situation when

    f(n) is 0.1n3+20n while g(n) are the functions n3, 20n2, and 0.1n4, respectively.

Note that the leftmost plot tends toward a positive constant value (a
horizontal line), the middle plot increases continuously and has no upper
bound, and the right plot converges towards zero. These plots reflect the
fact that two cubics grow at the same rate, a cubic grows faster than a quadratic,
and a cubic grows slower than a quartic. 

"""

import simpleplot
import math

def f(n):
    """
    A test function
    """
    return (0.5*( n ** 2)) - (5 * n) + 20

def g(n):
    """
    A test function
    """
    #return n
    #return n * math.log(n)
    return n ** 2
    #return n ** 3

def make_plot(fun1, fun2, plot_length):
    """
    Create a plot relating the growth of fun1 vs. fun2
    """
    answer = []
    for index in range(10, plot_length):
        answer.append([index, fun1(index) / float(fun2(index))])

    simpleplot.plot_lines("Growth rate comparison", 300, 300, "n", "f(n)/g(n)", [answer], True, ["Growth rate"])

# create an example plot
# Note that:
# the n^2 plot tends toward 0.5 positive constant value (a horizontal line) - same rate
# the n or n * log(n) plot increases continuously and has no upper bound, and - faster rate
# the n^3 plot converges towards zero. - slower rate
make_plot(f, g, 5000)
