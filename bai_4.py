# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:09:23 2024

@author: HP
"""

N = int(input("Nhập số nguyên N có 2 chữ số: "))
if 9 < N < 100:
    a = N // 10
    b = N % 10
print("Tổng 2 chữ số của N là: ", a + b)