#! /usr/bin/env python


import roslaunch
import rospy

# Soruce: http://wiki.ros.org/roslaunch/API%20Usage
def mapping():
    rospy.init_node('start_mapping', anonymous=True)
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    mapping = roslaunch.parent.ROSLaunchParent(uuid, ["/home/nvidia/catkin_ws/src/mapping_zed/launch/zed_rtabmap.launch"])
    
    mapping.start()
    rospy.loginfo("Mapping started")
    rospy.sleep(10)
    mapping.shutdown()

if __name__ == '__main__':
    try:
        mapping()
        
    except rospy.ROSInterruptException:
        pass
