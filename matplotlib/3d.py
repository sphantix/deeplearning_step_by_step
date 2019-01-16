#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : sphantix

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义fig
fig = plt.figure()

# 将fig变为3d
ax = Axes3D(fig)

# 定义x, y取值范围
x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)

# 生成网格数据
X, Y = np.meshgrid(x,y)

#Z = np.sin(np.sqrt(X**2 + Y**2))
Z = X**2 + Y**2

# 绘制3D曲面
ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = plt.get_cmap('rainbow'))
# 绘制从3D曲面到底部的投影
ax.contour(X, Y, Z, zdim = 'z', offset = -2, cmap = 'rainbow')

# 设置z轴的维度
#ax.set_zlim(-2, 2)
ax.set_zlim(0, 32)

plt.show()
