#!/usr/bin/python3
# 《Python语言程序设计》程序清单３－２
# Programed List 3-2
# Compute three angles of a triangle by three points for a triangle

import math

x1, y1, x2, y2, x3, y3 = eval(input("请按照顺序输入三角形三个顶点的坐标（x1,y1,x2,y2,x3,y3），以逗号分隔："))  # 修改了原书中例子的提示
# input("Enter six coordinates of three points separated by commas like x1,y1,x2,y2,x3,y3")  原书中的提示

a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

print("The three angles are ", round(A * 100) / 100.0, round(B * 100) / 100.0, round(C * 100) / 100.0)