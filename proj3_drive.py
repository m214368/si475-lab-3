import math, rospy
from turtleAPI import robot

# make the robot and lists for tracking error
r = robot()
error_list_pos = []
error_list_angle = []

#error function for angle
def angleDiff(cur_angle, desired):
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
    to_return += kd * error - old_error

    return to_return


#take input
x = float(input("X coordinate?"))
y = float(input("Y coordinate?"))
goal_pos = (x, y)

# loop until at position
old_ang_error = 0
old_pos_error = 0
rate = rospy.Rate(10)

while True:
    #current pos
    current_pos = r.getPositionTup()
    print('current pos: ' + str(current_pos))
    current_angle = current_pos[2]

    #calculate the goal angle
    relative_x = goal_pos[0]-current_pos[0]
    relative_y = goal_pos[1]-current_pos[1]
    goal_angle = math.atan2(relative_y, relative_x)
    print('goal angle: ' + str(goal_angle))
    #break if within .1 m
    if (posDiff(current_pos, goal_pos) < .1 ):
        break

    #calculate angle speed and lin speed drive
    ang_error = angleDiff(current_angle, goal_angle)
    pos_error = posDiff(current_pos, goal_pos)
    print('error: ' + str(ang_error) + ' ' +str(pos_error))

    #speed
    ang_speed = pid_speed(.25, 0, 0, ang_error, old_ang_error, error_list_angle)
    lin_speed = pid_speed(.1, 0, 0, pos_error, old_pos_error, error_list_pos)
    r.drive(angSpeed=ang_speed, linSpeed=lin_speed)
    print('speed: ' + str(ang_speed) + ' ' + str(lin_speed))

    #set old values
    old_ang_error=ang_error
    old_pos_error=pos_error
    rate.sleep()
    print(' ')

r.drive(angSpeed=0, linSpeed=0)
