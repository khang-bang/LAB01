# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:37:19 2024

@author: HP
"""

so_xe = int(input("Nhập số xe có 4 chữ số của bạn: "))
a = so_xe // 1000
b = (so_xe // 100) % 10
c = (so_xe % 100) // 10
d = so_xe % 10
so_nut = sum([a, b, c, d])
if 0 <= so_nut <10:
    print(" Số xe của bạn có số nút là: ", so_nut)
elif 10 <= so_nut < 100:
    so_nut = so_nut % 10 + so_nut // 10
    print(" Số xe của bạn có số nút là: ", so_nut)
    