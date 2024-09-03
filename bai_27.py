# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:45:20 2024

@author: HP
"""
import math
Nhaphinh = input("Nhập hình (v - hình vuông, n - hình chữ nhật, t - hình tròn): ")

if Nhaphinh == "v":
    canhHV = float(input("Nhập độ dài cạnh hình vuông: "))
    S_v = canhHV**2
    C_v = 4*canhHV
    print(f"Diện tích hình vuông: {S_v}\nChu vi hình vuông: {C_v}")
if Nhaphinh == "n":
    cdai = float(input("Nhập độ dài chiều dài HCN: "))
    crong = float(input("Nhập độ dài chiều rộng HCN: "))
    S_n = cdai * crong
    C_n = (cdai + crong)*2
    print(f"Diện tích hình chữ nhật: {S_n}\nChu vi hình chữ nhật: {C_n}")
if Nhaphinh == "t":
    r = float(input("Nhập bán kính hình tròn: "))
    S_t = math.pi*(r**2)
    C_t = 2*math.pi*r
    print(f"Diện tích hình tròn: {S_t}\nChu vi hình tròn: {C_t}")
    
    
    



