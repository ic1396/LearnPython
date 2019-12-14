#!/usr/bin/python3
# 《Python语言程序设计》程序清单７－７
# Programed List 7-7
# 示例：调用利息类

from Loan import Loan

def main():
    # Enter yearly interest rate
    annualInterestRate = eval(input("请输入年利率，例如 7.25 :"))

    # Enter number of years
    numberOfYears = eval(input("请输入贷款年限，整数："))

    # Enter loan amount
    loanAmount = eval(input("请输入贷款总数，例如 120000.95 ："))

    # Enter a borrower
    borrower = input("请输入贷款人姓名：")

    # Create a Loan object
    loan = Loan(annualInterestRate, numberOfYears, loanAmount, borrower)

    # Display loan date, monthly payment, and total payment
    print("The loan is for", loan.getBorrower())
    print("The monthly payment is", format(loan.getMonthlyPayment(), ".2f"))
    print("The total payment is", format(loan.getTotalPayment(), ".2f"))

main()    # Call the main function