#!/usr/bin/env python3

import os
import glob

# Get all .txt files
txt_files = glob.glob("*.txt")

for file in txt_files:
    name, _ = os.path.splitext(file)
    new_name = name + ".html"
    os.rename(file, new_name)

# List all .html files
html_files = glob.glob("*.html")
for file in html_files:
    print(file)
