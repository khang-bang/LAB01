# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:30:20 2024

@author: HP
"""

# Nhập vào 1 số nguyên N sau đó in ra số có các con số theo thứ tự tăng dần

N = input("Nhập vào một số nguyên N: ")
n = list(N)
n.sort()
n1 = ''.join(n)
print("Số sau khi sắp xếp các chữ số theo thứ tự tăng dần là:", n1)
