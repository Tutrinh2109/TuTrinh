# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 23:26:18 2024

@author: TuTrinh
"""
import math 
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))        
if a==0:
    print("Phương trình không phải phương trình bậc hai")
elif a!=0:
    delta = b**2- 4*a*c
    if delta<0:
        print("Phương trình vô nghiệm")
    elif delta==0:
        print("Phương trình có nghiệm kép x1 = x2 = ",x=-b/2*a)
    elif delta>0:
        x1 = (-b+delta**(1/2))/(2*a)
        x2 = (-b-delta**(1/2))/(2*a)
        print("Phương trình có 2 nghiệm phân biệt")
        print("x1 = ",(-b + math.sqrt(delta))/2*a)
        print("x2 = ",(-b - math.sqrt(delta))/2*a)
else:
    print("Không xác định")   