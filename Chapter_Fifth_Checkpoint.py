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

# 5.6 假设输入值为“2，3，4，5，0”（每行一个数）。下面代码的输出结果是什么？
number = 0
sum = 0

for count in range(5):
    number = eval(input("Enter an integer: "))
    sum += number
print("sum is", sum)
print("count is", count)

# 输出：
# sum is 14
# count is 4

# 5.7

# 5.8 将下面的 for 循环语句转换成 while 循环。
sum = 0
for i in range(1001):
    sum = sum + i
print(sum)
i = 1
sum = 0
while i < 1001:
    sum = sum + i
    i += 1
print(sum)

# 5.9 你能将任意 while 循环转换成 for 循环吗？将下面这个 while 循环转换成 for 循环。
i = 1
sum = 0
while sum < 10000:
    sum = sum + i
    i += 1
print(sum)
sum = 0
for i in range(1, 10001):
    sum = sum + i
    if sum > 10000:
        break
print(sum)

# 5.10 统计下面循环中的迭代次数：
# a) 在 n > 0 时，执行 n 次。
count = 0
while  count < n:
    count += 1
# b) 在 n > 0 时，执行 n 次。
for count in range(n):
    print(count)
# c) 在 n > 5 时，执行 n - 5 次。
count = 5
while  count < n:
    count += 1
# d)
count = 5
while  count < n:
    count = count + 3

# 5.11 显示下面这个程序的输出（提示：绘制一个表格，列出所有的变量来跟踪这个程序）。
# a)
for i in range(1, 5):
    j = 0
while j < i:
    print(j, end = "")
    j += 1
# b)
i = 0
while i < 5:
    for j in range(i, 1, -1):
        print(j, end = "")
    print("****")
    i += 1
# c)
i = 5
while i >= 1:
    num = 1
    for j in range(i, i + 1):
        print(num, end = "***")
        num *= 2
    print()
    i += 1
# d)
i = 1
while i <= 5:
    num = 1
    for j in range(1, i + 1):
        print(num, end = "G")
        num += 2
    print()
    i += 1

# 5.12 如果你知道一个数n1的公约数不可能大于 n1 / 2 ，你就可以试图使用下面的循环来改善你的程序：
k = 2
while k <= n1 / 2 and k <= n2 / 2:
    if n1 % k == 0 and n2 % k == 0:
        gcd = k
    k += 1
# 这个程序是错误的。你能找出原因吗？

# 5.13 关键字break的作用是什么？关键字continue的作用是什么？下面这个程序会终止吗？如果会，请给出程序运行的结果。
# a)
balance = 1000
while True:
    if balance < 9:
        break
    balance = balance - 9
print("Balance is", balance)
# b)
balance = 1000
while True:
    if balance < 9:
        continue
    balance = balance - 9
print("Balance is", balance)

# 5.14 左边的for循环被转换成右边的while循环。哪里出了错误？请改正。
for i in range(4):
    if i % 3 == 0:
        continue
    sum += 1
i = 0
while i < 4:
    if i % 3 == 0:
        continue
    sum += i
    i += 1

# 5.15 使用break和continue语句改写程序清单5-11和5-12的程序TestBreak和TestContinue。

# 5.16 在下面a的循环里如果break语句执行完后，哪些语句就被终止？显示输出结果。在下面b的循环里如果continue语句执行完后，哪些语句就被终止？显示输出结果。
# a)
for i in range(1, 4):
    for j in range(1, 4):
        if i * j > 2:
            break
        print(i * j)
    print(i)
# b)
for i in range(1, 4):
    for j in range(1, 4):
        if i * j > 2:
            continue
        print(i * j)
    print(i)
'''
