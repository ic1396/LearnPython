#!/usr/bin/python3
# 《Python语言程序设计》程序清单６－编程题
# Programed List 6-Test Programme
# 第六章　编程题　６．１～６．４８

# from PrimeNumberFunction import *

'''
# 6.1
# 一个返回五角数（n * （3 * n - 1） / 2， 其中 n = 1、2、3...）的函数。
def getPentagonalNumber(n):
    return int(n * (3 * n - 1) / 2)
def main():
    for i in range(1, 101, 1):
        print(format(getPentagonalNumber(i), "5d"), end=" ")
        if i % 10 == 0:
            print()
main()
# 6.2
# 计算一个整数各数字和的函数。
def sumDigits(n):
    sum = 0
    while n > 0:
        sum = sum + n % 10
        n = n // 10
    return sum

def main():
    n = eval(input("请输入一个正整数："))
    print("各数字之和为（若输入负数返回 0 ）：", sumDigits(n))
main()
# 6.3
# 判断一个数是否为回文数。
# 生成一个数的反向数
def reverse(number):
    if number <= 0:
        return  0
    re_number = 0
    while number > 0:
        re_number = re_number * 10
        re_number = re_number + number % 10
        number = number // 10
    return re_number
# 判断一个数是否为回文数
def isPalindrome(number):
    if number <= 0:
        return False
    return True if number == reverse(number) else False
def main():
    n = eval(input("请输入一个正整数："))
    if isPalindrome(n):
        print(n, "是一个回文数。")
    else:
        print(n, "不是一个回文数。")
main()
# 6.4
# 反向显示一个整数
# 生成一个数的反向数
def reverse(number):
    if number <= 0:
        return  0
    re_number = 0
    while number > 0:
        re_number = re_number * 10
        re_number = re_number + number % 10
        number = number // 10
    return re_number
def main():
    n = eval(input("请输入一个正整数："))
    print(n, "的反向数是", reverse(n))
main()
# 6.5
# 对三个数按升序进行排序。
def displaySortedNumbers(num1, num2, num3):
    minnum1 = num1
    if num2 < num1:
        minnum1 = num2
        num2 = num1
        num1 = minnum1
    if num3 < num1:
        minnum1 = num3
        num3 = num2
        num2 = num1
        num1 = minnum1
    elif num3 < num2:
        minnum1 = num3
        num3 = num2
        num2 = minnum1
    print("按升序排序为：", num1, num2, num3)
def main():
    num1, num2, num3 = eval(input("请输入三个数："))
    displaySortedNumbers(num1, num2, num3)
main():
# 6.6
def displayPattern(n):
    for i in range(1, n + 1, 1):
        j = 0
        while j < n - i:
            print("    ", end='')
            j += 1
        for k in range(i, 0, -1):
            print(format(k, "4d"), end='')
        print()
def main():
    n = eval(input("请输入一个正整数："))
    displayPattern(n)
main()
# 6.7
# 用指定的投资额度、年数和给定的利率计算未来投资价值
def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    return investmentAmount * pow(1 + monthlyInterestRate, years * 12)
def main():
    investmentAmount = eval(input("请输入投资总额度："))
    yearInterestRate = eval(input("请输入年利率："))
    years = eval(input("请输入投资总年数："))
    print("投资总额度：", investmentAmount)
    print("年利率：", yearInterestRate)
    print("投资总年数：", years)
    print("  年  ", "  收益  ")
    for i in range(1, years + 1, 1):
        print(format(i, "3d"), "    ", format(futureInvestmentValue(investmentAmount, yearInterestRate / 12 / 100, i), "6.2f"))
main()
# 6.8
# 摄氏度和华氏度间的互相转换
# 摄氏度转华氏度
def celsiusToFahrenheit(celsius):
    return (9 / 5) * celsius + 32
# 华氏度转摄氏度
def fahrenheitToCelsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)
def main():
    print("______________________________________________________")
    print("  Celsius  |  Fahrenheit  ||  Fahrenheit  |  Celsius  ")
    print("------------------------------------------------------")
    cel = 40.0
    fah = 120.0
    for i in range(0, 10, 1):
        print("  ", format(cel - i, "5.1f"), "  |  ", format(celsiusToFahrenheit(cel - i), "8.1f"),"  ||  ",
              format(fah - i * 10, "8.1f"), "  |  ", format(fahrenheitToCelsius(fah - i * 10), "4.2f"))
main()
# 6.9
# 英尺和米间的互相转换
# 英尺转米
def footToMeter(foot):
    return 0.305 * foot
# 米转英尺
def meterToFoot(meter):
    return meter / 0.305
def main():
    print("______________________________________________________")
    print("  Feet  |  Meters  ||  Meters  |  Feet  ")
    print("------------------------------------------------------")
    feet = 1.0
    meters = 20.0
    for i in range(0, 10, 1):
        print("  ", format(feet + i, "2.1f"), "  |  ", format(footToMeter(feet + i), "1.3f"),"  ||  ",
              format(meters + i * 5, "2.1f"), "  |  ", format(meterToFoot(meters + i * 5), "3.3f"))
main()
# 6.10
# 计算小于 10000 的素数的个数
# 列出个数并打印所有小于 10000 的素数
def main():
    count = 0
    Number_Per_line = 10
    for i in range(2, 10001):
        if isPrime(i):
            count += 1
            print(format(i,"6d"), end='')
            if count % Number_Per_line == 0:
                print()
    print()
    print("共有", count, "个小于 10000 的素数。")
main()
# 6.11
# 计算佣金
def computeCommission(salesAmount):
    if 0.01 <= salesAmount <= 5000:
        return salesAmount * 0.08
    elif 5000.01 <= salesAmount <= 10000:
        return 5000 * 0.08 + (salesAmount - 5000) * 0.1
    elif 10000.01 <= salesAmount:
        return 5000 * 0.08 + 5000 * 0.1 + (salesAmount - 10000) * 0.12
def main():
    print("_______________________________")
    print("  Sales Amount  |  Commission  ")
    print("-------------------------------")
    amount = 10000
    for i in range(0, 19, 1):
        print("  ", format(amount + i * 5000, "7d"), "     |  ", format(computeCommission(amount + i * 5000), "6.1f"))
main()
# 6.12
# 按规则打印字符串
def printChars(ch1, ch2, numberPerLine):
    if ord(ch1) <= ord(ch2):
        j = 1
    else:
        j = -1
    count = 0
    for i in range(ord(ch1), ord(ch2) + j, j):
        print(chr(i), end='')
        count += 1
        if count % numberPerLine == 0:
            print()
def main():
    printChars("1", "Z", 10)
main()
# 6.13
# 计算指定数列的和
def computeSum(feed):
    if feed <= 0:
        return 0
    sum = 0
    for i in range(1, feed + 1, 1):
        sum += i / (i + 1)
    return sum
def main():
    print("___________________________")
    print("     i    |      m(i)      ")
    print("---------------------------")
    count = 20
    for i in range(1, count + 1, 1):
        print("  ", format(i, "3d"), "   |    ", format(computeSum(i), "2.4f"))
main()
# 6.14
# 估算 Pi 值
def computePi(feed):
    if feed <= 0:
        return 0
    sum = 0
    for i in range(1, feed + 1, 1):
        sum += 4 * (pow(-1, i + 1) / (2 * i - 1))
    return sum
def main():
    print("___________________________")
    print("      i    |      Pi(i)    ")
    print("---------------------------")
    count = 20
    print("  ", format(1, "4d"), "   |    ", format(computePi(1), "2.4f"))
    for i in range(101, 1000, 100):
        print("  ", format(i, "4d"), "   |    ", format(computePi(i), "2.4f"))
main()
'''
# 6.15

# 6.16

# 6.17

# 6.18

# 6.19

# 6.20

# 6.21

# 6.22

# 6.23

# 6.24

# 6.25

# 6.26

# 6.27

# 6.28

# 6.29

# 6.30

# 6.31

# 6.32

# 6.33

# 6.34

# 6.35

# 6.36

# 6.37

# 6.38

# 6.39

# 6.40

# 6.41

# 6.42

# 6.43

# 6.44

# 6.45

# 6.46

# 6.47

# 6.48
