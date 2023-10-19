# pyTimer
# github link here

# this project creates a countdown timer in python

import time
import datetime

def countDown(hours, minutes, second):
    total_seconds = hours * 3600 + minutes * 60 + second

   
    while total_seconds > 0 :
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
           

    print("timeover!")

h = input("input hours: ")
m = input("input minutes: ")
s = input("input seconds: ")
countDown(int(h), int(m), int(s))