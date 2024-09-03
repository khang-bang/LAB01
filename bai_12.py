# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:03:41 2024

@author: HP
"""

import random
# 0 đến 100
so_thuc_ngau_nhien = random.uniform(0, 100)
print("Số thực ngẫu nhiên từ 0 đến 100: ", so_thuc_ngau_nhien)
so_nguyen_ngau_nhien = random.randrange(0, 100)
print("Số nguyên ngẫu nhiên từ 0 đến 100: ", so_nguyen_ngau_nhien)

# 50 đến 99
so_thuc = random.uniform(50, 99)
print("Số thực ngẫu nhiên từ 50 đến 99: ", so_thuc)
so_nguyen = random.randrange(50, 99)
print("Số nguyên ngẫu nhiên từ 50 đến 99: ", so_nguyen)

# -39 đến 79
so_thucc = random.uniform(-39, 79)
print("Số thực ngẫu nhiên từ -39 đến 79: ", so_thucc)
so_nguyenn = random.randrange(-39, 79)
print("Số nguyên ngẫu nhiên từ -39 đến 79: ", so_nguyenn)

# -79 đến -39
sso_thucc = random.uniform(-79, -39)
print("Số thực ngẫu nhiên từ -79 đến -39: ", sso_thucc)
sso_nguyenn = random.randrange(-79, -39)
print("Số nguyên ngẫu nhiên từ -79 đến -39: ", sso_nguyenn)


