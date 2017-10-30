#!/usr/bin/python3
# 《Python语言程序设计》程序清单５－７
# Programed List 5-7
#

# Initialize sum
sum = 0

# Add 0.01, 0.02, ..., 0.99, 1 to sum
i = 0.01
while i <= 1.0:
    sum += i
    i = i + 0.01

# Display result
print("The sum is", sum)