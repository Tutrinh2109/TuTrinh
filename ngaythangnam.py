# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:35:15 2024

@author: 
"""

date_str = input("Nhập vào ngày tháng năm theo định dạng dd/mm/yyyy hoặc dd-mm-yyyy: ")

if '/' in date_str:
    day, month, year = map(int, date_str.split('/'))
elif '-' in date_str:
    day, month, year = map(int, date_str.split('-'))
else:
    print("Định dạng ngày tháng không hợp lệ.")

if 1 <= month <= 12 and day > 0 and (
    (month in [1, 3, 5, 7, 8, 10, 12] and day <= 31) or 
    (month in [4, 6, 9, 11] and day <= 30) or 
    (month == 2 and (
        (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) and day <= 29) or 
        (day <= 28)
    )):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"Ngày {day}/{month}/{year} là ngày hợp lệ và năm {year} là năm nhuận.")
    else:
        print(f"Ngày {day}/{month}/{year} là ngày hợp lệ nhưng năm {year} không phải là năm nhuận.")
else:
    print("Ngày tháng năm không hợp lệ.")