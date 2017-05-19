#!/usr/bin/python3
# 《Python语言程序设计》程序清单３－６
# Programed List 3-6
# Draw simple shapes and fill color in shapes on graphics

import turtle

turtle.pensize(3)    # Set pen thickness to 3 pixels
turtle.penup()       # Pull the pen up
turtle.goto(-200, -50)
turtle.pendown()      # Pull the pen down
turtle.begin_fill()   # Begin to fill color in a shape
turtle.color("red")
turtle.circle(40, steps = 3)  # Draw a triangle
turtle.end_fill()     # Fill the shape

turtle.penup()       # Pull the pen up
turtle.goto(-100, -50)
turtle.pendown()      # Pull the pen down
turtle.begin_fill()   # Begin to fill color in a shape
turtle.color("blue")
turtle.circle(40, steps = 4)  # Draw a square
turtle.end_fill()     # Fill the shape

turtle.penup()       # Pull the pen up
turtle.goto(0, -50)
turtle.pendown()      # Pull the pen down
turtle.begin_fill()   # Begin to fill color in a shape
turtle.color("green")
turtle.circle(40, steps = 5)  # Draw a pentagon
turtle.end_fill()     # Fill the shape

turtle.penup()       # Pull the pen up
turtle.goto(100, -50)
turtle.pendown()      # Pull the pen down
turtle.begin_fill()   # Begin to fill color in a shape
turtle.color("yellow")
turtle.circle(40, steps = 6)  # Draw a hexagon
turtle.end_fill()     # Fill the shape

turtle.penup()       # Pull the pen up
turtle.goto(200, -50)
turtle.pendown()      # Pull the pen down
turtle.begin_fill()   # Begin to fill color in a shape
turtle.color("purple")
turtle.circle(40)  # Draw a circle
turtle.end_fill()     # Fill the shape

turtle.color("green")
turtle.penup()       # Pull the pen up
turtle.goto(-100, 50)
turtle.pendown()      # Pull the pen down
turtle.write("Cool Colorful Shapes", font = ("Times", 18, "bold"))
turtle.hideturtle()

turtle.done()