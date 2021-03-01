import rospy,time,tf
from nav_msgs.msg import Odometry 
from geometry_msgs.msg import Twist

#Just print the odometry
def handleOdom(odomData):
    print(odomData)
    quater = (odomData.pose.pose.orientation.x ,odomData.pose.pose.orientation.y,odomData.pose.pose.orientation.z,odomData.pose.pose.orientation.w)
    #function that does math from quaternions to yaw pitch and roll.
    euler = tf.transformations.euler_from_quaternion(quater)	
    print('Orientation in roll-pitch-yaw',euler)

rospy.init_node('driveExample',anonymous=False)
driveCmd=rospy.Publisher('/si475/usercmd',Twist,queue_size=10)
odomSub=rospy.Subscriber('/odom',Odometry,handleOdom)

# Give the processes a chance to spin up
time.sleep(1)

# We will only ever change these two parts of the Twist object.
# Can you guess why?
move_cmd=Twist()
move_cmd.linear.x=.2
move_cmd.angular.z=0

driveCmd.publish(move_cmd)

time.sleep(5)

move_cmd.linear.x=0
move_cmd.angular.z=0
driveCmd.publish(move_cmd)
