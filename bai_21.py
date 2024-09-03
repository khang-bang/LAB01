# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:58:10 2024

@author: HP
"""

x = int(input("Nhập một số bất kỳ: "))
so_thanh_chu = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
if 0 <= x <= 9:
    print(so_thanh_chu[x])
else:
    print("không đọc được")
    