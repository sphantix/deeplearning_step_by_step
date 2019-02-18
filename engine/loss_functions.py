#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Author: Sphantix
# Mail: sphantix@gmail.cn
# created time: Mon 18 Feb 2019 09:26:00 PM CST

import numpy as np

# mean squared error
def mean_squared_error(y, t):
    return 0.5*np.sum((y-t)**2)

# cross entropy error
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))
