#!/usr/bin/python3
# 《Python语言程序设计》程序清单6－4
# Programed List 6-4
# 实参参数的传递。

def main():
    x = 1
    print("Before the call, x is", x)
    increment(x)
    print("After the call, x is", x)

def increment(n):
    n += 1
    print("\tn inside the function is", n)

main() # Call the main function