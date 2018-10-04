#!/usr/bin/python3.4

import ev3dev.ev3 as ev3
import time

mA = ev3.LargeMotor('outA')
mB = ev3.LargeMotor('outB')

#Test effect of polarity:
mB.polarity = "inversed"


while True:
    valA = mA.position
    valB = mB.position
    print("Motor 1 sp:  ", valA, "\t Motor 2 sp:  ", valB)

    time.sleep(0.5)

    