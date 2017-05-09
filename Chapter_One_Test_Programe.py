#!/usr/bin/python3
# 《Python语言程序设计》程序清单１－编程题
# Programed List 1-Test Programme
# 第一章　编程题　１．１～１．２１

import math
import turtle
import time
'''
# 1.1
print("   1.1   ")
print("Welcome to Python")
print("Welcome to Computer Science")
print("Programming is fun")

# 1.2
print("   1.2   ")
print("Welcome to Python")
print("Welcome to Python")
print("Welcome to Python")
print("Welcome to Python")
print("Welcome to Python")

# 1.3
print("   1.3   ")
print("FFFFFFF   U     U   NN    NN")
print("FF        U     U   NNN   NN")
print("FFFFFFF   U     U   NN N  NN")
print("FF         U   U    NN  N NN")
print("FF          UUU     NN   NNN")

# 1.4
print("   1.4   ")
print("a  a^2  a^3")
a = 1
print(a, end='')
print("   ", end='')
print(a ** 2, end='')
print("    ", end='')
print(a ** 3)

a = 2
print(a, end='')
print("   ", end='')
print(a ** 2, end='')
print("    ", end='')
print(a ** 3)

a = 3
print(a, end='')
print("   ", end='')
print(a ** 2, end='')
print("    ", end='')
print(a ** 3)

a = 4
print(a, end='')
print("   ", end='')
print(a ** 2, end='')
print("   ", end='')
print(a ** 3)

# 1.5
print("   1.5   ")
print((9.5 * 4.5 - 2.5 * 3) / (45.5 - 3.5))

# 1.6
print("   1.6   ")
print(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9)

# 1.7
print("   1.7   ")
print(4 * (1 - 1.0 / 3 + 1.0 / 5 - 1.0 / 7 + 1.0 / 9 - 1.0 / 11))
print(4 * (1 - 1.0 / 3 + 1.0 / 5 - 1.0 / 7 + 1.0 / 9 - 1.0 / 11 + 1.0 / 13 - 1.0 / 15))
print(4 * (1 - 1 / 3 + 1 / 5 - 1 / 7 + 1 / 9 - 1 / 11))
print(4 * (1 - 1 / 3 + 1 / 5 - 1 / 7 + 1 / 9 - 1 / 11 + 1 / 13 - 1 / 15))
'''
# 1.8
print("   1.8   ")
R = 5.5
area = 5.5 ** 2 * math.pi
perimeter = 2 * math.pi * R
print("R=5.5")
print("Area is ", end='')
print(area)
print("Perimeter is ", end='')
print(perimeter)
'''
# 1.9
print("   1.9   ")
width = 4.5
height = 5.5
area = width * height
perimeter = 2 * (width + height)
print("width = 4.5, height = 5.5")
print("Area is ", end='')
print(area)
print("Perimeter is ", end='')
print(perimeter)

# 1.10
print("   1.10   ")
v = 14 / 1.6 / ((45+ 30 / 60)/60)
print("V = ",end='')
print(v,end='')
print(" mail/h")

# 1.11
print("   1.11   ")
CurrentPerson = 3120324986
second_of_year = 60*60*24*365
FirstYear = CurrentPerson + second_of_year // 7 + second_of_year // 45 - second_of_year // 13
SecondYear = FirstYear + second_of_year // 7 + second_of_year // 45 - second_of_year // 13
ThirdYear = SecondYear + second_of_year // 7 + second_of_year // 45 - second_of_year // 13
FourthYear = ThirdYear + second_of_year // 7 + second_of_year // 45 - second_of_year // 13
FifthYear = FourthYear + second_of_year // 7 + second_of_year // 45 - second_of_year // 13
print("第一年 ",end="")
print(FirstYear,end="")
print(" 人")
print("第二年 ",end="")
print(SecondYear,end="")
print(" 人")
print("第三年 ",end="")
print(ThirdYear,end="")
print(" 人")
print("第四年 ",end="")
print(FourthYear,end="")
print(" 人")
print("第五年 ",end="")
print(FifthYear,end="")
print(" 人")

# 1.12
print("   1.12   ")
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()

turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.done()

# 1.13
print("   1.13   ")
turtle.penup()
turtle.goto(0, 100)
turtle.right(90)
turtle.pendown()
turtle.forward(200)

turtle.penup()
turtle.goto(-100, 0)
turtle.left(90)
turtle.pendown()
turtle.forward(200)

turtle.done()

# 1.14
print("   1.14   ")
turtle.right(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)

turtle.done()

# 1.15
print("   1.15   ")
turtle.right(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)

turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)

turtle.done()

# 1.16
print("   1.16   ")
turtle.penup()
turtle.goto(50, 50)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(50, -50)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(-50, 50)
turtle.pendown()
turtle.circle(50)

turtle.done()

# 1.17
print("   1.17   ")
turtle.penup()
turtle.goto(50, -50)
turtle.color("red")
turtle.write("(50, -50)")
turtle.pendown()
turtle.goto(-39, 48)
turtle.write("(-39, 48)")
turtle.done()

# 1.18
print("   1.18   ")
turtle.right(72)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.done()

# 1.19
print("   1.19   ")
turtle.penup()
turtle.goto(40, -69.28)
turtle.color("red")
turtle.pendown()
turtle.goto(-40, -69.28)
turtle.goto(-80, -9.8)
turtle.goto(-40, 69)
turtle.goto(40, 69)
turtle.goto(80, 0)
turtle.goto(40, -69.28)

turtle.done()

# 1.20
print("   1.20   ")
turtle.penup()
turtle.goto(-70, -35)
turtle.pendown()

turtle.forward(140)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(70)

turtle.penup()
turtle.goto(-70, 35)
turtle.pendown()

turtle.left(135)
turtle.forward(30)
turtle.right(45)
turtle.forward(140)
turtle.right(135)
turtle.forward(30)

turtle.penup()
turtle.goto(70, -35)
turtle.pendown()

turtle.left(180)
turtle.forward(30)
turtle.left(45)
turtle.forward(70)

turtle.penup()
turtle.goto(-70, -35)
turtle.pendown()

turtle.right(45)
turtle.forward(30)
turtle.left(45)
turtle.forward(70)

turtle.penup()
turtle.goto(-70, -35)
turtle.right(45)
turtle.forward(30)
turtle.pendown()
turtle.right(45)
turtle.forward(140)

turtle.done()
'''
# 1.21
# 在本例中时钟获取当前时间
print("   1.21   ")
# 表盘
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(100)
# 标注时刻坐标
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.write("12")
turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
turtle.write("03")
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.write("06")
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.write("09")
# 获取当前时间
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()
turtle.write((time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
hour = time.strftime('%I',time.localtime(time.time()))    # 取12小时制小时数（01-12）
minutes = time.strftime('%M',time.localtime(time.time()))
second = time.strftime('%S',time.localtime(time.time()))
# 初始化画笔位置和角度
turtle.penup()
turtle.goto(0, 0)
turtle.left(90)
turtle.pendown()
# 计算指针偏转角度
SecondDegrees = int(second) / 60 * 360
MinutesDegrees = int(minutes) / 60 * 360 + int(second) / 60 * 6
HourDegrees = int(hour) * 30 + int(minutes) / 60 * 30
# 画时针
turtle.right(HourDegrees)
turtle.color("red")
turtle.forward(60)
# 画笔回到初始位置
turtle.penup()
turtle.goto(0, 0)
turtle.left(HourDegrees)
turtle.pendown()
# 画分针
turtle.right(MinutesDegrees)
turtle.color("green")
turtle.forward(80)
# 画笔回到初始位置
turtle.penup()
turtle.goto(0, 0)
turtle.left(MinutesDegrees)
turtle.pendown()
# 画秒针
turtle.right(SecondDegrees)
turtle.color("blue")
turtle.forward(90)
# 画笔回到初始位置
turtle.penup()
turtle.goto(0, 0)
turtle.left(SecondDegrees)
turtle.pendown()

turtle.done()