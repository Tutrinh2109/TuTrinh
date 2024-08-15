# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 23:17:53 2024

@author: TuTrinh
"""

a=float(input("Nhập hệ số a: "))
b=float(input("Nhập hệ số b: "))
if a==0:
    if b==0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b/a
    print("Phương trình có nghiệm x = ",x)
