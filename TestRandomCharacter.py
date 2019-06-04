#!/usr/bin/python3
# 《Python语言程序设计》程序清单6－12
# Programed List 6-12
# 测试随机生成特定类型字符的函数。

import RandomCharacter

NUMBER_OF_CHARS = 175
CHARS_PER_LINE = 25

# Print random character between 'a' and 'z', 25 chars per line
for i in range(NUMBER_OF_CHARS):
    print(RandomCharacter.getRandomLowercaseCharacter(), end=" ")
    if (i + 1) % CHARS_PER_LINE == 0:
        print()