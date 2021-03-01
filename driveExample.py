import rospy
from turtleAPI import robot

try:
<<<<<<< HEAD
  print("creating robot")
  r= robot()
  r.drive(angSpeed=.4,linSpeed=.25)
  while not rospy.is_shutdown():
    print(r.getPositionTup())
    pass
=======
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
    
>>>>>>> a801abd1c91ac845e2615dc3b853361fdd5c6927
except Exception as e:
  print(e)
  rospy.loginto("node now terminated")
