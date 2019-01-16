#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from gpiozero import Button
from workshop.msg import Bumpers

def bumper():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('bumper', anonymous=True)
    rate = rospy.Rate(10) # 10hz


    bumpers = Bumpers()
    button_forward = Button(4, pull_up=True)
    button_backward = Button(5, pull_up=True)
    while not rospy.is_shutdown():
        bumpers.BUMPER_FORWARD = button_forward.is_pressed()
        bumpers.BUMPER_BACKWARD = button_backward.is_pressed()
        msg_str = "%s %s" % bumpers.BUMPER_FORWARD, bumpers.BUMPER_BACKWARD
        rospy.loginfo(msg_str)
        pub.publish(bumpers)
        rate.sleep()

if __name__ == '__main__':
    try:
        bumper()
    except rospy.ROSInterruptException:
        pass