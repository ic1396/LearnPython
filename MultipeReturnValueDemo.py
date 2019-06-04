#!/usr/bin/python3
# 《Python语言程序设计》程序清单6－10
# Programed List 6-10
# 返回多个值的函数。

def sort(number1, number2):
    if number1 < number2:
        return number1, number2
    else:
        return number2, number1

n1, n2 = sort(3, 2)
print("n1 is", n1)
print("n2 is", n2)