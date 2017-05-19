#!/usr/bin/python3
# 《Python语言程序设计》程序清单３－１
# Programed List 3-1
# Some examples of Math Functions

import math     # import math module to use the math functions

# Test algebraic functions
print("exp(1.0) = ", math.exp(1))   # 返回ｅ的ｘ次幂的值，本例中为ｅ的１次幂。
print("log(2.78) = ", math.log(math.e))   # 返回自然对数的值
print("log10(10) = ", math.log(10, 10))   # log(x, base)返回以base为底的x的对数值，本例中返回以１０为底的１０的对数的值，
print("sqrt(4.0) = ", math.sqrt(4.0))   # 返回给定数值的平方根

# Test trigonometric functions
print("sin(PI / 2) = ", math.sin(math.pi / 2))   # 计算给定弧度值的正弦值
print("cos(PI / 2) = ", math.cos(math.pi / 2))   # 计算给定弧度值的余弦值
print("tan(PI / 2) = ", math.tan(math.pi / 2))   # 计算给定弧度值的正切值
print("degrees(1.57) = ", math.degrees(1.57))   # 将弧度转换为角度
print("radians(90) = ", math.radians(90))    # 将角度转换为弧度