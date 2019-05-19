#!/usr/bin/python3
# 《Python语言程序设计》程序清单6－5
# Programed List 6-5
# 返回两个数的最大公约数。

# Return the gcd of two integer
def gcd(n1, n2):
    gcd = 1 # Initial gcd is 1
    k = 2 # Possible gcd

    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k # Update gcd
        k += 1

    return gcd