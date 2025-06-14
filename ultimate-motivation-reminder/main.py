import time
from pync import Notifier
from datetime import datetime

final = datetime(2085, 7, 19)
now = datetime.now()
time_left = final - now

total_time_hours = int(time_left.total_seconds() // 3600)
while True:
    time.sleep(60 * 60)
    Notifier.notify(f'Previous: {total_time_hours}\nLeft: {total_time_hours-1}', title = "Life Expectency: ")
    total_time_hours -= 1
    