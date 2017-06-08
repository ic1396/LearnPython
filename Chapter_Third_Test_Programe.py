#!/usr/bin/python3
# 《Python语言程序设计》程序清单３－编程题
# Programed List 3-Test Programme
# 第三章　编程题　３．１～３．１９

import math
import turtle
import time
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
# 计算球面上两点间距离的公式
# 设所求点A ，纬度β1 ，经度α1 ；点B ，纬度β2 ，经度α2。则距离
# S=R·arc cos[cosβ1cosβ2cos（α1-α2）+sinβ1sinβ2]
# 其中R为球体半径。
# Prompt the user to enter point1(latitude and longitude)
lati1, longi1 = eval(input("起始点的纬度（负数表示南纬，小数点后一位）和经度（负数表示东经，小数点后两位）："))
# Prompt the user to enter point2(latitude and longitude)
lati2, longi2 = eval(input("结束点的纬度（负数表示南纬，小数点后一位）和经度（负数表示东经，小数点后两位）："))
radius = 6371.01
d = radius * math.acos(math.sin(math.radians(lati1)) * math.sin(math.radians(lati2)) + math.cos(math.radians(lati1)) * math.cos(math.radians(lati2)) * math.cos(math.radians(longi1 - longi2)))
print("地球上点（",longi1,",",lati1,"）与点（",longi2,",",lati2,"）间的球面距离为",d,"km")
# 注意前面所列公式，不要被题目3.2中＂假设(x1, y1)和(x2, y2)是两点的经度和纬度，两点之间．．．＂误导为 x 代表经度， y 代表纬度，实际在书上提供的公式中， x 代表纬度， y 代表经度
# 起始点的纬度（负数表示南纬，小数点后一位）和经度（负数表示东经，小数点后两位）：39.55,-116.25
# 结束点的纬度（负数表示南纬，小数点后一位）和经度（负数表示东经，小数点后两位）：41.5,87.37
# 地球上点（ -116.25 , 39.55 ）与点（ 87.37 , 41.5 ）间的球面距离为 10691.79183231593 km
'''
# 3.3

'''
# 3.4 Compute area of the regular by length of a side
# Prompt the user to enter length of a side
lengthOfSide = eval(input("请输入正五边形的边长（小数点后一位）："))
area = 5 / 4 * lengthOfSide ** 2 / math.tan(math.pi / 5)
print("边长为", lengthOfSide, "的正五边形面积是", area)
# 书中名称为五角形的面积，从给出的公式看就是计算正五边形的面积

# 3.5 Compute area of the regular polygon
# Prompt the user to enter length of a side
countOfSide = eval(input("请输入正多边形的边数（整数）："))
# Prompt the user to enter length of a side
lengthOfSide = eval(input("请输入正多边形的边长（小数点后一位）："))
area = countOfSide / 4 * lengthOfSide ** 2 / math.tan(math.pi / countOfSide)
print("边长为", lengthOfSide, "的正", countOfSide, "边形面积是", area)

# 3.6 Translate the ASCII code into char
# Prompt the user to enter a ASCII code
code = eval(input("请输入一个ASCII code（0～127之间的整数）: "))
print("ASCII code ", str(code), "对应的字符是“", chr(code), "”")

# 3.7 Print a random char from A(ASC II 65) to Z(ASC II 90)
# Random generate a integer by time.time()
random = int(time.time())
print("产生的随机字符是",chr((random % 26) + 65))

# 3.8 Asking for change and Coins at least
# 修改书中示例 程序清单 3-4
# Receive the amount
amount = eval(input("请输入一个以分为单位的整数,代表钱的总数, 如 1156: "))

remainingAmount = int(amount)

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

# Display the results
print("Your amount", amount, "consists of\n", "\t", numberOfOneDollars, "dollars\n", "\t", \
      numberOfQuarters, "quarters\n", "\t", numberOfDimes, "dimes\n", "\t", numberOfNickels, "nickels\n" \
      "\t", numberOfPennies, "pennies")

# 3.9 Generate a employee's payoff table and Print it
employeeName = input("请输入员工姓名: ")
hoursWorkedPerWeek = eval(input("请输入员工每周工作小时数: "))  # number of hours worked in a week
hourlyPayRate = eval(input("请输入员工每小时报酬: "))     # hourly pay rate
theFederalTaxWithholdingRate = eval(input("请输入联邦预扣税率: "))   # the federal tax withholding rate
theStateTaxWithholdingRate = eval(input("请输入州预扣税率: "))       # the state tax withholding rate
allPay = hourlyPayRate * hoursWorkedPerWeek
theFederalTax = allPay * theFederalTaxWithholdingRate
theStateTax = allPay * theStateTaxWithholdingRate
theTax = allPay * (theFederalTaxWithholdingRate + theStateTaxWithholdingRate)
netPay = allPay - theTax
print("员工姓名: ", employeeName)
print("每周工作小时数: ", format(hoursWorkedPerWeek,"7.1f"))
print("每小时报酬:    ", format(hourlyPayRate,"7.2f"))
print("应发工资金额:  ", format(allPay,"7.1f"))
print("工资明细: ")
print("    联邦预扣税(税率", format(theFederalTaxWithholdingRate, "6.2%"),"): ", format(theFederalTax,"7.2f"))
print("    州预扣税(税率", format(theStateTaxWithholdingRate, "6.2%"),"): ", format(theStateTax,"7.2f"))
print("    合计预扣税: ", format(theTax,"7.2f"))
print("实发金额: ", format(netPay,"7.2f"))

# 3.10 Display Greek alphabet by the Unicode
print("\u03b1 \u03b2 \u03b3 \u03b4 \u03b5 \u03b6 \u03b7 \u03b8 \u03b9 \u03ba \u03bb \u03bc \u03bd \u03be \u03bf")
print("\u03c0 \u03c1 \u03c2 \u03c3 \u03c4 \u03c5 \u03c6 \u03c7 \u03c8 \u03c9 ")

# 3.11
code = eval(input("请输入一个四位整数: "))
codestring = ''
first = code % 10
codestring += str(first)
code = code // 10
first = code % 10
codestring += str(first)
code = code // 10
first = code % 10
codestring += str(first)
code = code // 10
first = code % 10
codestring += str(first)
print("数字倒序后为：", codestring)

# 3.12 Draw a pentagram on graphics and the user to enter a length of side
lengthOfSide = eval(input("请输入五角星的边长："))
turtle.pensize(3)
turtle.left(36)
turtle.forward(lengthOfSide)

turtle.left(180 - 36)
turtle.forward(lengthOfSide)

turtle.left(180 - 36)
turtle.forward(lengthOfSide)

turtle.left(180 - 36)
turtle.forward(lengthOfSide)

turtle.left(180 - 36)
turtle.forward(lengthOfSide)

turtle.done()

# 3.13
turtle.penup()       # Pull the pen up
turtle.goto(0, 0)
turtle.setheading(0)
turtle.left(30)
turtle.pendown()      # Pull the pen down
turtle.begin_fill()   # Begin to fill color in a shape
turtle.color("red")
turtle.circle(60, steps = 6)  # Draw a hexagon
turtle.end_fill()     # Fill the shape

turtle.color("white")
turtle.penup()       # Pull the pen up
turtle.goto(-67, 35)
turtle.pendown()      # Pull the pen down
turtle.write("STOP", font = ("Times", 24, "bold"))
turtle.hideturtle()
turtle.done()

# 3.14
radius = eval(input("请输入环形的半径："))
size = 15  # 笔的大小
distance = 2 * size + 2   # 环的间距

turtle.pensize(size)

turtle.penup()
turtle.goto(0 - 2 * radius - distance, 50)
turtle.setheading(0)
turtle.pendown()
turtle.color("blue")
turtle.circle(radius)

turtle.penup()
turtle.goto(0, 50)
turtle.setheading(0)
turtle.pendown()
turtle.color("black")
turtle.circle(radius)

turtle.penup()
turtle.goto(0 + 2 * radius + distance, 50)
turtle.setheading(0)
turtle.pendown()
turtle.color("red")
turtle.circle(radius)

turtle.penup()
turtle.goto(0 - radius - distance / 2, 50 - radius)
turtle.setheading(0)
turtle.pendown()
turtle.color("yellow")
turtle.circle(radius)

turtle.penup()
turtle.goto(0 + radius + distance / 2, 50 - radius)
turtle.setheading(0)
turtle.pendown()
turtle.color("green")
turtle.circle(radius)

turtle.done()

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
#turtle.circle(200, 20)
turtle.goto(0, -60)
turtle.goto(50, -50)
# Draw face
turtle.penup()
turtle.goto(0, -100)
turtle.setheading(0)
turtle.pendown()
turtle.color("black")
turtle.circle(150)

turtle.done()

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