# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:35:11 2024

@author: HP
"""

import math
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
bieu_thuc = ((a + b)/(math.pow(a, (1/3) + math.pow(b, (1/3)))) - math.pow(a*b, (1/3))) / ((math.pow(a, (1/3) - math.pow(b, (1/3)))))**2
print("Kết quả của biểu thức là: ", bieu_thuc)
