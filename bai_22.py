# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:12:50 2024

@author: HP
"""

# Giải và biện luận phương trình bậc nhất: ax + b = 0
# điều kiện có pt bậc nhất: a khác 0
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a != 0:
    print("Phương trình có nghiệm là: ", -b/a)
elif a == 0:
    print("Không thỏa điều kiện pt bậc nhất")
    