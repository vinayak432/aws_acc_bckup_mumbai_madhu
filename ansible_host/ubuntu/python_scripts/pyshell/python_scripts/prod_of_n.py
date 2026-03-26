#!/usr/bin/env python3

try:
    n = int(input("enter the value of n: "))
    prod = 1

    while n > 0:
        prod *= n
        n -= 1

    print(f"the result is {prod}")

except ValueError:
    print("Please enter a valid number")
