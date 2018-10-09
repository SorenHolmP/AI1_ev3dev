#!/usr/bin/python3.4

import ev3dev.ev3 as ev3
from robot_defines import *
#Robot class

class Robot:
    def __init__(self, path):
        #Load sensors and motors:
        self.c1 = ev3.ColorSensor('in1')
        self.c2 = ev3.ColorSensor('in2')
        self.mA = ev3.LargeMotor('outA')
        self.mB = ev3.LargeMotor('outB')

        #Load directions
        self.path     = path
        self.path_ptr = 0

        #Set init state
        self.state = STATE_INIT

        #Check that sensoros are connected 
        assert self.c1.connected, "c1 is not connected"
        assert self.c2.connected, "c2 is not connected"
        assert self.mA.connected, "mA is not connected"
        assert self.mB.connected, "mB is not connected"

        #Setup motor
        #Set the polarity. mB is inversed for convenience. 
        self.mA.polarity = "normal"
        self.mB.polarity = 'inversed'

        #Set motor mode
        self.mA.run_direct()
        self.mB.run_direct()

        #Initially at a stand still:
        self.mA.duty_cycle_sp = 0
        self.mB.duty_cycle_sp = 0

        #Set brake mode:
        self.mA.stop_action = ev3.Motor.STOP_ACTION_BRAKE
        self.mB.stop_action = ev3.Motor.STOP_ACTION_BRAKE

    def FSM(self):
        val1 = self.c1.reflected_light_intensity
        val2 = self.c2.reflected_light_intensity
        
        if self.state == STATE_NORTH:
            if(val2 < BLACK_THRESHOLD): #Because c2 is front sensor
                self.move_blind()
                self.state = self.path[self.path_ptr]
                self.path_ptr += 1
            else:
                diff = val2-val1
                self.mA.duty_cycle_sp = BASE_SPEED
                self.mB.duty_cycle_sp = diff


        elif self.state == STATE_WEST:
            if(val2 < BLACK_THRESHOLD):
                self.move_blind()                     
                self.state = self.path[self.path_ptr]
                self.path_ptr += 1 
            else:
                diff = val1 - val2
                self.mA.duty_cycle_sp = diff
                self.mB.duty_cycle_sp = -BASE_SPEED         #Negative because west bound


        elif self.state == STATE_SOUTH:
            if(val1 < BLACK_THRESHOLD):
                self.move_blind()                     
                self.state = self.path[self.path_ptr]
                self.path_ptr += 1
            else:
                diff = val2-val1
                self.mA.duty_cycle_sp = -BASE_SPEED         #Negative because south bound
                self.mB.duty_cycle_sp = diff
        

        elif self.state == STATE_EAST:
            if(val1 < BLACK_THRESHOLD):
                self.move_blind()                     
                self.state = self.path[self.path_ptr]
                self.path_ptr += 1
            else:
                diff = val1 - val2
                self.mA.duty_cycle_sp = diff
                self.mB.duty_cycle_sp = BASE_SPEED


        elif self.state == STATE_INIT:
            print("Beginning mission with path: ")
            print(*self.path, sep = ", ")
            self.state = self.path[self.path_ptr]
            self.path_ptr += 1


    def move_blind(self):
        #Notice the sign on ticks in the function calls. 
        ssp = ( BASE_SPEED / 100 ) * 800 #800 is supposedly max value
        ticks = 120

        if(self.state == STATE_NORTH):
            self.mA.run_to_rel_pos(speed_sp = ssp, position_sp = ticks, stop_action = ev3.Motor.STOP_ACTION_BRAKE)
            self.mA.wait_while(ev3.Motor.STATE_RUNNING)

        elif(self.state == STATE_WEST):
            self.mB.run_to_rel_pos(speed_sp = ssp, position_sp = -ticks, stop_action = ev3.Motor.STOP_ACTION_BRAKE)
            self.mB.wait_while(ev3.Motor.STATE_RUNNING)

        elif(self.state == STATE_SOUTH):
            self.mA.run_to_rel_pos(speed_sp = ssp, position_sp = -ticks, stop_action = ev3.Motor.STOP_ACTION_BRAKE)
            self.mA.wait_while(ev3.Motor.STATE_RUNNING)

        elif(self.state == STATE_EAST):
            self.mB.run_to_rel_pos(speed_sp = ssp, position_sp = ticks, stop_action = ev3.Motor.STOP_ACTION_BRAKE)
            self.mB.wait_while(ev3.Motor.STATE_RUNNING)

        #Reset the motor mode, so they run by duty cycle values again
        self.mA.run_direct()
        self.mB.run_direct()

    def run_timed(self, time):
        self.mA.run_timed(speed_sp = 500, time_sp = time, stop_action = ev3.Motor.STOP_ACTION_BRAKE)
        self.mB.run_timed(speed_sp = 500, time_sp = time, stop_action = ev3.Motor.STOP_ACTION_BRAKE)

        self.mA.wait_while(ev3.Motor.STATE_RUNNING)    
        self.mB.wait_while(ev3.Motor.STATE_RUNNING)

        #self.mA.duty_cycle_sp = 50
        #self.mB.duty_cycle_sp = 25

    def stop(self):
         self.mA.duty_cycle_sp = 0
         self.mB.duty_cycle_sp = 0
        









    


