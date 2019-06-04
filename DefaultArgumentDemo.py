#!/usr/bin/python3
# 《Python语言程序设计》程序清单6－9
# Programed List 6-9
# 定义带默认参数值的函数。

def printArea(width = 1, height = 2):
    area = width * height
    print("width: ", width, "\theight: ", height, "\tarea: ", area)

printArea()
printArea(4, 2.5)
printArea(height=5, width=3)
printArea(width=1.2)
printArea(height=6.2)