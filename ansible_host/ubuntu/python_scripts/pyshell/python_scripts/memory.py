#!/usr/bin/env python3

import subprocess

THRESHOLD = 40
EMAIL = "vinayakvk062@gmail.com"

# Get disk usage percentage (same as: df -h .)
output = subprocess.check_output(
    "df -h . | awk 'NR==2 {print $(NF-1)}' | sed 's/%//g'",
    shell=True,
    text=True
).strip()

memusage = int(output)

if memusage >= THRESHO
