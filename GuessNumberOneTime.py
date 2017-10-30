#!/usr/bin/python3
# 《Python语言程序设计》程序清单５－２
# Programed List 5-2
#

import random

# Generate a random number to be guessed
number = random.randint(1, 100)

print("Guess a magic number between 0 and 100")

# Prompt the user to guess the number
guess = eval(input("Enter your guess: "))

if guess == number:
    print("Yes, the number is " + str(number))
elif guess > number:
    print("Your guess is too high")
else:
    print("Your guess is too low")