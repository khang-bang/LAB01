# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:24:57 2024

@author: HP
"""

# chương trình tính số đo kiểm tra sức khỏe BMI
can_nang = float(input("Nhập số cân nặng của bạn (kg): "))
chieu_cao = float(input("Nhập chiều cao của bạn (m): "))
BMI = can_nang/(chieu_cao)**2
print("BMI của bạn là: ", BMI)