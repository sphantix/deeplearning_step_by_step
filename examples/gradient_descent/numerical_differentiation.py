#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : sphantix

import numpy as np
import matplotlib.pylab as plt

def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)


def function_1(x):
    return 0.01*x**2 + 0.1*x

def function_tmp1(x):
    return x*x + 4.0**2.0

print("x=5处的导数: {0}".format(numerical_diff(function_1, 5)))
print("x=10处的导数: {0}".format(numerical_diff(function_1, 10)))

print("x0=3, x1=4时的偏导数: {0}".format(numerical_diff(function_tmp1, 3.0)))
