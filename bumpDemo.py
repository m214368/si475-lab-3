#continuously drive until you get hit and then turn and continue

import rospy
from turtleAPI import robot
from time import sleep


gas=4
wheel=1

rate = rospy.Rate(10)

try:
  #print("creating robot")
  r= robot()

  #drive forward
  r.drive(angSpeed=0,linSpeed=gas)

  while not rospy.is_shutdown():
  	#check if bump has been detected
    print r.getBumpStatus()
    if (r.getBumpStatus().state == 1) #bump detected
    	r.drive(angSpeed=0,linSpeed=-gas)
    	sleep(.5)
    	if (r.getBumpStatus().bumper == 2): #right side bump
    		r.drive(angSpeed=-wheel,linSpeed=gas)
    	else if (r.getBumpStatus().bumper == 0): #left side
    		r.drive(angSpeed=wheel,linSpeed=gas)
    	else: #left pump
    		r.drive(angSpeed=wheel,linSpeed=0)
		sleep(.5)
	rate.sleep()
except Exception as e:
  print(e)
  rospy.loginto("node now terminated")