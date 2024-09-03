# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:41:19 2024

@author: HP
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))

if a < b and a < c and a < d:
    print("Số có giá trị nhỏ nhất là: ", a)
elif b < a and b < c and b < d:
    print("Số có giá trị nhỏ nhất là: ", b)
elif c < a and c < b and c < d:
    print("Số có giá trị nhỏ nhất là: ", c)
else:
    print("Số có giá trị nhỏ nhất là: ", d)



