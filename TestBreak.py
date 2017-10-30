#!/usr/bin/python3
# 《Python语言程序设计》程序清单５－１１
# Programed List 5-11
#

sum = 0
number = 0

while number < 20:
    number += 1
    sum += number
    if sum >= 100:
        break

print("The number is", number)
print("The sum is", sum)