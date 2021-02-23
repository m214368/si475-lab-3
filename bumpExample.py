import rospy
from turtleAPI import robot

try:
  print("creating robot")
  r= robot()
  while not rospy.is_shutdown():
    print r.getBumpStatus()
except Exception as e:
  print(e)
  rospy.loginto("node now terminated")
