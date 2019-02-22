#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Author: Sphantix
# Mail: sphantix@gmail.cn
# created time: Fri 22 Feb 2019 01:58:52 PM CST

from layers import MulLayer

apple_unit_price = 100
apple_num = 2
tax = 1.1

mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

# forward
apple_total_price = mul_apple_layer.forward(apple_unit_price, apple_num)
price_with_tax = mul_tax_layer.forward(apple_total_price, tax)

# backward
dprice_with_tax = 1
dapple_total_price, dtax = mul_tax_layer.backward(dprice_with_tax)
dapple_unit_price, dapple_num = mul_apple_layer.backward(dapple_total_price)

print("price_with_tax:", int(price_with_tax))
print("dapple_unit_price:", dapple_unit_price)
print("dapple_num:", int(dapple_num))
print("dtax:", dtax)
