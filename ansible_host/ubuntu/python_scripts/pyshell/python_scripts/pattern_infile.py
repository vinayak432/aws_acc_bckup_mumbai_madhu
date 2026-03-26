#!/usr/bin/env python3

import subprocess

pat = input("enter the pattern to search in a file: ")

result = subprocess.run(
    f'grep -l -r "{pat}" * > outpat',
    shell=True
)

if result.returncode == 0:
    print(f"{pat} Pattern found in below files")
    with open("outpat") as f:
        print(f.read(), end="")
else:
    print(f"{pat} is not found in any of the files")
