#!/usr/bin/python3
# 《Python语言程序设计》程序清单２－４
# Programed List 2-3
# Compute Average of three numbers from Console

# Prompt the user enter three numbers
number1, number2, number3 = eval(input("Enter three numbers separated by commas: "))

# Compute average
average = (number1 + number2 + number3) / 3

# Display result
print("The average of [", number1, number2, number3, "] is ", average)