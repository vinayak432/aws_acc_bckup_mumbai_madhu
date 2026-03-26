#!/usr/bin/env python3

try:
    num = int(input("enter the number: "))

    if num % 2 == 0:
        print("It is an even no")
    else:
        print("It is an odd no")

except ValueError:
    print("Please enter a valid number")
