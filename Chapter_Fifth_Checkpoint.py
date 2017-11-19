#!/usr/bin/python3
# 《Python语言程序设计》程序清单５－检查点练习
# Programed List 5-Checkpoint Programme
# 第五章　检查点练习程序　５．１～５．１６
'''
# 5.1
count = 0
while count < 100:
    # PointA    总为 True
    print("Programming is fun")
    count += 1
    # PointB  有时 True，有时 False
# 5.2

# 5.3
# a) 无限循环，i 的值一直为 1，没有输出
i = 1
while i < 10:
    if i % 2 == 0:
        print( i )
# b) 无限循环，i 的值一直为 1，没有输出
i = 1
while i < 10:
    if i % 2 == 0:
        print( i )
        i += 1
# c) 循环被执行 9 次，输出2 4 6 8，每行一个。
i = 1
while i < 10:
    if i % 2 == 0:
        print( i )
        i += 1

# 5.4
# a) 循环中没有改变 count 的值，一直等于 0，小于 100，死循环。
count = 0
while count < 100:
    print(count)
# b) 循环中将 count 的值越改越小，一直小于 100，死循环。
count = 0
while count < 100:
    print(count)
    count -= 1
# c) 循环体为空，没有改变 count 的值
count = 0
while count < 100:
count += 1

# 5.5
number = eval(input("Enter an integer: "))
max = number

while number != 0:
    number = eval(input("Enter an integer: "))
    if number > max:
        max = number
print("max is", max)
print("number is", number)

# 输出：
# max is 5
# number is 5
'''
# 5.6

# 5.7

# 5.8

# 5.9

# 5.10

# 5.11

# 5.12

# 5.13

# 5.14

# 5.15

# 5.16
