#!/usr/bin/env python3

import os
import subprocess
from datetime import datetime

day = datetime.now().strftime("%A")

if day == "Tuesday":
    os.makedirs("/home/ubuntu/auto", exist_ok=True)

elif day == "Wednesday":
    # find /home/ubuntu -type f -mmin -30 > filelist
    with open("filelist", "w") as f:
        subprocess.run(
            ["find", "/home/ubuntu", "-type", "f", "-mmin", "-30"],
            stdout=f
        )

elif day == "Friday":
    # cat filelist | xargs cp -t /home/ubuntu/auto/
    if os.path.exists("filelist"):
        subprocess.run(
            ["xargs", "cp", "-t", "/home/ubuntu/auto/"],
            stdin=open("filelist")
        )
    else:
        print("filelist not found")

elif day == "Thursday":
    subprocess.run(["ls", "-ltr", "/home/ubuntu"])

elif day == "Monday":
    subprocess.run(["sudo", "adduser", "vinayak1"])

elif day in ("Saturday", "Sunday"):
    print("It's holiday")
