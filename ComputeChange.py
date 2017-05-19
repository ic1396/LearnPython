#!/usr/bin/python3
# 《Python语言程序设计》程序清单３－４
# Programed List 3-4
# Asking for change and Coins at least

# Receive the amount
amount = eval(input("Enter an amount, for example, 11.56: "))

# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

# Display the results
print("Your amount", amount, "consists of\n", "\t", numberOfOneDollars, "dollars\n", "\t", \
      numberOfQuarters, "quarters\n", "\t", numberOfDimes, "dimes\n", "\t", numberOfNickels, "nickels\n" \
      "\t", numberOfPennies, "pennies")
'''
这个程序里有一个计算精度问题，将浮点数转换成整型时可能会损失数字的精度，例如下面的例子：
Enter an amount, for example, 11.56: 10.03
Your amount 10.03 consists of
 	 10 dollars
 	 0 quarters
 	 0 dimes
 	 0 nickels
	 2 pennies

Process finished with exit code 0

解决问题的一个方法是输入以美分表示的整型数值。
'''
