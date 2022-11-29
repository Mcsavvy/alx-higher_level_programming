#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mul = 1
if number < 0:
    mul = -1
last_digit = ((number * mul) % 10) * mul
print(f"Last digit of {number} is {last_digit}", end=" ")
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
