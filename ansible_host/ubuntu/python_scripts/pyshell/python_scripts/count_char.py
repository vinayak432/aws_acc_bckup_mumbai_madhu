#!/usr/bin/env python3

filename = input("enter the filename: ")

try:
    with open(filename, "r") as file:
        i = 1
        for line in file:
            count = len(line)
            print(f"the no of characters in line {i} is {count}")
            i += 1

except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
