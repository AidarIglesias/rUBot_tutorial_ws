#!/usr/bin/env python3
import rospy
from numpy.random import choice as choose
from std_msgs.msg import String

def ping():
    rospy.init_node('ping_node', anonymous=True)            # "ping_node" node 
    pub = rospy.Publisher('ping', String, queue_size=10)    # "ping" topic 
    rate = rospy.Rate(1)                                    # Rate of 1Hz (1 msg/sec)
    messages = ["Ping!", "Pong!", "Bleb!", "Meow!"]         # Let's make it fun! There are 4 possible messages chosen randomly
    while not rospy.is_shutdown():
        choice = choose(messages, 1)                                # Choose from the string array messages one of the messages (following a uniform distribution)
        ping_str = "%s! [tstamp: %s]" % (choice, rospy.get_time())  # ping_str is set to the chosen message from before
        rospy.loginfo(ping_str) 
        pub.publisher(ping_str) 
        rate.sleep()

if __name__ == '__main__':
    try:
        ping()
    except rospy.ROSInterruptException:
        pass
