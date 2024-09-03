# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:45:56 2024

@author: HP
"""

h = int(input("Nhập giờ: "))
m = int(input("Nhập phút: "))
s = int(input("Nhập giây: "))
if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
    print("Thời gian hợp lệ")
else:
    print("Thời gian không hợp lệ")

