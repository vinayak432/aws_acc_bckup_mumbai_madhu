#!/usr/bin/env python3

import psutil
import subprocess
import time

THRESHOLD = 80  # CPU usage %
EMAIL = "vinayakvk062@gmail.com"

# Stress CPU for 1 minute (same as bash)
subprocess.Popen(["stress", "--cpu", "4", "--timeout", "60s"])

print("Monitoring CPU usage...")

while True:
    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu}%")

    if cpu > THRESHOLD:
        message = f"High CPU usage detected: {cpu}%"
        subprocess.run(
            ["mail", "-s", "CPU Alert!", EMAIL],
            input=message,
            text=True
        )
        print(f"Email sent to {EMAIL}")
        break

    time.sleep(5)
