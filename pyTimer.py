# pyTimer
# github link here

# this project creates a countdown timer in python

import time
import datetime
from tqdm import tqdm

def countDown(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds

    with tqdm(total = total_seconds, unit = "s", dynamic_ncols=True) as pbar:
        while total_seconds > 0 :
            timer = datetime.timedelta(seconds=total_seconds)
            pbar.set_description(f"Countdown: {timer}")
            time.sleep(1)
            total_seconds -= 1
            pbar.update(1)

    print("TIMES UP!")

h = input("input hours: ")
m = input("input minutes: ")
s = input("input seconds: ")
countDown(int(h), int(m), int(s))