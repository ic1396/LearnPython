#!/usr/bin/python3
# 《Python语言程序设计》程序清单6－11
# Programed List 6-11
# 能随机生成特定类型字符的函数。

from random import randint

# Generate a random character between ch1 and ch2
def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1),ord(ch2)))

# Generate  a random lowercase character
def getRandomLowercaseCharacter():
    return getRandomCharacter('a', 'z')

# Generate  a random uppercase character
def getRandomUppercaseCharacter():
    return getRandomCharacter('A', 'Z')

# Generate  a random digit character
def getRandomDigitCharacter():
    return getRandomCharacter('0', '9')

# Generate  a random character
def getRandomASCIICharacter():
    return chr(randint(0, 127))