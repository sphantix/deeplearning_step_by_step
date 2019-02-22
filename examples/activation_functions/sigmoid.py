#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Author: Sphantix
# Mail: sphantix@gmail.cn
# created time: Wed 16 Jan 2019 01:57:36 PM CST

import numpy as np
import matplotlib.pylab as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

X = np.arange(-5.0, 5.0, 0.1)
Y = sigmoid(X)

# 获取当前的坐标轴, gca = get current axis
ax = plt.gca()
# 设置右边框和上边框
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 设置x坐标轴为下边框
ax.xaxis.set_ticks_position('bottom')
# 设置y坐标轴为左边框
ax.yaxis.set_ticks_position('left')
# 设置x轴, y周在(0, 0)的位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.plot(X, Y)
plt.ylim(-0.1, 1.1)
plt.show()
