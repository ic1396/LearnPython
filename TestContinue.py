#!/usr/bin/python3
# 《Python语言程序设计》程序清单５－１２
# Programed List 5-12
#

sum = 0
number = 0

while number < 20:
    number += 1
    if number == 10 or number == 11:
        continue
    sum += number

print("The sum is", sum)