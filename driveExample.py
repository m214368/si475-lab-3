import rospy
from turtleAPI import robot

try:
    print("creating robot")
    r= robot()
    r.drive(linSpeed=.25)

    # get initial position
    init_pos = r.getPositionTup()[0]
    goal_pos = init_pos + 1

    # checking to see how far it is
    while r.getPositionTup()[0] < goal_pos:
        pass

    # stop
    r.drive(linSpeed=0)
    
except Exception as e:
  print(e)
  rospy.loginto("node now terminated")
