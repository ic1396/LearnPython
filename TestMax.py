#!/usr/bin/python3
# 《Python语言程序设计》程序清单6－1
# Programed List 6-1
# 返回两个数中较大的数

# Return the max of two numbers
def max(num1, num2):
    if num1 > num2:
        result = num1
    else:
        result = num2

    return result
def main():
    i = 5
    j = 2
    k = max(i, j)  # Call the max function
    print(i, "与", j, "中最大的是", k)

main() # Call the main function