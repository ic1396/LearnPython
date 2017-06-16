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
'''
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