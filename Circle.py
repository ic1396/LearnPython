#!/usr/bin/python3
# 《Python语言程序设计》程序清单７－１
# Programed List 7-1
# 示例：定义一个圆类，有一个数据域为半径，三个方法，分别为计算圆的周长、面积、设置元的半径。
import math

class Circle:
    # Construct a circle object
    def __init__(self, radius = 1):
        self.radius = radius

    def getPerimeter(self):
        return 2 * self.radius * math.pi

    def getArea(self):
        return  self.radius * self.radius * math.pi
    def setRadius(self, radius):
        self.radius = radius