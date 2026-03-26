#!/usr/bin/env python3

filename = input("enter the filename: ")

try:
    with open(filename, "r") as file:
        i = 1
        for line in file:
            word_count = len(line.split())
            print(f"No of letters in line {i} is {word_count}")
            i += 1

except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
