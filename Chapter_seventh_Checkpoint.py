#!/usr/bin/python3
# 《Python语言程序设计》程序清单７－检查点练习
# Programed List 7-Checkpoint Programme
# 第七章　检查点练习程序　７．１～７．１８

# 7.1

# 7.2

# 7.3

# 7.4

# 7.5

# 7.6

# 7.7

# 7.8

# 7.9
# class A:
#     def __init__(self, i):  # def __init__(self, i = 0):
#         self.i = i
# def main():
#     a = A()
#     print(a.i)
# main() # Call the main function
# 7.10
# class A:
#     # Construct an object of the class
#     def A(self):
#         radius = 3
# class A:
#     # Construct an object of the class
#     def __init__(self):
#         radius = 3
#     def setRadius(radius):
#         self.radius = radius
# 7.11
# class Count:
#     def __init__(self, count = 0):
#         self.count = count
#
# def main():
#     c = Count()
#     times = 0
#     for i in range(100):
#         increment(c, times)
#     print("count is", c.count)
#     print("times is", times)
#
# def increment(c, times):
#     c.count += 1
#     times += 1
#
# main()    # Call the main function
# 7.12
# class Count:
#     def __init__(self, count = 0):
#         self.count = count
#
# def main():
#     c = Count()
#     n = 1
#     m(c, n)
#
#     print("count is", c.count)
#     print("n is", n)
#
# def m(c, n):
#     c = Count(5)
#     n = 3
#
# main()    # Call the main function
# 7.13
# class A:
#     def __init__(self, i):
#         self.__i = i
# def main():
#     a = A(5)
#     print(a.__i)
# main() # Call the main function
# 修改后：
# class A:
#     def __init__(self, i):
#         self.__i = i
#     def getI(self):
#         return self.__i
# def main():
#     a = A(5)
#     print(a.getI())
# main()    # Call the main function
# 7.14
# def main():
#     a = A()
#     a.print()
# class A:
#     def __init__(self, newS = "Welcome"):
#         self.__s = newS
#     def print(self):
#         print(self.__s)
# main()    # Call the main function
# 7.15
# class A:
#     def __init__(self, on):
#         self.__on = not on
# def main():
#     a = A(False)
#     print(a.on)
# main()    # Call the main function
# 修改后：
# class A:
#     def __init__(self, on):
#         self.__on = not on
#     def getOn(self):
#         return self.__on
# def main():
#     a = A(False)
#     print(a.getOn())
# main()    # Call the main function
# 7.16

# 7.17

# 7.18