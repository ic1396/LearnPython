#!/usr/bin/python3
# 《Python语言程序设计》程序清单４－检查点练习
# Programed List 4-Checkpoint Programme
# 第四章　检查点练习程序　４．１～４．３７

import random
'''
# 4.1
# 4.2
i = int(True)
j = int(False)
b1 = bool(4)
b2 = bool(0)
print(i, j, b1, b2)
# 4.3
print(random.randrange(0, 20))
# 4.4
print(random.randrange(10, 20))
# 4.5
print(random.randint(10, 50))
# 4.6
print(random.randint(0, 1))
# 4.7
x = 0
y = eval(input("请输入一个整数: "))
if y > 0 :
    x = 1
print("x == " + str(x))
# 4.8
pay = eval(input("请输入当前支付额（整数）: "))
score = eval(input("请输入评分（0~100间的数）: "))
if score > 90.0 :
    pay *= 1.03
print("pay == " + str(pay))
# 4.9
pay = eval(input("请输入当前支付额（整数）: "))
score = eval(input("请输入评分（0~100间的数）: "))
if score > 90.0 :
    pay *= 1.03
else :
    pay *= 1.01
print("pay == " + str(pay))
# 4.10
print("代码a：number == 30")
number = 30
if number % 2 == 0:
    print (number, "is even.")
print(number, "is odd.")
print("代码a：number == 35")
number = 35
if number % 2 == 0:
    print (number, "is even.")
print(number, "is odd.")
print("代码b：number == 30")
number = 30
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")
print("代码b：number == 35")
number = 35
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")
# 4.11
print("x = 3而且 y = 2：")
x = 3
y = 2
if x > 2:
    if y > 2:
        z = x + y
        print("z is ", z)
    else:
        print("x is", x)
print("x = 3而且 y = 4：")
x = 3
y = 4
if x > 2:
    if y > 2:
        z = x + y
        print("z is ", z)
    else:
        print("x is", x)
# 4.12
print("x = 2 而且 y = 4：")
x = 2
y = 4
if x > 2:
    if y > 2:
        z = x + y
        print("z is ", z)
else:
    print("x is", x)
print("x = 3 而且 y = 2 ：")
x = 3
y = 2
if x > 2:
    if y > 2:
        z = x + y
        print("z is ", z)
else:
    print("x is", x)
print("x = 3 而且 y = 3 ：")
x = 3
y = 3
if x > 2:
    if y > 2:
        z = x + y
        print("z is ", z)
else:
    print("x is", x)
# 4.13
score = eval(input("请输入评分（0~150间的数）: "))
if score >= 60.0:
    grade = 'D'
    print("Grade(60) is ", grade)
elif score >= 70.0:
    grade = 'C'
    print("Grade(70) is ", grade)
elif score >= 80.0:
    grade = 'B'
    print("Grade(80) is ", grade)
elif score >= 90.0:
    grade = 'A'
    print("Grade(90) is ", grade)
else:
    grade = 'F'
    print("Grade(else) is ", grade)
print("Final Grade is ", grade)
# 4.14
# a
if i > 0:
    x = 0
    y = 1
else:
    y = 0
    z = 0
# b
if i > 0:
    x = 0
  y = 1
else:
    y = 0
    z = 0
# c
if i > 0:
  x = 0
  y = 1
else:
    y = 0
    z = 0
# d
if i > 0:
  x = 0
  y = 1
else:
    y = 0
  z = 0
# 4.15
if count % 10 == 0:
    newLine = True
else:
    newLine = False
# 4.16
# a
if age < 16:
    print("Cannot get a driver's license")
if age >= 16:
    print("Can get a driver's license")
# b
if age < 16:
    print("Cannot get a driver's license")
else:
    print("Can get a driver's license")
# 4.17
number = 14
# number = 15
# number = 30
# a
if number % 2 == 0:
    print(number, "is even")
if number % 5 == 0:
    print(number, "is multiple of 5")
# b
if number % 2 == 0:
    print(number, "is even")
elif number % 5 == 0:
    print(number, "is multiple of 5")
# 4.18
# a
if income <= 10000:
    tax = income * 0.1
elif income <= 20000:
    tax = 1000 + (income - 10000) * 0.15
# b
if income <= 10000:
    tax = income * 0.1
elif income > 10000 and income <= 20000:
    tax = 1000 + (income - 10000) * 0.15
# 4.19
income = 232323
if income <= 10000:
    tax = income * 0.1
elif income > 10000 and income <= 20000:
    tax = 1000 + (income - 10000) * 0.15
# 4.20
x = 1
print(True and (3 > 4))
print(not (x > 0) and (x > 0))
print((x > 0) or (x < 0))
print((x != 0) or (x == 0))
print((x >= 0) or (x < 0))
print((x != 1) == (not(x == 1)))   #print((x != 1) == not(x == 1))
# 4.21
print(1 <= x <= 100)
# 4.22
x = 101
print( x < 0 or ( 1 < x < 100 ))
x = 100
print( x < 0 or ( 1 < x < 100 ))
x = 90
print( x < 0 or ( 1 < x < 100 ))
x = 1
print( x < 0 or ( 1 < x < 100 ))
x = 0
print( x < 0 or ( 1 < x < 100 ))
x = -10
print( x < 0 or ( 1 < x < 100 ))
# 4.23
x = 4
y = 5
print(x >= y >= 0)
print(x <= y >= 0)
print(x != y == 5)
print((x != 0) or (x == 0))
# 4.24
# a
(x >= 1) and (x < 10)
# b
(1 <= x < 10)
# 4.25
ch = 'A'
print((ch >= 'A' and ch <= 'Z'))
ch = 'p'
print((ch >= 'A' and ch <= 'Z'))
ch = 'E'
print((ch >= 'A' and ch <= 'Z'))
ch = '5'
print((ch >= 'A' and ch <= 'Z'))
# 4.26
x, y, z = eval(input("Enter three numbers:"))
print("(x < y and y < z) is ", x < y and y < z)
print("(x < y or y < z) is ", x < y or y < z)
print("(x < y < z) is ", x < y < z)
print("not(x < y < z) is ", not(x < y < z))
# 4.27
13 < age <18
# 4.28
weight > 50 or height < 160
# 4.29
weight > 50 and height < 160
# 4.30
(weight > 50 or height > 160) and (not (weight > 50 and height > 160))
'''
# 4.31 假设你在运行下列程序时，从控制台输入２，３，６。结果是什么？
x, y, z = eval(input("Enter three numbers: "))
print("sorted" if x > y and y < z else "not sorted")
# 输出  not sorted
# 4.32 使用一个条件表达式来改写下面的if语句：
if ages >= 16:
    ticketPrice = 20
else:
    ticketPrice = 10

if count % 10 == 0:
    print(count)
else:
    print(count, end = " ")

# 4.33 使用if/else语句改写下面的条件表达式。
# (a) score = 3 * scale if x > 10 else 4 * scale
# (b) tax income * 0.2 if income > 10000 else income * 0.17 + 1000
# (c) print(i if number % 3 == 0 else j)

# 4.34 列出布尔运算符的优先级。计算下面的表达式：
True or True and False
True and True or False
# 4.35 除了 = 之外的其他所有二元运算符都是从左往右的结合顺序，这种说法是对还是错？

# 4.36 计算下面的表达式：
2 * 2 - 3 > 2 and 4 - 2 > 5
2 * 2 - 3 > 2 or 4 - 2 > 5

# 4.37 (x > 0 and x < 10)和((x > 0) and (x < 10))是否一样？(x > 0 or x < 10)和((x > 0) or (x < 10))是否一样？(x > 0 or x < 10 and y < 0)和(x > 0 or (x < 10 and y < 0))是否一样？
