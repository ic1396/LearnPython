#!/usr/bin/python3
# 《Python语言程序设计》程序清单３－编程题
# Programed List 3-Test Programme
# 第三章　编程题　３．１～３．１９

import math
import turtle
'''
# 3.1 Compute the area of a pentagon
# Prompt the user to enter length of radius of the pentagon's circumcircle
radius = eval(input("请输入正五边形外接圆的半径："))

# Compute length of side of the pentagon
side = 2 * radius * math.sin(math.pi / 5)

# Compute area of the pentagon
area = 5 * side ** 2 / (4 * math.tan(math.pi / 5))

# Display result
print("The area of the pentagon is ", area)

# 3.2 Compute Great-circledistance of the between two points on the Earth.
# The length of the Earth's radius is 6371.01 km.
# Prompt the user to enter point1(latitude and longitude)
lati1, longi1 = eval(input("起始点的纬度（负数表示南纬，小数点后一位）和经度（负数表示东经，小数点后两位）："))
# Prompt the user to enter point2(latitude and longitude)
lati2, longi2 = eval(input("结束点的纬度（负数表示南纬，小数点后一位）和经度（负数表示东经，小数点后两位）："))

radius = 6371.01
# d = radius * math.acos(math.sin(math.radians(abs(longi1))) * math.sin(math.radians(abs(longi2))) + math.cos(math.radians(abs(longi1))) * math.cos(math.radians(abs(longi2))) * math.cos(math.radians(abs(lati1 - lati2))))
d = radius * math.acos(math.sin(math.radians(longi1)) * math.sin(math.radians(longi2)) + math.cos(math.radians(longi1)) * math.cos(math.radians(longi2)) * math.cos(math.radians(lati1 - lati2)))
print(d)
# 3.3
# 3.4
# 3.5
# 3.6
# 3.7
# 3.8
# 3.9
# 3.10
# 3.11
# 3.12
# 3.13
# 3.14
'''
# 3.15 Draw a smile face on graphics
turtle.pensize(3)    # Set pen thickness to 3 pixels

# Draw eyes
turtle.penup()
turtle.goto(-60, 100)
turtle.pendown()
turtle.begin_fill()   # Begin to fill color in a shape
turtle.color("red")
turtle.circle(10)
turtle.end_fill()     # Fill the shape
turtle.penup()
turtle.goto(60, 100)
turtle.pendown()
turtle.begin_fill()   # Begin to fill color in a shape
turtle.color("red")
turtle.circle(10)
turtle.end_fill()     # Fill the shape
# Draw nose
turtle.penup()
turtle.goto(20, 0)
turtle.setheading(0)
turtle.left(60)
turtle.pendown()
turtle.color("blue")
turtle.circle(20, steps = 3)
# Draw mouth
turtle.penup()
turtle.goto(-50, -50)
turtle.setheading(0)
turtle.pendown()
turtle.color("green")
turtle.circle(500, 10)
# Draw face
turtle.penup()
turtle.goto(0, -100)
turtle.setheading(0)
turtle.pendown()
turtle.color("black")
turtle.circle(150)

turtle.done()
'''
# 3.16 Draw simple shapes and fill color in shapes on graphics
turtle.pensize(3)    # Set pen thickness to 3 pixels
turtle.penup()       # Pull the pen up
turtle.goto(-200, -50)
turtle.left(60)
turtle.pendown()      # Pull the pen down
turtle.begin_fill()   # Begin to fill color in a shape
turtle.color("red")
turtle.circle(40, steps = 3)  # Draw a triangle
turtle.end_fill()     # Fill the shape

turtle.penup()       # Pull the pen up
turtle.goto(-100, -50)
turtle.setheading(0)
turtle.left(45)
turtle.pendown()      # Pull the pen down
turtle.begin_fill()   # Begin to fill color in a shape
turtle.color("blue")
turtle.circle(40, steps = 4)  # Draw a square
turtle.end_fill()     # Fill the shape

turtle.penup()       # Pull the pen up
turtle.goto(0, -50)
turtle.setheading(0)
turtle.left(36)
turtle.pendown()      # Pull the pen down
turtle.begin_fill()   # Begin to fill color in a shape
turtle.color("green")
turtle.circle(40, steps = 5)  # Draw a pentagon
turtle.end_fill()     # Fill the shape

turtle.penup()       # Pull the pen up
turtle.goto(100, -50)
turtle.setheading(0)
turtle.left(30)
turtle.pendown()      # Pull the pen down
turtle.begin_fill()   # Begin to fill color in a shape
turtle.color("yellow")
turtle.circle(40, steps = 6)  # Draw a hexagon
turtle.end_fill()     # Fill the shape

turtle.penup()       # Pull the pen up
turtle.goto(200, -50)
turtle.setheading(0)
turtle.left(22.5)
turtle.pendown()      # Pull the pen down
turtle.begin_fill()   # Begin to fill color in a shape
turtle.color("purple")
turtle.circle(40, steps = 8)  # Draw a circle
turtle.end_fill()     # Fill the shape

turtle.color("green")
turtle.penup()       # Pull the pen up
turtle.goto(-100, 50)
turtle.pendown()      # Pull the pen down
turtle.write("Cool Colorful Shapes", font = ("Times", 18, "bold"))
turtle.hideturtle()

turtle.done()
# 3.17 Compute the area of a triangle by side of the triangle and draw the triangle on Graphics
# Prompt the user to enter three points for a triangle,separated by commas
x1, y1, x2, y2, x3, y3 = eval(input("请按照顺序输入三角形三个顶点的坐标（x1,y1,x2,y2,x3,y3），以逗号分隔："))
# Compute side of a triangle
side1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
side2 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
side3 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
# Draw the triangle
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
point1 = 'A('
point1 += str(x1)
point1 += ','
point1 += str(y1)
point1 += ')'
turtle.write(point1)
turtle.goto(x2, y2)
point2 = 'B('
point2 += str(x2)
point2 += ','
point2 += str(y2)
point2 += ')'
turtle.write(point2)
turtle.goto(x3, y3)
point3 = 'C('
point3 += str(x3)
point3 += ','
point3 += str(y3)
point3 += ')'
turtle.write(point3)
turtle.goto(x1,y1)
sarea = "三角形的面积是：" + str(area)
x = min(x1, x2, x3)
y = min(y1, y2, y3)
turtle.penup()
turtle.goto(x, y - 50)
turtle.pendown()
turtle.write(sarea)
turtle.done()
# print("三角形的面积是：",area)
# 3.18 Compute three angles of a triangle by three points for a triangle and draw the triangle on Graphics
x1, y1, x2, y2, x3, y3 = eval(input("请按照顺序输入三角形三个顶点的坐标（x1,y1,x2,y2,x3,y3），以逗号分隔："))

a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))
# Draw the triangle
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
point1 = 'A('
point1 += str(x1)
point1 += ','
point1 += str(y1)
point1 += ')'
point1 += "角A的大小是"
point1 += str(A)
turtle.write(point1)
turtle.goto(x2, y2)
point2 = 'B('
point2 += str(x2)
point2 += ','
point2 += str(y2)
point2 += ')'
point2 += "角B的大小是"
point2 += str(B)
turtle.write(point2)
turtle.goto(x3, y3)
point3 = 'C('
point3 += str(x3)
point3 += ','
point3 += str(y3)
point3 += ')'
point3 += "角C的大小是"
point3 += str(C)
turtle.write(point3)
turtle.goto(x1,y1)
turtle.done()
# print("The three angles are ", round(A * 100) / 100.0, round(B * 100) / 100.0, round(C * 100) / 100.0)
# 3.19 Draw a line on Graphics
# Prompt the user to enter the start point(x, y) separated by commas
x1, y1 = eval(input("请输入起始点的坐标ｘ和ｙ（ｘ、ｙ的取值范围在-200～200），以逗号分隔："))
# Prompt the user to enter the end point(x, y) separated by commas
x2, y2 = eval(input("请输入结束点的坐标ｘ和ｙ（ｘ、ｙ的取值范围在-200～200），以逗号分隔："))
# Draw the line
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
point1 = '('
point1 += str(x1)
point1 += ','
point1 += str(y1)
point1 += ')'
turtle.write(point1)
turtle.goto(x2, y2)
point2 = '('
point2 += str(x2)
point2 += ','
point2 += str(y2)
point2 += ')'
turtle.write(point2)

turtle.done()
'''