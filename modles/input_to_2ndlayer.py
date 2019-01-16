#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Author: Sphantix
# Mail: sphantix@gmail.cn
# created time: Wed 16 Jan 2019 11:19:08 AM CST

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.2, 0.3], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print("X.shape: {0}".format(X.shape))
print("W1.shape: {0}".format(W1.shape))
print("B1.shape: {0}".format(B1.shape))

A1 = np.dot(X, W1) + B1

print("A1: {0}".format(A1))

Z1 = sigmoid(A1)

print("Z1: {0}".format(Z1))

W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

print("Z1.shape: {0}".format(Z1.shape))
print("W2.shape: {0}".format(W2.shape))
print("B2.shape: {0}".format(B2.shape))

A2 = np.dot(Z1, W2) + B2
print("A2: {0}".format(A2))

Z2 = sigmoid(A2)
print("Z2: {0}".format(Z2))

