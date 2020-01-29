#! /usr/bin/env python
import time
import rospy
from duckietown_msgs.msg import Twist2DStamped

rospy.init_node('modified_velocity')

pub=rospy.Publisher('/modified_velocity/velocity',
                        Twist2DStamped,
                        queue_size=10)

time.sleep(1)

msg=Twist2DStamped()

msg.v=1

while not rospy.is_shutdown():
    msg.v = 3.0
    msg.omega = 0.0
    pub.publish(msg)
    rate.sleep()
    msg.v = 0.0
    msg.omega = 0.0
    pub.publish(msg)
    rate.sleep()
