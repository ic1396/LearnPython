#!/usr/bin/python3
# 《Python语言程序设计》程序清单6－2
# Programed List 6-2
# 打印成绩等级，无返回值。

# Print grade for the score
def printGrade(score):
    if score >= 90.0:
        print('A')
    elif score >= 80.0:
        print('B')
    elif score >= 70.0:
        print('C')
    elif score >= 60.0:
        print('D')
    else:
        print('F')

def main():
    score = eval(input("请输入成绩："))
    print("这个成绩是", end = " ")
    printGrade(score)

main() # Call the main function