#!/usr/bin/env python3

try:
    num = int(input("enter the number: "))
    total = 0

    for i in range(1, num + 1):
        total += i

    print(f"sum of {num} is: {total}")

except ValueError:
    print("Please enter a valid number")
