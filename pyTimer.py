# pyTimer
# https://github.com/N0x1an/pyTimer

# this project creates a countdown timer in python using time, datetime, and tqdm

# importing the needed modules
import time
import datetime
from tqdm import tqdm

# main function of the timer
def countDown(hours, minutes, seconds):

    #variable to store the total amount of time in seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds

    # Creating a progress bar using tqdm
    with tqdm(total = total_seconds, unit = "s", dynamic_ncols=True) as pbar:
        # while loop that runs until the timer hits 0
        while total_seconds > 0 :
            # calculating the remaining time 
            timer = datetime.timedelta(seconds=total_seconds)
            # outputting the updated timer and progress bar
            pbar.set_description(f"Countdown: {timer}")
            time.sleep(1) # pausing the countdown by 1 second
            total_seconds -= 1 # decrementing the total seconds by 1
            pbar.update(1) # updating the progress bar

    # when out of the while loop print out that the timer is done
    print("TIMES UP!")

# taking in the inputs for the hour, minute, and second
h = input("input hours: ")
m = input("input minutes: ")
s = input("input seconds: ")

# calling the countDown function to being the countdown timer with the inputs
countDown(int(h), int(m), int(s))