#!/usr/bin/python3
# 《Python语言程序设计》程序清单6－3
# Programed List 6-3
# 返回成绩等级，有返回值。

# Return the grade for the score
def getGrade(score):
    if score >= 90.0:
        return 'A'
    elif score >= 80.0:
        return 'B'
    elif score >= 70.0:
        return 'C'
    elif score >= 60.0:
        return 'D'
    else:
        return 'F'

def main():
    score = eval(input("请输入成绩："))
    print("这个成绩是", getGrade(score))

main() # Call the main function