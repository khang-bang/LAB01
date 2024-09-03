# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:01:20 2024

@author: HP
"""

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
so_lon_nhat = max(a, b, c)
so_nho_nhat = min(a, b, c)
print("Số lớn nhất là: ", so_lon_nhat, "\nSố nhỏ nhất là: ", so_nho_nhat)