#!/usr/bin/python3
# 《Python语言程序设计》程序清单４－２
# Programed List 4-2
# 判断一个整数能否被５整除，能否被２整除

number = eval(input("Enter an integer: "))

if number % 5 == 0:
    print("HiFive")

if number % 2 == 0:
    print("HiEven")
