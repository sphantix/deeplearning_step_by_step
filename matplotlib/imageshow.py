#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : sphantix

import matplotlib.pyplot as plt
from matplotlib.image import imread

# 读入图片
img = imread('../data/cat.jpeg')
plt.imshow(img)

plt.show()
