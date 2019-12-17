#!/usr/bin/python3
# 《Python语言程序设计》程序清单７－９
# Programed List 7-10
# 示例： 使用人体质量指数类

from BMI import BMI

def main():
    bmi1 = BMI("John Doe", 18, 145, 70)
    print("THe BMI for", bmi1.getName(), "is", bmi1.getBMI(), bmi1.getStatus())
    bmi2 = BMI("Peter King", 50, 215, 70)
    print("THe BMI for", bmi2.getName(), "is", bmi2.getBMI(), bmi2.getStatus())

main()    # Call the main function