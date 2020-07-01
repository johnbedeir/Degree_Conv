#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#Python
#title 		:Converter.py
#description:This is a degree convertor app
#author 	:JohnBedeir
#website	:johnydesigns.com
#date		:01July20
"""


def Cel_to_Fah(Cel):
    Fah = (Cel * 9/5) + 32
    print (Cel, " Celsius is equal to", Fah, "Fahrenheit")


def Fah_to_Cel(Fah):
    Cel = (Fah - 32) * 5/9
    print (Fah, "Fahrenheit is equal to", Cel, "Celsius")
    

print ("""Choose one of the following: 
       
       1. Celsius to Fahrenheit
       2. Fahrenheit to Celsius
       
       
       """)

ans = input("Enter your choice: ")


if ans == "1":
    print (Cel_to_Fah(float(input("Enter the degree in Celisus: "))))
elif ans == "2":
    print(Fah_to_Cel(float(input("Enter the degree in Fahrenheit: "))))   
else: 
    print("...Wrong Entry...")    
    
    











