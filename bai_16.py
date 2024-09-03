# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:53:19 2024

@author: HP
"""
hh = int(input("Nhập số giờ: "))
mm = int(input("Nhập số phút: "))
ss = int(input("Nhập số giây: "))
t = f"{hh}/{mm}/{ss}"
print("t:", t)
s = 60*60*hh + 60*mm + ss 
print("Đổi ra giây là: ", s)
