#!/usr/bin/env python
from workshop.srv import GoToXYZ
import rospy

def handle_go_to_xyz(req):
    print ("[%s %s %s]"%(req.x, req.y, req.z))
    return "youpi"

def go_to_xyz_server():
    rospy.init_node('go_to_xyz_server')
    s = rospy.Service('go_to_xyz', GoToXYZ, handle_go_to_xyz)
    print "Ready to receive X Y Z"
    rospy.spin()

if __name__ == "__main__":
    go_to_xyz_server()