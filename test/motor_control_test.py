#!/usr/bin/python3.4
import ev3dev.ev3 as ev3

#Load the motors:
mA = ev3.LargeMotor('outA')
mB = ev3.LargeMotor('outB')

#Load the color sensors:
c1 = ev3.ColorSensor('in1')
c2 = ev3.ColorSensor('in2')

#Define base forward speed
BASE_SPEED = 35

STATE_NORTH  = 1
STATE_EAST   = 2
STATE_SOUTH  = 3
STATE_WEST   = 4
STATE_INTERSECTION = 5

#Set the polarity. mB is inversed for convenience. 
mA.polarity = "normal"
mB.polarity = 'inversed'

#Set motor mode
mA.run_direct()
mB.run_direct()


#NORTH state
#Collect data
val1 = c1.reflected_light_intensity
val2 = c2.reflected_light_intensity
diff = val2-val1

#Set duty cycle as function of 
mA.duty_cycle_sp = BASE_SPEED
mB.duty_cycle_sp = diff

#EAST state
val1 = c1.reflected_light_intensity
val2 = c2.reflected_light_intensity
diff = val1 - val2

mA.duty_cycle_sp = diff
mB.duty_cycle_sp = BASE_SPEED

#SOUTH state
val1 = c1.reflected_light_intensity
val2 = c2.reflected_light_intensity
diff = val2-val1

mA.duty_cycle_sp = -BASE_SPEED #Negative because south bound
mB.duty_cycle_sp = diff

#WEST state
val1 = c1.reflected_light_intensity
val2 = c2.reflected_light_intensity
diff = val1 - val2

mA.duty_cycle_sp = diff
mB.duty_cycle_sp = -BASE_SPEED #Negative because west bound


#while True:





