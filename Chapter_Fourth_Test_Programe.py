#!/usr/bin/python3
# 《Python语言程序设计》程序清单４－编程题
# Programed List 4-Test Programme
# 第四章　编程题　４．１～４．３９

import random
'''
# 4.1 求解一元二次方程 a * x * x + b * x + c = 0
a, b, c = eval(input("请依次输入一元二次方程 a * x * x + b * x + c = 0 中的常数a、b、c："))
if (b * b - 4 * a * c) > 0:
    x1 = (-b + (b ** 2 - 4 * a *c) ** 0.5) / (2 * a)
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print("方程" + str(a) + " * x * x + " + str(b) + " * x + " + str(c) + " = 0有两个实根：","x1 == ", x1, "；x2 == ", x2)
elif (b * b - 4 * a * c) == 0:
    x1 = (-b) / (2 * a)
    print("方程" + str(a) + " * x * x + " + str(b) + " * x + " + str(c) + " = 0有两个相等实根：", "x1 == x2 == ", x1)
else:
    print("方程" + str(a) + " * x * x + " + str(b) + " * x + " + str(c) + " = 0无实根。")
# 4.2 判断三个一位整数加法结果是否正确。
# Generate random numbers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
number3 = random.randint(0, 9)
# Prompt the user to enter an answer
answer = eval(input("what is " + str(number1) + " + " + str(number2) +  " + " + str(number3) + "?"))
# Display result
print(number1, "+", number2, "+", number3, "=", answer, "is", number1 + number2 + number3 == answer)
# 4.3 利用克莱姆法则求解二元一次线性方程组 a * x + b * y = e
#                                       c * x + d * y = f
a, b, c, d, e, f = eval(input("请依次输入二元一次线性方程组 a * x + b * y = e、c * x + d * y = f 中的常数a、b、c、d、e、f："))
print("方程组" + str(a) + " * x + " + str(b) + " * y = " + str(e) )
print("      " + str(c) + " * x + " + str(d) + " * y = " + str(f) )
if (a * d - b * c) == 0:
    print("无解")
else:
    print("解为：")
    print("x == ", (e * d - b * f) / (a * d - b * c))
    print("y == ", (a * f - e * c) / (a * d - b * c))
'''
# 4.4
# 4.5
# 4.6
# 4.7
# 4.8
# 4.9
# 4.0
# 4.11
# 4.12
# 4.13
# 4.14
# 4.15
# 4.16
# 4.17
# 4.18
# 4.19
# 4.20
# 4.21
# 4.22
# 4.23
# 4.24
# 4.25
# 4.26
# 4.27
# 4.28
# 4.29
# 4.30
# 4.31
# 4.32
# 4.33
# 4.34
# 4.35
# 4.36
# 4.37
# 4.38
# 4.39