#!/usr/bin/python3
# 《Python语言程序设计》程序清单７－６
# Programed List 7-6
# 示例：使用私有数据域

import math

class Circle:
    # Construct a Circle object
    def __init__(self, radius = 1):
        self.__radius = radius
    def getRadius(self):
        return self.__radius
    def getPerimeter(self):
        return 2 * self.__radius * math.pi
    def getArea(self):
        return self.__radius * self.__radius * math.pi