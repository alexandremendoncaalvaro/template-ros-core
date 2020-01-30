#! /usr/bin/env python

import rospy
from duckietown_msgs.msg import Twist2DStamped
import time

rospy.init_node('modified_velocity')

pub=rospy.Publisher('/duckpi4/lane_controller_node/car_cmd',
                        Twist2DStamped,
                        queue_size=10)

time.sleep(1)


def callback(msg):
    msg.v *= 0.5
    msg.omega *= 0.5
    pub.publish(msg)


rospy.Subscriber('/duckpi4/new_velocity/car_cmd',
                 Twist2DStamped,
                 callback)

rospy.spin()