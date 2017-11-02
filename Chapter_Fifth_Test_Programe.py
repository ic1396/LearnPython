#!/usr/bin/python3
# 《Python语言程序设计》程序清单５－编程题
# Programed List 5-Test Programme
# 第五章　编程题　５．１～５．５５

import random
import time

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
'''
# 5.3 （公斤转换成磅）编写一个程序能显示下面的表格（１公斤是２．２磅）。

# 5.4 （英里转换成公里）编写一个程序能显示下面的表格（注意：１英里是１．６０９公里）。

# 5.5 （公斤转换成磅，磅转换成公斤）编写一个程序能显示下面两个相邻的表格（注意：１公斤等于２．２磅）。

# 5.6 （将英里转换成公里，公里转换成英里）编写一个程序能显示下面两个相邻的表格（注意：１英里等于１．６０９公里）。。

# 5.7 （使用三角函数）打印下面的表格显示从０度到３６０度每隔１０度的角度的ｓｉｎ值和ｃｏｓ值。四舍五入这些值，保持小数点
# 后四位。

# 5.8 （使用ｍａｔｈ．ｓｑｒｔ函数）使用ｍａｔｈ模块中的ｓｑｒｔ函数来编写程序输出下面的表格。

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

# 5.23 （财务应用程序：比较不同利率的贷款）

# 5.24 （财务应用程序：贷款摊销时间表）

# 5.25 （演示消除错误）

# 5.26 （数列求和）

# 5.27 （计算Ｐｉ）

# 5.28 （计算ｅ）

# 5.29 （显示闰年）

# 5.30 （显示每个月的第一天）

# 5.31 （显示日历）

# 5.32 （财务应用程序：复合值）

# 5.33 （财务应用程序：计算ＣＤ值）

# 5.34 （游戏：彩票）

# 5.35 （完全数）

# 5.36 （游戏：石头、剪刀、布）

# 5.37 （求和）

# 5.38 （模拟：时钟倒计时）

# 5.39 （财务应用程序：找出销售额）

# 5.40 （模拟：硬币正反面）

# 5.41 （最大数字的出现）

# 5.42 （蒙特卡罗模拟）

# 5.43 （数学问题：组合）

# 5.44 （十进制到二进制）

# 5.45 （十进制到十六进制）

# 5.46 （统计方面：计算均值和标准方差）

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
