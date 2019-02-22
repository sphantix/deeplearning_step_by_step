#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : sphantix

import numpy as np

# 生成一维矩阵
x = np.array([1.0, 2.0, 3.0])
print(" x:\n{0}\n\n x.flatten() => \n{1}\n\n".format(x, x.flatten()))

# 生成二维矩阵
y = np.array([[1, 2, 3],[4, 5, 6]])
print(" y:\n{0}\n\n y.flatten() => \n{1}\n\n".format(y, y.flatten()))

z = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(" z:\n{0}\n\n z.flatten() => \n{1}\n\n".format(z, z.flatten()))

# 生成三维矩阵
t = np.array([[[1, 2, 3],[4, 5, 6],[7, 8, 9]],[[1, 2, 3],[4, 5, 6],[7, 8, 9]]])
print(" t:\n{0}\n\n t.flatten() => \n{1}\n\n".format(t, t.flatten()))

