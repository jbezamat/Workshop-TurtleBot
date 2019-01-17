#!/usr/bin/env python
import sys
import rospy
from workshop.srv import GoToXYTHETA

def send_xytheta(x, y, theta):
    rospy.wait_for_service('go_to_xytheta')
    try:
        go_to_xytheta = rospy.ServiceProxy('go_to_xytheta', GoToXYTHETA)
        resp1 = go_to_xytheta(x, y, theta)
        return resp1.return_msg
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y theta]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        theta = int(sys.argv[3])
    else:
        print usage()
        sys.exit(1)
    print "Requesting [%s %s %s]"%(x, y, theta)
    print "Return : %s"%(send_xytheta(x, y, theta))