#!/usr/bin/python3
# 《Python语言程序设计》程序清单１－测试Turtle模块
# Programed List 1-Test Turtle
# Test Turtle in IDLE
# 在IDLE或命令行中利用Turtle模块绘图的示例
import turtle  # Import turtle module

turtle.showturtle()
turtle.write("Welcome to Python")
turtle.forward(100)
turtle.right(90)
turtle.color("red")
turtle.forward(90)
turtle.right(90)
turtle.color("blue")
turtle.forward(100)
turtle.right(45)
turtle.forward(80)
turtle.goto(0, 50)
turtle.goto(0, 0)
turtle.goto(0, 50)
turtle.penup()
turtle.goto(50, -50)
turtle.pendown()
turtle.color("blue")
turtle.circle(50)
turtle.done()