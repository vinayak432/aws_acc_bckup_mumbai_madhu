#!/usr/bin/env python3

import os

name = input("enter the path: ")

if os.path.isfile(name):
    print(f"{name} is a file")

elif os.path.isdir(name):
    print(f"{name} is a directory")

elif os.path.islink(name):
    print(f"{name} is a link file")

elif name.endswith((".tar", ".tar.gz", ".tgz", ".zip")):
    print("it is a zip file")

else:
    print("it does not exist")
