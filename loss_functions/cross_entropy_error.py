#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Author: Sphantix
# Mail: sphantix@gmail.cn
# created time: Mon 18 Feb 2019 09:47:44 PM CST

import numpy as np

# cross entropy error
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

t = [0,0,1,0,0,0,0,0,0,0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]

print("正确标签值：{0}".format(t))
print("输出值：{0}".format(y))
print("交叉熵误差：{0}".format(cross_entropy_error(np.array(y), np.array(t))))
