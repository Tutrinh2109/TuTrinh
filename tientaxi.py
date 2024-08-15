# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:43:04 2024

@author: TuTrinh
"""
s=float(input("So km di duoc "))
if s<=1:
    Tong_tien = 20000
if s<=3:
    Tong_tien = 20000 + (s-1)*13000
if s<=8:
    Tong_tien = 20000 + 2*13000 + (s-3)*12000
if s>8:
    Tong_tien = 20000 + 2*13000 + 5*12000 + (s-8)*10000
if Tong_tien > 100000:
    Tong_so_tien = Tong_tien*(92/100)
elif Tong_tien <=100000:
    Tong_so_tien = Tong_tien
print("Tien taxi la",Tong_so_tien)
  
