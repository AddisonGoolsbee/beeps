import subprocess
import time

interval = 1

while True:
    subprocess.Popen(["afplay", "/System/Library/Sounds/Ping.aiff"])
    time.sleep(interval)
    interval *= 0.99
