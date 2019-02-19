#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Author: Sphantix
# Mail: sphantix@gmail.cn
# created time: Mon 18 Feb 2019 09:38:59 PM CST

import numpy as np

# mean squared error
def mean_squared_error(y, t):
    return 0.5*np.sum((y-t)**2)

t = [0,0,1,0,0,0,0,0,0,0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]

print("正确标签值：{0}".format(t))
print("输出值：{0}".format(y))
print("均方误差：{0}".format(mean_squared_error(np.array(y), np.array(t))))

print("\n*****************************************\n")

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print("正确标签值：{0}".format(t))
print("输出值：{0}".format(y))
print("均方误差：{0}".format(mean_squared_error(np.array(y), np.array(t))))
