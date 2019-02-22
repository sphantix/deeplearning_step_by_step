#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Author: Sphantix
# Mail: sphantix@gmail.cn
# created time: Wed 16 Jan 2019 10:23:19 AM CST

import numpy as np

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.2, 0.3], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(X.shape)
print(W1.shape)
print(B1.shape)

A1 = np.dot(X, W1) + B1

print(A1)
