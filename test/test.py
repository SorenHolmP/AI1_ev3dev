#!/usr/bin/python3.4

import ev3dev.ev3 as ev3
import time
import os
os.system('setfont Lat15-TerminusBold14')

lcd = ev3.Screen()

ev3.LargeMotor()

lcd.draw.rectangle((0,0,177,40), fill='black')
lcd.draw.text((48,13),'Hello, world.', fill='white')
lcd.draw.text((36,80),'THIS TEXT IS BLACK')
lcd.update()
time.sleep(6)
