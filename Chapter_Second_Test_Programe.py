#!/usr/bin/python3
# 《Python语言程序设计》程序清单２－编程题
# Programed List 1-Test Programme
# 第二章　编程题　２．１～２．２６

import math
import turtle
import time
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

# 2.7 Compute years and days from minutes  (1 year = 365 days)
# Prompt the user to enter a number （从控制台输入一个０～１０００的数字）
minutes = eval(input("请输入一个表示时间的整数，单位为分钟："))

# Compute total minutes of a day
minOfDay = 24 * 60

# Compute total days
totalOfDay = minutes // minOfDay

# Compute total completed years
years = totalOfDay // 365

# Compute total days of last year
days = totalOfDay % 365

# Display result
print(minutes, "分钟代表", years, "年，", days, "天")

# 2.8 Compute the energy needed of the water's temperature raise
# Prompt the amount of water(kilograms)、initial temperature(C)、final temperature(C) from console
# Q = M * (final temperature - initial temperature) * 4184
m_water = eval(input("请输入水的总质量，单位为千克："))
initial_temperature = eval(input("请输入一个初始温度，单位为摄氏度："))
final_temperature = eval(input("请输入一个结束温度，单位为摄氏度："))
q_energy = m_water * (final_temperature - initial_temperature) * 4184
print("需要的热量为",q_energy,"焦耳")

# 2.9 Compute the wind chill index by the wind speed and the temperature in Fahrenheit between -58 and 41
# Prompt the user to enter the temperature in Fahrenheit between -58 and 41
temperature = eval(input("请输入室外温度，单位为华氏度："))
# Prompt the user to enter the wind speed(miles per hour)
speedOfWind = eval(input("请输入风速，单位为英里每小时："))
temperatureWindChill = 35.74 + 0.6215 * temperature - 35.75 * speedOfWind ** 0.16 + 0.4275 * temperature * speedOfWind ** 0.16
print("风寒温度为",temperatureWindChill,"华氏度")

# 2.10 Compute the runway length for the airplane by speed and acceleration
# Prompt the user to enter the speed and acceleration,separated by commas
speed, acceleration = eval(input("请输入飞机的起飞速度（米/秒）和加速度（米/秒的平方），以逗号分隔："))
length = speed ** 2 / (2 * acceleration)   # 或可写为：length = speed ** 2 / 2 / acceleration
print("飞机跑道长度最小为",length,"米")

# 2.11 Compute the Initial deposit value by the Final account value and the Annual Interest Rate in percent
# Prompt the user to enter the temperature in Fahrenheit between -58 and 41
finalAccount = eval(input("最终帐户金额："))
# Prompt the user to enter the temperature in Fahrenheit between -58 and 41
annualInterestRate = eval(input("百分比表示的年利率："))
# Prompt the user to enter the temperature in Fahrenheit between -58 and 41
numberOfYears = eval(input("存入年数："))
initialDeposit = finalAccount / (1 + annualInterestRate/1200) ** (numberOfYears * 12)
print("应存入",initialDeposit,"元")

# 2.12 Print the Table,the title is (a     b     a ** b), the number of row is five
# 根据书上的学习进度，没有使用循环、条件判断
print("a    b    a ** b")
# 一个简化的计算
print(a,"   ",a + 1,"   ",a ** (a + 1))
a += 1
print(a,"   ",a + 1,"   ",a ** (a + 1))
a += 1
print(a,"   ",a + 1,"   ",a ** (a + 1))
a += 1
print(a,"   ",a + 1,"   ",a ** (a + 1))
a += 1
print(a,"   ",a + 1,"   ",a ** (a + 1))
# 使用三个变量计算
a = 1
b = a + 1
c = a ** b
print(a,"   ",b,"   ",c)
a += 1
b = a + 1
c = a ** b
print(a,"   ",b,"   ",c)
a += 1
b = a + 1
c = a ** b
print(a,"   ",b,"   ",c)
a += 1
b = a + 1
c = a ** b
print(a,"   ",b,"   ",c)
a += 1
b = a + 1
c = a ** b
print(a,"   ",b,"   ",c)

# 2.13 Print the unit、decade、hundreds place and kilobit of an integer of four digit
# 根据书上的学习进度，没有使用循环、条件判断
# Prompt the user to enter an integer of four digit
numberOfFourDigit = eval(input("请输入一个四位整数："))
unitDigit = numberOfFourDigit % 10
decadeDigit = numberOfFourDigit // 10 % 10
hundredsDigit = numberOfFourDigit // 100 % 10
kilobieDigit = numberOfFourDigit // 1000
print("输入的整数是：",numberOfFourDigit)
print("从个位至千位依次是：",unitDigit,decadeDigit,hundredsDigit,kilobieDigit)

# 2.14 Compute the area of a triangle by side of the triangle
# Prompt the user to enter three points for a triangle,separated by commas
x1,y1,x2,y2,x3,y3 = eval(input("请按照顺序输入三角形三个顶点的坐标（x1,y1,x2,y2,x3,y3），以逗号分隔："))
# Compute side of a triangle
side1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
side2 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
side3 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
print("三角形的面积是：",area)

# 2.15 Compute the area for the regular hexagon by side
# Prompt the user to enter length of side of the regular hexagon
length = eval(input("请输入正六边形的边长："))
area = 3 * 3 ** 0.5 * length ** 2 / 2
print("边长为",length,"的正六边形的面积是：",area)
# 请输入正六边形的边长：5.5
# 边长为 5.5 的正六边形的面积是： 78.59180539343781
# 与书上答案不一致

# 2.16 Compute the average acceleration by Initial Speed(v0,m/s)、Final Speed(v1,m/s) and cost time(second)
# Prompt the user to enter Initial Speed(v0,m/s)、Final Speed(v1,m/s) and cost time(second),separated by commas
v0,v1,costTime = eval(input("请依次输入初始速度（米/秒）、末速度（米/秒）、所用时间（秒），以逗号分隔："))
acce = (v1 - v0) / costTime
print("平均加速度是",acce,"米/秒的平方")

# 2.17 Compute BMI by weight and height of the person. weight in kg, height in meter, BMI = weighe / height.
# Prompt the user to enter weight in pounds and height in inches
weight = eval(input("请输入体重，单位为磅："))
height = eval(input("请输入身高，单位为英寸："))
# 1 pounds = 0.45359237 kg
# 1 inches = 0.0254 m  （书上单位换算写错了，写成1英尺等于0.0254米）
POUNDStoKG = 0.45359237
INCHEStoM = 0.0254
BMI = weight * POUNDStoKG / (height * INCHEStoM)
print("BMI is ",BMI)
# 请输入体重，单位为磅：95.5
# 请输入身高，单位为英寸：50
# BMI is  34.10871758661417
# 与书上答案不一致
'''
# 2.18 Compute the time of a Time Zone by GMT and an integer for Time Zone
# Prompt the user to enter the integer between -12 and 12 for Time Zone
timeZone = eval(input("请输入整数代表时区，在-12到12之间："))
# 计算指定时区相对GMT偏差的秒数
offsetTime = timeZone * 60 * 60

currentTime = time.time()

# Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime + offsetTime)

# Get the current second
currentSecond = totalSeconds % 60

# Obtain the total minutes
totalMinutes = totalSeconds // 60

# Compute current minute in the hour
currentMinutes = totalMinutes % 60

# Obtain the total hours
totalHours = totalMinutes // 60

# Compute current hour in the day
currentHour = totalHours % 24

# Display results
print("Time is ", currentHour,":", currentMinutes, ":", currentSecond, "in",timeZone,"Time Zone")
'''
# 2.19 Compute Future investment by amount、rate、number of years
# Prompt the user to enter the investment amount
amount = eval(input("请输入投资额："))
# Prompt the user to enter the investment rate of years
rate = eval(input("请输入年利率："))
# Prompt the user to enter the number of years
years = eval(input("请输入投资年限："))

future = amount * (1 + rate / 1200) ** (years * 12)

print("未来投资额为",future,"元。")

# 2.20 Compute the interest by balance and interest rate
# Prompt the user to enter the balance and interest rate,separated by commas
balance, rate = eval(input("请输入每月月供和年利率，以逗号分隔："))
interest = balance * (rate / 1200)
print("每月利息为", interest)

# 2.21 Compute the interest and total of the account by compound rate(5%) after six month
# 根据书上的学习进度，没有使用循环、条件判断
# Prompt the user to enter the monthly saving amount
amount = eval(input("请输入每月存入金额："))
year_rate = 0.05
monthly_rate = 0.05 / 12

total = amount * (1 + monthly_rate) ** 6 + amount * (1 + monthly_rate) ** 5  + amount * (1 + monthly_rate) ** 4 + \
        amount * (1 + monthly_rate) ** 3 + amount * (1 + monthly_rate) ** 2 + amount * (1 + monthly_rate)

print("六个月后合计有",total,"元")

# 2.22 Compute total person of after years from console years
# Prompt the user to enter years （从控制台输入一个整数，作为指定年数）
years = eval(input("请输入要计算几年之后的数据："))

CurrentPerson = 3120324986
second_of_year = 60 * 60 * 24 * 365
afterYear = CurrentPerson + (second_of_year // 7 + second_of_year // 45 - second_of_year // 13) * years
print("第",years,"年后预计有",afterYear,"人")

# 2.23 Draw four circle on Graphics from console radius
# 根据书上的学习进度，没有使用循环、条件判断
# Prompt the user to enter radius of a circle （从控制台输入一个圆的半径）
radius = eval(input("请输入圆形的半径："))
# the centre of circle(x, y)
x = radius
y = radius
turtle.penup()
turtle.goto(x, y - radius)
turtle.pendown()
turtle.circle(radius)

x = -radius
y = radius
turtle.penup()
turtle.goto(x, y - radius)
turtle.pendown()
turtle.circle(radius)

x = -radius
y = -radius
turtle.penup()
turtle.goto(x, y - radius)
turtle.pendown()
turtle.circle(radius)

x = radius
y = -radius
turtle.penup()
turtle.goto(x, y - radius)
turtle.pendown()
turtle.circle(radius)

turtle.done()

# 2.24 Draw four regular hexagon on the centre of Graphics
# 根据书上的学习进度，没有使用循环、条件判断
# the radius of the regular hexagon's circumcircle
radius = 50
# the centre of regular hexagon's circumcircle(x, y)
x = 50
y = 50
turtle.penup()
turtle.goto(x, y - radius)
turtle.pendown()
turtle.left(30)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(30)   # 回到初始角度

turtle.penup()
turtle.goto(-x, y - radius)
turtle.pendown()
turtle.left(30)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(30)   # 回到初始角度

turtle.penup()
turtle.goto(-x, -y - radius)
turtle.pendown()
turtle.left(30)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(30)   # 回到初始角度

turtle.penup()
turtle.goto(x, -y - radius)
turtle.pendown()
turtle.left(30)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(60)
turtle.forward(radius)
turtle.left(30)   # 回到初始角度

turtle.done()

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