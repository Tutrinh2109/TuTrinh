# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 23:52:36 2024

@author: TuTrinh
"""

a=float(input("Nhập cạnh a: "))
b=float(input("Nhập cạnh b: "))
c=float(input("Nhập cạnh c: "))
if a+b>c and a+c>b and b+c>a:
    print("a,b,c là 3 cạnh của tam giác")
else:
    print("a,b,c không là 3 cạnh của tam giác")
    
    
