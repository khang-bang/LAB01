# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:03:36 2024

@author: HP
"""

a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
chialaydu_a = a % b
chialaydu_b = b % a
print("Kết quả phép chia lấy phần dư ( a là số bị chia ): ", chialaydu_a)
print("Kết quả phép chia lấy phần dư ( b là số bị chia ): ", chialaydu_b)
chialaynguyen_a = a // b
chialaynguyen_b = b // a
print("Kết quả phép chia lấy phần nguyên ( a là số bị chia ): ", chialaynguyen_a)
print("Kết quả phép chia lấy phần nguyên ( b là số bị chia ): ", chialaynguyen_b)

