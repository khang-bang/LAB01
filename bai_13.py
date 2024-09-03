# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:32:35 2024

@author: HP
"""
# a) Ngày/tháng/năm (Nhập 20 8 1990 thì xuất 20/8/1990)
dd = int(input("Nhập ngày sinh: "))
mm = int(input("Nhập tháng sinh: "))
yy = int(input("Nhập năm sinh: "))
ngaysinh = f"{dd}/{mm}/{yy}"
print(ngaysinh)

# b) Ngày/tháng/năm (Nhập 20 8 1990 thì xuất 20/8/90)
y = yy % 100
ngay_sinh = f"{dd}/{mm}/{y:02}"
print(ngay_sinh)

# c) Năm/tháng/ngày (Nhập 20 8 1990 thì xuất 1990/8/20)
ngaysinhh = f"{yy}/{mm}/{dd}"
print(ngaysinhh)


