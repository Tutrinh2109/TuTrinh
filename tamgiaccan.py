# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:14:05 2024

@author: TuTrinh
"""
a=float(input("Nhap canh a:"))
b=float(input("Nhap canh b:"))
c=float(input("Nhap canh c:"))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("Tam giac deu")
    elif a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
        print("Tam giac vuong")
    elif (a==b and a!=c) or (a==c and a!=b) or(b==c and b!=a):
        print("Tam giac can")
    else:
        print("Khong phai la tam giac")
else:
    print("Tam giac thuong")
        