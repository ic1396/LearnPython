#!/usr/bin/python3
# 《Python语言程序设计》程序清单２－１０
# Programed List 2-10
# Compute distance between the two points on Graphics

import turtle
# Prompt the user for inputting two points
x1, y1 = eval(input("Enter x1 and y1 for Point 1: "))
x2, y2 = eval(input("Enter x2 and y2 for Point 2: "))

# Compute the distance
distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5

# Display two points and the connecting line
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("Point 1")
turtle.goto(x2, y2)
turtle.write("Point 2")
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.pendown()
turtle.write(distance)

turtle.done()