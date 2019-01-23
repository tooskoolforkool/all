#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
 
def callback(msg):
    print ("Right")
    print msg.ranges[265:274]
    print ("Left")
    print msg.ranges[85:94]
    print ("Back")
    print msg.ranges[170:189]
    print ("Front")
    print [msg.ranges[350:359],msg.ranges[0:9]]
    
  
    
 
rospy.init_node('scan_values')
sub = rospy.Subscriber('/laser/scan', LaserScan, callback)
rospy.spin()


