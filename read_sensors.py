#!/usr/bin/python3.4

import ev3dev.ev3 as ev3
import time

northSensor = ev3.ColorSensor('in1')
southSensor = ev3.ColorSensor('in2')

#Setup the emitted light
northSensor.mode = northSensor.MODE_COL_COLOR

#Setup which colors to look for:
#northSensor.color = northSensor.COLOR_WHITE
#northSensor.color = northSensor.COLOR_GREEN 


northVal = northSensor.value()
southVal = southSensor.value()


while True:
    northVal = northSensor.value()
    southVal = southSensor.value()
    print("North value: ", northVal, "\t South value: ", southVal)
    time.sleep(0.5)

