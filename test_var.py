#!/usr/bin/python3
a = 1
print(a)
print("a")
b = 6
print(a + b)
#变量被重新赋值后，变量指向的地址不同
print("变量ａ第一次赋值后地址为")
print(id(a))
a = 100
print("变量ａ重新赋值后地址为")
print(id(a))
#同样的数据，可能有两个不同的变量指向同一个地址
c = 3
print("变量c第一次赋值后地址为")
print(id(c))
c = 100
print("变量c重新赋值后地址为")
print(id(c))
