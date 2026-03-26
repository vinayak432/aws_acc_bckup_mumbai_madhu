#!/usr/bin/env python3

try:
    num = int(input("enter the number: "))

    if num <= 1:
        print(f"{num} is not a prime number")
        exit(1)

    if num % 2 == 0 and num != 2:
        print(f"{num} is not a prime number")
    elif num % 3 == 0 and num != 3:
        print(f"{num} is not a prime number")
    elif num % 5 == 0 and num != 5:
        print(f"{num} is not a prime number")
    elif num % 7 == 0 and num != 7:
        print(f"{num} is not a prime number")
    else:
        print(f"{num} is a prime number")

except ValueError:
    print("Please enter a valid number")
