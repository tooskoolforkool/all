#! /usr/bin/env python

import roslaunch
import rospy

# Soruce: http://wiki.ros.org/roslaunch/API%20Usage
def test():
    rospy.init_node('starting_launch_files_from_script', anonymous=True)
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)

    person = roslaunch.parent.ROSLaunchParent(uuid, ["/home/nvidia/catkin_ws/src/darknet_ros/darknet_ros/launch/person.launch"])
    tags = roslaunch.parent.ROSLaunchParent(uuid, ["/home/nvidia/catkin_ws/src/darknet_ros/darknet_ros/launch/tags.launch"])

    print "Starting Person Detection"
    person.start()

    rospy.sleep(30)

    print "Starting Tags Detection"
    tags.start()

if __name__ == '__main__':
    try:
        test()

    except rospy.ROSInterruptException:
        pass
