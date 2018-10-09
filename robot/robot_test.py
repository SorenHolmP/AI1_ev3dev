#!/usr/bin/python3.4

import ev3dev.ev3 as ev3
import robot
import time
from robot_defines import *

path = [1,1,2,3,3,3,2,1,4,4,2,3]

rb = robot.Robot(path)


#rb.move_blind(3000)

ticks_var = 1000
rb.mA.run_to_rel_pos(speed_sp = 400, position_sp = -ticks_var, stop_action = ev3.Motor.STOP_ACTION_BRAKE)

rb.mA.wait_while(ev3.Motor.STATE_RUNNING)

#time.sleep(5)
print("Finished run_to_rel_pos")
rb.mA.duty_cycle_sp = -50
rb.mA.run_direct()

time.sleep(5)
rb.stop()

# while(rb.path_ptr < len(rb.path)):
#     rb.FSM()

#rb.stop()

print("Finished the task")
