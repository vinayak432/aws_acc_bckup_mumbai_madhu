#!/usr/bin/env python3

import subprocess

chkproc = ["sshd", "jenkins", "bash"]
EMAIL = "vinayakvk062@gmail.com"

for proc in chkproc:
    result = subprocess.run(
        ["ps", "-C", proc],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if result.returncode != 0:
        subprocess.run(
            ["mail", "-s", "Processes stopped working", EMAIL],
            input=f"process {proc} is not running",
            text=True
        )
        print(f"process {proc} is not running")
