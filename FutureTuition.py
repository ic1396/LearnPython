#!/usr/bin/python3
# 《Python语言程序设计》程序清单５－９
# Programed List 5-8
#

year = 0 # Year 0
tuition = 10000   # Year 1

while tuition < 20000:
    year += 1
    tuition = tuition * 1.07

print("Tuition will be doubled in", year, "years")
print("Tuition will be $" + format(tuition, ".2f"),
      "in", year, "years")