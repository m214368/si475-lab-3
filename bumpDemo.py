#continuously drive until you get hit and then turn and continue

import rospy
from turtleAPI import robot






try:
  #print("creating robot")
  r= robot()

  #drive forward
  r.drive(angSpeed=0,linSpeed=.75)

  while not rospy.is_shutdown():
  	#check if bump has been detected
    print r.getBumpStatus()
    if (r.getBumpStatus().state == 1) #bump detected
    	if (r.getBumpStatus().bumper == 2): #right side bump

    	else if (r.getBumpStatus().bumper == 1): #middle bump

    	else: #left pump
except Exception as e:
  print(e)
  rospy.loginto("node now terminated")