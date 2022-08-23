#!/usr/bin/python3
import random
number = random.randint(-100, 100)
if number > 0:
    print(f"{number:d} is positive")
elif number == 0:
    print(f"{number:d} is zero")
elif number < 0:
    print(f"{number:d} is negative")
