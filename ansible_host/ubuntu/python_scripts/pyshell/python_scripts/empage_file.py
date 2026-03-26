#!/usr/bin/env python3

filename = input("enter the filename: ")

try:
    with open(filename, "r") as file:
        i = 1
        for line in file:
            line = line.strip()

            # Skip header (same as i > 1)
            if i > 1 and line:
                fields = line.split()
                age = int(fields[-1])

                if age >= 60:
                    print(fields[0])

            i += 1

except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except ValueError:
    print("Invali
