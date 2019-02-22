#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : sphantix

import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.arange(-1, 6, 0.1) # 以0.1为单位，生成0到6的数据
y1 = np.sin(x)
y2 = 2 * x + 1

# 设置坐标轴取值范围
plt.xlim((-1, 6))
plt.ylim((-2, 6))

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

# 设置坐标轴的label
plt.xlabel(u'x',fontproperties='DejaVu Sans',fontsize=14)
plt.ylabel(u'y',fontproperties='DejaVu Sans',fontsize=14)

# 绘图
plt.plot(x, y1, color = 'blue', linewidth = 1.0, label = 'y=sin(x)')
plt.plot(x, y2, color = 'red', linewidth = 1.0, linestyle = '--', label = 'y=2x+1')

# 绘制图例
plt.legend()

plt.show()
