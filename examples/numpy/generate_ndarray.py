#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : sphantix

import numpy as np

# 生成一维矩阵
x = np.array([1.0, 2.0, 3.0])
print(" x: {0}\n type(x): {1}\n x.ndim: {2}\n x.shape: {3}\n x.dtype: {4}\n".format(x, type(x), x.ndim, x.shape, x.dtype))

# 生成二维矩阵
y = np.array([[1, 2, 3],[4, 5, 6]])
print(" y: {0}\n type(y): {1}\n y.ndim: {2}\n y.shape: {3}\n y.dtype: {4}\n".format(y, type(y), y.ndim, y.shape, y.dtype))

z = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(" z: {0}\n type(z): {1}\n z.ndim: {2}\n z.shape: {3}\n z.dtype: {4}\n".format(z, type(z), z.ndim, z.shape, z.dtype))

# 生成三维矩阵
t = np.array([[[1, 2, 3],[4, 5, 6],[7, 8, 9]],[[1, 2, 3],[4, 5, 6],[7, 8, 9]]])
print(" t: {0}\n type(t): {1}\n t.ndim: {2}\n t.shape: {3}\n t.dtype: {4}\n".format(t, type(t), t.ndim, t.shape, t.dtype))
