#!/usr/bin/python3
# 《Python语言程序设计》程序清单５－编程题
# Programed List 5-Test Programme
# 第五章　编程题　５．１～５．５５

import random
import time
import math

'''
# 5.1 （统计正数和负数的个数然后计算这些数的平均值）编写一个程序来读入不指定个数的整数，然后决定已经读取的整数
# 中有多少个正整数和多少个负整数并计算这些输入值（不统计０）的总和，最终得出它们的平均值。这个程序以输入值０来
# 结束。使用浮点数显示这个平均值。
positive_Number = 0
negative_Number = 0
average = 0
total = 0
number = eval(input("Enter an integer, the input ends if it is 0: "))
while number != 0:
    if number > 0:
        positive_Number += 1
    else:
        negative_Number += 1
    total = total + number
    number = eval(input("Enter an integer, the input ends if it is 0: "))
average = total / (positive_Number + negative_Number)
print("Positive Number: ", positive_Number)
print("Negative Number: ", negative_Number)
print("Total: ", total)
print("Average: ", average)

# 5.2 （累加）程序清单５－４中产生五个随机减法的问题。改写这个程序，产生两个在１到１５之间的随机数的加法问题，
# 显示回答正确的次数和测试所用的时间。
correctCount = 0 # Count the number of correct answers
count = 0 # Count the number of questions
NUMBER_OF_QUESTIONS = 5 # Constant

startTime = time.time() # Get start time

while count < NUMBER_OF_QUESTIONS:
    # 1. Generate two random single-digit integers
    number1 = random.randint(1, 16)
    number2 = random.randint(1, 16)

    # 2. Prompt the student to answer "what is number1 - number2?"
    answer = eval(input("What is " + str(number1) + " + " +
        str(number2) + "? "))

    # 5. Grade the answer and display the result
    if number1 + number2 == answer:
        print("You are correct!")
        correctCount += 1
    else:
        print("Your answer is wrong.\n", number1, "+",
            number2, "should be", (number1 + number2))

    # Increase the count
    count += 1

endTime = time.time() # Get end time
testTime = int(endTime - startTime) # Get test time
print("Correct count is", correctCount, "out of",
    NUMBER_OF_QUESTIONS, "\nTest time is", testTime, "seconds")

# 5.3 （公斤转换成磅）编写一个程序能显示下面的表格（１公斤是２．２磅）。
print("______________")
print("   公斤  |   磅   ")
for i in range(1,200):
    if i % 2 == 1:
        print("--------------")
        print(format(i,"4d"), end='')
        print("    |  ", end='')
        print(format(i * 2.2,".1f"))
print("______________")

# 5.4 （英里转换成公里）编写一个程序能显示下面的表格（注意：１英里是１．６０９公里）。
i = 1
print("________________")
print("   英里  |   公里    ")
while i < 11:
    print("----------------")
    print(format(i,"4d"), end='')
    print("  |  ", end='')
    print(format(i * 1.609,".3f"))
    i += 1
print("________________")

# 5.5 （公斤转换成磅，磅转换成公斤）编写一个程序能显示下面两个相邻的表格（注意：１公斤等于２．２磅）。
j = 20
print("____________________________________")
print("   k  |   b   ||   k  |   b   ")
for i in range(1,200):
    if i % 2 == 1:
        print("------------------------------------")
        print(format(i,"4d"), end='')
        print("  |  ", end='')
        print(format(i * 2.2,".1f"), end='')
        print("  ||  ", end='')
        print(format(j / 2.2, ".2f"), end='')
        print("  |  ", end='')
        print(j)
    if i % 2 == 0:
        j += 5
print("____________________________________")

# 5.6 （将英里转换成公里，公里转换成英里）编写一个程序能显示下面两个相邻的表格（注意：１英里等于１．６０９公里）。。
i = 1
j = 20
print("___________________________________")
print("   m  |   km    ||   m    |   km   ")
while i < 11:
    print("-----------------------------------")
    print(format(i,"4d"), end='')
    print("  |  ", end='')
    print(format(i * 1.609,".3f"), end='')
    print("  ||  ", end='')
    print(format(j / 1.609, ".3f"), end='')
    print("|  ", end='')
    print(format(j, "4d"))
    j = j + 5
    i += 1
print("___________________________________")

# 5.7 （使用三角函数）打印下面的表格显示从０度到３６０度每隔１０度的角度的ｓｉｎ值和ｃｏｓ值。四舍五入这些值，保持小数点
# 后四位。
i = 10
print("___________________________")
print("   d  |   sin    |   cos   ")
while i <= 360:
    print("----------------------------")
    print(format(i,"4d"), end='')
    print("  |  ", end='')
    print(format(math.sin(math.radians(i)),".4f"), end='')
    print("  |  ", end='')
    print(format(math.cos(math.radians(i)), ".4f"))
    i += 10
print("___________________________")

# 5.8 （使用ｍａｔｈ．ｓｑｒｔ函数）使用ｍａｔｈ模块中的ｓｑｒｔ函数来编写程序输出下面的表格。
i = 0
print("___________________________")
print("  Number  | Square Root   ")
while i <= 20:
    print("----------------------------")
    print(format(i,"4d"), end='')
    print("  |  ", end='')
    print(format(math.sqrt(i),".4f"))
    i += 2
print("___________________________")
'''
# 5.9 （财务应用程序：计算未来学费）假设大学今年的学费是１００００美元，且以每年５％增长。编写程序计算十年之后的学费以及
# 从现在开始到十年后大学四年的总学费。

# 5.10 （找出最高分）编写程序提示用户输入学生个数以及每个学生的分数，然后显示最高分。假设输入是存储在一个名
# 为ｓｃｏｒｅ．ｔｘｔ的文件，程序从这个文件获取输入。

# 5.11 （找出两个最高分）编写程序提示用户输入学生个数以及每个学生的分数，然后显示最高分和次高分的分数。

# 5.12 （找出可被５和６同时整除的数）编写程序找出在１００和１０００之间所有被５和６同时整除的数，每行显示１０个数。这
# 些数被一个空格隔开。

# 5.13 （找出可被５或６整除但又不能被它俩同时整除的数）编写程序找出在１００和１０００之间所有被５或６整除但又不能被它俩
# 同时整除的数，每行显示１０个数。这些数被一个空格隔开。

# 5.14 （找出最小的ｎ满足ｎ的平方大于１２０００）使用ｗｈｉｌｅ循环找出最小的整数ｎ满足大于１２０００。

# 5.15 （找出最大的ｎ满足ｎ的立方小于１２０００）使用ｗｈｉｌｅ循环找出最大的整数ｎ满足小于１２０００。

# 5.16 （计算最大公约数）对于程序清单５－８，另外一种找出两个整数ｎ１和ｎ２的最大公约数的解决方案如下所示：首先找出ｎ１
# 和ｎ２的最小数ｄ，然后以ｄ、ｄ－１、ｄ－２、．．．、２、１的顺序依次检测它们是否是ｎ１和ｎ２的公因子。第一个这样的公
# 约数就是ｎ１和ｎ２的最大公约数。

# 5.17 （显示ＡＳＣＩＩ字符表）编写程序显示ＡＳＣＩＩ字符表中从！到～的字符。每行显示十个字符，字符被一个空格隔开。

# 5.18 （找出一个整数的所有因子）编写程序读取一个整数，然后显示它所有的最小因子，也称之为素因子。

# 5.19 （显示一个金字塔）编写程序提示用户输入一个在１到１５之间的整数，然后显示一个金字塔，示例运行如下所示。

# 5.20 （使用循环显示四种模式）使用嵌套循环在四个独立的程序中显示下面四种模式。

# 5.21 （在金字塔模式中显示数字）编写一个嵌套ｆｏｒ循环来显示下面的输出。

# 5.22 （显示在２和１０００之间的素数）修改程序清单５－１３，显示在２和１０００之间且包括２和１０００的素数，每行显示８
# 个素数。

# 5.23 （财务应用程序：比较不同利率的贷款）编写程序让用户输入贷款额以及以年为单位的贷款周期，然后显示利率从５％开始，
# 每次增加１／８，直到８％的每月还贷额和总的还款额。

# 5.24 （财务应用程序：贷款摊销时间表）编写程序让用户输入贷款额、年数以及利率，然后显示贷款摊销时间表。

'''
# 5.25 （演示消除错误）当你操作一个非常大的数和非常小的数时，就会出现消除错误。大数可能会抵消比较小的数。为了避免消除
# 错误并获取更精确的结果，应该仔细选择计算的顺序。例如：在计算下面数列的过程中，可以从右向左而不是从左向右计算，这样将
# 会获取更精确地结果。
# 使用１＋１／２＋１／３＋．．．＋１／ｎ的顺序计算
total = 0
for i in range(1, 50001):
    total = total + 1 / i
print(format(total, ".100f"))
total = 0
number = 50000
while number > 0:
    total = total + 1 / number
    number -= 1
print(format(total, ".100f"))
# 使用１／ｎ＋．．．＋１／３＋１／２＋１的顺序计算

# 5.26 （数列求和）编写程序对下面的数列求和。
# 使用１／３＋３／５＋５／７＋．．．＋９７／９９计算
item = 0
for i in range(1, 98):
    if i % 2 == 1:
        item = item + i / (i + 2)
print(item)

# 5.27 （计算Ｐｉ）使用下面的数列近似计算ｅ。
number = eval(input("Enter an integer: "))
number0 = number
# 使用（－１）的（ｉ＋１）次幂除以（２ｉ－１）
item = 0
while number > 0:
    if number % 2 == 0:
        item = item - 1 / (2 * number - 1)
    if number % 2 == 1:
        item = item + 1 / (2 * number - 1)
    number -= 1
Pi = 4 * item
print("Pi is", format(Pi, ".100f"))

# 5.28 （计算ｅ）使用下面的数列近似计算ｅ。
number = eval(input("Enter an integer: "))
number0 = number
# 使用 １＋１／１！＋１／２！＋１／３！＋．．．＋１／ｎ！计算，使用１＊２＊３＊．．．＊ｎ的方式计算ｎ！
e = 1
item = 1
for i in range(1, number + 1):
    item = item * i
    e = e + 1 / item
print(format(e, ".100f"))
# 使用 １＋１／１！＋１／２！＋１／３！＋．．．＋１／ｎ！计算，使用１／（ｎ－１）！／ｎ的方式计算１／ｎ！
e = 1
item = 1
for i in range(1, number + 1):
    item = item / i
    e = e + item
print(format(e, ".100f"))
# 使用 １／ｎ！＋．．．＋１／３！＋１／２！＋１／１！＋１计算，使用１＊２＊３＊．．．＊ｎ的方式计算ｎ！
e = 0
number = number0
while number > 0:
    item = 1
    for j in range(1, number + 1):
        item = item * j
    e = e + 1 / item
    number -= 1
e = e + 1
print(format(e, ".100f"))
# 使用 １／ｎ！＋．．．＋１／３！＋１／２！＋１／１！＋１计算，使用１／（ｎ－１）！／ｎ的方式计算１／ｎ！
e = 0
number = number0
while number > 0:
    item = 1
    for j in range(1, number + 1):
        item = item / j
    e = e + item
    number -= 1
e = e + 1
print(format(e, ".100f"))
'''
# 5.29 （显示闰年）编写程序显示２１世纪（从２００１年到２１００年）里所有的闰年，每行显示１０个闰年。这些年被一个空格隔开。

# 5.30 （显示每个月的第一天）编写程序提示用户输入年份以及该年的第一天是星期几，然后在控制台上显示该年每个月的第一天是
# 星期几。

# 5.31 （显示日历）编写程序提示用户输入年份以及该年的第一天是星期几，然后在控制台上显示该年的日历表。

# 5.32 （财务应用程序：复合值）编写程序提使用户输入一个数额、年利率和月份数，然后显示给定的月份之后的储蓄账户上的数额。

# 5.33 （财务应用程序：计算ＣＤ值）编写程序提使用户输入一个数额、年收益率以及月份数，然后显示如下所示的示例运行结果。

# 5.34 （游戏：彩票）改写程序清单４－１０来随机产生一个两位数的抽奖数。数字中的两位是不同的。

# 5.35 （完全数）如果一个正整数等于除了它本身之外所有正因子的和，那么这个数被称为完全数。例如６＝３＋２＋１，
# ２８＝１４＋７＋４＋２＋１。小于１００００的完全数有四个。编写程序找出这四个数。

# 5.36 （游戏：石头、剪刀、布）编程题４．１７给出玩石头、剪刀、布游戏的程序。改写程序让用户不断玩直到用户或计算机中的某
# 一方能够赢得游戏超过两次。

# 5.37 （求和）编写程序计算下面的和。

# 5.38 （模拟：时钟倒计时）你可以使用ｔｉｍｅ模块中的ｔｉｍｅ．ｓｌｅｅｐ（ｓｅｃｏｎｄｓ）函数让程序暂停指定的秒数。

# 5.39 （财务应用程序：找出销售额）编写程序找出为了挣３００００美元，你的最小销售额。

# 5.40 （模拟：硬币正反面）编写程序模拟将硬币翻一百万次，然后显示硬币出现正面和反面的次数。

# 5.41 （最大数的出现）编写程序读取整数，找出它们中的最大值，然后计算它的出现次数。假使输入以数字０结束。

# 5.42 （蒙特卡罗模拟）一个正方形被分为四个更小的区域，如图ａ所示。如果你投掷一个飞镖到这个正方形一百万次，这个飞镖落
# 在一个奇数区域里的概率是多少？编写程序模拟这个过程然后显示结果。

# 5.43 （数学问题：组合）编写程序显示从１到７的整数中选取两个数的所有可能组合，同时显示组合的总个数。

# 5.44 （十进制到二进制）编写程序提示用户输入一个十进制数，然后显示它对应的二进制数。

# 5.45 （十进制到十六进制）编写程序提示用户输入一个十进制数，然后显示它对应的十六进制数。

# 5.46 （统计方面：计算均值和标准方差）编写一个程序提示用户输入１０个数字，然后使用下面的公式显示均值和标准方差。

# 5.47 （Turtle：绘制随机球）编写程序显示１０个随机球，它们在一个宽１２０高１００的矩形里，这个矩形的中心点在（０，０）。

# 5.48 （Turtle：绘制圆）编写程序绘制１０个圆，中心选在（０，０）。

# 5.49 （Turtle：显示乘法口诀表）编写程序显示一个乘法口诀表。

# 5.50 （Turtle：显示三角形图案的数字）编写程序显示三角形图案的数字。

# 5.51 （Turtle：显示一个格子）编写程序显示１８＊１８的格子。

# 5.52 （Turtle：绘制ｓｉｎ函数）编写程序绘制ｓｉｎ函数，如图所示。在点（－１００，－１５）处显示－２Ｐｉ，坐标原点在
# （０，０）处，在点（１００，－１５）出显示２Ｐｉ。

# 5.53 （Turtle：绘制ｓｉｎ函数和ｃｏｓ函数）编写程序绘制蓝色的ｓｉｎ函数和红色的ｃｏｓ函数。

# 5.54 （Turtle：绘制平方函数）编写程序绘制平方函数示意图。

# 5.55 （Turtle：棋盘）编写程序绘制一个棋盘，如图所示（国际象棋棋盘）。
