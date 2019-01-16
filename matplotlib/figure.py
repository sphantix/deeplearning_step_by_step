#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : sphantix

import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.arange(0, 6, 0.1) # 以0.1为单位，生成0到6的数据
y1 = np.sin(x)
plt.figure()
plt.plot(x, y1)


y2 = 2 * x + 1
plt.figure()
plt.plot(x, y2)


plt.show()
