#!/usr/bin/env python
from workshop.srv import GoToXYTHETA
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from nav_msgs.msg import Odometry
import rospy
import math

class Robot():
    def __init__(self):
        self.odom_sub = rospy.Subscriber('odom', Odometry, self.tick_asserv)
        self.bump_sub = rospy.Subscriber('bumper_topic', Bumpers, self.callback_bump)
        self.goal_x = 0
        self.goal_y = 0
        self.goal_theta = 0
        self.x = 0
        self.y = 0
        self.theta = 0
        self.P = 3
        self.cmd_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        self.move_cmd = Twist()

    def tick_asserv(self, odom):
        self.x = odom.pose.pose.position.x
        self.y = odom.pose.pose.position.y
        self.theta = 0
        distance = math.sqrt(pow(self.x - self.goal_x, 2) + pow(self.y - self.goal_y, 2))
        if(abs(self.theta - self.goal_theta) < 10):
            self.move_cmd.linear.x = distance * self.P
            self.move_cmd.angular.z = 0
        else:
            self.move_cmd.linear.x = 0
            self.move_cmd.angular.z = 0

    def send_order(self):
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            self.cmd_pub.publish(self.move_cmd)
            rate.sleep()
    
    def callback_bump(self):
        stop_cmd = Twist()
        stop_cmd.linear.x = 0
        stop_cmd.linear.y = 0
        stop_cmd.linear.z = 0
        stop_cmd.angular.z = 0
        self.cmd_pub.publish(stop_cmd)

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_theta(self):
        return self.theta

    def handle_go_to_xytheta(self, req):
        print ("[%s %s %s]"%(req.x, req.y, req.theta))
        self.goal_x = req.x + self.x
        self.goal_y = req.y + self.y
        self.goal_theta = req.theta + self.theta
        self.send.order()
        return "youpi"

    def go_to_xytheta_server(self):
        s = rospy.Service('go_to_xytheta', GoToXYTHETA, self.handle_go_to_xytheta)
        print "Ready to receive X Y THETA"
        rospy.spin()


def main():
    rospy.init_node('go_to_xytheta_server')
    try:
        robot = Robot()
        robot.go_to_xytheta_server()
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()