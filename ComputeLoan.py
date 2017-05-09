#!/usr/bin/python3
# 《Python语言程序设计》程序清单２－８
# Programed List 2-8
# Compute total_payment and month_payment of rate and years and loan amount from console

# Enter annual interest rate as a percentage, e.g., 7.25
annualInterestRate = eval(input("Enter annual interest rate, e.g., 7.25 : "))
monthlyInterestRate = annualInterestRate / 1200

# Enter number of years
numberofYears = eval(input("Enter number of years as an integer, e.g., 5 :"))

#Enter loan amount
loanAmount = eval(input("Enter loan amount, e.g., 120000.95 :"))

# Calculate payment
monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberofYears * 12))
totalPayment = monthlyPayment * numberofYears * 12

# Display results
print("The monthly payment is ",int(monthlyPayment * 100) / 100)
print("The total payment is ",int(totalPayment * 100) / 100)