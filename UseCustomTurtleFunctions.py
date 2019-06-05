#!/usr/bin/python3
# 《Python语言程序设计》程序清单6－15
# Programed List 6-15
# 使用图形函数。

import turtle
from UsefulTurtleFunctions import *

# Draw a line from (-50, -50) to (50, 50)
drawLine(-50, -50, 50, 50)

# Write test at (-50, -60)
writeText("Test Useful Turtle Functions", -100, -100)

# Draw a point at (0, 0)
drawPoint(0, 0)

# Draw a circle ar (0, 0) with radius 80
drawCircle(0, 0, 80)

# Draw a rectangle at (0, 0) with width 60 and height 40
drawRectangle(0, 0, 160, 160)

turtle.hideturtle()
turtle.done()