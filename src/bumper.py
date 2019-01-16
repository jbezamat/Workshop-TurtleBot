#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from gpiozero import Button

def bumper():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('bumper', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    button = Button(4, pull_up=True)
    while not rospy.is_shutdown():
        state = button.is_pressed()
        hello_str = "hello world %s" % state
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        bumper()
    except rospy.ROSInterruptException:
        pass