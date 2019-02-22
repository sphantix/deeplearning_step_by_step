#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : sphantix

import numpy as np

# 生成一维矩阵
x = np.array([1.0, 2.0, 3.0])
print(" x:\n{0}\n\n x[x > 1] => \n{1}\n\n".format(x, x[x>1]))

# 生成二维矩阵
y = np.array([[1, 2, 3],[4, 5, 6]])
print(" y:\n{0}\n\n y[y < 0] => \n{1}\n\n".format(y, y[y<0]))

z = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(" z:\n{0}\n\n z[z > 3] => \n{1}\n\n".format(z, z[z>3]))

# 生成三维矩阵
t = np.array([[[1, 2, 3],[4, 5, 6],[7, 8, 9]],[[1, 2, 3],[4, 5, 6],[7, 8, 9]]])
print(" t:\n{0}\n\n t[t >= 6] => \n{1}\n\n".format(t, t[t>=6]))

