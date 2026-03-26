#!/usr/bin/env python3

try:
    num = int(input("enter the number: "))

    if num > 20:
        print("greater than 20")
    else:
        print("not greater than 20")

except ValueError:
    print("Please enter a valid number")
