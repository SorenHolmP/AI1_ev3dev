#!/usr/bin/python3.4

import ev3dev.ev3 as ev3
import time

ev3.Sound.speak('Hell').wait()

lcd = ev3.Screen()

print("X_res: " ,lcd.shape[0], "Y_res: ", lcd.shape[1], sep='---')

time.sleep(5)