# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:43:20 2024

@author: HP
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
Tong = a + b
print("Tổng 2 số nguyên là: ", Tong)
Hieu_a = a - b
print("Hiệu 2 số nguyên (a là số bị trừ ) là: ", Hieu_a)
Hieu_b = b - a
print("Hiêu 2 số nguyên (b là số bị trừ ) là: ", Hieu_b)
Tich = a*b
print("Tích 2 số nguyên là: ", Tich)
Thuong_a = a/b
print("Thương 2 số nguyên (a là số bị chia, làm tròn 2 chữ số thập phân ) là: ", round(Thuong_a, 2))
print("Thương 2 số nguyên (a là số bị chia, làm tròn 3 chữ số thập phân ) là: ", round(Thuong_a, 3))
Thuong_b = b/a
print("Thuong 2 số nguyên (b là số bị chia, làm tròn 2 chữ số thập phân ) là: ", round(Thuong_b, 2))
print("Thuong 2 số nguyên (b là số bị chia, làm tròn 3 chữ số thập phân ) là: ", round(Thuong_b, 3))