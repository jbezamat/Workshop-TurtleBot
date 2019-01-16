#!/usr/bin/env python
import sys
import rospy
from workshop.srv import GoToXYZ

def send_xyz(x, y, z):
    rospy.wait_for_service('go_to_xyz')
    try:
        go_to_xyz = rospy.ServiceProxy('go_to_xyz', GoToXYZ)
        resp1 = go_to_xyz(x, y, z)
        return resp1.return_msg
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y z]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z = int(sys.argv[3])
    else:
        print usage()
        sys.exit(1)
    print "Requesting [%s %s %s]"%(x, y, z)
    print "Return : %s"%(send_xyz(x, y, z))