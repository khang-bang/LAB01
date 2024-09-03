# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:07:02 2024

@author: HP
"""
import math
# Nhập thời gian đầu tiên
h1 = int(input("Nhập giờ đầu tiên: "))
m1 = int(input("Nhập phút đầu tiên: "))
s1 = int(input("Nhập giây đầu tiên: "))

# Nhập thời gian thứ hai
h2 = int(input("Nhập giờ thứ hai: "))
m2 = int(input("Nhập phút thứ hai: "))
s2 = int(input("Nhập giây thứ hai: "))

# Đổi ra giây
s1 = h1*60*60 + m1*60 + s1
s2 = h2*60*60 + m2*60 + s2

# cộng 2 giờ
t1 = s1 + s2
h = t1 // 3600
m = (t1 % 3600) // 60
s = (t1 % 3600) % 60
t_Tong = f"{h} giờ {m} phút {s} giây"
print("Tổng 2 giờ là: ", t_Tong)

# Hiệu 2 giờ
t_hieu = math.fabs(s1 - s2)
t2 = int(t_hieu)
h = t2 // 3600
m = (t2 % 3600) // 60
s = (t2 % 3600) % 60
t_Hieu = f"{h} giờ {m} phút {s} giây"
print("Hiệu 2 giờ là: ", t_Hieu)


