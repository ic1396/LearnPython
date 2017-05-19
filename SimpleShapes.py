#!/usr/bin/python3
# 《Python语言程序设计》程序清单３－５
# Programed List 3-5
# Draw simple shapes on graphics

import turtle

turtle.pensize(3)    # Set pen thickness to 3 pixels
turtle.penup()       # Pull the pen up
turtle.goto(-200, -50)
turtle.pendown()      # Pull the pen down
turtle.circle(40, steps = 3)  # Draw a triangle

turtle.penup()       # Pull the pen up
turtle.goto(-100, -50)
turtle.pendown()      # Pull the pen down
turtle.circle(40, steps = 4)  # Draw a square

turtle.penup()       # Pull the pen up
turtle.goto(0, -50)
turtle.pendown()      # Pull the pen down
turtle.circle(40, steps = 5)  # Draw a pentagon

turtle.penup()       # Pull the pen up
turtle.goto(100, -50)
turtle.pendown()      # Pull the pen down
turtle.circle(40, steps = 6)  # Draw a hexagon

turtle.penup()       # Pull the pen up
turtle.goto(200, -50)
turtle.pendown()      # Pull the pen down
turtle.circle(40)  # Draw a circle

turtle.done()