import os
import schedule
import time


def job():
    os.system('afplay /System/Library/Sounds/Funk.aiff')
    print("Drink Water")



schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

