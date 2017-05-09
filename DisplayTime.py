#!/usr/bin/python3
# 《Python语言程序设计》程序清单２－５
# Programed List 2-5
# Compute minutes and second of second from Console

# Prompt the user for input
second = eval(input("Enter an integer for second: "))

# Get minutes and remaining second
minutes = second // 60 # Find minutes in second
remainingSecond = second % 60 # Second remaining

print(second, " second is ", minutes, " minutes and ",remainingSecond, "seconds")