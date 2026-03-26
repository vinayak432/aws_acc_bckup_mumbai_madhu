#!/usr/bin/env python3

import sys

# Check number of arguments
if len(sys.argv) != 3:
    print("Enter the two arguments")
    sys.exit(1)

# Convert arguments to integers
try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
except ValueError:
    print("Please enter valid integers")
    sys.exit(1)

# Compare values
if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")

