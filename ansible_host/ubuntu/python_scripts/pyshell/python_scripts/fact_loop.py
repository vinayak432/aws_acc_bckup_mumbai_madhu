#!/usr/bin/env python3

numbers = [3, 5, 8]

for n in numbers:
    fact = 1
    temp = n

    while n > 0:
        fact *= n
        n -= 1

    print(f"The factorial of {temp} is {fact}")
