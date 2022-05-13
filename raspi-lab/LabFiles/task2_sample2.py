from pythymiodw import *

robot = ThymioReal() # create an object

while True:
    print(robot.prox_ground.delta)
    # Read values from the ground sensors 
    left_sensor = robot.prox_ground.delta[0]
    right_sensor = robot.prox_ground.delta[1]

    print( left_sensor, right_sensor)
    robot.sleep(1) #Wait for 1 second 

robot.quit() # disconnect communication
