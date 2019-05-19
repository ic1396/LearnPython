#!/usr/bin/python3
# 《Python语言程序设计》程序清单6－5
# Programed List 6-5
# 测试返回两个数的最大公约数函数。

from GCDFunction import gcd     # Import the GCD function

# Prompt the user to enter two integers
n1 = eval(input("Enter the first integer: "))
n2 = eval(input("Enter the second integer: "))

print("The greatest common divisor for", n1, "and", n2, "is", gcd(n1, n2))