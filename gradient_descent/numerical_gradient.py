#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : sphantix

import numpy as np
import matplotlib.pylab as plt

def numerical_gradient_one_dim(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x) # 生成和x形状相同的数组

    for i in range(x.size):
        tmp_val = x[i]
        # f(x+h)的计算
        x[i] = tmp_val + h
        fxh1 = f(x)

        # f(x-h)的计算
        x[i] = tmp_val - h
        fxh2 = f(x)

        grad[i] = (fxh1 - fxh2) / (2*h)
        x[i] = tmp_val # 还原值

    return grad

def numerical_gradient(f, X):
    if X.ndim == 1:
        return numerical_gradient_one_dim(f, X)
    else:
        grad = np.zeros_like(X)

        for i, x in enumerate(X):
            grad[i] = numerical_gradient_one_dim(f, x)

        return grad

def function_2(x):
    if x.ndim == 1:
        return np.sum(x**2)
    else:
        return np.sum(x**2, axis=1)

x0 = np.arange(-2, 2.5, 0.25)
x1 = np.arange(-2, 2.5, 0.25)
X, Y = np.meshgrid(x0, x1)

X = X.flatten()
Y = Y.flatten()

grad = numerical_gradient(function_2, np.array([X, Y]) )

plt.figure()
plt.quiver(X, Y, -grad[0], -grad[1],  angles="xy",color="#666666")#,headwidth=10,scale=40,color="#444444")
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xlabel('x0')
plt.ylabel('x1')
plt.grid()
plt.legend()
plt.draw()
plt.show()
