import rospy
from turtleAPI import robot

try:
  print("creating robot")
  r= robot()
  r.drive(angSpeed=.4,linSpeed=.25)
  while not rospy.is_shutdown():
    pass
except Exception as e:
  print(e)
  rospy.loginto("node now terminated")