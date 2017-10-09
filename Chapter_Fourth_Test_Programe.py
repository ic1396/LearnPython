#!/usr/bin/python3
# 《Python语言程序设计》程序清单４－编程题
# Programed List 4-Test Programme
# 第四章　编程题　４．１～４．３９

import random
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
# 4.5 输入今天是一星期的第几天（０代表星期日，１代表星期一，２代表星期二，依次类推），输入天数，计算从今天起经过输入的天数后，是星期几
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
'''
# 4.12 （检测一个数字）编写一个程序提示用户输入一个整数，然后检测该数字是否能被５和６都整除、能被５或６整除还是
# 只被它们中的一个整除（但又不能被它们同时整除）。
num = eval(input("请输入一个整数："))
# print("能被５整除","能被６整除","不能被５整除","不能被６整除","并且","或","")
# if num % 5 == 0 and num % 6 == 0
# if num % 5 == 0 or num % 6 == 0
# if num % 5 == 0 and num % 6 == 0
# 4.13 （财务应用程序：计算税款）程序清单４－７给出源代码计算单身报税人的税款。完善程序清单４－７给出其他纳税状态的源代码。

# 4.14 （游戏：头或尾）编写程序让用户猜测一个弹起的硬币显示的是正面还是反面。程序提示用户输入一个猜测值，然后显示这个猜测值是正确的还是错误的。

# 4.15 （游戏：彩票）改写程序清单４－１０产生一个三位彩票数。程序提示用户输入一个三位整数，然后根据下面的规则判断用户是否赢得奖金。

# 4.16 （随机字符）编写程序显示一个随机大写字母。

# 4.17 （游戏：剪刀、石头、布）编写程序来玩流行的剪刀－石头－布的游戏。

# 4.18 （金融问题：货币兑换）编写一个程序提示用户输入美元和人民币之间的货币汇率。

# 4.19 （计算三角形的周长）编写程序读取三角形的三个边，如果输入都是合法的则计算它的周长。否则，显示这个输入是非法的。

# 4.20 （）

# 4.21 （）

# 4.22 （）

# 4.23 （）

# 4.24 （）

# 4.25 （）

# 4.26 （）

# 4.27 （）

# 4.28 （）

# 4.29 （）

# 4.30 （）

# 4.31 （）

# 4.32 （）

# 4.33 （）

# 4.34 （）

# 4.35 （）

# 4.36 （）

# 4.37 （）

# 4.38 （）

# 4.39 （）