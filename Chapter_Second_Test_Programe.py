#!/usr/bin/python3
# 《Python语言程序设计》程序清单２－编程题
# Programed List 1-Test Programme
# 第二章　编程题　２．１～２．２６

import math
import turtle
'''
# 2.1 Compute fahrenheit from a celsius
# Prompt the user to enter a celsius （从控制台输入一个温度，单位为摄氏度）
celsius = eval(input("请输入一个以摄氏度为单位的温度值："))

# Compute fahrenheit from a celsius
fahrenheit = (9 / 5) * celsius + 32

# Display result
print("温度 ", celsius, "摄氏度", "转换为 ", fahrenheit, '华氏度')

# 2.2 Compute colume of a cylinder
# In this code, use math.pi
# Prompt the user to enter a radius and a length of a cylinder separated by commas （从控制台输入一个圆柱体的底面半径和高）
radius, length = eval(input("请输入一个圆柱体的底面半径和高，以逗号分隔："))

# Compute area
area = radius ** 2 * math.pi

# Compute volume
volume = area * length

# Display result
print("底面面积为", area)
print("底面半径为", radius, "，高为", length, "的圆柱体体积为", volume)

# 2.3 Compute meters from feet
# Prompt the user to enter a length for feet （从控制台输入一个长度，单位为英尺）
feet = eval(input("请输入一个以英尺为单位的长度："))

# Compute fahrenheit from a celsius
meters = feet * 0.305

# Display result
print(feet, "英尺", "转换为 ", meters, "米")

# 2.4 Compute pounds from kilograms
# Prompt the user to enter a weight for feet （从控制台输入一个质量值，单位为磅）
pounds = eval(input("请输入一个以磅为单位的值："))

# Compute fahrenheit from a celsius
kilograms = pounds * 0.454

# Display result
print(pounds, "磅", "转换为 ", kilograms, "千克")

# 2.5 Compute gratuity from subtotal
# Prompt the user to enter a subtotal and a gratuity rate separated by commas（从控制台输入小计和酬金率）
subtotal, gratuity_rate = eval(input("请输入小计和费率（％）："))

# Compute gratuity from subtotal
gratuity = subtotal * gratuity_rate / 100

# Compute gratuity total
total = subtotal + gratuity

# Display result
print("The gratuity is ", gratuity)
print("The total is ", total)

# 2.6 Compute total of every digit (0 ~1000) from console
# 根据书上的学习进度，没有使用循环、条件判断，输入数字的范围是 0<=输入数字<=1000
# Prompt the user to enter a number （从控制台输入一个０～１０００的数字）
number = eval(input("请输入一个０～１０００间的整数："))

# Compute total from all digit
first_digit = number % 10
number //= 10
second_digit = number % 10
number //= 10
third_digit = number % 10
number //= 10
fouth_digit = number % 10
total = first_digit + second_digit + third_digit + fouth_digit

# Display result
print("各位数字的和是", total)
'''
# 2.7 Compute years and days from minutes  1 year = 365 days

# 2.8

# 2.9

# 2.10

# 2.11

# 2.12

# 2.13

# 2.14

# 2.15

# 2.16

# 2.17

# 2.18

# 2.19

# 2.20

# 2.21

# 2.22

# 2.23

# 2.24
'''
# 2.25 Draw a rectangle on Graphics from console width and height and the centre of rectangle
# Prompt the user to enter width and height of a rectangle （从控制台输入一个矩形的长和宽）
width, height = eval(input("请输入矩形的长和宽，以逗号分隔："))

# Prompt the user to enter the centre of rectangle(x, y)  separated by commas（从控制台输入矩形中心的位置）
x, y = eval(input("请输入矩形中心的位置坐标ｘ和ｙ，以逗号分隔："))

# Draw the rectangle
turtle.penup()
turtle.goto(0,0)
turtle.goto(x - width / 2, y - height / 2)
turtle.pendown()
turtle.forward(width)
turtle.left(90)
turtle.forward(height)
turtle.left(90)
turtle.forward(width)
turtle.left(90)
turtle.forward(height)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()

turtle.done()

# 2.26 Compute area of a circle on Graphics
# In this code, use math.pi
# Prompt the user to enter a radius of a circle （从控制台输入一个圆的半径）
radius = eval(input("请输入一个圆的半径："))

# Prompt the user to enter the centre of a circle(x, y) separated by commas（从控制台输入一个圆心的位置）
x, y = eval(input("请输入一个圆心的位置坐标ｘ和ｙ，以逗号分隔："))

# Compute area of the circle
area = math.pi * radius ** 2

# Draw the circle and write its area
turtle.penup()
turtle.goto(0,0)
turtle.goto(x, y - radius)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write(area)

turtle.done()
'''