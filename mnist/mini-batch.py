#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Author: Sphantix
# Mail: sphantix@gmail.cn
# created time: Tue 19 Feb 2019 09:23:51 AM CST

import sys, os
import mnist
import numpy as np

# 第一次调用会花费几分钟……
(x_train, t_train), (x_test, t_test) = mnist.load_mnist(normalize=True, one_hot_label=True)

# 输出各个数据的形状
print("x shape: {0}".format(x_train.shape)) # (60000, 784) 784行, 60000列
print("t shape: {0}".format(t_train.shape)) # (60000,)

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print("train_size: {0}".format(train_size))
print("batch_size: {0}".format(batch_size))
print("batch_mask: {0}".format(batch_mask))
print("x batch: {0}".format(x_batch))
print("t batch: {0}".format(t_batch))
