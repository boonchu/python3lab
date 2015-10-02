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

def f(n):
    """
    A test function
    """
    #return 0.1 * n ** 3 + 20 * n
    return 2 **(-n)

def g(n):
    """
    A test function
    """
    return n
    #return n ** 3
    #return 20 * n ** 2
    #return .1 * n ** 4

def make_plot(fun1, fun2, plot_length):
    """
    Create a plot relating the growth of fun1 vs. fun2
    """
    answer = []
    for index in range(10, plot_length):
        answer.append([index, fun1(index) / float(fun2(index))])

    simpleplot.plot_lines("Growth rate comparison", 300, 300, "n", "f(n)/g(n)", [answer], True, ["Growth rate"])

# create an example plot
make_plot(f, g, 100)
