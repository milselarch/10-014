from pythymiodw import *

robot = ThymioReal() #create an object

robot.wheels(100, 100) # make the robot move at same speed on both wheels
robot.sleep(1) # wait for 1 second

robot.wheels(50, 0) # make the left wheel move and right wheel stationary
robot.sleep(1) # wait for 1 second

robot.wheels(0, 0) # make both wheels stationary
robot.sleep(1) # wait for 1 seconds

robot.quit() # disconnect communication
