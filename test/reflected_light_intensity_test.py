#!/usr/bin/python3.4

import ev3dev.ev3 as ev3
import time

colorSensor1 = ev3.ColorSensor('in1')
colorSensor2 = ev3.ColorSensor('in2')

# user_input = 'g' #go

# print("Press s to exit")

while True:
    val1 = colorSensor1.reflected_light_intensity
    val2 = colorSensor2.reflected_light_intensity
    print("Reflected light 1:   ", val1, "Reflected light 2: \t :  ", val2)

    time.sleep(0.5)
    