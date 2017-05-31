#!/usr/bin/python3
# 《Python语言程序设计》程序清单３－编程题
# Programed List 3-Test Programme
# 第三章　编程题　３．１～３．１９

import math
'''
# 3.1 Compute the area of a pentagon
# Prompt the user to enter length of radius of the pentagon's circumcircle
radius = eval(input("请输入正五边形外接圆的半径："))

# Compute length of side of the pentagon
side = 2 * radius * math.sin(math.pi / 5)

# Compute area of the pentagon
area = 5 * side ** 2 / (4 * math.tan(math.pi / 5))

# Display result
print("The area of the pentagon is ", area)
'''
# 3.2 Compute Great-circledistance of the between two points on the Earth.
# The length of the Earth's radius is 6371.01 km.
# Prompt the user to enter point1(latitude and longitude)
lati1, longi1 = eval(input("起始点的纬度（负数表示南纬，小数点后一位）和经度（负数表示东经，小数点后两位）："))
# Prompt the user to enter point2(latitude and longitude)
lati2, longi2 = eval(input("结束点的纬度（负数表示南纬，小数点后一位）和经度（负数表示东经，小数点后两位）："))

radius = 6371.01
d = radius * math.acos(math.sin(math.radians(longi1)) * math.sin(math.radians(longi2)) + math.cos(math.radians(longi1)) * math.cos(math.radians(longi2)) * math.cos(math.radians(lati1 - lati2)))
print(d)
# 3.3
# 3.4
# 3.5
# 3.6
# 3.7
# 3.8
# 3.9
# 3.10
# 3.11
# 3.12
# 3.13
# 3.14
# 3.15
# 3.16
# 3.17
# 3.18
# 3.19