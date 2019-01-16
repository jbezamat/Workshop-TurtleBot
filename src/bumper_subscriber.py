#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from workshop.msg import Bumpers

def callback(bumpers):
    rospy.loginfo(rospy.get_caller_id() + "BUMPER_FORWARD: %s ; BUMPER_BACKWARD", bumpers.BUMPER_FORWARD, bumpers.BUMPER_BACKWARD)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('bumper_subscriber', anonymous=True)

    rospy.Subscriber('chatter', Bumpers, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
