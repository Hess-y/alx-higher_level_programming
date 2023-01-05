#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last digit of number = abs(number) % 10
if number < 5:
    print(f"last digit of {number} is {last digit of number} and is greater than 5")
elif number == 0:
    print(f"last digit of {number} is {last digit of number} and is 0")
else:
    print(f"last digit of {number} is {last digit of number} and is less than 6 and not 0")
