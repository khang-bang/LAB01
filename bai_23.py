# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:20:10 2024

@author: HP
"""
import math
# Giải và biện luận phương trình bậc hai: ax2 + bx + c = 0
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

delta = b**2 - 4*a*c

# Điều kiện pt bậc 2: a khác 0
if a != 0:
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("Phương trình có 2 nghiệm phân biệt: ", x1, "và", x2)
    elif delta == 0:
        x = -b/(2*a)
        print("Phương trình có một nghiệm kép là: ", x)
    else:
        print("Phương trình vô nghiệm")

