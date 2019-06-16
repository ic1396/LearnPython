#!/usr/bin/python3
# 《Python语言程序设计》程序清单４－编程题
# Programed List 4-Test Programme
# 第四章　编程题　４．１～４．３９

import random
import math
import turtle
import time
import re
'''
# 4.1 求解一元二：次方程 a * x * x + b * x + c = 0
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

# 4.4 判断个一位整数加法结果是否正确。
# Generate random numbers
number1 = random.randint(0, 99)
number2 = random.randint(0, 99)
# Prompt the user to enter an answer
answer = eval(input("what is " + str(number1) + " + " + str(number2) + "?"))
# Display result
print(number1, "+", number2, "=", answer, "is", number1 + number2 == answer)

# 4.5 输入今天是一星期的第几天（０代表星期日，１代表星期一，２代表星期二，依次类推），输入天数，计算从今天起
# 经过输入的天数后，是星期几
# 例如：输入１（代表今天星期一），再输入２（代表经过两天），得到结果３（代表从星期一开始经过两天后为星期三）。
today = eval(input("请输入今天是星期几（一个整数，０代表星期日，１代表星期一，２代表星期二，依次类推）："))
number = eval(input("请输入经过的天数（整数）"))
day = today + (number % 7)
if day > 7:
    day = day - 7
print(day)

# 4.6 改写《Python语言程序设计》程序清单４－６，输入身高时用英尺和英寸表示
# Prompt the user to enter weight in pounds
weight = eval(input("Enter weight in pounds: "))

# Prompt the user to enter feet of height
heightFeet = eval(input("请输入身高的英尺数部分："))

# Prompt the user to enter inches of height
heightInches = eval(input("请输入身高的英寸数部分："))

KILOGRAMS_PER_POUND = 0.45359237  # Constant
METERS_PER_INCH = 0.0254  # Constant

# Compute BMI
weightInKilograms = weight * KILOGRAMS_PER_POUND
# 1 feet == 12 inches
heightInMeters = (heightFeet * 12 + heightInches) * METERS_PER_INCH
bmi = weightInKilograms / (heightInMeters * heightInMeters)

# Display result
print("BMI is", format(bmi, ".2f"))
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

# 4.7 改写《Python语言程序设计》程序清单３－４，在结果中使用单数和复数，去掉０个的行。
# Receive the amount
amount = eval(input("Enter an amount, for example, 11.56: "))

# Convert the amount to cents
remainingAmount = int(amount * 100)

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
result = "Your amount " + str(amount) + " consists of\n" + "\t"
if numberOfOneDollars > 1:
    result += str(numberOfOneDollars) + " dollars\n" + "\t"
elif numberOfOneDollars == 1:
    result += str(numberOfOneDollars) + " dollar\n" + "\t"
if numberOfQuarters > 1:
    result += str(numberOfQuarters) + " quarters\n" + "\t"
elif numberOfQuarters == 1:
    result += str(numberOfQuarters) + " quarter\n" + "\t"
if numberOfDimes > 1:
    result += str(numberOfDimes) + " dimes\n" + "\t"
elif numberOfDimes == 1:
    result += str(numberOfDimes) + " dime\n" + "\t"
if numberOfNickels > 1:
    result += str(numberOfNickels) + " nickels\n" + "\t"
elif numberOfNickels == 1:
    result += str(numberOfNickels) + " nickel\n" + "\t"
if numberOfPennies > 1:
    result += str(numberOfPennies) + " pennies\n" + "\t"
elif numberOfPennies == 1:
    result += str(numberOfPennies) + " pennie\n" + "\t"
print(result)
这个程序里有一个计算精度问题，将浮点数转换成整型时可能会损失数字的精度，例如下面的例子：
Enter an amount, for example, 11.56: 10.03
Your amount 10.03 consists of
 	 10 dollars
 	 0 quarters
 	 0 dimes
 	 0 nickels
	 2 pennies
Process finished with exit code 0
解决问题的一个方法是输入以美分表示的整型数值。

# 4.8 三个整数按照升序排序。
a, b, c = eval(input("请输入三个整数："))
if a > b:
    a, b = b, a
    if b > c:
        b, c = c, b
        if a > b:
            a, b = b, a
elif b > c:
    b, c = c, b
    if a > b:
        a, b = b, a
print(a, b, c)

# 4.9　比较价格，同一商品的两种包装，输入每种包装的重量和价格，选择单价低的包装。
price1, weight1 = eval(input("请依次输入第一种包装的价格和重量，用逗号隔开："))
price2, weight2 = eval(input("请依次输入第二种包装的价格和重量，用逗号隔开："))
if (price1 / weight1) < (price2 / weight2) :
    print("第一种包装单价更低")
elif (price1 / weight1) > (price2 / weight2) :
    print("第二种包装单价更低")
elif (price1 / weight1) == (price2 / weight2) :
    print("两种包装单价一样")
if price1 < price2 :
    print("第一种包装价格更低")
elif price1 > price2 :
    print("第二种包装价格更低")
elif price1 == price2 :
    print("两种包装价格一样")

# 4.10 程序清单４－４随机产生一个减法问题。修改程序随机产生两个小于１００的整数的乘法。
# Generate random numbers
number1 = random.randint(0, 99)
number2 = random.randint(0, 99)
# Prompt the user to enter an answer
answer = eval(input("what is " + str(number1) + " * " + str(number2) + "?"))
# Display result
print(number1, "*", number2, "=", answer, "is", number1 * number2 == answer)

# 4.11 （找出一个月中的天数）编写程序提示用户输入月和年，然后显示这个月的天数。
year = eval(input("请输入年份："))
month = eval(input("请输入月份："))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print(year,"年",month,"月共有","31","天")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(year,"年",month,"月共有","30","天")
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        print(year,"年",month,"月共有","29","天")
    else:
        print(year,"年",month,"月共有","28","天")
        
# 4.12 （检测一个数字）编写一个程序提示用户输入一个整数，然后检测该数字是否能被５和６都整除、能被５或６整除还是
# 只被它们中的一个整除（但又不能被它们同时整除）。
num = eval(input("请输入一个整数："))
# print("能被５整除","能被６整除","不能被５整除","不能被６整除","并且","或","")
if (num % 5 == 0 and num % 6 == 0):
    print(num,"能被５整除","并且","能被６整除")
if (num % 5 == 0 or num % 6 == 0):
    print(num,"能被５整除","或","能被６整除")
if (num % 5 == 0 or num % 6 == 0) and not (num % 5 == 0 and num % 6 == 0):
    print(num,"能被５整除","或","能被６整除","not","能被５整除","并且","能被６整除")
    
# 4.13 （财务应用程序：计算税款）程序清单４－７给出源代码计算单身报税人的税款。完善程序清单４－７给出其他纳
# 税状态的源代码。
# 见 《Python语言程序设计》程序清单６－编程题 6.15

# 4.14 （游戏：头或尾）编写程序让用户猜测一个弹起的硬币显示的是正面还是反面。程序提示用户输入一个猜测值，然后
# 显示这个猜测值是正确的还是错误的。
userbool = False
user = eval(input("请输入硬币是正面还是反面向上, 0 (反面) or 1 (正面): "))
if user == 0:
    userbool = False
if user == 1:
    userbool = True
# 随机生成一个０－１００范围内的整数，偶数当作正面，奇数当作背面。
num = random.randint(0,100)
if num % 2 == 0:
    bool = True
else:
    bool = False
if userbool == bool:
    print("猜对了")
else:
    print("猜错了")

# 4.15 （游戏：彩票）改写程序清单４－１０产生一个三位彩票数。程序提示用户输入一个三位整数，然后根据下面的规则
# 判断用户是否赢得奖金。
# Generate a lottery number
lottery = random.randint(100, 999)

# Prompt the user to enter a guess
guess = eval(input("Enter your lottery pick (three digits): "))

# Get digits from lottery
lotteryDigit0 = lottery // 100
lotteryDigit1 = (lottery % 100) // 10
lotteryDigit2 = lottery % 10

# Get digits from guess
guessDigit0 = guess // 100
guessDigit1 = (guess % 100) // 10
guessDigit2 = guess % 10

print("The lottery number is", lottery)

# Check the guess
if guess == lottery:
    print("Exact match: you win $10,000")
elif ((guessDigit0 == lotteryDigit0 or guessDigit0 == lotteryDigit1 or guessDigit0 == lotteryDigit2) and \
     (guessDigit1 == lotteryDigit0 or guessDigit1 == lotteryDigit1 or guessDigit1 == lotteryDigit2) and \
     (guessDigit2 == lotteryDigit0 or guessDigit2 == lotteryDigit1 or guessDigit2 == lotteryDigit2)):
    print("Match all digits: you win $3,000")
elif ((guessDigit0 == lotteryDigit0 or guessDigit0 == lotteryDigit1 or guessDigit0 == lotteryDigit2) or \
     (guessDigit1 == lotteryDigit0 or guessDigit1 == lotteryDigit1 or guessDigit1 == lotteryDigit2) or \
     (guessDigit2 == lotteryDigit0 or guessDigit2 == lotteryDigit1 or guessDigit2 == lotteryDigit2)):
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")

# 4.16 （随机字符）编写程序显示一个随机大写字母。
num = random.randint(65, 90)
print("ASCII", num, "is", chr(num))

# 4.17 （游戏：剪刀、石头、布）编写程序来玩流行的剪刀－石头－布的游戏。
# 剪刀
SCISSOR = 0
# 石头
ROCK = 1
# 布
PAPER = 2
guess = eval(input("请输入0、１、２中的一个整数, 其中 0：剪刀, 1：石头, 2：布: "))
num = random.randint(0, 2)
if guess == SCISSOR:
    print("You are 剪刀. ")
elif guess == ROCK:
    print("You are 石头. ")
elif guess == PAPER:
    print("You are 布. ")
if num == SCISSOR:
    print("Computer are 剪刀. ")
elif num == ROCK:
    print("Computer are 石头. ")
elif num == PAPER:
    print("Computer are 布. ")
if guess == num:
    print("It is a draw.")
elif (guess < num and not(num == PAPER and guess == SCISSOR)) or (num == SCISSOR and guess == PAPER):
    print("You lost.")
elif (guess > num and not(guess == PAPER and num == SCISSOR)) or (guess == SCISSOR and num == PAPER):
    print("You won.")

# 4.18 （金融问题：货币兑换）编写一个程序提示用户输入美元和人民币之间的货币汇率。
rate = eval(input("Enter the exchange rate from Dollars to RMB: "))
exchange = eval(input("Enter 0 to convert Dollars to RMB and 1 vice versa: "))
# 0: convert Dollars to RMB; 1: convert RMB to Dollars
if exchange == 0:
    amount = eval(input("Enter the Dollars amount: "))
    print("$", amount, "is", rate * amount, "元")
else:
    amount = eval(input("Enter the RMB amount: "))
    print(amount, "元 is $", amount / rate)

# 4.19 （计算三角形的周长）编写程序读取三角形的三个边，如果输入都是合法的则计算它的周长。否则，显示这个输入
# 是非法的。
a, b, c = eval(input("请输入三角形三条边的边长，以逗号分隔："))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("三角形的周长是", a + b + c, ".")
else:
    print("输入错误，不能构成三角形。")

# 4.20 （科学方面：风寒温度）编程题２．９给出计算风寒温度的公式。实现在要求范围内计算风寒温度。
# Prompt the user to enter the temperature in Fahrenheit between -58 and 41
temperature = eval(input("请输入室外温度，单位为华氏度："))
# Prompt the user to enter the wind speed(miles per hour)
speedOfWind = eval(input("请输入风速，单位为英里每小时："))
if (-58 < temperature < 41) and (speedOfWind >= 2):
    temperatureWindChill = 35.74 + 0.6215 * temperature - 35.75 * speedOfWind ** 0.16 + 0.4275 * \
                        temperature * speedOfWind ** 0.16
    print("风寒温度为",temperatureWindChill,"华氏度")
else:
    print("输入错误，室外温度或风速不在范围内，要求　-58华氏度 < 室外温度 < 41华氏度　并且　风速 >= 2米／秒")

# 4.21 （科学问题：一周的星期几）泽勒的一致性是一个由泽勒开发的算法，用于计算一周的星期几。实现泽勒公式。
year = eval(input("请输入年(例如：2008)："))
month = eval(input("请输入月(在1-12范围内)："))
day = eval(input("请输入日期(在1-31范围内)："))
# 泽勒公式基础数据和条件
if month <= 2:
    m = 12 + month
    y = year - 1
else:
    m = month
    y = year
q = day
k = y % 100
j = y // 100
# 泽勒公式计算
h = (q + (26 * (m + 1) // 10) + k + (k // 4) + (j // 4) + 5 * j) % 7
if h == 0:
    dayOfweek = "星期六"
elif h == 1:
    dayOfweek = "星期日"
elif h == 2:
    dayOfweek = "星期一"
elif h == 3:
    dayOfweek = "星期二"
elif h == 4:
    dayOfweek = "星期三"
elif h == 5:
    dayOfweek = "星期四"
elif h == 6:
    dayOfweek = "星期五"
print(year, "年", month, "月", day, "日是", dayOfweek, "。")

# 4.22 （几何问题：点在圆内吗？）编写一个程序提示用户输入一个点(x, y)，然后检测这个点是否在圆心为(0, 0)半径
# 为10的圆内。
# 输入一个点(x, y)
pointx, pointy = eval(input("请输入 x, y："))
# 圆心为(0, 0)半径为10的圆
cx = 0
cy = 0
cr = 10
# 计算点至圆心的距离，点在圆上按在圆内计算
distance = math.sqrt(pow(pointx - cx, 2) + pow(pointy - cy, 2))
if distance <= cr:
    print("The point (", pointx, ",", pointy, ") 在以 (", cx, ",", cy, ")为圆心，半径为", cr, "的圆内。")
else:
    print("The point (", pointx, ",", pointy, ") 不在以 (", cx, ",", cy, ")为圆心，半径为", cr, "的圆内。")

# 4.23 （几何问题：点在矩形内吗？）编写一个程序提示用户输入一个点(x, y)，然后检测这个点是否在以(0, 0)为中心
# 而宽为10高为5的矩形内。
# 输入一个点(x, y)
pointx, pointy = eval(input("请输入点的坐标 x, y："))
# 以(0, 0)为中心而宽为10高为5的矩形
x = 0
y = 0
length = 10
height = 5
# 比较坐标范围判断点是否在矩形内，点在矩形边界上按矩形内计算
if (x - length / 2) <= pointx <= (x + length / 2) and (y - height / 2) <= pointy <= (y + height / 2):
    print("点 (", pointx, ",", pointy, ") 在以 (", x, ",", y, ")为中心，宽", length, "高", height, "的矩形内。")
else:
    print("点 (", pointx, ",", pointy, ") 不在以 (", x, ",", y, ")为中心，宽", length, "高", height, "的矩形内。")

# 4.24 （游戏：选出一张牌）编写程序模拟从５２张牌中选出一张。你的程序应该显示这张牌的大小和花色。
# １－１３为牌的数字，０－３为花色
num = random.randint(1, 13)
color = random.randint(0, 3)
# 将牌的数字转换为字符名称
if num == 1:
    cardname = "Ace"
elif num == 11:
    cardname = "Jack"
elif num == 12:
    cardname = "Queen"
elif num == 13:
    cardname = "King"
else:
    cardname = str(num)
# 将牌的花色转换为字符名称
if color == 0:
    cardcolor = "草花"
elif color == 1:
    cardcolor ="方块"
elif color == 2:
    cardcolor = "红桃"
elif color == 3:
    cardcolor = "黑桃"

print("抽取的牌是", cardcolor, cardname,"。")

# 4.25 （几何问题：交点）编写程序提示用户输入四个点（代表两条直线），然后显示交点（求两条直线的交点坐标）。
# 输入第一条直线
p0x, p0y, p1x, p1y = eval(input("请输入点的坐标 p0x, p0y, p1x, p1y："))
# 输入第二条直线
p2x, p2y, p3x, p3y = eval(input("请输入点的坐标 p2x, p2y, p3x, p3y："))
# 计算交点方程参数
a = p0y - p1y
b = -(p0x - p1x)
c = p2y - p3y
d = -(p2x - p3x)
e = (p0y - p1y) * p0x - (p0x - p1x) * p0y
f = (p2y - p3y) * p2x - (p2x - p3x) * p2y
# 根据计算结果判断两条直线相交还是平行
if a * d - b * c == 0:
    print("两条直线平行")
else:
# 计算两条直线的交点坐标
    px = (e * d - b * f) / (a * d - b * c)
    py = (a * f - e * c) / (a * d - b * c)
    print("两条直线的交点坐标为(", px, ",",py, ")")

# 4.26 （回文数）编写程序提示用户输入一个三位整数，然后判断它是否是一个回文数。
# 读入一个三位整数
num = eval(input("请输入一个三位整数："))
# 使用整数方式判断
new_num = (num % 10) *100 + (num // 10 % 10) * 10 + num // 100
if num == new_num:
    print(True)
else:
    print(False)
# 使用字符串方式判断
num_s = str(num)
if num == int(num_s[::-1]):
    print(True)
else:
    print(False)

# 4.27 （几何问题：点在三角形内吗？）编写程序提示用户输入一个带 x 坐标和 y 坐标的点，然后决定这个点是否在三角形内。
# 输入一个点(x, y)
x0, y0 = eval(input("请输入点的坐标 x, y："))
# 输入三角形三个顶点的坐标
x1, y1, x2, y2, x3, y3 = eval(input("请输入三角形三个顶点的坐标 x1, y1, x2, y2, x3, y3："))
# 判断是否构成三角形，以三点不在一条直线上为条件，计算由三角形三个顶点坐标构成的三阶行列式，若为0，则三点共线。
# 初始化参数值
line = True  # 三点共线标志，True：三点在一条直线上；False：三点不在一条直线上
Lambda1 = 0   # 重心坐标 λ1
Lambda2 = 0   # 重心坐标 λ2
Lambda3 = 0   # 重心坐标 λ3
if (x1 * y2 * 1 + y1 * 1 * x3 + 1 * y3 * x2 - 1 * y2 * x3 - 1 * y3 * x1 - 1 * x2 * y1) == 0:
    line = True
else:
    line = False
# 判断点在三角形内还是三角形外，使用重心坐标判断点在三角形内或外
# 计算给定点的重心坐标
if not line:
    Lambda1 = (1 * x1 * y2 + x0 * y1 * 1 + y0 * x2 * 1 - y0 * x1 * 1 - y1 * x2 * 1 - y2 * 1 * x0) / \
              (1 * x2 * y3 + x1 * y2 * 1 + y1 * x3 * 1 - y1 * x2 * 1 - y2 * x3 * 1 - y3 * 1 * x1)
    Lambda2 = (1 * x3 * y1 + x0 * y3 * 1 + y0 * x1 * 1 - y0 * x3 * 1 - y3 * x1 * 1 - y1 * 1 * x0) / \
              (1 * x2 * y3 + x1 * y2 * 1 + y1 * x3 * 1 - y1 * x2 * 1 - y2 * x3 * 1 - y3 * 1 * x1)
    Lambda3 = (1 * x2 * y3 + x0 * y2 * 1 + y0 * x3 * 1 - y0 * x2 * 1 - y2 * x3 * 1 - y3 * 1 * x0) / \
              (1 * x2 * y3 + x1 * y2 * 1 + y1 * x3 * 1 - y1 * x2 * 1 - y2 * x3 * 1 - y3 * 1 * x1)
# 根据重心坐标判断给定点的位置
if line:
    print("没有给出三角形，三点在一条直线上。")
else:
    if Lambda1 == 0 or Lambda2 == 0 or Lambda3 == 0:
        print("点在三角形的边上。", "λ1 = ", Lambda1, "，λ2 = ", Lambda2, "，λ3 = ", Lambda3)
    elif Lambda1 > 0 and Lambda2 > 0 and Lambda3 > 0:
        print("点在三角形内。", "λ1 = ", Lambda1, "，λ2 = ", Lambda2, "，λ3 = ", Lambda3)
    else:
        print("点在三角形外。", "λ1 = ", Lambda1, "，λ2 = ", Lambda2, "，λ3 = ", Lambda3)
# 在计算重心坐标时使用下列行列式：
# λ1 = det(1,x0,y0,1,x1,y1,1,x2,y2) / det(1,x1,y1,1,x2,y2,1,x3,y3)
# λ2 = det(1,x0,y0,1,x3,y3,1,x1,y1) / det(1,x1,y1,1,x2,y2,1,x3,y3)
# λ3 = det(1,x0,y0,1,x2,y2,1,x3,y3) / det(1,x1,y1,1,x2,y2,1,x3,y3)
# 之前使用下列行列式计算时，结果正好相反：
# λ1 = det(1,x0,y0,1,x1,y1,1,x2,y2) / det(1,x1,y1,1,x2,y2,1,x3,y3)
# λ2 = det(1,x0,y0,1,x1,y1,1,x3,y3) / det(1,x1,y1,1,x2,y2,1,x3,y3)
# 与上面 λ2 行列式的区别在于第二行和第三行的顺序不同，结果是与上面的 λ2 符号相反
# 问题的根源在于需要计算的面积量是有向的，没有注意矢量方向导致问题。
# λ3 = det(1,x0,y0,1,x2,y2,1,x3,y3) / det(1,x1,y1,1,x2,y2,1,x3,y3)

# 4.28 （几何问题：两个矩形）编写程序提示用户输入两个矩形中心的 x 坐标和 y 坐标以及他们的宽和高，然后决定
# 第二个矩形是否在第一个矩形里还是和第一个矩形有重叠部分。
# 输入第一个矩形的中心坐标、长和宽，矩形的长边平行于Ｘ轴，宽边平行于Ｙ轴
x0, y0, l0, h0 = eval(input("请输入矩形中心的坐标、长、宽，依次为 x, y, l, h："))
# 输入第二个矩形的中心坐标、长和宽，矩形的长边平行于Ｘ轴，宽边平行于Ｙ轴
x1, y1, l1, h1 = eval(input("请输入矩形中心的坐标、长、宽，依次为 x, y, l, h："))
# 判断两个矩形是否包含或重叠
# 判断矩形包含的条件为两个矩形中心Ｘ轴方向的距离小于等于两个矩形长之差的一半，
# 并且Ｙ轴方向的距离小于等于宽之差的一半。
if (abs(x1 - x0) <= abs(l0 - l1) / 2) and (abs(y1 - y0) <= abs(h0 - h1) / 2):
    print("第二个矩形在第一个矩形中。")
# 判断矩形重叠的条件为两个矩形中心Ｘ轴方向的距离大于两个矩形长之差的一半，小于等于两个矩形的长度一半的和；
# 并且Ｙ轴方向的距离大于宽之差的一半，小于等于两个矩形的宽度一半的和。
if (abs(l0 - l1) / 2 < abs(x1 - x0) <= l0 / 2 + l1 / 2) and (abs(h0 - h1) / 2 < abs(y1 - y0) <= h0 / 2 + h1 / 2):
    print("第二个矩形和第一个矩形有重叠。")
# 判断矩形分离的条件为两个矩形中心Ｘ轴方向的距离大于两个矩形的长度一半的和；
# 或Ｙ轴方向的距离大于两个矩形的宽度一半的和。
if (abs(x1 - x0) > l0 / 2 + l1 / 2) or (abs(y1 - y0) > h0 / 2 + h1 / 2):
    print("第二个矩形在第一个矩形外。")

# 4.29 （几何问题：两个圆）编写程序提示用户输入两个圆的中心的 x 坐标和 y 坐标以及他们的半径，然后决定第二个圆是否
# 在第一个圆里还是和第一个圆有重叠部分。
# 输入第一个圆的圆心坐标和半径
x0, y0, r0 = eval(input("请输入第一个圆的圆心坐标和半径，依次为 x, y, r："))
# 输入第二个圆的圆心坐标和半径
x1, y1, r1 = eval(input("请输入第二个圆的圆心坐标和半径，依次为 x, y, r："))
# 计算两个圆心间的距离
distance = math.sqrt(pow(x1 - x0, 2) + pow(y1 - y0, 2))
# 判断两个圆是否包含或重叠
if distance <= abs(r1 - r0):
    # 两个圆包含的条件：圆心的距离小于等于半径之差
    print("两个圆包含。")
elif abs(r1 - r0) < distance <= r1 + r0:
    # 两个圆重叠的条件：圆心的距离大于半径之差，小于等于半径之和
    print("两个圆相交。")
else:
    # 两个圆分离的条件：圆心的距离大于半径之和
    print("两个圆分离。")

# 4.30 （当前时间）使用１２小时的时钟修改编程题 2.18 来显示小时数。
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
if currentHour > 12:
    currentHour_12 = currentHour % 12
    currentHour_s = str(currentHour_12) + "PM"
else:
    currentHour_s = str(currentHour) + "AM"

# Display results
print("Time is ", currentHour,":", currentMinutes, ":", currentSecond, "in",timeZone,"Time Zone (24H)")
print("Time is ", currentHour_s,":", currentMinutes, ":", currentSecond, "in",timeZone,"Time Zone (12H)")

# 4.31 （几何问题：点的位置）编写程序提示用户输入三个点 p0、p1、p2 的 x 坐标和 y 坐标，然后显示 p2 是在从 p0 到 p1 的线
# 的左边、右边还是在同一线上。
pointx, pointy = eval(input("请输入点的坐标 x, y："))
x0, y0 = eval(input("请输入点的坐标 x0, y0："))
x1, y1 = eval(input("请输入点的坐标 x1, y1："))
if (x1 - x0) * (pointy - y0) - (pointx - x0) * (y1 - y0) > 0:
    print("点在直线左侧")
elif (x1 - x0) * (pointy - y0) - (pointx - x0) * (y1 - y0) == 0:
    print("点在直线上")
else:
    print("点在直线右侧")

# 4.32 （几何问题：线段上的点）编程题 4.31 显示如何测试一个点是否在一个无界的行上。修改编程题 4.31 来测试一个点是否在一
# 个线段上。
pointx, pointy = eval(input("请输入点的坐标 x, y："))
x0, y0 = eval(input("请输入有向线段起始点的坐标 x0, y0："))
x1, y1 = eval(input("请输入有向线段结束点的坐标 x1, y1："))
if (x1 - x0) * (pointy - y0) - (pointx - x0) * (y1 - y0) > 0:
    print("点在线段所在直线左侧")
elif (x1 - x0) * (pointy - y0) - (pointx - x0) * (y1 - y0) == 0:
    print("点在线段所在直线上")
    if abs(pointx - x0) < abs(x1 - x0) and abs(pointx - x1) < abs(x1 - x0) and \
       abs(pointy - y0) < abs(y1 - y0) and abs(pointy - y1) < abs(y1 - y0):
        print("同时点在线段内")
    else:
        print("同时点在线段外")
else:
    print("点在线段所在直线右侧")

# 4.33 （十进制转十六进制）编写一个程序提示用户输入一个０到１５之间的整数，然后显示它对应的十六进制数。
dec = eval(input("请输入："))
print("十进制数为：", dec)
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))

# 4.34 （十六进制转十进制）编写一个程序提示用户输入一个十六进制的字符，然后显示它对应的十进制整数。
s_hex = input("请输入：")
#
re_Hex = r'\A[0-9a-fA-F]+\Z'
p_hex = re.compile(re_Hex)

print("十进制数为：", int(s_hex, 16))

# 4.35 （Tuttle：点的位置）编写程序提示用户输入三个点 p0、p1、p2 的 x 坐标和 y 坐标，然后显示 p2 是在从 p0 到 p1 的线
# 的左边、右边还是在线上。参见编程题 4.31 确定点的位置。
pointx, pointy = eval(input("请输入点的坐标 x, y："))
x0, y0 = eval(input("请输入有向线段起始点的坐标 x0, y0："))
x1, y1 = eval(input("请输入有向线段结束点的坐标 x1, y1："))
if (x1 - x0) * (pointy - y0) - (pointx - x0) * (y1 - y0) > 0:
    print("left")
    result = "left"
elif (x1 - x0) * (pointy - y0) - (pointx - x0) * (y1 - y0) == 0:
    print("on")
    result = "on"
    if abs(pointx - x0) < abs(x1 - x0) and abs(pointx - x1) < abs(x1 - x0) and \
        abs(pointy - y0) < abs(y1 - y0) and abs(pointy - y1) < abs(y1 - y0):
        print("on the line segment")
        result = "on the line segment"
else:
    print("right")
    result = "right"
# 绘制有向线段，从起始点到结束点
turtle.penup()
turtle.goto(x0, y0)
turtle.pendown()
turtle.goto(x1, y1)

# 绘制点
turtle.penup()
turtle.goto(pointx, pointy)
turtle.pendown()
turtle.dot(3, "red")
# 结论
turtle.color("green")
turtle.penup()       # Pull the pen up
turtle.goto(150, -150)
turtle.pendown()      # Pull the pen down
turtle.write(result, font = ("Times", 16, "bold"))
turtle.hideturtle()

turtle.done()

# 4.36 （Tuttle：点在矩形内吗？）编写一个程序提示用户输入一个点(x, y)，然后检测这个点是否在以(0, 0)为中心、宽为 100、高
# 为 50 的矩形内。
# 输入一个点(x, y)
pointx, pointy = eval(input("请输入点的坐标 x, y："))
# 以(0, 0)为中心而宽为100高为50的矩形
x = 0
y = 0
length = 100
height = 50
# 比较坐标范围判断点是否在矩形内，点在矩形边界上按矩形内计算
if (x - length / 2) <= pointx <= (x + length / 2) and (y - height / 2) <= pointy <= (y + height / 2):
    print("点 (", pointx, ",", pointy, ") 在以 (", x, ",", y, ")为中心，宽", length, "高", height, "的矩形内。")
    result = "点 (" + str(pointx) + "," + str(pointy) + ") 在以 (" + str(x) + "," + str(y) + \ 
    ")为中心，宽" + str(length) + "高" + str(height) + "的矩形内。"
else:
    print("点 (", pointx, ",", pointy, ") 不在以 (", x, ",", y, ")为中心，宽", length, "高", height, "的矩形内。")
    result = "点 (" + str(pointx) + "," + str(pointy) + ") 不在以 (" + str(x) + "," + str(y) + \ 
    ")为中心，宽" + str(length) + "高" + str(height) + "的矩形内。"
# 绘制矩形
turtle.penup()
turtle.goto(x - length / 2, y + height / 2)
turtle.pendown()
turtle.goto(x + length / 2, y + height / 2)
turtle.goto(x + length / 2, y - height / 2)
turtle.goto(x - length / 2, y - height / 2)
turtle.goto(x - length / 2, y + height / 2)
# 绘制点
turtle.penup()
turtle.goto(pointx, pointy)
turtle.pendown()
turtle.dot(3, "red")
# 结论
turtle.color("green")
turtle.penup()       # Pull the pen up
turtle.goto(200, -200)
turtle.pendown()      # Pull the pen down
turtle.write(result, font = ("Times", 18, "bold"))
turtle.hideturtle()

turtle.done()

# 4.37 （）
# 书中没有题号 4.37

# 4.38 （几何问题：两个矩形）编写程序提示用户输入两个矩形的中心的 x　坐标、　y　坐标、宽度和高度，然后决定第二个矩形是在
# 第一个矩形内还是和第一个矩形有重叠，还是没有重叠。
# 输入第一个矩形的中心坐标、长和宽，矩形的长边平行于Ｘ轴，宽边平行于Ｙ轴
x0, y0, l0, h0 = eval(input("请输入矩形中心的坐标、长、宽，依次为 x, y, l, h："))
# 输入第二个矩形的中心坐标、长和宽，矩形的长边平行于Ｘ轴，宽边平行于Ｙ轴
x1, y1, l1, h1 = eval(input("请输入矩形中心的坐标、长、宽，依次为 x, y, l, h："))
# 判断两个矩形是否包含或重叠
# 判断矩形包含的条件为两个矩形中心Ｘ轴方向的距离小于等于两个矩形长之差的一半，
# 并且Ｙ轴方向的距离小于等于宽之差的一半。
if (abs(x1 - x0) <= abs(l0 - l1) / 2) and (abs(y1 - y0) <= abs(h0 - h1) / 2):
    print("第二个矩形在第一个矩形中。")
    result = "第二个矩形在第一个矩形中。"
# 判断矩形重叠的条件为两个矩形中心Ｘ轴方向的距离大于两个矩形长之差的一半，小于等于两个矩形的长度一半的和；
# 并且Ｙ轴方向的距离大于宽之差的一半，小于等于两个矩形的宽度一半的和。
if (abs(l0 - l1) / 2 < abs(x1 - x0) <= l0 / 2 + l1 / 2) and (abs(h0 - h1) / 2 < abs(y1 - y0) <= h0 / 2 + h1 / 2):
    print("第二个矩形和第一个矩形有重叠。")
    result = "第二个矩形和第一个矩形有重叠。"
# 判断矩形分离的条件为两个矩形中心Ｘ轴方向的距离大于两个矩形的长度一半的和；
# 或Ｙ轴方向的距离大于两个矩形的宽度一半的和。
if (abs(x1 - x0) > l0 / 2 + l1 / 2) or (abs(y1 - y0) > h0 / 2 + h1 / 2):
    print("第二个矩形在第一个矩形外。")
    result = "第二个矩形在第一个矩形外。"
# 绘制第一个矩形
turtle.penup()
turtle.goto(x0 - l0 / 2, y0 + h0 / 2)
turtle.pendown()
turtle.goto(x0 + l0 / 2, y0 + h0 / 2)
turtle.goto(x0 + l0 / 2, y0 - h0 / 2)
turtle.goto(x0 - l0 / 2, y0 - h0 / 2)
turtle.goto(x0 - l0 / 2, y0 + h0 / 2)
# 绘制第二个矩形
turtle.penup()
turtle.goto(x1 - l1 / 2, y1 + h1 / 2)
turtle.pendown()
turtle.goto(x1 + l1 / 2, y1 + h1 / 2)
turtle.goto(x1 + l1 / 2, y1 - h1 / 2)
turtle.goto(x1 - l1 / 2, y1 - h1 / 2)
turtle.goto(x1 - l1 / 2, y1 + h1 / 2)
# 结论
turtle.color("green")
turtle.penup()       # Pull the pen up
turtle.goto(200, -200)
turtle.pendown()      # Pull the pen down
turtle.write(result, font = ("Times", 18, "bold"))
turtle.hideturtle()

turtle.done()

# 4.39 （Tuttle：两个圆）编写程序提示用户输入两个圆的圆心的坐标以及两个半径，然后确定第二个圆是在第一个圆内还是和第一个
# 圆有重叠部分。
# 输入第一个圆的圆心坐标和半径
x0, y0, r0 = eval(input("请输入第一个圆的圆心坐标和半径，依次为 x, y, r："))
# 输入第二个圆的圆心坐标和半径
x1, y1, r1 = eval(input("请输入第二个圆的圆心坐标和半径，依次为 x, y, r："))
# 计算两个圆心间的距离
distance = math.sqrt(pow(x1 - x0, 2) + pow(y1 - y0, 2))
# 判断两个圆是否包含或重叠
if distance <= abs(r1 - r0):
    # 两个圆包含的条件：圆心的距离小于等于半径之差
    print("两个圆包含。")
    result = "两个圆包含。"
elif abs(r1 - r0) < distance <= r1 + r0:
    # 两个圆重叠的条件：圆心的距离大于半径之差，小于等于半径之和
    print("两个圆相交。")
    result = "两个圆相交。"
else:
    # 两个圆分离的条件：圆心的距离大于半径之和
    print("两个圆分离。")
    result = "两个圆分离。"

# 绘图：第一个圆
turtle.penup()       # Pull the pen up
turtle.goto(x0, y0 - r0)
turtle.setheading(0)
turtle.left(0)
turtle.pendown()      # Pull the pen down
# turtle.begin_fill()   # Begin to fill color in a shape
turtle.color("purple")
turtle.circle(r0)  # Draw a circle
# turtle.end_fill()     # Fill the shape

# 绘图：第二个圆
turtle.penup()       # Pull the pen up
turtle.goto(x1, y1 - r1)
turtle.setheading(0)
turtle.left(0)
turtle.pendown()      # Pull the pen down
# turtle.begin_fill()   # Begin to fill color in a shape
turtle.color("red")
turtle.circle(r1)  # Draw a circle
# turtle.end_fill()     # Fill the shape

# 结论
turtle.color("green")
turtle.penup()       # Pull the pen up
turtle.goto(200, -200)
turtle.pendown()      # Pull the pen down
turtle.write(result, font = ("Times", 18, "bold"))
turtle.hideturtle()

turtle.done()
'''