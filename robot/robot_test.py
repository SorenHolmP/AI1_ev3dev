#!/usr/bin/python3.4

import robot
import time

path = [0,1,2,3]

rb = robot.Robot(path)

rb.run_timed(3000)

print("Finished the task")
