#!/usr/bin/env python3

import sys

# Check number of arguments
if len(sys.argv) != 4:
    print("Enter the three arguments")
    sys.exit(1)

# Convert arguments to integers
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
except ValueError:
    print("Please enter valid integers")
    sys.exit(1)

# Compare values
if a > b and a > c:
    print(f"{a} is greater than {b} and {c}")
elif b > a and b > c:
    print(f"{b} is greater than {a} and {c}")
else:
    print(f"{c} is greater than {a} and {b}")
