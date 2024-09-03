# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:54:44 2024

@author: HP
"""
# in ra màn hình theo thứ tự tăng dần các số
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print("Ba số theo thứ tự tăng dần là:", a, b, c)
