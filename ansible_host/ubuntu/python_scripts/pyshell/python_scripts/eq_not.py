#!/usr/bin/env python3

try:
    num = int(input("enter the number: "))

    if num == 20:
        print("equal to 20")
    else:
        print("not equal to 20")

except ValueError:
    print("Please enter a valid number")
