#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lDigit = 0
remainder = number % 10

if remainder:
    if number > 0:
        lDigit = remainder
    else:
        lDigit = remainder - 10
else:
    lDigit = 0

if lDigit > 5:
    print(f"Last digit of {number} is {lDigit} and is greater than 5")
elif lDigit == 0:
    print(f"Last digit of {number} is {lDigit} and is 0")
else:
    print(f"Last digit of {number} is {lDigit} and is less than 6 and not 0")
