#!/usr/bin/python3.4

import ev3dev.ev3 as ev3

northSensor = ev3.LightSensor('in1')
southSensor = ev3.LightSensor('in2')

mA = ev3.LargeMotor('outA')
mB = ev3.LargeMotor('outB')

