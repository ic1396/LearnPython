#!/usr/bin/python3
# 《Python语言程序设计》程序清单２－７
# Programed List 2-7
# Compute current time(hour\minute\second) from current time temp

import time

currentTime = time.time()

# Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)

# Get the current second
currentSecond = totalSeconds % 60

# Obtain the total minutes
totalMinutes = totalSeconds // 60

# Compute current minute in the hour
currentMinutes = totalMinutes % 60

# Obtain the total hours
totalHours = totalMinutes // 60

# Compute current hour in the day
currentHour = totalHours % 24

# Display results
print("Current time is ", currentHour,":", currentMinutes, ":", currentSecond, "GMT")