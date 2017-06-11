#!/usr/bin/python3
# 《Python语言程序设计》程序清单４－９
# Programed List 4-9
# 判断闰年

year = eval(input("Enter a year: "))

# Check if the year is a leap year
isLeapYear = (year % 4 == 0 and year % 100 != 0) or \
   (year % 400 == 0)

# Display the result
print(year, "is a leap year?", isLeapYear)