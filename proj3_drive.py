import math
from turtleAPI import robot

# make the robot and lists for tracking error
r = robot()
error_list_pos = []
error_list_angle = []

#error function for angle
def angleDiff(current, desired):
    cur_angle = current[2]

    # calculate difference
    diff = cur_angle - desired
    if abs(diff) > math.pi:
        diff = abs(diff) - math.pi

    return diff

# error function for position
def posDiff(current, desired):
    #calculate component differences
    x_diff = current[0] - desired[0]
    y_diff = current[1] - desired[1]

    #calculate the total distance
    return (x_diff**2 + y_diff**2)**.5

# pid
def pid_speed(kp, ki, kd, error, old_error, error_list):

    # add the error to the integral portion
    if len(error_list) > 5:
        error_list.pop()
    error_list.append(error)

    #calculate sum
    error_sum = 0
    for i in error_list:
        error_sum += i

    # kp portion + ki portion
    to_return = kp * error + ki * error_sum

    # kd
    to_return += kd * error - old_error

    return to_return


#take input 
x = float(input("X coordinate?"))
y = float(input("Y coordinate?"))
goal_pos = (x, y)

# loop until at position
while true:

