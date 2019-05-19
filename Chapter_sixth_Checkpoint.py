#!/usr/bin/python3
# 《Python语言程序设计》程序清单６－检查点练习
# Programed List 6-Checkpoint Programme
# 第六章　检查点练习程序　６．１～６．２７

# 6.1

# 6.2

# 6.3

# 6.4
'''
# 6.5
def xFunction(x, y):
    print(x + y)
    return

xFunction(2, 4)
'''
# 6.6

# 6.7
'''
# 6.8
def function1(n, m):
function2(3, 4

def function2(n):
    if n >0 :
        return 1
    elif n == 0:
        return 0
    elif n < 0 :
        return -1
function1(2, 3)

# 6.9
def main():
    print(min(5, 6))
def min(n1, n2):
    smallest = n1
    if n2 < smallest:
        smallest = n2

main() # Call the main function

# 6.10
def main():
    print(min(min(5, 6), (51, 6)))
def min(n1, n2):
    smallest = n1
    if n2 < smallest:
        smallest = n2

main() # Call the main function
'''
# 6.11

# 6.12

# 6.13

# 6.14

# 6.15
# a)
'''
def main():
    max = 0
    getmax(1, 2, max)
    print(max)
def getmax(value1, value2, max):
    if value1 > value2:
        max = value1
    else:
        max = value2

main()
'''
# b)
'''
def main():
    i = 1
    while i <= 6:
        print(function(i, 2))
        i += 1

def function(i, num):
    line = ""
    for j in range(1, i):
        line += str(num) + " "
        num *= 2
    return line
main()
'''
# c)
'''
def main():
    # Initialize times
    times = 3
    print("Before the call, variable", "times is", times)

    # Invoke nPrintln and display times
    nPrint("Welcome to CS!", times)
    print("After the call, variable", "times is", times)

# Print the message n times
def nPrint(message, n):
    while n > 0:
        print("n = ", n)
        print(message)
        n -= 1
main()
'''
# d)
'''
def main():
    i = 0
    while i <= 4:
        function1(i)
        i += 1
        print("i is ", i)

def function1(i):
    line = " "
    while i >= 1:
        if i % 3 != 0:
            line += str(i) + " "
            i -= 1
    print(line)
main()
'''
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

