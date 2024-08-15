# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:43:13 2024

@author: TuTrinh
"""
y=float(input("Nhap nam sinh: "))
if y>0 and y<2005:
    if (y%4==0 and y%100!=0) or (y%400==0):
        m=float(input("Nhap thang sinh: "))
        if m>=1 and m<=12:
            if m==2:
                d=float(input("Nhap ngay sinh: "))
                if d>=1 and d<=29:
                    print("Hop le")
                else:
                    print("Khong hop le")
            if m==1 and m==3 and m==5 and m==7 and m==8 and m==10 and m==12:
                d=float(input("Nhap ngay sinh: "))
                if d>=1 and d<=31:
                    print("Hop le")
                else:
                    print("Khong hop le")
            if m==4 and m==6 and m==9 and m==11:
                d=float(input("Nhap ngay sinh: "))
                if d>=1 and d<=30:
                    print("Hop le")
                else:
                    print("Khong hop le")
    else:
        m=float(input("Nhap thang sinh: "))
        if m==2:
            d=float(input("Nhap ngay sinh: "))
            if d>=1 and d<=28:
                print("Hop le")
            else:
                print("Khong hop le")
        if m==1 and m==3 and m==5 and m==7 and m==8 and m==10 and m==12:
            d=float(input("Nhap ngay sinh: "))
            if d>=1 and d<=31:
                print("Hop le")
            else:
                print("Khong hop le")
        if m==4 and m==6 and m==9 and m==11:
            d=float(input("Nhap ngay sinh: "))
            if d>=1 and d<=30:
                print("Hop le")
            else:
                print("Khong hop le")
else:
    print("Khong hop le")
        
