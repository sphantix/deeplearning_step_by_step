#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Author: Sphantix
# Mail: sphantix@gmail.cn
# created time: Wed 16 Jan 2019 01:57:31 PM CST

import numpy as np

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) # 溢出对策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)

print("a: {0}".format(a))
print("y: {0}".format(y))
print("np.sum(y): {0}".format(np.sum(y)))
