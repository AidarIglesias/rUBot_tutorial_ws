#!/usr/bin/env python3
import rospy
from numpy.random import choice as choose
from std_msgs.msg import String

messages = ["Ping!", "Pong!", "Bleb!", "Meow!"]             # let's make it fun! There are 4 possible messages chosen randomly

def ping():
    rospy.init_node('ping_node', anonymous=True)            # "ping_node" node initialization
    pub = rospy.Publisher('ping', String, queue_size=100)   # publisher initialization --> publishing to /ping topic
    rate = rospy.Rate(1)                                    # publishing rate of 1Hz (1 msg/sec)
    while not rospy.is_shutdown():
        choice = choose(messages, 1)    # choose from the string array messages one of the messages (following a uniform distribution)
        ping_str = "%s" % choice        # ping_str is set to the chosen message from before
        rospy.loginfo(ping_str)         # print the message on screen
        pub.publish(ping_str)           # node /ping_node publishes the message on /ping topic
        rate.sleep()

if __name__ == '__main__':
    try:
        ping()
    except rospy.ROSInterruptException:
        pass
