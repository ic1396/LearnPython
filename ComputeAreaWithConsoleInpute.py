#!/usr/bin/python3
# 《Python语言程序设计》程序清单２－２
# Programed List 2-2
# Compute Area of Circle, radius from Console

# Prompt the user to enter a radius
radius = eval(input("Enter a value for radius: "))

# Compute area
area = radius * radius * 3.14159

# Display result
print("The area for the circle of radius", radius, "is", area)