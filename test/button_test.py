#!/usr/bin/python3.4

import ev3dev.ev3 as ev3
import time

button = ev3.Button()

time_now = time.time() 
time_old = time_now

while time_now - time_old < 10:
    time_now = time.time()
    print(time_now - time_old)
    if button.any():
        print("You clicked a button")
