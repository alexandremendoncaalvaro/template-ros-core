#! /usr/bin/env python
import time
import rospy
from duckitown_msg.msg import Twist2DStamped

rospy.init_node('modified_velocity')

pub=rospy.Publisher('/duckpi4/kinematics_node/velocity',
                        Twist2DStamped,
                        queue_size=10)

time.sleep(1)

msg=Twist2DStamped()

msg.v=1

while not rospy.is_shutdown():
	pub.publish(msg)
	time.sleep(1)
