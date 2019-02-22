#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Author: Sphantix
# Mail: sphantix@gmail.cn
# created time: Fri 22 Feb 2019 02:11:53 PM CST

from layers import *

apple_unit_price = 100
apple_num = 2
orange_unit_price = 150
orange_num = 3
tax = 1.1

# layers
mul_apple_layer = MulLayer()
mul_orange_layer = MulLayer()
add_apple_orange_layer = AddLayer()
mul_tax_layer = MulLayer()

# forward
apple_total_price = mul_apple_layer.forward(apple_unit_price, apple_num)
orange_total_price = mul_orange_layer.forward(orange_unit_price, orange_num)
all_price = add_apple_orange_layer.forward(apple_total_price, orange_total_price)
price_with_tax = mul_tax_layer.forward(all_price, tax)

# backward
dprice = 1
dall_price, dtax = mul_tax_layer.backward(dprice)
dapple_total_price, dorange_total_price = add_apple_orange_layer.backward(dall_price)
dorange_unit_price, dorange_num = mul_orange_layer.backward(dorange_total_price)
dapple_unit_price, dapple_num = mul_apple_layer.backward(dapple_total_price)

print("price_with_tax:", int(price_with_tax))
print("dapple_unit_price:", dapple_unit_price)
print("dapple_num:", int(dapple_num))
print("dorange_unit_price:", dorange_unit_price)
print("dorange_num:", int(dorange_num))
print("dtax:", dtax)
