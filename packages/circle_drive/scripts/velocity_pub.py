#! /usr/bin/env python

import rospy
from duckietown_msgs.msg import Twist2DStamped
import time

rospy.init_node('modified_velocity')

pub=rospy.Publisher('/duckpi4/lane_controller_node/car_cmd',
                        Twist2DStamped,
                        queue_size=10)

time.sleep(1)

msg=Twist2DStamped()

while not rospy.is_shutdown():
    msg.v = 0.2
    msg.omega = 0.0
    pub.publish(msg)
    time.sleep(1)
    msg.v = 0.0
    msg.omega = 0.0
    pub.publish(msg)
    time.sleep(1)
